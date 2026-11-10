---
name: validacao-barata
description: Valida uma ideia de renda (plataforma, serviço ou nicho) com testes de até R$100 e 7 dias antes de qualquer investimento. Use quando a operadora quiser testar um modelo novo da Missão R$50k ou decidir se libera orçamento.
---

# Validação barata

Princípio: **só conta o que alguém paga ou aceita, não o que alguém diz.** Opinião, curtida e "achei interessante" valem zero.

## Passos

1. **Escreva a hipótese em uma linha**: "Empresas X pagam US$Y por Z, e eu consigo entregar em W horas."
2. **Liste os 3 riscos** que matam a ideia (sem demanda, sem acesso da operadora no Brasil, hora efetiva baixa, exige aparecer, viola termos de uso).
3. **Cheque termos de uso**: a plataforma aceita residentes no Brasil? Proíbe uso de IA na tarefa? Cobra para entrar (se sim, descartar)?
4. **Desenhe 1 teste por risco**, cada um com:
   - custo máximo (≤ R$100),
   - prazo (≤ 7 dias),
   - número de corte decidido ANTES do teste (ex.: "≥ 2 respostas em 20 propostas").
5. **Rode o teste e registre** o resultado em `missao-50k/rastreador.py` (comando `teste`).
6. **Decida sem renegociar o corte**:
   - passou em todos → liberar o próximo degrau de orçamento (nunca acima do limite do mês);
   - falhou em 1 → ajustar uma variável e rodar uma única vez de novo;
   - falhou de novo → descartar a ideia.

## Saída esperada

Uma tabela com: hipótese, risco, teste, custo, prazo, corte, resultado, decisão.

## Nunca

- Gastar com anúncio antes de ter 1 venda orgânica.
- Pagar curso, mentoria ou taxa de entrada para "validar".
- Usar IA para responder tarefas de plataformas de treinamento de IA que proíbem isso.
