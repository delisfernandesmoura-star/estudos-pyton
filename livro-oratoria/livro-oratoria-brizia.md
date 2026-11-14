# Memória: livro de oratória "Voz, Palco e Presença"

- **Título de trabalho:** Voz, Palco e Presença. **Subtítulo:** Oratória com ciência, da preparação vocal à grande apresentação. A cliente não escolheu título ("sem preferência"); confirmar com ela.
- **Autora:** Dra. Brízia Lacerda.
- **Formato:** PDF premium de 17 × 24 cm, com 126 páginas (o pedido era "umas 120").

## Pedido da cliente
- Pegar o principal dos livros de oratória mais vendidos nos EUA, sem contrariar os princípios da fonoaudiologia e a literatura fonoaudiológica brasileira. Somar a isso o conteúdo do livro principal ("Voz, Canto e Ciência").
- **Ordem obrigatória:**
  1. princípios: produção da voz, higiene vocal, aquecimento e desaquecimento;
  2. preparação, exercícios e dicas técnicas;
  3. capacitação: comunicação;
  4. palco e treinamento.

## Estrutura (4 partes, 16 capítulos)
- **I · O Instrumento:**
  1. A voz de quem fala em público
  2. Como a voz é produzida
  3. Higiene vocal
- **II · Preparação Vocal:**
  4. Postura e respiração
  5. Aquecimento
  6. Desaquecimento e recuperação
  7. Articulação e dicção
  8. Ressonância e projeção
- **III · Técnica de Comunicação:**
  9. Recursos vocais
  10. Presença
  11. A mensagem que fica
  12. Improviso e conversas difíceis
- **IV · Palco e Treinamento:**
  13. Ansiedade e confiança
  14. A preparação do palco
  15. Cada palco, uma voz
  16. Plano de 8 semanas

## Base e referências
- **Livros americanos:** Anderson (TED), Gallo (Talk Like TED), Heath & Heath (Made to Stick), Abrahams, Carnegie, Berkun, Fisher, Hasan e Roger Love. As ideias foram parafraseadas e creditadas.
- **Literatura brasileira:**
  - Behlau (2001);
  - Behlau & Pontes (Higiene vocal);
  - Behlau, Dragone & Nagano (A voz que ensina);
  - Kyrillos (Expressividade);
  - Kyrillos & Jung (Comunicar para liderar);
  - Polito;
  - Lei nº 6.965/1981.
- **Ciência:** Titze (1994 e 2006) e Alves et al. (2019).
- **Pendência:** confirmar a edição e o ano de Polito ("Como falar corretamente e sem inibições", Saraiva).

## Ética (CFFa)
- Livro educativo, sem promessas, sem diagnóstico e sem orientação de medicamentos.
- Receitas caseiras (mel, gengibre, pastilhas) não aparecem como tratamento.
- Ansiedade intensa leva ao psicólogo ou ao médico.
- Papéis separados entre fonoaudiólogo, médico e treinador.

## Visual
- Mesmo padrão premium do "Voz, Canto e Ciência": creme, preto e dourado, Bodoni + Inter.
- Aberturas de parte pretas com foto P&B esfumada.
- Páginas pretas de impacto com as frases-destaque do próprio texto.
- Rodapé "VOZ, PALCO E PRESENÇA".
- Quadros: Exercício, Dica técnica, Por trás da ciência (preto), No palco, Para quem treina, Atenção.
- **Capa:** preta, com foto P&B da autora de braços cruzados (bw-p4), título em Bodoni à esquerda e "Presença" em dourado.
- **Contracapa:** preta, com a frase "Antes do discurso, existe a voz.", as 4 partes e uma foto pequena em arco.
- **Figuras:** reaproveitadas do livro principal (aparelho, fonte-filtro, diafragma, postura) e 4 novas (recursos vocais, estrutura da fala, microfone, plano de 8 semanas).

## Áudios
Sem QR code. O aviso fica em "Sobre este livro" e em cada exercício: "Áudio de apoio disponível na plataforma onde você adquiriu este livro."

## Como gerar de novo
- **Preparação:** copiar `livro-oratoria/fonte/` para /tmp/work/orat. As fontes ficam em /tmp/work/fonts e as figuras do livro principal estão em img/. O `ofig.py` importa `gen2.py`, que fica em /tmp/work/book2.
- **Passos:**
  1. `python3 ofig.py && node rfig.js`
  2. `node rcov.js`
  3. `python3 build_orat.py && node rorat.js && python3 pages_orat.py && python3 build_orat.py && node rorat.js`
- Os capítulos extras (extra1 e extra2) são inseridos e renumerados automaticamente.
