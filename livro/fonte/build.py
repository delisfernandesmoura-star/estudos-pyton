import re, json, os, sys, html
TITLE="Voz, Canto e Ciência"
SUB="Saúde vocal, técnica vocal e inspiração: fonoaudiologia aplicada à voz cantada e falada"
AUTHOR="Dra. Brízia Lacerda"
FONTS="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}

def read(f): return open(f,encoding="utf-8").read()
parts=[read("part1.html"),read("part2.html"),read("part3.html")]
body="\n".join(parts)

# discreet citations
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: ET AL\.)?, \d{4})\)', r'<span class="cit">(\1)</span>', body)
body=body.replace('.svg"','.png"')
roman={"parte-1":"I","parte-2":"II","parte-3":"III"}
def opener(m):
    sid=m.group(1)
    return f'<section class="part" id="{sid}">\n<div class="part-opener" data-num="{roman[sid]}">'
body=re.sub(r'<section class="part" id="(parte-\d)">\s*<div class="part-opener">',opener,body)

# TOC data
toc=[]
for m in re.finditer(r'<section class="part" id="(parte-\d)">.*?<p class="part-label">(.*?)</p>\s*<h1 class="part-title">(.*?)</h1>(.*?)</section>',body,re.S):
    sid,label,title,rest=m.groups()
    chs=[(c.group(1),c.group(2),c.group(3)) for c in re.finditer(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',rest)]
    toc.append((sid,label,title,chs))

def pg(k): return str(pages.get(k,""))
def toc_html(pdf=True):
    o=['<ol>']
    for key,label in (("sobre-livro","Sobre este livro"),("sobre-autora","Sobre a autora")):
        o.append(f'<li class="tf"><span>{label}</span><span class="n">{pg(key)}</span></li>')
    for sid,label,title,chs in toc:
        o.append(f'<li class="tp"><span><small>{label}</small>{title}</span><span class="n">{pg(sid)}</span></li>')
        for cid,num,t in chs:
            o.append(f'<li class="tc"><span>{num}. {t}</span><span class="n">{pg(cid)}</span></li>')
    o.append(f'<li class="tf" style="margin-top:5mm"><span>Referências</span><span class="n">{pg("referencias")}</span></li>')
    o.append('</ol>')
    return "\n".join(o)

SOBRE_LIVRO=f'''<h1>Sobre este livro</h1><div class="rule"></div>
<p>A voz é, ao mesmo tempo, o instrumento mais íntimo e o mais exigido que temos — para cantar, para ensinar, para vender, para liderar, para acolher. Este livro nasceu para quem quer entender como ela funciona e aprender a usá-la com técnica, expressão e segurança.</p>
<p>O conteúdo reúne e atualiza o material didático da Faculdade da Voz, organizado pela Dra. Brízia Lacerda a partir da prática clínica e do ensino do canto, de estudos e de referências da literatura científica e da pedagogia vocal. Os textos foram revistos, corrigidos e acrescidos de atualizações, e as fontes aparecem de forma discreta ao longo dos capítulos, com a lista completa ao final.</p>
<h3>Para quem é este livro</h3>
<div class="publico">
<div><b>Quem quer aprender a cantar</b><span>Respiração, apoio, registros, classificação vocal e exercícios para treinar com segurança.</span></div>
<div><b>Professores de canto</b><span>Terminologia, fisiologia, estilos e ornamentos organizados para consulta e para a sala de aula.</span></div>
<div><b>Quem quer se comunicar bem</b><span>Cuidados com a voz falada, hidratação, higiene vocal e dicas para quem fala em público.</span></div>
<div><b>Fonoaudiólogos</b><span>Avaliação do cantor, fatores de risco, hábitos inadequados e a base fisiológica da fonação.</span></div>
</div>
<h3>Como o livro está organizado</h3>
<p><strong>Parte I · Saúde Vocal</strong> trata da avaliação, do aquecimento e desaquecimento, da postura, da higiene vocal e dos fatores que protegem ou ameaçam a voz. <strong>Parte II · Fundamentos do Canto</strong> apresenta a terminologia, a classificação vocal, os estilos de canto, a respiração e a fisiologia da fonação. <strong>Parte III · Ornamentos Vocais</strong> explora fry, twang, yodel, vibrato, melismas, cry e apogiatura.</p>
<p>Ao longo do texto, você encontra quadros de <em>Exercício</em>, <em>Atenção</em>, <em>Atualização científica</em>, <em>Para ouvir</em> e <em>De onde vem o termo</em>. Pratique sempre devagar, sem desconforto, e procure um profissional diante de qualquer sintoma persistente.</p>
<div class="box aviso"><p class="box-title">Aviso</p><p>Este livro tem finalidade educativa e não substitui a avaliação de um médico, de um fonoaudiólogo ou de um professor de canto. Sintomas como rouquidão persistente, dor ou perda da voz exigem avaliação profissional.</p></div>'''

SOBRE_AUTORA=f'''<h1>Sobre a autora</h1><div class="rule"></div>
<div class="sobre-autora">
<div class="foto"><img src="assets/foto1_s.jpg" alt="Dra. Brízia Lacerda"></div>
<p><strong>Dra. Brízia Lacerda</strong> é fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. Atua como cantora, vocal coach, pesquisadora, escritora e palestrante, e é autora de artigo científico publicado.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos, cantores e profissionais que buscam desenvolver conhecimento e prática sobre voz.</p>
<p>Mãe e esposa, leva para o ensino da voz o mesmo cuidado com que enxerga a vida: a voz como expressão da pessoa inteira — corpo, emoção e propósito.</p>
</div>'''

CREDITOS=f'''<h2>{TITLE}</h2>
<p><strong>{TITLE}</strong><br>{SUB}.</p>
<p>Autora: {AUTHOR}<br>Editora: Faculdade da Voz<br>Edição digital · 2026</p>
<p>© 2026 {AUTHOR}. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>ISBN (e-book): [a ser atribuído pela Agência Brasileira do ISBN]</p>
<div class="cip">[Ficha catalográfica (CIP): a ser emitida pela Biblioteca Nacional]</div>
<p>Capa, projeto gráfico e ilustrações: Faculdade da Voz. Fotografias: acervo da autora.</p>
<p>Este livro tem finalidade educativa e não substitui a avaliação de profissionais de saúde.</p>'''

REFS='''<section class="refs" id="referencias">
<h1>Referências</h1>
<p class="intro">Esta obra reúne e atualiza o material didático da Faculdade da Voz, organizado pela autora a partir de estudos e da prática profissional. Abaixo estão as fontes citadas ao longo do texto, seguidas de leituras recomendadas.</p>
<ul>
<li>ALVES, M.; KRÜGER, E.; PILLAY, B.; VAN LIERDE, K.; VAN DER LINDE, J. The effect of hydration on voice quality in adults: a systematic review. <em>Journal of Voice</em>, v. 33, n. 1, p. 125.e13–125.e28, 2019.</li>
<li>BJORKNER, E. Musical theater and opera singing – why so different? A study of subglottal pressure, voice source, and formant frequency characteristics. <em>Journal of Voice</em>, v. 22, n. 5, p. 533–540, 2008.</li>
<li>COELHO. 1994. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>CURCIO; BEHLAU; PONTES. <em>Estudo da frequência do vibrato em três estilos de canto</em>. 2000. <span class="pend">[dados de publicação a confirmar]</span></li>
<li>DINVILLE, C. <em>A técnica da voz cantada</em>. Rio de Janeiro: Enelivros, 1993.</li>
<li>GAVA JUNIOR. 2010. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>HOLLIEN, H.; MICHEL, J. Vocal fry as a phonational register. <em>Journal of Speech and Hearing Research</em>, v. 11, n. 3, p. 600–604, 1968.</li>
<li>KAYES, G. <em>Singing and the actor</em>. 2. ed. London: A&amp;C Black, 2004.</li>
<li>LADEFOGED, P.; MADDIESON, I. <em>The sounds of the world’s languages</em>. Oxford: Blackwell, 1996.</li>
<li>LAVER, J. <em>The phonetic description of voice quality</em>. Cambridge: Cambridge University Press, 1980.</li>
<li>MARSOLA, M.; BAÊ, T. <em>Canto, canção, cantoria: como montar um coral infantil</em>. 2000. <span class="pend">[dados de publicação a confirmar]</span></li>
<li>MAZZOLENI. 2012. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>PAGET, R. 1940. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>PINNOCK, C. B.; GRAHAM, N. M.; MYLVAGANAM, A.; DOUGLAS, R. M. Relationship between milk intake and mucus production in adult volunteers challenged with rhinovirus-2. <em>American Review of Respiratory Disease</em>, v. 141, n. 2, p. 352–356, 1990.</li>
<li>STEINHAUER, K.; KLIMEK, M. M.; ESTILL, J. <em>The Estill Voice Model: theory and translation</em>. Pittsburgh: Estill Voice International, 2017.</li>
<li>SUNDBERG, J. <em>The science of the singing voice</em>. DeKalb: Northern Illinois University Press, 1987.</li>
<li>SUNDBERG, J.; GRAMMING, P.; LOVETRI, J. Comparisons of pharynx, source, formant, and pressure characteristics in operatic and musical theatre singing. <em>Journal of Voice</em>, v. 7, n. 4, p. 301–310, 1993.</li>
<li>TITZE, I. R. <em>Principles of voice production</em>. Englewood Cliffs: Prentice Hall, 1994.</li>
<li>WÜTHRICH, B.; SCHMID, A.; WALTHER, B.; SIEBER, R. Milk consumption does not lead to mucus production or occurrence of asthma. <em>Journal of the American College of Nutrition</em>, v. 24, n. 6, suppl., p. 547S–555S, 2005.</li>
<li>YANAGISAWA, E.; ESTILL, J.; KMUCHA, S. T.; LEDER, S. B. The contribution of aryepiglottic constriction to “ringing” voice quality: a videolaryngoscopic study with acoustic analysis. <em>Journal of Voice</em>, v. 3, n. 4, p. 342–350, 1989.</li>
</ul>
<h3>Leituras recomendadas</h3>
<ul>
<li>BEHLAU, M. (org.). <em>Voz: o livro do especialista</em>. Rio de Janeiro: Revinter, 2001. v. 1.</li>
<li>SUNDBERG, J. <em>The science of the singing voice</em>. DeKalb: Northern Illinois University Press, 1987.</li>
<li>TITZE, I. R. <em>Principles of voice production</em>. Englewood Cliffs: Prentice Hall, 1994.</li>
<li>STEINHAUER, K.; KLIMEK, M. M.; ESTILL, J. <em>The Estill Voice Model: theory and translation</em>. Pittsburgh: Estill Voice International, 2017.</li>
</ul>
</section>'''

def fonts_css():
    L=FONTS+"lora/files/lora-latin-"; I=FONTS+"inter/files/inter-latin-"
    css=""
    for w,s in ((400,"normal"),(600,"normal"),(700,"normal"),(400,"italic"),(600,"italic")):
        css+=f"@font-face{{font-family:Lora;font-weight:{w};font-style:{s};src:url(file://{L}{w}-{s}.woff2) format('woff2')}}\n"
    for w in (400,500,600,700):
        css+=f"@font-face{{font-family:Inter;font-weight:{w};font-style:normal;src:url(file://{I}{w}-normal.woff2) format('woff2')}}\n"
    return css

# ------------ PDF html ------------
body_pdf=body.replace('<p class="part-label">','<img class="pl" src="assets/logo_creme.png" alt="Faculdade da Voz"><p class="part-label">',3)
body_pdf=body_pdf
pdf=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>{fonts_css()}</style><link rel="stylesheet" href="book.css"></head><body>
<div class="fullpage cover"><img class="bg" src="cover.png" alt="Capa"></div>
<section class="titlepage"><img class="logo" src="assets/logo_azul.png" alt="Faculdade da Voz"><p class="t">{TITLE}</p><p class="st">{SUB}</p><div class="rule"></div><p class="au">{AUTHOR}</p></section>
<section class="creditos">{CREDITOS}</section>
<div class="fullpage frontispicio"><img src="assets/foto4.jpg" alt=""><div class="legenda"><p>{AUTHOR}</p><small>Fonoaudióloga · Especialista em voz · Cantora · Vocal coach</small></div></div>
<section class="toc"><h1>Sumário</h1>{toc_html()}</section>
<section class="frontsec" id="sobre-livro">{SOBRE_LIVRO}</section>
<section class="frontsec" id="sobre-autora">{SOBRE_AUTORA}</section>
{body_pdf}
<div style="break-before:page"></div>
{REFS}
<div class="fullpage contracapa"><img class="bg" src="back.png" alt="Contracapa"></div>
</body></html>'''
open("book.html","w",encoding="utf-8").write(pdf)

# ------------ EPUB html ------------
ep_body=body
for n,r in (("I","p1"),("II","p2"),("III","p3")):
    ep_body=ep_body.replace(f'<div class="part-opener" data-num="{n}">',f'<div class="part-opener {r}">')
def flat_open(m):
    cls,label,title,sub,intro=m.group(1),m.group(2),m.group(3),m.group(4),m.group(5)
    out=f'<h1 class="part-title {cls}"><span class="part-label">{label}</span>{title}</h1>\n'
    last = '' if intro else ' last'
    out+=f'<p class="part-sub {cls}{last}">{sub}</p>\n'
    if intro: out+=f'<p class="part-intro {cls} last">{intro}</p>\n'
    return out
ep_body=re.sub(r'<div class="part-opener (p\d)">\s*<p class="part-label">(.*?)</p>\s*<h1 class="part-title">(.*?)</h1>\s*<p class="part-sub">(.*?)</p>(?:\s*<p class="part-intro">(.*?)</p>)?\s*</div>',flat_open,ep_body,flags=re.S)
ep_body=re.sub(r'</?section[^>]*>','',ep_body)
def p2div(t):
    return re.sub(r'<p class="((?:box-title|nota|seq|beneficios|lead-in|fonte-tabela|part-sub|part-intro|intro|figura-pendente)[^"]*)">(.*?)</p>',r'<div class="\1">\2</div>',t,flags=re.S)
ep_body=p2div(ep_body)
def h2cls(m):
    n=int(m.group(1)); c="p1" if n<=5 else ("p2" if n<=11 else "p3")
    return f'<h2 class="chapter {c}" id="cap-{n}">'
ep_body=re.sub(r'<h2 class="chapter" id="cap-(\d+)">',h2cls,ep_body)
ep_body=ep_body.replace('class="chapter" id="cap-','class="chapter" id="cap-')
sobre_livro_ep=p2div(SOBRE_LIVRO).replace('<h1>Sobre este livro</h1><div class="rule"></div>','<h1 class="front">Sobre este livro</h1>')
sobre_autora_ep=SOBRE_AUTORA.replace('<h1>Sobre a autora</h1><div class="rule"></div>','<h1 class="front">Sobre a autora</h1>').replace("assets/foto1_s.jpg","assets/foto1_s.jpg")
cred_ep=CREDITOS.replace(f'<h2>{TITLE}</h2>','')
refs_ep=p2div(re.sub(r'</?section[^>]*>','',REFS.replace('<h1>Referências</h1>','<h1 class="front">Referências</h1>')))
ep=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{TITLE}</title></head><body>
<h1 class="front">Créditos</h1><div class="creditos">{cred_ep}</div>
<div class="frontispicio-ep"><p><img src="assets/foto4_s.jpg" alt="{AUTHOR}"></p></div>
{sobre_livro_ep}
{sobre_autora_ep}
{ep_body}
{refs_ep}
</body></html>'''
open("epub.html","w",encoding="utf-8").write(ep)
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
print("built", len(toc),"parts", sum(len(t[3]) for t in toc),"chapters")
