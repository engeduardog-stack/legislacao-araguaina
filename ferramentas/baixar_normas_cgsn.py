"""Baixa todos os atos de um órgão no Normas da Receita Federal (padrão: CGSN).

Fontes (API pública, sem login, a mesma que o site usa):
  lista:  POST https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar
  texto:  GET  https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/{id}/visao/{vigente|original|multivigente}
  anexo:  GET  https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato/{id}/anexo/{idArquivo}

Uso:
  python baixar_normas.py                 (CGSN, órgão 51)
  python baixar_normas.py --orgao 52      (Secretaria Executiva do CGSN)
  python baixar_normas.py --refazer       (baixa de novo mesmo o que já existe)

Rodar de novo só baixa o que for novo. Atos já baixados são pulados. Quando aparece ato novo,
o texto de todos os atos vigentes é baixado de novo (o ato novo pode ter alterado algum deles),
e o programa lista os que mudaram.
"""
import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PESQUISA = "https://normas.receita.fazenda.gov.br/api/indexacao/ato/pesquisar"
CONSULTA = "https://normasinternet2.receita.fazenda.gov.br/api/consulta-externa/ato"
LINK = "https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/{}"
VISOES = ("vigente", "original", "multivigente")
UA = "Mozilla/5.0 (normas-cgsn; uso fiscal municipal)"
PAUSA = 0.4


def http(url, corpo=None, tentativas=4):
    dados = json.dumps(corpo).encode("utf-8") if corpo is not None else None
    for n in range(tentativas):
        try:
            req = urllib.request.Request(url, data=dados, headers={"User-Agent": UA})
            if dados:
                req.add_header("Content-Type", "application/json; charset=UTF-8")
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500 or n == tentativas - 1:  # erro do pedido: não adianta repetir
                raise
            print(f"   falha ({e}); tentando de novo...")
            time.sleep(3 * (n + 1))
        except Exception as e:
            if n == tentativas - 1:
                raise
            print(f"   falha ({e}); tentando de novo...")
            time.sleep(3 * (n + 1))


def listar(orgao):
    atos, pagina = [], 1
    while True:
        corpo = {
            "tipoData": "dataPublicacao", "tiposAtosSelecionados": "", "orgaosSelecionados": str(orgao),
            "numeroAto": "", "dataInicio": "", "dataFim": "", "publicado": True, "internet": True,
            "apenasAtosVigentes": False, "apenasAtosInternos": False, "termo": "", "refino": {},
            "ordenacaoColuna": "publicacao", "ordenacaoDirecao": "desc",
            "paginacaoPaginaAtual": pagina, "paginacaoQuantidadePorPagina": 100, "skipAggregations": True,
        }
        r = json.loads(http(PESQUISA, corpo).decode("utf-8"))
        atos += r.get("atos") or []
        print(f"lista: página {pagina}/{r.get('quantidadePaginas')} ({len(atos)}/{r.get('quantidadeTotal')})")
        if pagina >= (r.get("quantidadePaginas") or 1):
            return atos, r.get("quantidadeTotal")
        pagina += 1
        time.sleep(PAUSA)


def nome_arquivo(a):
    sig = re.sub(r"[^\w]+", "", a["tipoAto"]["siglaTipoAto"]) or "Ato"
    num = re.sub(r"[^\w-]+", "-", a.get("numeroAto") or "sn").strip("-") or "sn"
    return f"{a.get('anoAto')}_{sig}_{num}_id{a['idAto']}"


def limpar(t):
    return re.sub(r"\s+", " ", t or "").strip()


def texto_puro(h):
    h = re.sub(r"<br\s*/?\s*>", "\n", h or "", flags=re.I)
    h = re.sub(r"</(p|div|tr|li|h\d)>", "\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    return "\n".join(limpar(l) for l in html.unescape(h).splitlines() if limpar(l))


def montar(v, visao, anexos_locais):
    """Monta HTML e TXT da visão, mostrando só os segmentos que o site mostra (omitir = falso)."""
    titulo = v.get("epigrafeCompleta") or ""
    partes_h = [f"<h1>{html.escape(titulo)}</h1>",
                f"<p class='meta'>{html.escape(v.get('dadosPublicacao') or '')}<br>"
                f"Visão: {visao} | Vigente: {'sim' if v.get('vigente') else 'não'} | "
                f"<a href='{LINK.format(v['idAto'])}'>ver no site da Receita</a></p>"]
    partes_t = [titulo, v.get("dadosPublicacao") or "", f"Visão: {visao}", LINK.format(v["idAto"]), ""]
    for h in v.get("historico") or []:
        partes_h.append(f"<p class='hist'>{html.escape(h.get('texto') or '')}</p>")
        partes_t.append(h.get("texto") or "")
    for s in (v.get("ementas") or []) + (v.get("outrosSegmentos") or []):
        if s.get("omitir"):
            continue
        corpo = s.get("textoIntegra") or ""
        notas = [a.get("texto") + (f" (vigência desde {a['dataInicioVigencia']})"
                                   if visao == "multivigente" and a.get("dataInicioVigencia") else "")
                 for a in (s.get("ancorasDestino") or []) if a.get("texto")]
        arq = s.get("arquivoBinario")
        if not limpar(texto_puro(corpo)) and not notas and not arq:
            continue
        cls = "ementa" if s.get("idTipoSegmento") == 1 else f"t{s.get('idTipoSegmento')}"
        h = f"<div class='{cls}'>{corpo}"
        if arq:
            local = anexos_locais.get(arq.get("idArquivoBinario"))
            nome = arq.get("nomeArquivoBinario") or "anexo"
            h += f" <a href='{html.escape(local or '')}'>[arquivo: {html.escape(nome)}]</a>"
        if notas:
            h += " <span class='nota'>" + " ".join(html.escape(n) for n in notas) + "</span>"
        partes_h.append(h + "</div>")
        linha = texto_puro(corpo)
        if arq:
            linha += f" [arquivo: {arq.get('nomeArquivoBinario')}]"
        if notas:
            linha += " " + " ".join(notas)
        partes_t.append(linha.strip())
    estilo = ("body{font-family:Arial,sans-serif;max-width:900px;margin:2em auto;line-height:1.45}"
              ".meta,.hist{color:#555;font-size:.9em}.ementa{margin-left:40%;font-style:italic}"
              ".nota{color:#1a5fb4;font-size:.85em}div{margin:.35em 0}table{border-collapse:collapse}"
              "td,th{border:1px solid #999;padding:2px 4px}")
    doc = (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>{html.escape(titulo)}</title>"
           f"<style>{estilo}</style></head><body>" + "\n".join(partes_h) + "</body></html>")
    return doc, "\n".join(partes_t) + "\n"


def baixar_ato(a, pasta, refazer, refazer_anexos=None):
    nome = nome_arquivo(a)
    visoes, novas, arquivos, mudou = {}, [], {}, False
    refazer_anexos = refazer if refazer_anexos is None else refazer_anexos
    for visao in VISOES:
        jarq = pasta / "json" / f"{nome}_{visao}.json"
        indisp = pasta / "json" / f"{nome}_{visao}.indisponivel"
        if not refazer and indisp.exists():
            continue
        if not refazer and jarq.exists():
            visoes[visao] = json.loads(jarq.read_text(encoding="utf-8"))
        else:
            try:
                bruto = http(f"{CONSULTA}/{a['idAto']}/visao/{visao}")
            except urllib.error.HTTPError as e:
                if e.code == 406 and visao != "original":  # o site só oferece a visão original deste ato
                    indisp.write_text("visão não oferecida pelo site (HTTP 406)", encoding="utf-8")
                    continue
                raise
            visoes[visao] = json.loads(bruto.decode("utf-8"))
            novas.append(visao)
            if jarq.exists() and visao != "vigente":  # compara com o que já estava baixado
                antigo = json.loads(jarq.read_text(encoding="utf-8")).get("outrosSegmentos")
                mudou = mudou or antigo != visoes[visao].get("outrosSegmentos")
            time.sleep(PAUSA)
    if not novas:
        return "pulado", [], False
    for visao in visoes:
        for s in visoes[visao].get("outrosSegmentos") or []:
            arq = s.get("arquivoBinario")
            if arq and arq.get("idArquivoBinario"):
                arquivos[arq["idArquivoBinario"]] = arq.get("nomeArquivoBinario") or "anexo"
    locais = {}
    for ida, nm in arquivos.items():
        nm_limpo = re.sub(r'[<>:"/\\|?*]+', "_", re.sub(r"\s+", " ", nm)).strip()
        destino = pasta / "anexos" / nome / f"{ida}_{nm_limpo}"
        if not destino.exists() or refazer_anexos:
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_bytes(http(f"{CONSULTA}/{a['idAto']}/anexo/{ida}"))
            time.sleep(PAUSA)
        locais[ida] = f"../anexos/{nome}/{destino.name}"
    for visao in novas:
        doc, txt = montar(visoes[visao], visao, locais)
        (pasta / visao / f"{nome}.html").write_text(doc, encoding="utf-8")
        (pasta / visao / f"{nome}.txt").write_text(txt, encoding="utf-8")
    for visao in novas:  # o JSON por último: marca a visão como concluída
        (pasta / "json" / f"{nome}_{visao}.json").write_text(json.dumps(visoes[visao], ensure_ascii=False), encoding="utf-8")
    return "baixado (" + ", ".join(novas) + ")", list(arquivos), mudou


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orgao", type=int, default=51, help="51 = CGSN; 52 = Secretaria Executiva do CGSN")
    ap.add_argument("--saida", default=None)
    ap.add_argument("--refazer", action="store_true")
    arg = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    base = Path(__file__).resolve().parent
    pasta = Path(arg.saida) if arg.saida else base / ("CGSN" if arg.orgao == 51 else f"orgao_{arg.orgao}")
    for sub in ("json", "anexos", *VISOES):
        (pasta / sub).mkdir(parents=True, exist_ok=True)

    conhecidos = set()
    if (pasta / "indice.json").exists():
        conhecidos = {x["idAto"] for x in json.loads((pasta / "indice.json").read_text(encoding="utf-8"))}
    atos, total = listar(arg.orgao)
    if len(atos) != total:
        print(f"ATENÇÃO: a lista trouxe {len(atos)} atos, mas o site informa {total}.")
    novos = [a for a in atos if conhecidos and a["idAto"] not in conhecidos]
    if novos:
        print(f"{len(novos)} ato(s) novo(s): " + ", ".join(nome_arquivo(a) for a in novos))
        print("Revendo o texto de todos os atos vigentes (o ato novo pode ter alterado algum).")

    falhas, linhas, alterados = [], [], []
    for i, a in enumerate(atos, 1):
        nome = nome_arquivo(a)
        try:
            rever = bool(novos) and a.get("vigente") == "1" and a["idAto"] in conhecidos
            situacao, anexos, mudou = baixar_ato(a, pasta, arg.refazer or rever, refazer_anexos=arg.refazer)
            if mudou:
                alterados.append(nome)
        except Exception as e:
            situacao, anexos = f"FALHA: {e}", []
            falhas.append(nome)
        print(f"{i:4}/{len(atos)} {nome}: {situacao}" + (f" ({len(anexos)} anexos)" if anexos else ""))
        linhas.append({
            "idAto": a["idAto"], "tipo": a["tipoAto"]["nomeTipoAto"], "numero": a.get("numeroAto"),
            "ano": a.get("anoAto"), "data_ato": a.get("dataAto"), "data_publicacao": a.get("dataPublicacao"),
            "vigente": "sim" if a.get("vigente") == "1" else "não", "revogacao": a.get("resumoRevogado") or "",
            "ementa": limpar(a.get("ementa")), "arquivo": nome, "link": LINK.format(a["idAto"]),
        })

    with open(pasta / "INDICE.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), delimiter=";")
        w.writeheader()
        w.writerows(linhas)
    (pasta / "indice.json").write_text(json.dumps(atos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nPronto: {len(atos)} atos em {pasta}")
    print(f"Atos novos: {len(novos)}" + (" (" + ", ".join(nome_arquivo(a) for a in novos) + ")" if novos else ""))
    print(f"Atos com texto alterado: {len(alterados)}" + (" (" + ", ".join(alterados) + ")" if alterados else ""))
    if falhas:
        print(f"FALHARAM {len(falhas)} (rode de novo para tentar só esses): {', '.join(falhas)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
