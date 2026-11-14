# Memória: livro sênior "A Voz Não Tem Idade"

Guia de canto e cuidados com a voz a partir dos 50 anos, para aprender e para ensinar. Autora: Dra. Brízia Lacerda. Mesma linhagem do infantojuvenil "Minha voz cresce comigo".

## Decisões
- Público duplo: pessoas de 50+ que querem aprender ou voltar a cantar; professores, regentes, educadores e profissionais de saúde que ensinam esse público.
- Tom adulto e respeitoso, nunca infantilizado ("vovó", "velhinho" proibidos).
- Ética do Código de Ética da Fonoaudiologia (CFFa): caráter educativo; sem promessa de cura, rejuvenescimento ou prazos; sem diagnóstico nem autodiagnóstico; sem orientação de medicamentos; exercícios só para vozes saudáveis (terapia é individual, com fonoaudiólogo); papéis separados (professor ensina, fono avalia e trata, médico diagnostica); sem "antes e depois", sem preços. Limites físicos: cadeira sempre, nada de prender o ar com esforço, parar com tontura ou dor.
- Personagens fictícios: Dona Célia (68, coral, voz mais fina e cansada), Seu Antônio (72, começou após aposentar, aparelho auditivo), Marta (55, professora, menopausa, voz mais grave).
- Referências permitidas (todas completas no livro): TITZE 1994; TITZE 2006; BEHLAU 2001; ALVES et al. 2019; STEMPLE et al. 1994; ZIEGLER et al. 2014; JOHNSON et al. 2020.

## Padrão visual
- Formato 200 × 260 mm, 141 páginas. Fundo creme #F7F0E4, tinta #2B2622, dourado #B8904A; cor por parte: coral #D9846E, sálvia #7FA58A, dourado #B8904A, lavanda #9C8CC4, grafite #4A4F5C.
- Texto em Atkinson Hyperlegible 14 pt (fonte criada para baixa visão), algarismos em Inter (sem zero cortado); títulos em Lora.
- Quadros: Para praticar (com aviso de áudio), Para o professor, Por trás da ciência, Bom saber, Atenção; atividades "Sua vez" com linhas e caixas de marcar.
- 13 ilustrações vetoriais originais (sfig.py): personagens, voz madura, postura, audição, hábitos, aquecimento, sinais de alerta, extensão, coral, plano de 12 semanas.
- Página escura de áudios no final com QR code (placeholder).

## Pendências (dependem da autora)
- URL do site de áudios para o QR code.
- ISBN apenas na versão final (esta é versão de impressão e revisão).
- Revisão técnica e ética pela autora antes de publicar.
- EPUB quando o texto estiver aprovado.

## Como gerar de novo
Arquivos em `livro-senior/fonte/` (copiar para /tmp/work/senior; fontes npm @fontsource em /tmp/work/fonts: lora, atkinson-hyperlegible, inter, fredoka, nunito).
1. `python3 sfig.py && node rfig.js` (ilustrações em img/)
2. `node rcov.js cover.html cover.png && node rcov.js back.html back.png`
3. `python3 build_senior.py && node rsen.js && python3 pages_sen.py && python3 build_senior.py && node rsen.js` (duas passagens para numerar o sumário)
