# Índice de alterações do CTM de Araguaína (LCM 058/2017) por dispositivo

Gerado em 23/11/2026 a partir de `ctm_versoes.json`. Janela prioritária: 01/01/2021 a 23/11/2026.

Como ler:
- **Estados**: cada entrada do JSON (redação com texto, "inexistente" antes de o dispositivo ser criado, "revogado" depois de extinto).
- **Redações**: só as entradas com texto (situação "vigente" na época). "Inexistente" e "revogado" não contam como redação, mas contam como estado na janela, porque mudam o resultado da fiscalização.
- **Na janela**: estados que regeram algum dia entre 01/01/2021 e 23/11/2026. 3 ou mais = a mesma fiscalização de 5 anos pode cruzar três regras.
- Datas = primeiro dia em que a redação rege fatos (efeitos da lei; em majoração, anterioridade). Detalhe e textos no JSON.

Totais: 352 chaves (206 dispositivos do texto e anexos + 146 subitens do quadro de alíquotas do art. 290).
- 15 chaves com 3 ou mais ESTADOS na janela (contando inexistente/revogado); 9 com 3 ou mais REDAÇÕES COM TEXTO na janela: 249.§14, 290.quadro.19.01, 290.quadro.21.01, 290.quadro.9.01, 315.§4, 361.I, 361.I.a, 361.I.c, 361.I.e.
- Selo do texto PARCIAL em 22 chaves (resumos de anexos e tabelas, dúvida do 310); selo da data PARCIAL em 175 chaves (noventena ou qualificação como majoração).
- Atenção: 380.§1 chega a 3 estados só por 6 dias de 'inexistente' em jan/2021; 361.I (cabeça do inciso) muda pouco em 2024 ("contáveis" para "contábeis"); 474.§7 tem uma só redação com texto.

## 1. Em destaque: 3 ou mais estados na janela 2021-2026

| Dispositivo | Assunto | Estados na janela | Datas de corte (início de cada regra) |
|---|---|---|---|
| 249.§14 | prazo para pedir baixa | 3 | LC 058/2017: antes de 2021 a 20/03/2024; LC 171/2024: 21/03/2024 a 25/12/2024; LC 195/2024: 26/12/2024 a hoje |
| 310.tabela | tabela de m² da construção civil | 3 | LC 058/2017: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; dúvida (LC 221/2025): 26/11/2025 a hoje |
| 315.§4 | prazo do TIAF/notificação | 3 | LC 058/2017: antes de 2021 a 20/03/2024; LC 171/2024: 21/03/2024 a 25/12/2024; LC 195/2024: 26/12/2024 a hoje |
| 361.I | 361 I: cabeça do inciso | 3 | LC 058/2017: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 361.I.a | 361 I a | 3 | LC 058/2017: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 361.I.c | 361 I c | 3 | LC 058/2017: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 361.I.d | 361 I d | 3 | LC 058/2017: antes de 2021 a 25/12/2024; revogado (LC 195/2024): 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 361.I.e | 361 I e | 3 | LC 058/2017: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 361.I.f | 361 I f | 3 | inexistente: antes de 2021 a 25/12/2024; LC 195/2024: 26/12/2024 a 25/11/2025; LC 221/2025: 26/11/2025 a hoje |
| 380.§1 | validade das licenças por decreto | 3 | inexistente: antes de 2021 a 06/01/2021; LC 080/2021: 07/01/2021 a 20/03/2024; LC 171/2024: 21/03/2024 a hoje |
| 474.§7 | ITBI: imóvel em construção | 3 | inexistente: antes de 2021 a 31/12/2021; LC 080/2021: 01/01/2022 a 25/12/2024; revogado (LC 195/2024): 26/12/2024 a hoje |

Alíquotas do art. 290 com 3 estados na janela:
- 290.quadro.11.05: inexistente (antes de 2021 a 31/12/2024); 11.05: 3% (01/01/2025 a 23/02/2026); 11.05: 5% (24/02/2026 a hoje)
- 290.quadro.19.01: 19.01: 3% (antes de 2021 a 31/12/2021); 19.01: 4% (01/01/2022 a 23/02/2026); 19.01: 5% (24/02/2026 a hoje)
- 290.quadro.21.01: 21.01: 2% (antes de 2021 a 31/12/2021); 21.01: 3,5% (01/01/2022 a 23/02/2026); 21.01: 5% (24/02/2026 a hoje)
- 290.quadro.9.01: 9.01: 4% (antes de 2021 a 06/01/2021); 9.01: 2% (07/01/2021 a 23/02/2026); 9.01: 5% (24/02/2026 a hoje)

## 2. Conduta x alínea do art. 361 por período (busca pela conduta)

A letra da alínea mudou de conduta entre as redações. Procure pela conduta e use a chave do período da infração.

| Conduta | até 25/12/2024 | 26/12/2024 a 25/11/2025 | desde 26/11/2025 |
|---|---|---|---|
| Entregar fora do prazo (TIAF/NF) | V 'a' (não apresentar no prazo, base 1.030,00) | V 'a' (2025: 1.426,36) ou I 'a' LC 195 (1.420,55): DEPENDE | V 'a' 1.426,36 |
| Não entregar / entregar ilegível ou inexato | V 'a' (não apresentação); I 'd' só para LIVROS (1.545,00) | I 'c' LC 195 (5.670,21) ou V 'a' (1.426,36); V 'c' só se RECUSA: DEPENDE | V 'c' 5.705,45 |
| Recusar a exibição | V 'c' (base 4.120,00) | V 'c' (2025: 5.705,45) | embaraço: V 'd' 5.705,45 (§1º define) |
| Desacato / embaraço / resistência | V 'd' (base 4.120,00) | V 'd' (2025: 5.705,45) | V 'd' 5.705,45 (§§1º e 2º) |
| Obstar ou dificultar | V 'e' (base 2.575,00) | V 'e' (3.188,76 publicado / 3.565,89 retificado) ou I 'e' LC 195 (5.670,21): DEPENDE | V 'e' 3.188,76 (mais branda: retroage a autos não definitivos) |
| Descumprir atos (retificar, emitir, cancelar) | V 'g' (base 3.090,00) | V 'g' (4.279,08) ou I 'f' LC 195 (3.210,00): DEPENDE | V 'f' 4.279,08 (mais grave que 3.210: não retroage) |
| Pagar ISS/taxa após o TIAF sem autorização | V 'f' (base 2.203,99) | V 'f' (2025: 3.052,12) | sem multa própria (CTN 106 II 'a') |
| Livros fiscais sem autenticação | I 'a' (824,00) | sem alínea (I 'a' mudou de conduta) | sem alínea |
| Livros em desacordo com as normas | I 'b' (824,00) | I 'b' (2025: 1.141,09) | I 'a' 1.141,09 |
| Deixar de lançar o imposto no livro | I 'c' (309,00) | sem alínea | sem alínea |
| Não comunicar inutilização/extravio de documentos | I 'e' (824,00) | sem alínea | sem alínea (para NFS: II 'i') |
| Não apresentar LIVROS no prazo | I 'd' (1.545,00) | revogada (ver V 'a') | ver V 'a' / V 'c' |
| Impressão de documentos fiscais | IV 'a' a 'c' | revogado | revogado |
| Fraude/omissão nos livros | sem alínea | sem alínea | I 'b' 5.670,21 |
| Documento com valor inferior ou declaração falsa | sem alínea (ver II 'g' por nota) | sem alínea | I 'c' 1.420,55 |
| Documento sem serviço prestado | sem alínea | sem alínea | I 'd' 1.420,55 |
| Cancelamento indevido de NFS-e | II 'h' se fraudulento (515,00/nota) | II 'h' | I 'e' 100% do imposto (e II 'h') |
| Não transmitir EFD / outra declaração | sem alínea | sem alínea | I 'f' / I 'g' 1.420,55 por exercício |

Valores por exercício: `valores_por_exercicio.json`. O inciso II (NFS-e), o III e o art. 362 I a III não mudaram de texto desde 2017 (só os valores anuais).

## 3. Todos os dispositivos alterados

| Dispositivo | Assunto | Estados | Redações | Estados na janela | Redações na janela | Linha do tempo | Selo |
|---|---|---|---|---|---|---|---|
| 9.III.b | imunidade de templos | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 9.§1 | imunidade recíproca | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 9.§2 | exclusão da imunidade | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 18.pu | intimação preferencialmente eletrônica | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 32.caput | Domicílio Eletrônico do Contribuinte | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 44.§1 | substituto tributário: nomeação por IN | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 44.§3 | solidariedade em eventos | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 55-A | requisição de dados cadastrais e patrimoniais | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 55-B | dever de colaboração de órgãos públicos | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 57.caput | prazo para lavrar os termos do procedimento fiscal | 3 | 3 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 63.caput | moratória | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 70.§3 | pagamento por cartão de crédito | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 77.§1.II | interrupção da prescrição pelo protesto | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 77.§3 | prescrição reconhecida de ofício | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 77.§4 | regulamento da prescrição de ofício | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 85.III | isenção de ofício | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 85.§3 | efeitos do despacho de isenção | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 87 | isenção x débitos anteriores | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 171/2024) desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 95.IV | cancelamento de débito de pessoa física | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 101.caput | conceito de infração | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 105.caput | representação fiscal para fins penais | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 109.caput | atualização monetária anual | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 110.pu | termo inicial da atualização | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 112.caput | juros de mora | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 113 | multa de mora (pagamento espontâneo) | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 114 | multa de ofício (ação fiscal) | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 115.caput | multa por sonegação/fraude | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 119.caput | princípios do processo | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 145.§3 | prazo da ordem de serviço | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data PARCIAL |
| 147-A | devedor contumaz | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 147.caput | regime especial de fiscalização | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 150.§4 | recusa de assinatura da notificação | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 156.§2 | julgador substituto | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 167 | Conselho Municipal de Contribuintes (8 para 7 membros) | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 217 | parcela mínima do parcelamento | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 218 | rescisão do parcelamento | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 220-A | liquidação antecipada do parcelamento | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 220.pu | parcelamento de débito ajuizado | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 223-A | pedido de restituição/compensação | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 230 | isenção de ITBI (dação ao Município) | 2 | 1 | 1 | 0 | LC 058/2017 desde 01/01/2018 > revogado (LC 063/2018) desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 234.§3 | retroação de benefício reconhecido | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 242.IV | Cadastro eletrônico de Contribuintes e NFS-e obrigatória | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 242.§4 | Cadastro eletrônico de Contribuintes e NFS-e obrigatória | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 242.§5 | Cadastro eletrônico de Contribuintes e NFS-e obrigatória | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 242.§6 | Cadastro eletrônico de Contribuintes e NFS-e obrigatória | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 247 | desconto de recadastramento do IPTU | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 249.§11 | inscrição sem força de licenciamento | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 249.§13 | paralisação temporária | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 249.§14 | prazo para pedir baixa | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 249.§14.I | solidariedade na baixa | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 249.§5 | alvará provisório | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 249.§6 | condição do alvará provisório | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 249.§9 | prazo de comunicação cadastral | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 250.§1 | suspensão da inscrição | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 250.§2 | inscrição | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 250.§3 | inscrição antes do início | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 251.caput | atualização cadastral | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 252.caput | comunicação de cessão e encerramento | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 252.§1.I | baixa x lançamento posterior | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 256-A_a_256-L | escritório virtual e coworking | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 127/2022 desde 08/12/2022 | texto VERIFICADO / data VERIFICADO |
| 256-I | multa do coworking | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 127/2022 desde 08/12/2022 | texto VERIFICADO / data VERIFICADO |
| 257 | requisitos do MEI | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 258 | análise de receitas do MEI | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 260.pu | MEI: alvará | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 261-A | MEI: alteração de cadastro em 30 dias | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 262 | desenquadramento do SIMEI | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 263 | exclusão de ofício do Simples Nacional | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 266.caput | contencioso de exclusão do Simples/SIMEI | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 266.§1 | rito do contencioso do Simples | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 266.§3 | prazo da autorregularização | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 269.caput | prazo de decisão (Simples) | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 274.caput | MEI: taxas de licença | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 064/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 274.pu | MEI mototaxista/taxista | 3 | 1 | 1 | 0 | inexistente desde 01/01/2018 > LC 060/2018 desde 19/04/2018 > revogado (LC 064/2018) desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 275 | MEI: redução de multas acessórias | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 277.11.05 | lista de serviços: 11.05 rastreamento | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 01/01/2025 | texto VERIFICADO / data VERIFICADO |
| 279.IV | não incidência: sem intenção de lucro | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/03/2025 | texto VERIFICADO / data PARCIAL |
| 282.III | local de incidência: obra | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 282.XXIII | local de incidência: tomador | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§10 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§11 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§12 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§5 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§6 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§7 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§8 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 282.§9 | conceito de tomador (LC 175) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 283.§4.II | responsável tomador PJ | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 283.§4.IV | responsável: cartões | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 283.§5 | 10.04 e 15.09 no tomador | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 080/2021) desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 290.caput | alíquotas do ISSQN (estrutura) | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 290.quadro.1.01 | alíquota do subitem 1.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.02 | alíquota do subitem 1.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.03 | alíquota do subitem 1.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.04 | alíquota do subitem 1.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.05 | alíquota do subitem 1.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.06 | alíquota do subitem 1.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.07 | alíquota do subitem 1.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.1.08 | alíquota do subitem 1.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.01 | alíquota do subitem 10.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.02 | alíquota do subitem 10.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.03 | alíquota do subitem 10.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.04 | alíquota do subitem 10.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.05 | alíquota do subitem 10.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.06 | alíquota do subitem 10.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.07 | alíquota do subitem 10.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.08 | alíquota do subitem 10.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.09 | alíquota do subitem 10.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.10.10 | alíquota do subitem 10.10 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.11.01 | alíquota do subitem 11.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.11.02 | alíquota do subitem 11.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.11.03 | alíquota do subitem 11.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.11.04 | alíquota do subitem 11.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.11.05 | alíquota do subitem 11.05 | 3 | 2 | 3 | 2 | inexistente desde 01/01/2018 > LC 171/2024 desde 01/01/2025 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.13.02 | alíquota do subitem 13.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.13.03 | alíquota do subitem 13.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.13.04 | alíquota do subitem 13.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.13.05 | alíquota do subitem 13.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.01 | alíquota do subitem 14.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.02 | alíquota do subitem 14.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.03 | alíquota do subitem 14.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.04 | alíquota do subitem 14.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.05 | alíquota do subitem 14.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.06 | alíquota do subitem 14.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.07 | alíquota do subitem 14.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.08 | alíquota do subitem 14.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.09 | alíquota do subitem 14.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.10 | alíquota do subitem 14.10 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.11 | alíquota do subitem 14.11 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.12 | alíquota do subitem 14.12 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.14.13 | alíquota do subitem 14.13 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.16.01 | alíquota do subitem 16.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.16.02 | alíquota do subitem 16.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.01 | alíquota do subitem 17.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.02 | alíquota do subitem 17.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.03 | alíquota do subitem 17.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.04 | alíquota do subitem 17.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.05 | alíquota do subitem 17.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.06 | alíquota do subitem 17.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.09 | alíquota do subitem 17.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.10 | alíquota do subitem 17.10 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.11 | alíquota do subitem 17.11 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.12 | alíquota do subitem 17.12 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.13 | alíquota do subitem 17.13 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.14 | alíquota do subitem 17.14 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.15 | alíquota do subitem 17.15 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.16 | alíquota do subitem 17.16 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.17 | alíquota do subitem 17.17 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.18 | alíquota do subitem 17.18 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.19 | alíquota do subitem 17.19 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.20 | alíquota do subitem 17.20 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.21 | alíquota do subitem 17.21 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.17.22 | alíquota do subitem 17.22 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.18.01 | alíquota do subitem 18.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.19.01 | alíquota do subitem 19.01 | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 01/01/2022 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.2.01 | alíquota do subitem 2.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.20.01 | alíquota do subitem 20.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.20.02 | alíquota do subitem 20.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.20.03 | alíquota do subitem 20.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.21.01 | alíquota do subitem 21.01 | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 01/01/2022 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.22.01 | alíquota do subitem 22.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.23.01 | alíquota do subitem 23.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.24.01 | alíquota do subitem 24.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.25.01 | alíquota do subitem 25.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.25.02 | alíquota do subitem 25.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.25.03 | alíquota do subitem 25.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.25.04 | alíquota do subitem 25.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.26.01 | alíquota do subitem 26.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.27.01 | alíquota do subitem 27.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.28.01 | alíquota do subitem 28.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.29.01 | alíquota do subitem 29.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.3.02 | alíquota do subitem 3.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.3.03 | alíquota do subitem 3.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.3.04 | alíquota do subitem 3.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.3.05 | alíquota do subitem 3.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.30.01 | alíquota do subitem 30.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.31.01 | alíquota do subitem 31.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.32.01 | alíquota do subitem 32.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.33.01 | alíquota do subitem 33.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.34.01 | alíquota do subitem 34.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.35.01 | alíquota do subitem 35.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.36.01 | alíquota do subitem 36.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.37.01 | alíquota do subitem 37.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.38.01 | alíquota do subitem 38.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.39.01 | alíquota do subitem 39.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.04 | alíquota do subitem 4.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.05 | alíquota do subitem 4.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.06 | alíquota do subitem 4.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.07 | alíquota do subitem 4.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.08 | alíquota do subitem 4.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.09 | alíquota do subitem 4.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.10 | alíquota do subitem 4.10 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.12 | alíquota do subitem 4.12 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.14 | alíquota do subitem 4.14 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.15 | alíquota do subitem 4.15 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.16 | alíquota do subitem 4.16 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.17 | alíquota do subitem 4.17 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.18 | alíquota do subitem 4.18 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.19 | alíquota do subitem 4.19 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.20 | alíquota do subitem 4.20 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.4.21 | alíquota do subitem 4.21 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.40.01 | alíquota do subitem 40.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.01 | alíquota do subitem 5.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.02 | alíquota do subitem 5.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.03 | alíquota do subitem 5.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.04 | alíquota do subitem 5.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.05 | alíquota do subitem 5.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.06 | alíquota do subitem 5.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.07 | alíquota do subitem 5.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.08 | alíquota do subitem 5.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.5.09 | alíquota do subitem 5.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.6.01 | alíquota do subitem 6.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.6.02 | alíquota do subitem 6.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.6.03 | alíquota do subitem 6.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.6.04 | alíquota do subitem 6.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.6.05 | alíquota do subitem 6.05 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.01 | alíquota do subitem 7.01 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.03 | alíquota do subitem 7.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.04 | alíquota do subitem 7.04 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.06 | alíquota do subitem 7.06 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.07 | alíquota do subitem 7.07 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.08 | alíquota do subitem 7.08 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.09 | alíquota do subitem 7.09 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.10 | alíquota do subitem 7.10 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.11 | alíquota do subitem 7.11 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.12 | alíquota do subitem 7.12 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.13 | alíquota do subitem 7.13 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.16 | alíquota do subitem 7.16 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.17 | alíquota do subitem 7.17 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.18 | alíquota do subitem 7.18 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.19 | alíquota do subitem 7.19 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.20 | alíquota do subitem 7.20 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.21 | alíquota do subitem 7.21 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.7.22 | alíquota do subitem 7.22 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.9.01 | alíquota do subitem 9.01 | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.9.02 | alíquota do subitem 9.02 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 290.quadro.9.03 | alíquota do subitem 9.03 | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 297.§4_UPR | UPR (R$ 1,00) | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 299 | ISS fixo: revisão | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 300.§2.f | arbitramento: atualização ou deflação | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 300.§2.h | arbitramento: base do autônomo | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 302 | base da construção civil: deduções | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 305 | incorporação: base | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 306.caput | valores mínimos de mão de obra | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 306.§1 | redução para demolição e reforma | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 306.§2 | pequenos reparos | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data VERIFICADO |
| 308 | arbitramento da construção civil | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 309 | materiais fora da base (7.02/7.05) | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 310 | incorporação imobiliária: ISS x ITBI | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 310.tabela | tabela de m² da construção civil | 3 | 2 | 3 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > dúvida (LC 221/2025) desde 26/11/2025 | texto PARCIAL / data PARCIAL |
| 311.IV | diversões: cachê do artista | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data PARCIAL |
| 311.§3 | diversões: bilheteria x mínimo | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 315.caput | TIAF/notificação: objeto | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 315.§1 | TIAF/notificação: forma de entrega | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 315.§10 | entrega a pessoa presente no local | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 315.§4 | prazo do TIAF/notificação | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 321.§3 | dispensa de NFS-e | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 321.§4 | dispensados de NFS-e mantêm registro | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 331.pu | dispensa de gerar notas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 333.§1 | cancelamento de NFS-e: prazo do pedido | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 333.§1-A | cancelamento de NFS-e sem intervenção | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 343.§7 | NFS avulsa: cancelamento | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 356.caput | conceito de infração (penalidades) | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 356.pu | concurso de infrações | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 361.I | 361 I: cabeça do inciso | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.a | 361 I a | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.b | 361 I b | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.c | 361 I c | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.d | 361 I d | 3 | 2 | 3 | 2 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.e | 361 I e | 3 | 3 | 3 | 3 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.f | 361 I f | 3 | 2 | 3 | 2 | inexistente desde 01/01/2018 > LC 195/2024 desde 26/12/2024 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.I.g | 361 I g | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.IV | 361 IV: cabeça do inciso | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 361.IV.a | 361 IV a | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 361.IV.b | 361 IV b | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 361.IV.c | 361 IV c | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 361.V | 361 V: cabeça do inciso | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.a | 361 V a | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.b | 361 V b | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.c | 361 V c | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.d | 361 V d | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.e | 361 V e | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.f | 361 V f | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.V.g | 361 V g | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 221/2025) desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.caput | multas fixas: destinatários | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 361.§1 | 361 §1º: embaraço | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 361.§2 | 361 §2º: resistência | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 362.IV | multa cadastral do MEI | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 372.caput | Calendário Fiscal para todos os tributos | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 375-A | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-B | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-C | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-D | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-E | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-F | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 375-G | padrão nacional (LC 175) | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 079/2020 desde 01/01/2021 | texto VERIFICADO / data PARCIAL |
| 377-A | momento do fato gerador das taxas de licença | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 377.II | fato gerador da TVRE | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 379.pu | TLL/TVRE em shoppings | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 01/01/2025 | texto VERIFICADO / data PARCIAL |
| 380-A | dispensa de TVRE | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 380.II.a | TVRE anual | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 380.II.b | TVRE de autônomos | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 171/2024) desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 380.§1 | validade das licenças por decreto | 3 | 2 | 3 | 2 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 380.§2 | renovação da licença | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 380.§3 | temporários | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 383.§9 | MEI sem alvará | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 385.§1 | exigências mínimas para alvará | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 385.§3.VI | assinatura do alvará | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 26/11/2025 | texto VERIFICADO / data VERIFICADO |
| 387.caput | estabelecimentos no mesmo imóvel | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 387.§1 | estabelecimentos no mesmo imóvel | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 387.§2 | estabelecimentos no mesmo imóvel | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 387.§3 | estabelecimentos no mesmo imóvel | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 221/2025 desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 392-A | taxistas e mototaxistas: dispensa de taxas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 444 | isenções de taxas de licença | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto VERIFICADO / data VERIFICADO |
| 446.§1 | taxas de licença: multa de mora | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 446.§2 | taxas de licença: multa de ofício | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 455-A | taxa do lixo: transição | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 195/2024 desde 01/01/2026 | texto VERIFICADO / data VERIFICADO |
| 455.§1 | taxa do lixo: rateio | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 01/01/2026 | texto VERIFICADO / data VERIFICADO |
| 458 | taxa do lixo: parcelamento | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 462.caput | taxa do lixo: desconto | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 01/01/2026 | texto VERIFICADO / data VERIFICADO |
| 464 | taxa do lixo: isenção | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data PARCIAL |
| 464-A | taxa do lixo: isenções novas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 464-B | taxa do lixo: isenções novas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 464-C | taxa do lixo: isenções novas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 464-D | taxa do lixo: isenções novas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 464-E | taxa do lixo: isenções novas | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto VERIFICADO / data VERIFICADO |
| 465 | grandes geradores de resíduos | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 467_a_479_ITBI | ITBI no CTM | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto PARCIAL / data VERIFICADO |
| 469.III | ITBI: alienação fiduciária | 3 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 063/2018 desde 01/01/2019 > revogado (LC 221/2025) desde 24/02/2026 | texto VERIFICADO / data PARCIAL |
| 469.§7 | ITBI: integralização de capital | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data PARCIAL |
| 474.§7 | ITBI: imóvel em construção | 3 | 1 | 3 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 01/01/2022 > revogado (LC 195/2024) desde 26/12/2024 | texto VERIFICADO / data VERIFICADO |
| 474.§8 | ITBI: terreno com obra do adquirente | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 080/2021 desde 07/01/2021 | texto VERIFICADO / data VERIFICADO |
| 474.§9 | ITBI: excedente do capital | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 171/2024 desde 21/03/2024 | texto VERIFICADO / data VERIFICADO |
| 480_a_493_contribuicao_melhoria | contribuição de melhoria | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 064/2018 desde 01/01/2019 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab1.itens1.1-1.2.c-d | taxas de licença: tabelas especiais | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 195/2024) desde 26/03/2025 | texto PARCIAL / data PARCIAL |
| AnexoIII.Tab4.demais | licença de publicidade: demais itens | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab4.f_painel_LED | licença de publicidade: painel LED | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 134/2022 desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab4.g_outdoor | licença de publicidade: outdoor | 3 | 3 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 065/2018 desde 31/03/2019 > LC 134/2022 desde 01/01/2023 | texto PARCIAL / data PARCIAL |
| AnexoIII.Tab6.102_CNAE | vigilância sanitária: 102 CNAEs | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab6.CNAE_4930-2 | vigilância sanitária: transporte de carga | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 072/2019 desde 27/12/2019 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab7_ambiental | taxas ambientais e de planejamento | 3 | 3 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 > LC 099/2021 desde 01/04/2022 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab8.apreensao_clandestino | apreensão de clandestino | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 134/2022 desde 20/03/2023 | texto PARCIAL / data PARCIAL |
| AnexoIII.Tab8.embarque_rodoviaria | embarque em rodoviária | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab8.itens_acrescidos_LC134 | trânsito: itens acrescidos | 2 | 1 | 2 | 1 | inexistente desde 01/01/2018 > LC 134/2022 desde 20/03/2023 | texto PARCIAL / data PARCIAL |
| AnexoIII.Tab8.itens_revogados_LC134 | trânsito: itens revogados | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab8.tarifas_aeroportuarias | tarifas aeroportuárias | 3 | 3 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 > LC 134/2022 desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab8.taxi_vistoria | táxi: vistoria | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIII.Tab8.transferencia_permissao | transferência de permissão | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 134/2022 desde 20/03/2023 | texto PARCIAL / data PARCIAL |
| AnexoII_ISS_fixo | ISS fixo do autônomo | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 221/2025 desde 01/03/2026 | texto PARCIAL / data VERIFICADO |
| AnexoIV.Tab2 | taxas de expediente | 2 | 2 | 1 | 1 | LC 058/2017 desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto PARCIAL / data VERIFICADO |
| AnexoIV.Tab4.vigilancia_atos | atos da vigilância sanitária | 2 | 1 | 2 | 1 | LC 058/2017 desde 01/01/2018 > revogado (LC 134/2022) desde 01/01/2023 | texto PARCIAL / data VERIFICADO |
| AnexoIV.Tab6.taxa_lixo | taxa do lixo: tabela | 2 | 2 | 2 | 2 | LC 058/2017 desde 01/01/2018 > LC 195/2024 desde 01/01/2026 | texto PARCIAL / data VERIFICADO |
| AnexoV_ITBI | modelo de certidão do ITBI | 2 | 1 | 1 | 1 | inexistente desde 01/01/2018 > LC 063/2018 desde 01/01/2019 | texto PARCIAL / data VERIFICADO |

## 4. Fora do índice (sem alteração de texto, conferidos)
Arts. 78, 106, 116, 149, 151, 195, 196, 200, 300 (salvo §2º 'f' e 'h'), 311 I a III e §§1º-2º, 312 a 314, 315 §§2º-3º e 5º a 9º, 361 II e III, 362 I a III, 363 a 366, 446 §3º e 147 §4º (o compilado o mostra riscado por erro: o texto original segue em vigor; ver 150.§4).
