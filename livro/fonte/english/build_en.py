import re, json, os
TITLE="Voice, Singing and Science"
SUB="Vocal health, vocal technique and inspiration: speech-language pathology applied to the singing and speaking voice"
AUTHOR="Dr. Brízia Lacerda"
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")).zfill(2) if pages.get(k) else ""
AUD=str(pages.get("audios","")) or "at the end of the book"

PT=[open(f"/tmp/work/book/part{i}.html",encoding="utf-8").read() for i in (1,2,3,4)]
EN=[open(f"/tmp/work/en/part{i}.html",encoding="utf-8").read() for i in (1,2,3,4)]

def nth_tag_pos(text,tag,k):
    it=list(re.finditer(r'<'+tag+r'[\s>]',text))
    return it[k].start()
def map_pos(pi,anchor,after=False):
    pt=PT[pi]; i=pt.index(anchor)
    if after:
        i=i+len(anchor); m=re.compile(r'<(\w+)[\s>]').search(pt,i); i=m.start()
    tag=re.match(r'<(\w+)',pt[i:]).group(1)
    k=len(re.findall(r'<'+tag+r'[\s>]',pt[:i]))
    return nth_tag_pos(EN[pi],tag,k)
FIGS=[(0,'<p>O processo de produção da voz inicia-se',False,"f-aparelho","The vocal apparatus: from the lungs to the lips, every structure involved in producing the voice.","tall"),
(0,'e assim são produzidas as vogais e as consoantes para a formação das palavras.</p>',True,"f-fonte-filtro","The source–filter model: the vocal folds generate the basic sound, and the vocal tract turns it into the voice we hear.",""),
(1,'<p>A cinta abdominal é composta',False,"f-diafragma","On inhalation, the diaphragm descends and the ribs open; on exhalation, the diaphragm relaxes and rises.",""),
(1,'<p>Alguns são abaixadores ou elevadores da laringe',False,"f-laringe-frente","The larynx seen from the front: hyoid bone, thyroid and cricoid cartilages, and the top of the trachea.",""),
(1,'volte a essa posição antes de começar.</p>\n</div>',True,"f-postura","The Starting Position: ear, shoulder, hip, knee and ankle in line, with your back against the wall.","tall"),
(1,'<h3>Intensidade da voz</h3>',False,"f-bascula","In the cricothyroid tilt, the cricothyroid muscle tips the thyroid cartilage forward and lengthens the vocal folds.",""),
(1,'<h3>Ontogenia vocal</h3>',False,"f-ondas","Frequency and intensity: pitch depends on frequency; loudness, on the amplitude of vibration.",""),
(2,'<p>A produção do <strong>fry relaxado</strong>',False,"f-fry","In fry, the glottal pulses become widely spaced and irregular.",""),
(2,'<div class="box origem">',False,"f-twang","Twang: a raised tongue base, aryepiglottic constriction and a sensation of brightness in the face.","tall"),
(2,'<h3>O yodel e a música <em>country</em></h3>',False,"f-yodel","The yodel deliberately alternates between the modal and elevated registers.",""),
(2,'<p>O vibrato é aplicado nas finalizações',False,"f-vibrato","Vibrato: a regular oscillation of frequency around the note.",""),
(2,'<p>Os melismas têm seu fundamento',False,"f-melisma","In a melisma, a single syllable travels through several notes.",""),
(2,'<p>Vendo-se a grosso modo',False,"f-apogiatura","The appoggiatura: a neighboring note that precedes and enhances the main note.","")]
ins={}
for pi,anc,after,name,cap,cls in FIGS:
    p=map_pos(pi,anc,after); ins.setdefault(pi,[]).append((p,f'<figure class="fig {cls}"><img src="img/{name}.png" alt=""><figcaption>{cap}</figcaption></figure>\n'))
# cool-down audio position (after first </ul> following that h3)
p=map_pos(0,'<h3>Desaquecimento vocal</h3>'); coolpos=EN[0].index('</ul>',p)+5
for pi in ins:
    for p,h in sorted(ins[pi],reverse=True):
        if pi==0 and p<coolpos: coolpos+=0
        EN[pi]=EN[pi][:p]+h+EN[pi][p:]
# recompute coolpos after insertions
p=re.finditer(r'<h3[\s>]',EN[0]); 
k=len(re.findall(r'<h3[\s>]',PT[0][:PT[0].index('<h3>Desaquecimento vocal</h3>')]))
h3pos=nth_tag_pos(EN[0],'h3',k); coolpos=EN[0].index('</ul>',h3pos)+5
ICON='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#B8975A" stroke-width="1.9" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Audio for this exercise available for download · see page {AUD}</span></p>'
EN[0]=EN[0][:coolpos]+"\n"+AUDIO.replace("for this exercise","for the cool-down exercises")+EN[0][coolpos:]
# cry -> see chapter 10
o=[m.start() for m in re.finditer(r'<div class="box origem">',EN[2])][1]
e=EN[2].index('</p>',o); EN[2]=EN[2][:e]+' See the cricothyroid tilt in Chapter 10.'+EN[2][e:]
body="\n".join(EN)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: ET AL\.)?, \d{4}(?:, p\. [\d\-]+)?)\)', r'<span class="cit">(\1)</span>', body)
for a,b in [("fig-registros","f-registros"),("fig-extensao-vozes","f-extensao"),("fig-laringe","f-laringe-corte"),("fig-ciclo-glotico","f-ciclo"),("fig-respiracao","f-respiracao")]:
    body=body.replace(f"img/{a}.svg",f"img/{b}.png")
body=re.sub(r'img/(f-[a-z-]+)\.svg',r'img/\1.png',body)
body=re.sub(r'(<div class="box exercicio">.*?)(</div>)', lambda m: m.group(1)+AUDIO+"\n"+m.group(2), body, flags=re.S)
CH={}
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3); CH[num]=re.sub(r"<[^>]+>","",title)
    return f'<header class="ch-open" id="{cid}"><div class="ch-n">{num:02d}</div><div class="ch-k">Chapter {num}</div><h2>{title}</h2></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Chapter (\d+)</span>(.*?)</h2>\s*<p>',lambda m: chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Chapter (\d+)</span>(.*?)</h2>',chap,body)
assert len(CH)==21, len(CH)
PH={"parte-1":("bw-p1.jpg","50% 22%"),"parte-2":("bw-p2.jpg","50% 30%"),"parte-3":("bw-p3.jpg","50% 25%"),"parte-4":("bw-p4.jpg","50% 20%")}
NUM={"parte-1":"I","parte-2":"II","parte-3":"III","parte-4":"IV"}
def popen(m):
    sid=m.group(1); inner=m.group(2)
    lab=re.search(r'<p class="part-label">(.*?)</p>',inner).group(1)
    tit=re.search(r'<h1 class="part-title">(.*?)</h1>',inner).group(1)
    sub=re.search(r'<p class="part-sub">(.*?)</p>',inner,re.S).group(1)
    it=re.search(r'<p class="part-intro">(.*?)</p>',inner,re.S)
    img,pos=PH[sid]
    return (f'<section class="part" id="{sid}">\n<div class="pg black popen"><div class="ph"><img src="assets/{img}" style="object-position:{pos}"></div>'
            f'<div class="tx"><div class="num">{NUM[sid]}</div><div class="lab">{lab}</div><h1>{tit}</h1><div class="sub">{sub}</div>'
            + (f'<div class="intro">{it.group(1)}</div>' if it else '') + '</div></div>')
body=re.sub(r'<section class="part" id="(parte-\d)">\s*<div class="part-opener">(.*?)</div>',popen,body,flags=re.S)
def qpage(text,src,photo=None,long=False):
    if photo:
        return f'<div class="pg black quote photo"><div class="ph"><img src="assets/{photo}"></div><div class="tx"><div class="q">{text}</div><div class="src">{src}</div></div></div>\n'
    return f'<div class="pg black quote"><div class="q{" l" if long else ""}">{text}</div><div class="src">{src}</div></div>\n'
src=lambda n: f"Chapter {n} · {CH[n]}"
QUOTES=[("cap-2","No singing exercise should ever be uncomfortable.",2,None,False),
 ("cap-4","Air is the fuel of voice production.",4,"bw-q1.jpg",False),
 ("cap-7","Timbre is the personality of the voice.",6,None,False),
 ("cap-8","A vocal signature is as unique as a fingerprint.",7,"bw-q2.jpg",False),
 ("cap-9","Learning to sing is, first of all, learning to breathe.",9,None,False),
 ("cap-10","The voice exists only when the breath from the lungs provides enough pressure to give birth to the laryngeal sound — and to sustain it.",9,None,True),
 ("cap-11","Always leave yourself the feeling that you could give a little more.",9,"bw-q3.jpg",False),
 ("cap-15","Vibrato gives the voice expressive richness and great emotional power.",15,None,False),
 ("cap-20","Every person is unique — and will reach unique sound colors and effects.",20,None,False),
 ("cap-21","The voice serves the text.",21,None,False)]
for cid,t,n,ph,lg in QUOTES:
    a=f'<header class="ch-open" id="{cid}">'; assert a in body
    body=body.replace(a,qpage(t,src(n),ph,lg)+a,1)
def fonts_css():
    css=""
    for w,st in ((400,"normal"),(500,"normal"),(400,"italic"),(500,"italic")):
        css+=f"@font-face{{font-family:Bodoni;font-weight:{w};font-style:{st};src:url(file://{F}bodoni-moda/files/bodoni-moda-latin-{w}-{st}.woff2)}}\n"
    for w in (300,400,500,600,700):
        css+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}inter/files/inter-latin-{w}-normal.woff2)}}\n"
    return css
toc=[]
for m in re.finditer(r'<section class="part" id="(parte-\d)">.*?<div class="lab">(.*?)</div><h1>(.*?)</h1>(.*?)</section>',body,re.S):
    sid,lab,tit,rest=m.groups()
    chs=[(c.group(1),c.group(2),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="ch-n">(\d+)</div><div class="ch-k">.*?</div><h2>(.*?)</h2>',rest)]
    toc.append((sid,lab,tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>About This Book</span><span class="p">{pg("sobre-livro")}</span></div>',
       f'<div class="fm"><span>About the Author</span><span class="p">{pg("sobre-autora")}</span></div>']
    for sid,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="k">{lab}</span><span class="t">{tit}</span><span class="p">{pg(sid)}</span></div>')
        for cid,n,t in chs:
            o.append(f'<div class="row"><span class="n">{n}</span><span class="t">{t}</span><span class="p">{pg(cid)}</span></div>')
    o.append(f'<div class="fm" style="margin-top:6mm"><span>References</span><span class="p">{pg("referencias")}</span></div>')
    o.append(f'<div class="fm"><span>Exercise Audio</span><span class="p">{pg("audios")}</span></div>')
    return "\n".join(o)
PT1=EN[0]; 
SOBRE_LIVRO=f'''<section class="fsec" id="sobre-livro"><div class="kick">Introduction</div><h1>About This Book</h1><div class="rule"></div>
<p class="lead">The voice is at once the most intimate instrument we have and the one we ask the most of — to sing, to teach, to sell, to lead, to comfort.</p>
<p>This book was written for anyone who wants to understand how the voice works and learn to use it with technique, expression and confidence. It brings together and updates the teaching material developed by Dr. Brízia Lacerda through her clinical practice and her work as a singing teacher, drawing on research and on the scientific and vocal-pedagogy literature. Sources are cited discreetly throughout the chapters, with the full list at the end.</p>
<h3>Who this book is for</h3>
<div class="publico">
<div><b>Anyone learning to sing</b><span>Breathing, support, registers, voice classification and exercises to train safely.</span></div>
<div><b>Voice teachers</b><span>Terminology, physiology, styles and ornaments, organized for reference and for the studio.</span></div>
<div><b>Anyone who wants to communicate well</b><span>Care for the speaking voice, hydration, vocal hygiene and guidance for public speakers.</span></div>
<div><b>Speech-language pathologists</b><span>Assessing the singer, risk factors, harmful habits and the physiological basis of phonation.</span></div>
</div>
<h3>How the book is organized</h3>
<p><strong>Part I · Vocal Health</strong> covers assessment, warm-up and cool-down, posture, vocal hygiene and the factors that protect or threaten the voice. <strong>Part II · Foundations of Singing</strong> presents terminology, voice classification, singing styles, breathing and the physiology of phonation. <strong>Part III · Vocal Ornaments</strong> explores fry, twang, yodel, vibrato, melismas, cry and the appoggiatura. <strong>Part IV · Advanced Techniques</strong> introduces the vocal modes, sound colors, effects and belting.</p>
<p>Exercises are marked with a headphone symbol: every one of them comes with supporting audio, which you can download using the QR code and website on page {AUD}.</p>
<div class="box aviso"><p class="box-title">Please note</p><p>This book is intended for education and does not replace an evaluation by a physician, a speech-language pathologist or a voice teacher. Symptoms such as persistent hoarseness, pain or loss of voice call for professional assessment.</p></div>
</section>'''
SOBRE_AUTORA=f'''<div class="pg cream autora" id="sobre-autora"><div class="ph"><img src="assets/bw-autora.jpg"></div><div class="tx">
<div class="kick">The author</div><h1>Dr. Brízia<br>Lacerda</h1><div class="rule"></div>
<p>A speech-language pathologist trained at PUC Minas (Pontifical Catholic University of Minas Gerais, Brazil), with postgraduate training and a specialization in voice. She works as a singer, vocal coach, researcher, writer and speaker, and is the author of a published scientific article.</p>
<p>As head of Faculdade da Voz, she brings together voice science, singing, teaching and mentorship for voice teachers, speech-language pathologists, singers and professionals who want to deepen their knowledge and practice of the voice.</p>
<p>A mother and a wife, she brings to voice teaching the same care with which she sees life itself: the voice as an expression of the whole person — body, emotion and purpose.</p>
<div class="sig">Brízia Lacerda</div>
</div></div>'''
CREDITOS=f'''<div class="cred">
<p><strong>{TITLE}</strong><br>{SUB}</p>
<p>Author: {AUTHOR}<br>Print and author-review edition · 2026<br>English edition translated from the Brazilian Portuguese <em>Voz, Canto e Ciência</em>.</p>
<p>© 2026 {AUTHOR}. All rights reserved. No part of this book may be reproduced or transmitted in any form or by any means without the prior written permission of the author.</p>
<p>Original book design, cover and illustrations. Photographs: author’s collection.</p>
<p>This book is intended for education and does not replace an assessment by health professionals.</p>
</div>'''
AUDIOS='''<div class="pg black audiopg" id="audios"><div class="k">Companion material</div><h1>Exercise<br>Audio</h1>
<p>Every exercise in this book comes with supporting audio, recorded so you can practice with the right reference for sound, rhythm and pitch. Point your phone camera at the QR code or visit the address below to download the complete set.</p>
<div class="qr"><div class="box">[QR CODE]</div><div class="url">[website address]<small>EXCLUSIVE ACCESS FOR READERS</small></div></div></div>'''
refs=open('/tmp/work/book2/refs_final.html',encoding='utf-8').read()
R=[('<div class="kick">Fontes</div>','<div class="kick">Sources</div>'),('<h1>Referências</h1>','<h1>References</h1>'),
('Esta obra reúne e atualiza o material didático organizado pela autora a partir de estudos e da prática profissional. Abaixo estão as fontes citadas ao longo do texto. Quando os dados completos de uma obra não puderam ser confirmados em catálogo, indicamos o contexto em que ela é citada.','This book brings together and updates teaching material developed by the author from research and professional practice. Below are the sources cited throughout the text. Where full bibliographic details could not be confirmed in a catalog, we indicate the context in which the work is cited.'),
('Obra citada em estudos brasileiros sobre canto coral; dados de edição não confirmados em catálogo.','Cited in Brazilian studies on choral singing; edition details not confirmed in a catalog.'),
('Trabalho citado em:','Cited in:'),('Tradução de La voix chantée: sa technique.','Portuguese translation of La voix chantée: sa technique.'),
('Jeannette LoVetri, pesquisadora norte-americana do canto comercial contemporâneo (CCM); citação do material original. Ver também:','Jeannette LoVetri, US researcher of Contemporary Commercial Music (CCM); as cited in the original material. See also:'),
('Mônica Marsola e Tutti Baê, professoras de canto; obra citada em estudos de técnica vocal; dados de edição não confirmados em catálogo.','Mônica Marsola and Tutti Baê, voice teachers; cited in studies of vocal technique; edition details not confirmed in a catalog.'),
('Tradução de Les racines du rock; ano conforme o material original.','Portuguese translation of Les racines du rock; year as given in the original material.'),
('Experimento com tubo ressonador citado em YANAGISAWA et al. (1989). Ver também:','Resonator-tube experiment cited in YANAGISAWA et al. (1989). See also:'),
('Lisa Popeil, professora e pesquisadora norte-americana do belting; citação do material original. Ver também:','Lisa Popeil, US voice teacher and belting researcher; as cited in the original material. See also:'),
('Neyde Veneziano, pesquisadora de teatro musical (Unicamp); trecho citado em ELME; FERNANDES (2014).','Neyde Veneziano, musical-theater scholar (Unicamp, Brazil); passage cited in ELME; FERNANDES (2014).'),
('Dado sobre o quociente de fechamento no belting, citado no material original; obra não localizada.','Data on the closed quotient in belting, as cited in the original material; source not located.'),
('<h3>Leituras recomendadas</h3>','<h3>Recommended reading</h3>'),('Tese (Doutorado) – Instituto de Artes, Universidade Estadual Paulista','PhD thesis – Institute of Arts, São Paulo State University (UNESP)'),
]
for a,b in R:
    assert a in refs, a[:40]; refs=refs.replace(a,b)
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title><style>{fonts_css()}</style><link rel="stylesheet" href="book_en.css"></head><body>
<div class="pg cream cover"><img src="cover.png"></div>
<div class="pg cream half"><div><p>{TITLE}</p><small>DR. BRÍZIA LACERDA</small></div></div>
<div class="pg black frontis"><img class="fill" src="assets/bw-front.jpg"><div class="cap"><p>{AUTHOR}</p><small>Speech-language pathologist · Voice specialist · Singer · Vocal coach</small></div></div>
<div class="pg cream titlep"><div class="k">Dr. Brízia Lacerda</div><div class="t">Voice,<br>Singing<br><i>and Science</i></div><div class="s">{SUB}</div><div class="a">SPEECH-LANGUAGE PATHOLOGY APPLIED TO THE VOICE</div></div>
{CREDITOS}
<div class="pg black quote"><div class="q">Singers are their own instrument.</div><div class="src">{src(9)}</div></div>
<section class="toc"><h1>Contents</h1>{toc_html()}</section>
{SOBRE_LIVRO}
{SOBRE_AUTORA}
{body}
{refs}
{AUDIOS}
<div class="pg cream cover"><img src="back.png"></div>
</body></html>'''
open("book_en.html","w",encoding="utf-8").write(html)
print("ok", len(toc), sum(len(t[3]) for t in toc))
