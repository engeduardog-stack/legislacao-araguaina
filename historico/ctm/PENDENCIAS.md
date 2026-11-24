# Pendências e dúvidas (PARCIAL)

23/11/2026. Cada item diz o motivo da dúvida e qual fonte resolveria. Nada foi inventado: onde faltou fonte, o JSON ficou PARCIAL.

## A. Decisões que vão ao titular ou à Procuradoria
1. **Art. 361 em 2025: duas multas para a mesma conduta.**
   - Entre 26/12/2024 e 25/11/2025 valiam o I novo (LC 195) e o V original, que a LC 195 não revogou.
   - O art. 30 da LC 195 anuncia "inciso I e alíneas a, c, d, e e g", mas o texto traz a, c, e, f.
   - Pares de 2025 (I, LC 195 x V, valor do Dec. 311/2024):
     - entrega fora do prazo: 1.420,55 x 1.426,36;
     - não entrega: 5.670,21 x 1.426,36 (ou x 5.705,45 se houve recusa);
     - obstar: 5.670,21 x 3.188,76 (publicado) / 3.565,89 (retificado);
     - descumprir atos: 3.210,00 x 4.279,08.
   - Resolveria: decisão do titular (CTN 112) e o teor da Emenda Supressiva 1/2024 (Câmara, processo 8705, não lido).
2. **Tabela do art. 310 depois da LC 221.**
   - A LC 221 revogou o art. 310 inteiro. Os arts. 306 e 308 (redação da LC 195) remetem à tabela de percentuais do SINAPI que fica nele.
   - O compilado manteve a tabela sem risco.
   - Resolveria: parecer da Procuradoria. No JSON: `310.tabela`, estado "duvidoso" desde 26/11/2025.
3. **OS em curso em 26/11/2025 (145 §3º).** Não está claro se passa de 90 para 180 dias. Resolveria: decisão do titular (tese de aplicação imediata x ato já praticado).
4. **TIAF emitido antes de uma mudança e com ciência depois** (315 §4º em 21/03/2024 e em 26/12/2024). A regra proposta em REGRAS (lei da data da ciência) precisa de confirmação do titular.
5. **Juros do art. 112 (LC 221).** O débito antigo passa a ter juros sobre o valor atualizado desde 26/11/2025? Posição conservadora registrada; decisão do titular.
6. **Base de comparação de "lei mais branda" no 361** (valor nominal da lei nova x valor antigo corrigido pelo decreto do ano). Muda o resultado em V "a" e V "c" de 2026. Decisão do titular.

## B. Datas de eficácia (selo_data PARCIAL)
7. **Contagem da noventena.**
   - Datas adotadas, como publicação + 90 dias (convenção da casa, VIGENCIA-E-REVOGACOES 2.1): 24/02/2026 (LC 221), 26/03/2025 (LC 195), 20/03/2023 (LC 134), 26/02/2019 (LC 063) e 31/03/2019 (LC 064 e 065).
   - Alternativa conservadora: o dia seguinte de cada uma.
   - Resolveria: decisão do titular sobre a contagem (CTN 210 e jurisprudência).
8. **Qualificação como majoração (data de início incerta):**
   - 311 IV e §3º (cachê e bilheteria, LC 171): 21/03/2024 ou 01/01/2025;
   - 469 §7º e 474 §9º (ITBI na integralização): 21/03/2024 ou 01/01/2025;
   - 379 p.u. (shoppings): 01/01/2025;
   - 308 (piso de 50% e SINAPI): 26/12/2024 ou 26/03/2025;
   - 464 (perda de isenção da taxa do lixo; STF Tema 1383): 2023 ou 01/01/2024;
   - 387 (área total presumida): TVRE em 2027;
   - painel LED da Tabela 4.
   - Resolveria: decisão do titular. O JSON usa a data mais cedo e avisa em obs.
9. **ISS fixo em UPR.** O JSON usa 01/03/2026 (Dec. 101/2025, art. 2º), mas a noventena da LC 221 levaria a 24/02/2026. A data de 01/03/2026 não está na lei; o decreto é mais favorável.
10. **Arts. 375-A a 375-G (LC 079).** Falta o alcance exato do julgamento do STF (ADI 5835, ADPF 499 e ADI 5862, 2023), inclusive a modulação. Resolveria: acórdão no portal do STF.
11. **Fatos do próprio dia 26/11/2025.** A edição 3403 é datada de 26/11 e foi cadastrada na API em 27/11. Resolveria: hora de disponibilização da edição no portal do DOM.
12. **Retificação do Dec. 311/2024** (DOM 3209, 05/02/2025; 361 V "e": 3.188,76 x 3.565,89). Não se sabe se retroage a 01/01/2025. O decreto de 2026 volta a 3.188,76.

## C. Lacunas de texto ou de valor
13. **Anexos III e IV (tabelas de taxas) só em resumo.**
    - Valores originais não conferidos: Tabela 2 do Anexo IV antes da LC 063; Tabela 6 do lixo original; tarifas aeroportuárias originais.
    - Resolveria: leitura linha a linha do DOM 1477, págs. 50 a 68, e dos anexos das LC 063, 134 e 195.
14. **LC 063, Tabela 6 do Anexo IV.** A CONFERENCIA_COMPILADO chama de "área aeroportuária" a Tabela 6 do Anexo IV alterada pela LC 063, e a LC 195 dá esse mesmo número à tabela do lixo. Resolveria: conferir no PDF do DOM 1699.
15. **CNAE 1031-7/00.** Riscado no compilado sem estar entre os 102 da LC 134. Origem desconhecida; tratar como vigente até prova.
16. **Transferência de permissão do escolar (LC 134).** O DOM é ambíguo e o compilado aplicou o novo valor só ao táxi.
17. **Valores por exercício** (ver `valores_por_exercicio.json`, campo `nao_coberto`):
    - ISS fixo e taxas de 2021 a 2025 não levantados;
    - decretos de 2018 a 2020 ausentes da pasta;
    - 362 IV em 2021 sem valor no Dec. 273/2020;
    - 361 II "b", faixa 81 a 100, de 2025 e 2026 (1.709,21 e 1.789,20) foge da progressão;
    - o Dec. 273/2020 declara IPCA de 4,31%, mas os valores sobem cerca de 7,7%;
    - 256-I (R$ 3.500,00) nunca aparece em decreto: atualizado ou não pelo art. 109?
    - Resolveria: leitura do Anexo I de cada decreto e dos decretos de 2018 a 2020 no DOM.
18. **Leis fora do inventário.** A varredura do DOM pegou as leis que citam a "LC 058" ou o "Código Tributário" na ementa. Uma lei que altere o CTM sem isso pode ter escapado. Resolveria: varredura por "passa a vigorar" + número de artigo do CTM.
19. **Arts. 257, 258, 262, 263, 167, 275, 464 e 299** foram tratados como artigo inteiro: a lei reescreveu o artigo, e o JSON não separa inciso por inciso.
20. **Título III (ITBI, 467 a 479) e Título IV (contribuição de melhoria, 480 a 493)** entraram como bloco resumido. Só os dispositivos alterados depois (469 III e §7º, 474 §§7º a 9º) têm chave própria com texto. A lei de ITBI anterior a 2019 não foi lida.
21. **Não houve revisão independente pelo Codex.**

## D. Erros do compilado que o JSON corrige (seguir o DOM)
- 150 §4º: a alteração da LC 195 foi lançada no 147 §4º, cujo texto original segue vigente.
- 297: a UPR é o §4º na lei e o §5º no compilado.
- 469: o compilado diz "Artigo revogado", mas só o inciso III foi revogado.
- LC 072, 099 e 127 não constam do compilado.
- Valores de tabela que o compilado traz errado:
  - Tabela 4 "f": 550,00 por painel;
  - embarque em rodoviária: 2,50;
  - vistoria de táxi: revogada;
  - tarifas do Grupo II: 93,94 e 5.772,94.
- 57 caput (LC 063): o DOM diz "quaisquer diligência", o compilado "diligências" (sem efeito).
