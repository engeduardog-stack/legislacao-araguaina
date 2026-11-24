# Base de consulta para IA: legislação de Araguaína/TO

Texto da legislação tributária (municipal, federal, CGSN), jurisprudência do STF/STJ e índices oficiais, para a IA
consultar **sem abrir PDF**. É a **fonte única**: skills, extensões e chats leem daqui e não guardam cópia própria.
Gerada automaticamente (`build_base.py`, toda semana); **nunca se edita à mão**.

## Como consultar (barato)
1. Abra `INDICE.json`: lista tudo, com situação (vigente, não vigente) e caminho.
2. Artigo de norma vigente: `legislacao/vigente/<SIGLA>/art-<N>.md` (ex.: `legislacao/vigente/CTM/art-361.md`).
   Endereço direto: `https://raw.githubusercontent.com/engeduardog-stack/legislacao-araguaina/main/legislacao/vigente/CTM/art-361.md`
3. Trechos marcados `RISCADO NO PDF` são redação antiga: só valem para fato anterior à alteração.
4. Norma não vigente ou histórica: `legislacao/nao-vigente/`. Outras normas e decretos: `legislacao/vigente-outros/`.
5. CGSN: `cgsn/INDICE.csv`; redação por data em `cgsn/original`, `cgsn/vigente`, `cgsn/multivigente`.
6. Jurisprudência: `jurisprudencia/itens.jsonl` (uma linha por súmula ou tema, com `situacao`).
7. Índices: `indices/` (IPCA com data de divulgação, Selic, TR, IGP-M).
8. Histórico por data do CTM: `historico/ctm/ctm_versoes.json` (cada redação de cada dispositivo, com `de`/`ate`, lei, selos de verificação), `valores_por_exercicio.json`, `INDICE-ALTERACOES.md`, `REGRAS-DE-APLICACAO.md` e `PENDENCIAS.md`. Consulta local: `lei.py ctm 361 --data dd/mm/aaaa`.

## Regra de ouro: norma pela data do fato
Um mesmo dispositivo pode ter tido várias redações no período fiscalizado (em regra, 5 anos). Antes de citar,
liste **todas** as redações do período e aplique cada uma ao fato da sua data; penalidade mais branda retroage
(CTN, art. 106, II, "c"); majoração de tributo exige anterioridade e noventena. Não trate o texto compilado
como a única redação.

## Limites
- Quatro documentos antigos são imagem sem texto; o cabeçalho de cada arquivo indica páginas sem texto.
- Em dúvida, vale o PDF original e o Diário Oficial. Isto é uma ferramenta de consulta, não a publicação oficial.
