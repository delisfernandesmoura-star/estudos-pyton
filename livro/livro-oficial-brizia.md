# Livro oficial Brízia — memória do projeto

> Leia este arquivo antes de qualquer trabalho no livro da Dra. Brízia Lacerda.

## Identidade do livro
- **Título:** Voz, Canto e Ciência
- **Subtítulo:** Saúde vocal, técnica vocal e inspiração: fonoaudiologia aplicada à voz cantada e falada
- **Autora:** Dra. Brízia Lacerda. Use esse nome também no ISBN.
- **Sobre a autora:**
  - fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz;
  - cantora, vocal coach, pesquisadora, escritora e palestrante, mãe e esposa;
  - tem artigo científico publicado (referência ainda não informada).
- **Público:** quem quer aprender a cantar, professores de canto, quem quer se comunicar bem e fonoaudiólogos que atendem cantores.
- **Origem do conteúdo:** apostilas da Faculdade da Voz, Módulos 1 a 4, organizadas pela autora. Foram revisadas, corrigidas e atualizadas com ciência atual.

## Estrutura (4 partes, 21 capítulos)
- **Parte I · Saúde Vocal:** capítulos 1 a 5.
- **Parte II · Fundamentos do Canto:** capítulos 6 a 11.
- **Parte III · Ornamentos Vocais:** capítulos 12 a 18 (fry, twang, yodel, vibrato, melismas, cry, apogiatura).
- **Parte IV · Técnicas Avançadas:** capítulos 19 a 21 (funções vocais, cores do som e efeitos, belting).
- **Páginas de abertura:** capa, falsa folha de rosto, frontispício, folha de rosto, créditos, epígrafe, sumário, "Sobre este livro" e "Sobre a autora".
- **Páginas finais:** referências, página de áudios (QR code e site) e contracapa.

## Decisões aprovadas pela cliente
- **Versão principal:** PDF premium, 17 × 24 cm.
- **EPUBs:** além do PDF, um EPUB de layout fixo (páginas em imagem) e um EPUB fluido.
- **Paleta:** creme, preto suave, dourado, cinza claro e branco, se precisar. **Nunca usar azul nem bordô.**
- **Tipografia:** Bodoni (Bodoni Moda) em títulos, números e frases, e Inter no texto. Pode sair do manual da marca: aquele é o manual da Faculdade da Voz, não do livro.
- **Estilo:** editorial e elegante, como um livro de biografia, mas técnico e rico. Nada engraçado e nada interativo.
- **Ritmo das páginas:**
  - creme para o texto;
  - pretas com frases de impacto grandes, sempre tiradas do texto da própria autora, nunca inventadas;
  - abertura de parte em preto, com foto da autora em preto e branco esfumada.
- **Capa aprovada:** palavra gigante "VOZ" em Bodoni, vazada sobre a foto (camisa azul-marinho em preto e branco).
  - Sem contorno nas letras e com o Z alinhado ao V.
  - Título "Voz, Canto e Ciência" do lado direito, abaixo do pescoço, com "e Ciência" em dourado. A linha abaixo do nome também é dourada.
  - Sem logo da Faculdade da Voz.
- **Fotos da autora:**
  - nunca ampliar demais, porque perdem qualidade;
  - nunca desfigurar o rosto;
  - as fotos alteradas por IA podem ser usadas;
  - não usar a foto da turma com certificados.
- **Imagens:**
  - preferir ilustrações;
  - **nunca usar rosto de outra pessoa**, nem de banco de imagens;
  - as fotos de cantoras das apostilas viraram quadros "Para ouvir", só com os nomes.
- **Áudios:**
  - todo exercício remete à página final "Áudios dos exercícios", que terá QR code e site para baixar os áudios;
  - não colocar QR code no meio do livro.
- **ISBN e ficha catalográfica:** **não deixar espaço reservado.** Só entram na versão final.
- **Referências:**
  - manter as citações das apostilas, de forma discreta;
  - referenciar também o que tiver origem identificável (por exemplo, CVT/Sadolin, Estill);
  - quando não der para confirmar os dados, deixar o contexto de onde veio.

## Capa dura (versão impressa de luxo)
- **Contracapa:** preta, preferência da cliente.
  - textos em creme e dourado com efeito de folha dourada;
  - frase "Conhecimento que ganha voz.", lista das 4 partes e foto pequena da autora em arco;
  - sem código de barras ou ISBN por enquanto.
- **Lombada:** preta, com "Voz, Canto e Ciência" em Bodoni dourado, "DRA. BRÍZIA LACERDA" em creme e um "V" dourado embaixo.
- **Mockups:** em `livro/mockups/` (capa, lombada e contracapa preta) e artes planas da contracapa e da lombada.

## Situação atual (14/11/2026)
- **Versão para impressão e revisão da autora:** `voz-canto-e-ciencia_PDF-premium.pdf`, 156 páginas.
- **EPUBs:** são da versão anterior. Ainda não têm as referências completadas nem a remoção do ISBN, e devem ser gerados de novo na versão final.
- **Pendências:**
  - endereço do site dos áudios, para gerar o QR code;
  - referência do artigo da autora;
  - confirmar a bio;
  - revisão do conteúdo clínico sobre medicamentos;
  - ISBN e ficha catalográfica na versão final.
- **Referências sem confirmação em catálogo**, mantidas com contexto: Coelho (1994), Marsola e Baê (2000), Mazzoleni (2012, ano), Paget (1940), Curcio, Behlau e Pontes (2000), LoVetri (2003), Popeil (2012), Veneziano (2008) e Wells (2006).

## Como gerar de novo
- **Fontes:** estão em `livro/fonte/`. Os textos dos capítulos são `part1.html` a `part4.html`, o estilo é `book2.css`, a montagem é `build2.py` e as ilustrações são geradas por `gen2.py`.
- **Ambiente:** os scripts usam caminhos de `/tmp/work`. Numa sessão nova é preciso:
  - recriar `/tmp/work/book` e `/tmp/work/book2` com esses arquivos;
  - instalar as fontes com `npm install @fontsource/bodoni-moda @fontsource/inter @fontsource/lora` em `/tmp/work/fonts`.
- **Ordem:**
  1. `python3 gen2.py && node render_figs.js` (ilustrações);
  2. `python3 build2.py && node render2.js` (PDF);
  3. `python3 pages2.py`, depois rodar o passo 2 de novo, para acertar os números do sumário;
  4. `python3 build_epub2.py` + pandoc (EPUB fluido);
  5. `fixed.py` (EPUB de layout fixo).
