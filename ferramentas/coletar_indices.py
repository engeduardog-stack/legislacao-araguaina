# -*- coding: utf-8 -*-
r"""Coleta os índices oficiais usados nos cálculos das auditorias e grava em C:\AUDITORIAS-IA\_DADOS\INDICES OFICIAIS.

Fontes (só oficiais, sem login):
  IBGE SIDRA  tabela 1737 (IPCA, v63 variação mensal, v69 acumulado no ano, v2266 número-índice dez/93=100)
              tabela 1736 (INPC, v44 variação mensal)
              tabela 3065 (IPCA-15, v1117 variação mensal)
  Banco Central SGS  433 IPCA | 188 INPC | 7478 IPCA-15 | 189 IGP-M | 190 IGP-DI | 4390 Selic acumulada no mês
                     4189 Selic acumulada no mês anualizada | 226 TR | 11 Selic diária (taxa % a.d.) | 1 dólar não entra

Cada série vira CSV (competência;valor;fonte;coletado_em) e entra no INDICES.json. O IPCA só é gravado como
"conferido" quando IBGE e Banco Central dão o mesmo valor mês a mês (as diferenças saem em CONFERENCIA.md).
Uso: python coletar_indices.py
"""
import csv, datetime as dt, json, os, sys, urllib.request

SAIDA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'indices')
HOJE = dt.date.today().isoformat()
os.makedirs(SAIDA, exist_ok=True)


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'consulta-indices'})
    return json.loads(urllib.request.urlopen(req, timeout=120).read().decode('utf-8'))


def sidra(tabela, var, nome):
    d = get(f'https://apisidra.ibge.gov.br/values/t/{tabela}/n1/all/v/{var}/p/all?formato=json')
    return {r['D3C']: float(r['V']) for r in d[1:] if r['V'] not in ('...', '-', '', 'X')}


def sgs(codigo, ini='01/01/1995'):
    # O SGS limita séries diárias a 10 anos por consulta; as mensais cabem de uma vez.
    d = get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={ini}')
    out = {}
    for r in d:
        dia, mes, ano = r['data'].split('/')
        out[ano + mes] = float(r['valor'])
    return out


def sgs_diaria_mensal_acum(codigo, ano_ini=2015):
    """Selic diária (% a.d.) -> acumulada do mês composta, por competência."""
    out = {}
    hoje = dt.date.today()
    for ano in range(ano_ini, hoje.year + 1):
        d = get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial=01/01/{ano}&dataFinal=31/12/{ano}')
        for r in d:
            dia, mes, a = r['data'].split('/')
            out.setdefault(a + mes, 1.0)
            out[a + mes] *= 1 + float(r['valor']) / 100
    return {k: round((v - 1) * 100, 2) for k, v in out.items()}


series = {}
conf = []

# --- IPCA: IBGE e BCB
ipca_ibge = sidra(1737, 63, 'IPCA')
ipca_bcb = sgs(433)
dif = [(k, ipca_ibge[k], ipca_bcb[k]) for k in sorted(set(ipca_ibge) & set(ipca_bcb)) if abs(ipca_ibge[k] - ipca_bcb[k]) > 0.005]
series['IPCA'] = {'descricao': 'IPCA, variação mensal (%)', 'fonte': 'IBGE SIDRA tabela 1737 variável 63 (conferido com BCB SGS 433)', 'dados': ipca_ibge,
                  'conferido_bcb': not dif}
conf.append(f'IPCA: IBGE {len(ipca_ibge)} meses ({min(ipca_ibge)} a {max(ipca_ibge)}); BCB {len(ipca_bcb)} meses; divergências: {dif or "nenhuma"}.')
series['IPCA_NUMERO_INDICE'] = {'descricao': 'IPCA, número-índice (dez/1993 = 100)', 'fonte': 'IBGE SIDRA tabela 1737 variável 2266', 'dados': sidra(1737, 2266, 'IPCA num')}
series['IPCA_ACUMULADO_ANO'] = {'descricao': 'IPCA acumulado no ano (%)', 'fonte': 'IBGE SIDRA tabela 1737 variável 69', 'dados': sidra(1737, 69, 'IPCA ano')}
series['IPCA_ACUMULADO_12M'] = {'descricao': 'IPCA acumulado em 12 meses (%)', 'fonte': 'IBGE SIDRA tabela 1737 variável 2265', 'dados': sidra(1737, 2265, 'IPCA 12m')}
# --- INPC, IPCA-15
inpc_ibge, inpc_bcb = sidra(1736, 44, 'INPC'), sgs(188)
d2 = [(k, inpc_ibge[k], inpc_bcb[k]) for k in sorted(set(inpc_ibge) & set(inpc_bcb)) if abs(inpc_ibge[k] - inpc_bcb[k]) > 0.005]
series['INPC'] = {'descricao': 'INPC, variação mensal (%)', 'fonte': 'IBGE SIDRA tabela 1736 variável 44 (conferido com BCB SGS 188)', 'dados': inpc_ibge, 'conferido_bcb': not d2}
conf.append(f'INPC: IBGE {len(inpc_ibge)} meses; divergências com BCB: {d2 or "nenhuma"}.')
ipca15 = sidra(3065, 1117, 'IPCA-15')
series['IPCA15'] = {'descricao': 'IPCA-15, variação mensal (%)', 'fonte': 'IBGE SIDRA tabela 3065 variável 1117', 'dados': ipca15}
# --- Banco Central
series['IGPM'] = {'descricao': 'IGP-M, variação mensal (%) (FGV, divulgado pelo BCB)', 'fonte': 'BCB SGS 189', 'dados': sgs(189)}
series['IGPDI'] = {'descricao': 'IGP-DI, variação mensal (%) (FGV, divulgado pelo BCB)', 'fonte': 'BCB SGS 190', 'dados': sgs(190)}
series['SELIC_MES'] = {'descricao': 'Selic acumulada no mês (%)', 'fonte': 'BCB SGS 4390', 'dados': sgs(4390)}
series['TR'] = {'descricao': 'TR, variação mensal (%)', 'fonte': 'BCB SGS 226 (taxa referencial, mensal, dia 1º)', 'dados': {}}
try:
    tr = {}
    for ini, fim in (('01/01/1995', '31/12/2004'), ('01/01/2005', '31/12/2014'), ('01/01/2015', '31/12/2026')):
        for r in get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7811/dados?formato=json&dataInicial={ini}&dataFinal={fim}'):
            dia, mes, ano = r['data'].split('/'); tr[ano + mes] = float(r['valor'])
    series['TR']['dados'] = tr
    series['TR']['fonte'] = 'BCB SGS 7811 (TR mensal, vigente no mês)'
except Exception as e:
    conf.append(f'TR: falhou ({e})')
try:
    series['SELIC_MES_DIARIA'] = {'descricao': 'Selic acumulada no mês, composta a partir da taxa diária (%) (conferência da 4390)', 'fonte': 'BCB SGS 11', 'dados': sgs_diaria_mensal_acum(11)}
    comp = [(k, series['SELIC_MES']['dados'][k], series['SELIC_MES_DIARIA']['dados'][k]) for k in sorted(set(series['SELIC_MES']['dados']) & set(series['SELIC_MES_DIARIA']['dados']))
            if abs(series['SELIC_MES']['dados'][k] - series['SELIC_MES_DIARIA']['dados'][k]) > 0.02 and k >= '201501']
    conf.append(f'Selic: 4390 x composição da diária (11), diferenças acima de 0,02 p.p.: {comp[:10] or "nenhuma"}')
except Exception as e:
    conf.append(f'Selic diária: falhou ({e})')

# --- datas de divulgação do IPCA (calendário oficial do IBGE)
divulg = {}
try:
    cal = get('https://servicodados.ibge.gov.br/api/v3/calendario/9256?qtd=1000')
    for it in cal['items']:
        dd, mm, aa = it['data_divulgacao'].split(' ')[0].split('/')
        divulg['%04d%02d' % (it['ano_referencia_inicio'], it['mes_referencia_inicio'])] = '%s-%s-%s' % (aa, mm, dd)
except Exception as e:
    conf.append(f'Calendário IBGE: falhou ({e})')
if divulg:
    with open(os.path.join(SAIDA, 'IPCA_DIVULGACAO.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';'); w.writerow(['competencia', 'divulgacao', 'ja_divulgado', 'fonte'])
        for k in sorted(divulg): w.writerow([k[:4] + '-' + k[4:], divulg[k], 'sim' if divulg[k] <= HOJE else 'não (previsto)', 'IBGE, calendário de divulgação (produto 9256)'])
    with open(os.path.join(SAIDA, 'IPCA_para_colar_no_sistema.txt'), 'w', encoding='utf-8') as f:
        for k in sorted(ipca_ibge):
            if k in divulg and k >= '201701':
                f.write('%s-%s;%s;%s' % (k[:4], k[4:], str(ipca_ibge[k]).replace('.', ','), divulg[k]) + chr(10))
    conf.append(f'Datas de divulgação do IPCA (IBGE): {len(divulg)} competências; próximo: ' + ', '.join(f'{k[:4]}-{k[4:]} em {v}' for k, v in sorted(divulg.items()) if v > HOJE)[:80])

# --- grava
meta = {'coletado_em': HOJE, 'series': {}}
for nome, s in series.items():
    dados = s['dados']
    if not dados: continue
    with open(os.path.join(SAIDA, f'{nome}.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';'); w.writerow(['competencia', 'valor', 'fonte', 'coletado_em'])
        for k in sorted(dados): w.writerow([k[:4] + '-' + k[4:], str(dados[k]).replace('.', ','), s['fonte'], HOJE])
    meta['series'][nome] = {k: v for k, v in s.items() if k != 'dados'}
    meta['series'][nome].update({'inicio': min(dados), 'fim': max(dados), 'meses': len(dados), 'valores': dados})
json.dump(meta, open(os.path.join(SAIDA, 'INDICES.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
open(os.path.join(SAIDA, 'CONFERENCIA.md'), 'w', encoding='utf-8').write(
    f'# Conferência dos índices oficiais (coletado em {HOJE})\n\n' + '\n'.join('- ' + c for c in conf) + '\n')
print('\n'.join(conf))
for n, m in meta['series'].items(): print(f"{n:22s} {m['inicio']} a {m['fim']}  {m['meses']} meses")
