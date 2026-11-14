# Memória: guia 50+ "Agora é a Minha Vez"

Título: **Agora é a Minha Vez**. Subtítulo: *O prazer de cantar na melhor fase da vida*. Autora: Dra. Brízia Lacerda.
Público: adultos de 50 a 65 anos, ativos, que realizaram o que queriam na vida e agora decidiram cantar por prazer, como hobby e sonho realizado; também professores, regentes e educadores.

## Histórico
- 1ª versão ("A Voz Não Tem Idade", bonecos coloridos, tom de "terceira idade") foi REPROVADA: ficou infantil e os personagens pareciam velhos demais. "50, 60 anos hoje são os novos 40; ninguém gosta de ser chamado de velho."
- Escolhas da cliente para a 2ª versão: título "Agora é a Minha Vez"; arte em traço fino dourado (sem bonecos, sem rostos); personagens repaginados.

## Tom e vocabulário
- Aspiracional, elegante, alegre: prazer, hobby, conquista, palco, sarau, banda, coral, gravar, cantar no casamento da filha.
- PROIBIDO: idoso(a), terceira idade, velho/velhice, vovó/vovô, melhor idade, "apesar da idade", qualquer tom de fragilidade. Usar "maturidade", "esta fase", "a partir dos 50".
- Mudanças da voz explicadas com naturalidade, sempre junto do que se ganha (interpretação, emoção, repertório).

## Ética (CFFa), obrigatória
Educativo; sem promessa de cura, rejuvenescimento ou prazo; sem diagnóstico; sem orientação de medicamentos; exercícios para vozes saudáveis (terapia é individual, com fonoaudiólogo); papéis separados professor / fono / médico; sem "antes e depois"; sinais de alerta → otorrino + fonoaudiólogo.

## Personagens (fictícios, só em texto, quadros "Uma história")
Helena, 58, ex-executiva, prepara um sarau; Ricardo, 63, engenheiro, voltou à banda da juventude (aparelho auditivo citado com naturalidade); Lúcia, 54, empresária, voz mais grave após a menopausa, quer cantar no casamento da filha.

## Estrutura (6 partes, 16 capítulos, 159 páginas, 190 × 250 mm)
1 Seu momento chegou · 2 Corpo, escuta e voz · 3 Técnica com prazer · 4 Viva a música (palco/sarau/karaokê, grupo, gravação) · 5 Cuidar para cantar por muitos anos · 6 Para quem ensina (inclui plano de 12 semanas).

## Padrão visual
- Creme #F7F0E4, preto #1E1B19, dourado #B8904A / #D9B26A, cinza claro #ECE8E2. Sem azul nem bordô.
- Títulos em Bodoni Moda; texto em Lora 13,5 pt; rótulos em Inter espaçado.
- Aberturas de parte em página preta com número grande dourado, frase de impacto e arte em traço dourado (op1 a op6).
- Quadros: Para praticar (branco, borda dourada), Uma história (preto), Por trás da ciência (creme escuro), Para o professor (cinza), Bom saber (filete), Atenção (borda preta); "Sua vez" tracejado dourado.
- 11 desenhos em traço fino (lfig.py), sem rostos. Capa preta com microfone dourado.
- Fotos da Brízia só na carta e em "Sobre a autora", pequenas, em arco.

## Áudios
Sem QR code e sem site: o livro digital fica numa plataforma que já reúne os áudios. Aviso no início ("Como usar este livro") e em cada quadro "Para praticar": "Áudio de apoio disponível na plataforma onde você adquiriu este livro."

## Pendências
ISBN só na versão final; revisão técnica e ética da autora; EPUB depois da aprovação.

## Como gerar de novo
Copiar `livro-senior/fonte/` para /tmp/work/vez (fontes @fontsource em /tmp/work/fonts: bodoni-moda, lora, inter).
1. `python3 lfig.py && node rfig.js`
2. `node rcov.js cover.html cover.png && node rcov.js back.html back.png`
3. `python3 build_vez.py && node rvez.js && python3 pages_vez.py && python3 build_vez.py && node rvez.js`
