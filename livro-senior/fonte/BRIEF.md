# Brief — livro da voz sênior da Dra. Brízia Lacerda

Livro: "A Voz Não Tem Idade" — guia de canto e cuidados vocais para pessoas a partir dos 50 anos, para aprender e para ensinar.
Autora: Dra. Brízia Lacerda — fonoaudióloga especialista em voz, cantora, vocal coach.
Público duplo: (1) adultos de 50+ e idosos que querem aprender a cantar ou voltar a cantar, cuidar da voz falada e cantada; (2) professores de canto, regentes de corais da terceira idade, educadores, fonoaudiólogos e cuidadores que ensinam esse público.
Língua: português do Brasil, perfeito. Tom: respeitoso, caloroso, adulto, NUNCA infantilizado nem condescendente ("vovó", "velhinho" proibidos; use "pessoas maduras", "a partir dos 50", "idosos" com respeito). Frases claras, parágrafos curtos (leitura com letras grandes), "você".
Base de conteúdo: o livro principal da autora (/tmp/work/book/part1.html a part4.html) para tom e termos — adapte, não copie trechos longos.

## ÉTICA PROFISSIONAL (OBRIGATÓRIO — Código de Ética da Fonoaudiologia / CFFa)
- Caráter educativo. Nunca prometer cura, rejuvenescimento da voz, resultados garantidos ou prazos ("em 10 dias sua voz volta a ser jovem" é PROIBIDO). Use "pode ajudar", "tende a", "muitas pessoas relatam".
- Nunca diagnosticar pelo livro nem sugerir autodiagnóstico; sinais de alerta → procurar médico otorrinolaringologista e fonoaudiólogo (e audiologista/fonoaudiólogo para audição).
- Nunca indicar, suspender ou ajustar medicamentos; falar apenas que alguns medicamentos podem ressecar ou afetar a voz e que a conduta é do médico.
- Exercícios do livro são para vozes saudáveis, como prática de canto e bem-estar vocal. Deixar claro que exercícios terapêuticos (para alterações vocais) são indicados e acompanhados individualmente por fonoaudiólogo. Pode mencionar que a pesquisa estudou programas de exercícios vocais em idosos, sem transformar o livro em terapia.
- Separar papéis: professor de canto ensina canto; fonoaudiólogo avalia e trata; médico diagnostica. O professor não diagnostica.
- Sem sensacionalismo, sem depoimentos de "antes e depois", sem preços, sem autopromoção exagerada.
- Saúde geral: lembrar de respeitar limites físicos (pressão arterial, tontura, cansaço, articulações): nada de prender a respiração com esforço, nada de exercícios bruscos; cadeira sempre disponível; parar se sentir mal-estar.

## Personagens (aparecem nas ilustrações; use com leveza)
- Dona Célia, 68 anos — canta no coral da comunidade há anos e percebeu a voz mais "fina e cansada".
- Seu Antônio, 72 anos — sempre quis cantar e começou agora, depois de se aposentar; usa aparelho auditivo.
- Marta, 55 anos — professora, passou pela menopausa e notou a voz mais grave; quer cantar e falar melhor.

## Formato HTML (OBRIGATÓRIO — só estas classes)
- Parte: <section class="part" id="parte-N"><div class="part-opener"><p class="part-label">Parte N</p><h1 class="part-title">Título</h1><p class="part-sub">Subtítulo curto.</p></div> ... </section>
- Capítulo: <h2 class="chapter" id="cap-N"><span class="chapter-num">Capítulo N</span>Título</h2> (numeração contínua)
- <h3>, <h4>, <p>, <ul>/<ol>, <strong>, <em>.
- Boxes: <div class="box TIPO"><p class="box-title">Título</p>...</div>
  - praticar → exercício (título com nome claro, ex. "Bocejo suspirado"). Dentro: passos em <ol>, quantas vezes, e <p class="beneficio"><strong>Para que serve:</strong> ...</p>. Se fizer sentido: <p class="idade">Pode ser feito sentado</p>.
  - professor → "Para o professor": didática, adaptações, erros comuns.
  - ciencia → "Por trás da ciência": explicação fonoaudiológica para adultos, com citações discretas.
  - saiba → "Bom saber": informação curta e útil.
  - cuidado → "Atenção": alerta de segurança/saúde.
- Atividades: <div class="atividade"><p class="box-title">Sua vez</p><p>Instrução</p> + <div class="linhas" data-n="4"></div> e/ou <ul class="check"><li>...</li></ul></div> (sem desenho).
- Figuras: <figure class="fig" data-fig="NOME"><figcaption>Legenda.</figcaption></figure> — SOMENTE estes nomes, cada um no máximo uma vez no livro todo:
  celia, antonio, marta, grupo (os três cantando juntos), voz-madura (o que muda na laringe com a idade, esquema simples), respiracao-sentado (respiração e postura sentado e em pé), audicao (escuta e aparelho auditivo), habitos (hábitos que protegem a voz), aquecimento (cartões do aquecimento suave), sinais (sinais de alerta), extensao (extensão confortável), coral (coral sênior em semicírculo), plano (linha do tempo do curso de 12 semanas)
- Citações: (AUTOR, ano) em maiúsculas. Use SOMENTE estas referências:
  TITZE, 1994 — Principles of voice production
  TITZE, 2006 — exercícios de trato vocal semiocluído
  BEHLAU, 2001 — Voz: o livro do especialista
  ALVES et al., 2019 — hidratação e qualidade vocal
  STEMPLE et al., 1994 — exercícios de função vocal
  ZIEGLER et al., 2014 — programas de exercícios vocais na presbifonia (estudo preliminar)
  JOHNSON et al., 2020 — coral comunitário e bem-estar de idosos
- Números: prudentes e aproximados; não invente estatísticas.
- Exercícios têm áudio no final do livro (o sistema adiciona o aviso; não escreva isso).
- Sem emojis, sem nomes de cantores reais, sem marcas.
Saída: um arquivo HTML só com o conteúdo, UTF-8.
