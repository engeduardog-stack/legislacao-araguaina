# Regras de aplicação no tempo (CTM de Araguaína)

Uso com `ctm_versoes.json`. Gerado em 23/11/2026.

## 1. Escolher a redação pela data
1. Fixe a data que manda em cada ponto:
   - tributo, alíquota, base e isenção: data do fato gerador de cada competência;
   - multa por obrigação acessória: data da infração (dia seguinte ao fim do prazo do TIAF ou da notificação, ou o dia da conduta);
   - multa de mora ou de ofício (113, 114, 446): data do vencimento não pago;
   - prazo e rito (57, 145, 266, 315): data do ato (emissão da OS, ciência do TIAF, ciência do termo).
2. Procure a chave do dispositivo e pegue a entrada com `de <= data <= ate` (`ate` nulo = vigente hoje). `ate` é inclusive: a redação seguinte começa no dia seguinte.
3. Se a entrada for `inexistente`, o dispositivo não existia na data: não capitule nele. Se for `revogado`, a regra não existia mais.
4. No art. 361, procure pela conduta, não pela letra. A letra mudou de conduta em 26/12/2024 e em 26/11/2025 (quadro em INDICE-ALTERACOES.md, seção 2).
5. Valor da multa fixa no exercício: `valores_por_exercicio.json`. A regra da casa de 05/11/2026 (valor do último decreto) só vale para alínea que já existia na data da infração.
6. Ligação entre os dois arquivos: em `valores_por_exercicio.json` a chave sem sufixo é a redação de 2017. "@LC195" é a redação da LC 195 (só 2025) e "@LC221" é a da LC 221 (2026). Exemplo: a infração do 361 I "a" em 2025 é a entrega fora do prazo, e o valor está em `361.I.a@LC195`. A chave `361.I.a` sem sufixo é a do livro sem autenticação.

## 2. Majoração de tributo
- Anterioridade anual e noventena (CF, art. 150, III, "b" e "c"), mesmo quando a lei diz "vigor na publicação".
- No JSON a data já vem em `de` e em `eficacia`. Exemplos:
  - LC 080: 19.01 e 21.01 e o 474 §7º desde 01/01/2022;
  - LC 171: 11.05 desde 01/01/2025;
  - LC 195: fim do 279, IV, e das tabelas especiais de TLL desde 26/03/2025;
  - LC 221: art. 290, revogação dos arts. 302, 305, 306 §1º, 309 e 310, 387 e 469, III desde 24/02/2026; ISS fixo em UPR desde 01/03/2026 (Dec. 101/2025).
- Noventena contada como publicação + 90 dias, que é a convenção da casa. A alternativa conservadora é o dia seguinte (`selo_data` PARCIAL).
- Redução de tributo vale desde o vigor e não retroage. O CTN 106 só alcança penalidade.
- Revogar isenção, não incidência ou dedução equivale a majorar.

## 3. Penalidade
- Penalidade nova ou mais grave só vale para infração posterior ao vigor (CF 5º, XXXIX e XL; CTN 144). Exemplos:
  - LC 195: 113 e 114 diários, 115 sobre "tributo", 356 p.u. e as alíneas novas do 361 I;
  - LC 221: 361 I "b" a "g" e V "c" e "f".
- Lei mais branda retroage a ato não definitivamente julgado (CTN 106, II):
  - "a" e "b": a conduta deixou de ser infração. Exemplos: 361 I "d" e IV revogados em 26/12/2024; 361 V "f" antigo (pagar após o TIAF) em 26/11/2025; dispensas de NFS-e do 321 §3º em 21/03/2024.
  - "c": a pena ficou menor. Exemplos: obstar, de 5.670,21 (I "e", LC 195) para 3.188,76 (V "e", LC 221); MEI com redução de 90% (275, LC 063).
- Para comparar "mais branda", use o valor nominal das duas leis na mesma data-base e registre a escolha. Em caso de dúvida na capitulação ou na graduação, aplica-se o CTN 112.
- Entre 26/12/2024 e 25/11/2025 conviveram o 361 I (LC 195) e o 361 V original. A capitulação de 2025 vai ao titular (PENDENCIAS, item 1).

## 4. Processo e fiscalização
- Norma processual e de fiscalização tem aplicação imediata (CTN 144, §1º), inclusive a fato antigo: novos critérios de apuração (300 §2º "f" e "h", 308), poderes de investigação (315 caput, 55-A) e prazos de procedimento.
- Exceção do mesmo §1º: lei nova não atribui responsabilidade a terceiro por fato anterior. Exemplos: 44 §1º e §3º (21/03/2024) e 249 §14, I (07/01/2021).
- Prazo para atender TIAF ou notificação (315 §4º), pela data da ciência:
  - até 20/03/2024: 5 dias;
  - de 21/03/2024 a 25/12/2024: 10 dias úteis, prorrogáveis;
  - desde 26/12/2024: 15 dias contínuos (art. 106), prorrogáveis.
  - Notificação de autorregularização do Simples (266 §3º, desde 26/11/2025): 30 dias.
- Lavrar os termos (57):
  - 2018: 30 dias + 30;
  - 01/01/2019 a 25/12/2024: 90 dias + 30 ou mais, justificado;
  - desde 26/12/2024: 180 dias + 30 ou mais.
- Ordem de serviço (145 §3º):
  - até 25/11/2025: 90 dias, prorrogáveis pelo Diretor de Tributos;
  - desde 26/11/2025: 180 dias.
  - OS em curso na troca: a extensão automática é discutível (PARCIAL).
- Mudança entre a emissão do TIAF e a ciência: o prazo segue a lei da data da ciência, porque o prazo nasce dela (art. 151). A multa só cabe depois de vencido esse prazo, e a alínea é a da data em que ele venceu. Exemplo: TIAF emitido em 20/11/2025 com ciência em 27/11/2025 tem 15 dias, e a não entrega cai no 361 V "c" da LC 221. Os casos de fronteira vão ao titular.
- Impugnação (art. 200, nunca alterado): 30 dias para lançamento tributário e 15 dias para não tributário. A leitura da multa acessória como 30 dias é decisão do titular de 21/11/2026, não mudança de texto.
- Contencioso do Simples/SIMEI (266):
  - reclamação: 15 dias até 25/11/2025, 30 dias desde 26/11/2025, pela data da ciência;
  - decisão (269): 15 dias em 2018, 90 dias desde 01/01/2019.

## 5. Leis com efeitos diferidos (não confundir vigor com efeito)
- LC 063, 064, 065 e 134: efeitos em 01/01 do ano seguinte à publicação.
- LC 079: efeitos em 01/01/2021.
- LC 099: efeitos em 01/04/2022.
- LC 195: arts. 32, 34, 35 e 38 da lei (455 §1º, 462, Tabela 6 do lixo e 455-A) com efeitos em 01/01/2026.

## 6. Onde o compilado engana (usar o DOM)
- O 150 §4º foi alterado pela LC 195, e o 147 §4º não foi (o original segue em vigor).
- A UPR é o 297 §4º na lei e o §5º no compilado.
- No 469 só o inciso III foi revogado.
- As LC 072, 099 e 127 não estão no compilado.
- Valores das tabelas:
  - Tabela 4 "f": 550,00 por painel;
  - embarque em rodoviária: 2,50;
  - vistoria de táxi: revogada;
  - tarifas aeroportuárias do Grupo II: 93,94 e 5.772,94.
- Detalhe em CONFERENCIA.md e PENDENCIAS.md.
