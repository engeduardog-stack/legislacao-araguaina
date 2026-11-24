# Conferência por amostragem: JSON x Diário Oficial

Data: 23/11/2026. Somente leitura das fontes. Textos do DOM: `C:\AUDITORIAS-IA\_ESTUDO_CONCLUIDOS\LEIS_ALTERADORAS_CTM\DOM\*.txt` (extraídos dos PDFs das edições).

## 1. Conferência automática (todas as entradas com texto)
- Como foi feita: o texto de cada redação foi normalizado (sem acento, pontuação, hifenização e marcas de página) e procurado em janelas de 6 palavras no DOM da lei que o introduziu. A redação original foi procurada no DOM 1477.
  - Resultado: 0 entradas abaixo de 85%. As redações com texto integral ficaram VERIFICADO.
  - As 43 entradas PARCIAL são resumos (anexos e tabelas), revogações sem texto ou a dúvida da tabela do art. 310.
- O teste pega erro:
  - Na 1ª rodada, a alínea 361 I "d" da LC 221 foi tirada da ocorrência errada do compilado (o texto revogado de 2017). A conferência deu 18% e a entrada caiu para PARCIAL até ser corrigida.
  - O 150 §4º da LC 195 não está no compilado (ver item 2, nº 5). O texto veio do DOM 3183 e casou 100%.
- Quadro de alíquotas do art. 290: o quadro original foi lido direto do DOM 1477 e comparado, por programa, com o quadro riscado do compilado (anterior à LC 221).
  - Só 4 subitens diferem, todos explicados por lei: 9.01 (4% para 2%), 19.01 (3% para 4%) e 21.01 (2% para 3,5%) pela LC 080, e 11.05 (novo, 3%) pela LC 171.
  - Isso confirma os outros subitens nos dois textos.
- Redações originais tiradas do DOM 1477 conferidas contra o trecho riscado do compilado: 104 de 106 com 80% ou mais. As 2 restantes (361 I "a" e "b") diferem só por erro de digitação do DOM ("quantro"), que o compilado corrigiu.

## 2. Amostra conferida à mão (10 dispositivos)

| Nº | Chave / entrada | Lei e período no JSON | Onde no DOM | Resultado |
|---|---|---|---|---|
| 1 | 113, redação original | LC 058, 01/01/2018 a 25/12/2024 | DOM 1477, txt linha 1553 (art. 113 e incisos I a VII, 2% a 20%) | CONFERE |
| 2 | 57.caput, LC 063 | 01/01/2019 a 25/12/2024 (efeitos pelo art. 19, txt da LC 063 linha 1605) | DOM 1699, linhas 21 a 29 (90 dias + 30) | CONFERE no conteúdo. Diferença do compilado: o DOM diz "quaisquer diligência", o compilado "diligências" (sem efeito) |
| 3 | 44.§1, LC 171 | desde 21/03/2024 | DOM 2995, linha 22 ("Outras empresas ou entidades poderão ser nomeadas...") | CONFERE |
| 4 | 315.§4, LC 171 | 21/03/2024 a 25/12/2024 | DOM 2995, linha 153 (10 dias úteis, prorrogável) | CONFERE |
| 5 | 150.§4, LC 195 | desde 26/12/2024 | DOM 3183, linhas 175 a 182 (art. 17 da LC 195: "O §4º do Art. 150 ... passa a vigorar...") | CONFERE com o DOM. **O compilado erra**: lançou esse texto no art. 147 §4º, riscou o 147 §4º original e deixou o 150 §4º com o texto de 2017, sem nota. O JSON segue o DOM |
| 6 | 217, LC 195 | desde 26/12/2024 | DOM 3183, linhas 183 a 195 (R$ 155,52 / R$ 310,97 e p.u. do art. 109) | CONFERE (89% na automática só pela quebra de página no meio do texto) |
| 7 | 361.I.c, LC 195 | 26/12/2024 a 25/11/2025 | DOM 3183, linha 440 (R$ 5.670,21, não entrega) | CONFERE. No mesmo DOM, o art. 30 anuncia "alíneas a, c, d, e e g" e o texto traz a, c, e, f: defeito da lei, registrado em obs e em PENDENCIAS |
| 8 | 145.§3, LC 221 | desde 26/11/2025 | DOM 3403, linha 90 (180 dias) | CONFERE |
| 9 | 361.V.c, LC 221 | desde 26/11/2025 | DOM 3403, linha 208 (R$ 5.705,45, não entregar) | CONFERE |
| 10 | 362.IV, LC 080 | desde 07/01/2021 | DOM 2220, linha 424 (R$ 3.090,00, MEI) | CONFERE |

Datas de vigência e efeitos conferidas no texto do DOM de cada lei:
- LC 060 art. 2º
- LC 063 art. 19 (efeitos 01/01/2019)
- LC 064 art. 3º e LC 065 art. 4º (efeitos 01/01/2019)
- LC 072 art. 2º
- LC 079 art. 2º (efeitos 01/01/2021)
- LC 080 art. 21
- LC 099 art. 10 (efeitos 01/04/2022)
- LC 127 art. 2º
- LC 134 art. 29 (efeitos 01/01/2023)
- LC 171 art. 4º
- LC 195 art. 39 (exceções em 01/01/2026)
- LC 221 art. 5º
- LC 058 art. 466 ("a partir de 1º de janeiro")

## 3. Outros pontos conferidos nesta tarefa
- CNAE 4930-2/01 e 4930-2/02:
  - R$ 243,50 no DOM 1477 (txt linhas 9680 a 9687) e R$ 110,00 pela LC 072;
  - os dois NÃO aparecem no texto da LC 134 (nenhuma ocorrência de "4930" no DOM 2693), logo não estão entre os 102 CNAEs revogados.
- Embarque em rodoviária: R$ 2,57 no DOM 1477 (linha 10047) e R$ 2,50 pela LC 063, art. 16 (CONFERENCIA_COMPILADO).
- Art. 256-I (LC 127): R$ 3.500,00 nos incisos I e II (DOM 2685, linhas 215 a 226).
- Valores dos decretos: a série 361 V "a" de 2021 a 2025 (1.109,10; 1.228,22; 1.300,68; 1.361,55; 1.426,36) confere com a LINHA_DO_TEMPO_CTM (tabela 2.1). O subagente que montou `valores_por_exercicio.json` conferiu por script cada um dos 330 valores VERIFICADO na página citada do decreto.

## 4. Limites
- A conferência automática confirma que o texto existe no DOM da lei. Não confirma, sozinha, que ele está na chave certa.
  - Nas chaves do núcleo da fiscalização (44, 57, 113 a 115, 145, 150, 217, 218, 249, 266, 290, 300, 311, 315, 356, 361, 362 e 446), a escolha da ocorrência foi revisada à mão.
  - Nas demais, a escolha seguiu as notas do compilado e as listas de dispositivos do DOM.
- O limite de 85% não pega contaminação em texto longo, quando um trecho estranho pesa pouco no total.
  - Foi o caso da redação original do `290.caput`: o quadro riscado do compilado, com as notas da LC 080, foi junto (28 mil caracteres) e mesmo assim passou.
  - Correção: o texto passou a vir do DOM 1477 e é cortado no "Quadro de Alíquotas".
  - Depois disso, uma varredura de todos os textos procurou notas do compilado ("LC nº", "alterada pela", "Redação dada", "Revogad", "Vigência a partir") e textos fora do tamanho normal. Não sobrou contaminação; os casos de "acrescidos" nos arts. 263 e 455-A são texto da própria lei.
- Na mesma revisão, 21 chaves "caput" pegavam o artigo original inteiro; foram corrigidas para só o caput.
- Anexos (tabelas de taxas) estão em resumo, sem conferência linha a linha (PARCIAL).
- Não houve revisão independente pelo Codex nesta tarefa.
