# -*- coding: utf-8 -*-
"""Alerta semanal: edicoes novas do Diario Oficial de Araguaina (API publica) com atos de interesse tributario.
Nao altera a base: grava alertas/dom_novos.md e estado/dom.json. O workflow abre uma Issue para revisao humana
(ato novo muda vigencia e precisa de decisao do auditor)."""
import datetime as dt, json, os, re, sys, time, unicodedata, urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EST = os.path.join(RAIZ, 'estado', 'dom.json')
API = 'https://api-araguaina.barcodigital.com.br/api/publico/diario?per_page=20&page={}'
HDR = {'User-Agent': 'Mozilla/5.0', 'Origin': 'https://diariooficial.araguaina.to.gov.br', 'Url': 'diariooficial.araguaina.to.gov.br'}
TERMOS = [r'ISSQN', r'IMPOSTO SOBRE SERVICOS', r'SIMPLES NACIONAL', r'NFS-?E', r'WEBISS', r'SUBSTITUI[CÇ]AO TRIBUTARIA', r'AUDITOR(?:ES)? FISCA',
          r'\bTIAF\b', r'ACAO FISCAL', r'AUTO DE INFRACAO', r'PROCESSO ADMINISTRATIVO (?:FISCAL|TRIBUTARIO)', r'DIVIDA ATIVA', r'REFIS',
          r'REGULARIZACAO FISCAL', r'PARCELAMENTO', r'DEVEDOR CONTUMAZ', r'DOMICILIO (?:ELETRONICO|TRIBUTARIO)', r'ATUALIZACAO MONETARIA',
          r'UNIDADE PADRAO DE REFERENCIA', r'CALENDARIO FISCAL', r'CODIGO TRIBUTARIO', r'LEI COMPLEMENTAR (?:MUNICIPAL )?N? ?0?58', r'DEFESA DO CONTRIBUINTE',
          r'CREDITO TRIBUTARIO', r'ADMINISTRACAO TRIBUTARIA', r'OBRIGACAO ACESSORIA', r'TVRE', r'ANISTIA', r'REMISSAO', r'ISENCAO', r'MICROEMPREENDEDOR',
          r'SIGILO', r'COMPLEMENTAR (?:FEDERAL )?N? ?105', r'PROTESTO', r'TRANSACAO TRIBUTARIA', r'ALVARA', r'PRESCRICAO', r'DECADENCIA', r'REDAF']
TIPO = r'(LEI COMPLEMENTAR|LEI MUNICIPAL|LEI ORDINARIA|LEI|DECRETO|PORTARIA|INSTRUCAO NORMATIVA|RESOLUCAO)'
RX = re.compile(TIPO + r'(?: MUNICIPAL)?(?: CONJUNTA)?(?:[ /-]*(?:GABSF|SEFAZ|SMF|GAB|PGM))?\s*(?:N\s*[º°O.]*\s*)?(\d{1,3}(?:\.\d{3})?)\s*(?:/\s*(20\d\d))?\s*,?\s*DE\s+(\d{1,2})(?:O|º)?\s+DE\s+([A-Z]+)\s+(?:DE\s+)?(20\d\d)')


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').upper()
    return re.sub(r'[ \t]+', ' ', s)


def get(pg):
    for _ in range(4):
        try:
            req = urllib.request.Request(API.format(pg), headers=HDR)
            return json.loads(urllib.request.urlopen(req, timeout=120).read())
        except Exception as e:
            print('erro', pg, e); time.sleep(15)
    sys.exit('API do DOM indisponivel')


est = json.load(open(EST, encoding='utf-8')) if os.path.exists(EST) else {'ultima_data': '2026-11-23'}
desde = (dt.date.fromisoformat(est['ultima_data']) - dt.timedelta(days=3)).isoformat()
achados, novas, pg, maior = [], 0, 1, est['ultima_data']
while True:
    d = get(pg); fim = False
    for x in d['data']:
        if x['data'] < desde:
            fim = True; continue
        novas += 1; maior = max(maior, x['data'])
        t = norm(x.get('conteudo') or '')
        for m in RX.finditer(t):
            tipo, num, _, dia, mes, ano = m.groups()
            jan = t[m.start():m.start() + 2500]
            termos = [k for k in TERMOS if re.search(k, jan)]
            if termos and tipo != 'PORTARIA' and not re.search(r'NOMEA|EXONERA|DESIGNA', jan[:300]):
                achados.append((x['data'], x['edicao'], '%s %s/%s' % (tipo, num.lstrip('0') or '0', ano), '; '.join(termos[:4]), re.sub(r'\s+', ' ', jan[:200])))
    if fim or not d.get('next_page_url'):
        break
    pg += 1; time.sleep(1.5)
vistos, unicos = set(), []
for a in achados:
    if (a[0], a[2]) not in vistos:
        vistos.add((a[0], a[2])); unicos.append(a)
os.makedirs(os.path.join(RAIZ, 'alertas'), exist_ok=True)
corpo = ['# Atos novos no DOM de Araguaina (para revisao humana)', '', 'Gerado em %s. Edicoes verificadas: %d.' % (dt.datetime.utcnow().strftime('%d/%m/%Y %H:%M UTC'), novas), '']
corpo += ['- **%s** (DOM %s, %s): %s\n  termos: %s' % (a[2], a[1], a[0], a[4][:160], a[3]) for a in unicos] or ['Nenhum ato novo com termo tributario.']
open(os.path.join(RAIZ, 'alertas', 'dom_novos.md'), 'w', encoding='utf-8').write('\n'.join(corpo) + '\n')
os.makedirs(os.path.dirname(EST), exist_ok=True)
json.dump({'ultima_data': maior, 'atualizado_em': dt.date.today().isoformat()}, open(EST, 'w'))
print(len(unicos), 'ato(s) com termo tributario em', novas, 'edicao(oes)')
if unicos:
    open(os.path.join(RAIZ, 'alertas', 'ISSUE.txt'), 'w', encoding='utf-8').write('\n'.join(corpo))
