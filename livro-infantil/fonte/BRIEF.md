# Brief — livro infantojuvenil da Dra. Brízia Lacerda

Livro: "Minha Voz Cresce Comigo" — técnica vocal e cuidados com a voz para crianças e adolescentes.
Autora: Dra. Brízia Lacerda — fonoaudióloga especialista em voz, cantora, vocal coach (escreve com as duas lentes: canto + fonoaudiologia).
Público duplo: (1) crianças de 4 a 12 anos e adolescentes de 12 a 17 participam lendo/fazendo junto; (2) professores de canto, regentes de coral infantil, educadores musicais, fonoaudiólogos e pais estudam e usam em aula.
Língua: português do Brasil, perfeito. Texto para a criança: frases curtas, tom acolhedor, alegre, "você", sem infantilizar demais; adolescentes: tom respeitoso e direto. Boxes para adultos: técnicos, precisos.
Base de conteúdo: o livro principal da autora (leia /tmp/work/book/part1.html a part4.html para tom, termos e conteúdo — adapte para crianças, não copie trechos longos).

## Personagens (aparecem nas ilustrações; use com leveza no texto)
- Lia, 8 anos — curiosa, adora cantar no coral da escola.
- Theo, 12 anos — está começando a muda vocal; às vezes a voz "falha".
- Bia, 15 anos — canta em banda, quer cantar agudos e cuidar da voz.

## Formato HTML (OBRIGATÓRIO — só estas classes)
- Parte: <section class="part" id="parte-N"><div class="part-opener"><p class="part-label">Parte N</p><h1 class="part-title">Título</h1><p class="part-sub">Subtítulo curto.</p></div> ... </section>
- Capítulo: <h2 class="chapter" id="cap-N"><span class="chapter-num">Capítulo N</span>Título</h2>  (numeração contínua no livro todo)
- Primeiro parágrafo de cada capítulo: frase de abertura convidativa.
- Subtítulos: <h3>, <h4>. Parágrafos <p>, listas <ul>/<ol>, <strong>, <em>.
- Boxes (sempre <div class="box TIPO"><p class="box-title">Título</p>...</div>):
  - brincar → exercício/brincadeira para fazer (título começa com nome divertido: ex. "A abelhinha"). Dentro: o que fazer em passos (<ol>), quantas vezes, e uma linha <p class="beneficio"><strong>Para que serve:</strong> ...</p>. Se for específico de idade, inclua <p class="idade">4 a 7 anos</p> (ou "8 a 12 anos", "12 a 17 anos", "Todas as idades") logo após o box-title.
  - professor → "Para o professor": orientação didática, adaptações por idade, erros comuns, como corrigir.
  - ciencia → "Por trás da ciência": explicação fonoaudiológica/fisiológica para adultos, com citações discretas.
  - curiosidade → "Você sabia?": fato curto e encantador para a criança.
  - cuidado → "Cuidado!": alerta de saúde vocal.
- Atividades interativas (a criança escreve/marca/desenha no livro):
  <div class="atividade"><p class="box-title">Sua vez!</p><p>Instrução</p> + um ou mais de:
     <div class="linhas" data-n="4"></div>  (linhas para escrever; data-n = nº de linhas)
     <ul class="check"><li>item para marcar</li>...</ul>
     <div class="desenho" data-h="70">Desenhe aqui ...</div> (data-h = altura em mm, 40–90)
  </div>
- Figuras: <figure class="fig" data-fig="NOME"><figcaption>Legenda.</figcaption></figure> — use SOMENTE nomes desta lista (cada um no máximo uma vez no livro todo, salvo personagens):
  personagens: lia, theo, bia, turma (os três juntos cantando)
  corpo: casa-da-voz (onde fica a laringe, perfil de criança), cortininhas (pregas vocais abertas/fechadas como cortinas), balao (respiração: barriga como balão), arvore (postura: corpo como árvore com raízes), termometro (termômetro do volume: sussurro → fala → voz forte → grito)
  cuidados: agua (garrafinha e hidratação), amigos-viloes (amigos e vilões da voz), semaforo (sinais de alerta verde/amarelo/vermelho)
  exercícios: abelhinha (humming), motorzinho (vibração de lábios), canudinho (exercício com canudo), sirene (glissando), bocejo (bocejo/relaxamento), escada (escala subindo e descendo)
  muda: muda-meninos (gráfico da extensão vocal dos meninos ao longo da muda), muda-meninas (idem meninas), faixas-idade (extensão confortável por idade no teclado), ouvido (escutar/afinação)
- Citações no texto: (AUTOR, ano) em maiúsculas, ex. (COOKSEY, 2000). Use APENAS referências desta lista (não invente outras):
  COOKSEY, 2000 — Working with adolescent voices (estágios da muda nos meninos)
  GACKLE, 2011 — Finding Ophelia's voice (estágios da muda nas meninas)
  TITZE, 2006 — exercícios de trato vocal semiocluído (canudo, lábios)
  TITZE, 1994 — Principles of voice production (anatomia, tamanho das pregas)
  PHILLIPS, 2014 — Teaching kids to sing
  BEHLAU, 2001 — Voz: o livro do especialista
  ALVES et al., 2019 — hidratação e qualidade vocal
- Números: use valores aproximados e prudentes ("cerca de", "em geral"). Ex.: na muda, a voz masculina desce cerca de uma oitava; a feminina, cerca de 3 a 4 semitons; a muda ocorre em geral entre 11 e 15 anos, com variação individual. Não invente estatísticas.
- Exercícios: SEMPRE seguros, sem dor, sem forçar agudos/volume; em cada parte lembre que "pare se doer/arranhar".
- Os exercícios têm áudio de apoio no final do livro (o sistema adiciona o aviso automaticamente — não escreva isso).
- Não use emojis. Não use nomes de cantores reais. Não cite marcas.
Saída: um arquivo HTML só com o conteúdo (sem <html>/<head>), em UTF-8.
