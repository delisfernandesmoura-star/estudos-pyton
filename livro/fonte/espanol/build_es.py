import re, json, os
TITLE="Voz, Canto y Ciencia"
SUB="Salud vocal, técnica vocal e inspiración: fonoaudiología aplicada a la voz cantada y hablada"
AUTHOR="Dra. Brízia Lacerda"
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")).zfill(2) if pages.get(k) else ""
AUD=str(pages.get("audios","")) or "final"

PT=[open(f"/tmp/work/book/part{i}.html",encoding="utf-8").read() for i in (1,2,3,4)]
EN=[open(f"/tmp/work/es/part{i}.html",encoding="utf-8").read() for i in (1,2,3,4)]

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
FIGS=[(0,'<p>O processo de produção da voz inicia-se',False,"f-aparelho","El aparato fonador: de los pulmones a los labios, todas las estructuras que participan en la producción de la voz.","tall"),
(0,'e assim são produzidas as vogais e as consoantes para a formação das palavras.</p>',True,"f-fonte-filtro","El modelo fuente-filtro: los pliegues vocales generan el sonido básico y el tracto vocal lo transforma en la voz que oímos.",""),
(1,'<p>A cinta abdominal é composta',False,"f-diafragma","En la inspiración, el diafragma desciende y las costillas se abren; en la espiración, el diafragma se relaja y sube.",""),
(1,'<p>Alguns são abaixadores ou elevadores da laringe',False,"f-laringe-frente","La laringe vista de frente: hueso hioides, cartílagos tiroides y cricoides y el inicio de la tráquea.",""),
(1,'volte a essa posição antes de começar.</p>\n</div>',True,"f-postura","El Punto de Partida: oreja, hombro, cadera, rodilla y tobillo alineados, con la espalda apoyada en la pared.","tall"),
(1,'<h3>Intensidade da voz</h3>',False,"f-bascula","En el movimiento de báscula, el músculo cricotiroideo inclina el cartílago tiroides y alarga los pliegues vocales.",""),
(1,'<h3>Ontogenia vocal</h3>',False,"f-ondas","Frecuencia e intensidad: la altura depende de la frecuencia; el volumen, de la amplitud de la vibración.",""),
(2,'<p>A produção do <strong>fry relaxado</strong>',False,"f-fry","En el fry, los pulsos glóticos se vuelven espaciados e irregulares.",""),
(2,'<div class="box origem">',False,"f-twang","El twang: base de la lengua elevada, constricción ariepiglótica y sensación de brillo en la cara.","tall"),
(2,'<h3>O yodel e a música <em>country</em></h3>',False,"f-yodel","El yodel alterna intencionalmente los registros modal y elevado.",""),
(2,'<p>O vibrato é aplicado nas finalizações',False,"f-vibrato","El vibrato: una oscilación regular de la frecuencia en torno a la nota.",""),
(2,'<p>Os melismas têm seu fundamento',False,"f-melisma","En el melisma, una sola sílaba recorre varias notas.",""),
(2,'<p>Vendo-se a grosso modo',False,"f-apogiatura","La apoyatura: una nota vecina que antecede y realza la nota principal.","")]
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
AUDIO=f'<p class="audio">{ICON}<span>Audio de este ejercicio disponible para descargar · ver página {AUD}</span></p>'
EN[0]=EN[0][:coolpos]+"\n"+AUDIO.replace("de este ejercicio","de los ejercicios de enfriamiento")+EN[0][coolpos:]
# cry -> see chapter 10
o=[m.start() for m in re.finditer(r'<div class="box origem">',EN[2])][1]
e=EN[2].index('</p>',o); EN[2]=EN[2][:e]+' Consulta el movimiento de báscula en el Capítulo 10.'+EN[2][e:]
body="\n".join(EN)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: ET AL\.)?, \d{4}(?:, p\. [\d\-]+)?)\)', r'<span class="cit">(\1)</span>', body)
for a,b in [("fig-registros","f-registros"),("fig-extensao-vozes","f-extensao"),("fig-laringe","f-laringe-corte"),("fig-ciclo-glotico","f-ciclo"),("fig-respiracao","f-respiracao")]:
    body=body.replace(f"img/{a}.svg",f"img/{b}.png")
body=re.sub(r'img/(f-[a-z-]+)\.svg',r'img/\1.png',body)
body=re.sub(r'(<div class="box exercicio">.*?)(</div>)', lambda m: m.group(1)+AUDIO+"\n"+m.group(2), body, flags=re.S)
CH={}
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3); CH[num]=re.sub(r"<[^>]+>","",title)
    return f'<header class="ch-open" id="{cid}"><div class="ch-n">{num:02d}</div><div class="ch-k">Capítulo {num}</div><h2>{title}</h2></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m: chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)
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
src=lambda n: f"Capítulo {n} · {CH[n]}"
QUOTES=[("cap-2","Ningún ejercicio de canto debe ser incómodo.",2,None,False),
 ("cap-4","El aire es el combustible de la producción de la voz.",4,"bw-q1.jpg",False),
 ("cap-7","El timbre es la personalidad de la voz.",6,None,False),
 ("cap-8","La huella vocal es como la huella digital.",7,"bw-q2.jpg",False),
 ("cap-9","Aprender a cantar es, ante todo, aprender a respirar.",9,None,False),
 ("cap-10","La voz solo existe a partir del momento en que la espiración pulmonar aporta la presión suficiente para hacer nacer y mantener el sonido laríngeo.",9,None,True),
 ("cap-11","Hay que tener siempre la impresión de que se puede dar más.",9,"bw-q3.jpg",False),
 ("cap-15","El vibrato ofrece a la voz una riqueza expresiva de gran poder emocional.",15,None,False),
 ("cap-20","Cada persona es única y alcanzará colores de sonido y efectos únicos.",20,None,False),
 ("cap-21","La voz está al servicio del texto.",21,None,False)]
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
    o=[f'<div class="fm"><span>Sobre este libro</span><span class="p">{pg("sobre-livro")}</span></div>',
       f'<div class="fm"><span>Sobre la autora</span><span class="p">{pg("sobre-autora")}</span></div>']
    for sid,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="k">{lab}</span><span class="t">{tit}</span><span class="p">{pg(sid)}</span></div>')
        for cid,n,t in chs:
            o.append(f'<div class="row"><span class="n">{n}</span><span class="t">{t}</span><span class="p">{pg(cid)}</span></div>')
    o.append(f'<div class="fm" style="margin-top:6mm"><span>Referencias</span><span class="p">{pg("referencias")}</span></div>')
    o.append(f'<div class="fm"><span>Audios de los ejercicios</span><span class="p">{pg("audios")}</span></div>')
    return "\n".join(o)
PT1=EN[0]; 
SOBRE_LIVRO=f'''<section class="fsec" id="sobre-livro"><div class="kick">Presentación</div><h1>Sobre este libro</h1><div class="rule"></div>
<p class="lead">La voz es, al mismo tiempo, el instrumento más íntimo y el más exigido que tenemos: para cantar, para enseñar, para vender, para liderar, para acoger.</p>
<p>Este libro nació para quienes quieren entender cómo funciona la voz y aprender a usarla con técnica, expresión y seguridad. Reúne y actualiza el material didáctico desarrollado por la Dra. Brízia Lacerda a partir de su práctica clínica y de la enseñanza del canto, de estudios y de referencias de la literatura científica y de la pedagogía vocal. Las fuentes aparecen de forma discreta a lo largo de los capítulos, con la lista completa al final.</p>
<h3>Para quién es este libro</h3>
<div class="publico">
<div><b>Quien quiere aprender a cantar</b><span>Respiración, apoyo, registros, clasificación vocal y ejercicios para entrenar con seguridad.</span></div>
<div><b>Profesores de canto</b><span>Terminología, fisiología, estilos y ornamentos organizados para consulta y para el aula.</span></div>
<div><b>Quien quiere comunicar bien</b><span>Cuidados de la voz hablada, hidratación, higiene vocal y orientaciones para quien habla en público.</span></div>
<div><b>Fonoaudiólogos y logopedas</b><span>Evaluación del cantante, factores de riesgo, hábitos inadecuados y la base fisiológica de la fonación.</span></div>
</div>
<h3>Cómo está organizado</h3>
<p><strong>Parte I · Salud Vocal</strong> aborda la evaluación, el calentamiento y el enfriamiento, la postura, la higiene vocal y los factores que protegen o amenazan la voz. <strong>Parte II · Fundamentos del Canto</strong> presenta la terminología, la clasificación vocal, los estilos de canto, la respiración y la fisiología de la fonación. <strong>Parte III · Ornamentos Vocales</strong> explora el fry, el twang, el yodel, el vibrato, los melismas, el cry y la apoyatura. <strong>Parte IV · Técnicas Avanzadas</strong> presenta las funciones vocales, los colores del sonido, los efectos y el belting.</p>
<p>Los ejercicios llevan el símbolo de unos auriculares: todos tienen audio de apoyo, que puedes descargar mediante el código QR y el sitio web indicados en la página {AUD}.</p>
<div class="box aviso"><p class="box-title">Aviso</p><p>Este libro tiene una finalidad educativa y no sustituye la evaluación de un médico, de un fonoaudiólogo o de un profesor de canto. Síntomas como ronquera persistente, dolor o pérdida de la voz requieren una evaluación profesional.</p></div>
</section>'''
SOBRE_AUTORA=f'''<div class="pg cream autora" id="sobre-autora"><div class="ph"><img src="assets/bw-autora.jpg"></div><div class="tx">
<div class="kick">La autora</div><h1>Dra. Brízia<br>Lacerda</h1><div class="rule"></div>
<p>Fonoaudióloga formada en la PUC Minas (Pontificia Universidad Católica de Minas Gerais, Brasil), con posgrado y especialización en voz. Es cantante, vocal coach, investigadora, escritora y conferencista, y autora de un artículo científico publicado.</p>
<p>Al frente de la Faculdade da Voz, reúne ciencia vocal, canto, enseñanza y mentoría para profesores de canto, fonoaudiólogos, cantantes y profesionales que desean desarrollar su conocimiento y su práctica sobre la voz.</p>
<p>Madre y esposa, lleva a la enseñanza de la voz el mismo cuidado con que mira la vida: la voz como expresión de la persona entera — cuerpo, emoción y propósito.</p>
<div class="sig">Brízia Lacerda</div>
</div></div>'''
CREDITOS=f'''<div class="cred">
<p><strong>{TITLE}</strong><br>{SUB}</p>
<p>Autora: {AUTHOR}<br>Versión para impresión y revisión de la autora · 2026<br>Edición en español traducida del original en portugués de Brasil <em>Voz, Canto e Ciência</em>.</p>
<p>© 2026 {AUTHOR}. Todos los derechos reservados. Ninguna parte de esta obra puede reproducirse ni transmitirse por ningún medio sin la autorización previa y por escrito de la autora.</p>
<p>Diseño gráfico, cubierta e ilustraciones originales. Fotografías: archivo de la autora.</p>
<p>Este libro tiene una finalidad educativa y no sustituye la evaluación de profesionales de la salud.</p>
</div>'''
AUDIOS='''<div class="pg black audiopg" id="audios"><div class="k">Material complementario</div><h1>Audios de los<br>ejercicios</h1>
<p>Todos los ejercicios de este libro tienen audio de apoyo, grabado para que practiques con la referencia correcta de sonido, ritmo y afinación. Apunta la cámara del móvil al código QR o visita la dirección de abajo para descargar el material completo.</p>
<div class="qr"><div class="box">[CÓDIGO QR]</div><div class="url">[dirección del sitio web]<small>ACCESO EXCLUSIVO PARA LECTORES</small></div></div></div>'''
refs=open('/tmp/work/book2/refs_final.html',encoding='utf-8').read()
R=[('<div class="kick">Fontes</div>','<div class="kick">Fuentes</div>'),('<h1>Referências</h1>','<h1>Referencias</h1>'),
('Esta obra reúne e atualiza o material didático organizado pela autora a partir de estudos e da prática profissional. Abaixo estão as fontes citadas ao longo do texto. Quando os dados completos de uma obra não puderam ser confirmados em catálogo, indicamos o contexto em que ela é citada.','Esta obra reúne y actualiza el material didáctico desarrollado por la autora a partir de estudios y de la práctica profesional. A continuación se indican las fuentes citadas a lo largo del texto. Cuando los datos completos de una obra no pudieron confirmarse en catálogo, se señala el contexto en que se cita.'),
('Obra citada em estudos brasileiros sobre canto coral; dados de edição não confirmados em catálogo.','Obra citada en estudios brasileños sobre canto coral; datos de edición no confirmados en catálogo.'),
('Trabalho citado em:','Trabajo citado en:'),('Tradução de La voix chantée: sa technique.','Traducción al portugués de La voix chantée: sa technique.'),
('Jeannette LoVetri, pesquisadora norte-americana do canto comercial contemporâneo (CCM); citação do material original. Ver também:','Jeannette LoVetri, investigadora estadounidense del canto comercial contemporáneo (CCM); cita del material original. Véase también:'),
('Mônica Marsola e Tutti Baê, professoras de canto; obra citada em estudos de técnica vocal; dados de edição não confirmados em catálogo.','Mônica Marsola y Tutti Baê, profesoras de canto; obra citada en estudios de técnica vocal; datos de edición no confirmados en catálogo.'),
('Tradução de Les racines du rock; ano conforme o material original.','Traducción al portugués de Les racines du rock; año según el material original.'),
('Experimento com tubo ressonador citado em YANAGISAWA et al. (1989). Ver também:','Experimento con tubo resonador citado en YANAGISAWA et al. (1989). Véase también:'),
('Lisa Popeil, professora e pesquisadora norte-americana do belting; citação do material original. Ver também:','Lisa Popeil, profesora e investigadora estadounidense del belting; cita del material original. Véase también:'),
('Neyde Veneziano, pesquisadora de teatro musical (Unicamp); trecho citado em ELME; FERNANDES (2014).','Neyde Veneziano, investigadora de teatro musical (Unicamp, Brasil); pasaje citado en ELME; FERNANDES (2014).'),
('Dado sobre o quociente de fechamento no belting, citado no material original; obra não localizada.','Dato sobre el cociente de cierre en el belting, citado en el material original; obra no localizada.'),
('<h3>Leituras recomendadas</h3>','<h3>Lecturas recomendadas</h3>'),('Tese (Doutorado) – Instituto de Artes, Universidade Estadual Paulista','Tesis doctoral – Instituto de Artes, Universidade Estadual Paulista'),
]
for a,b in R:
    assert a in refs, a[:40]; refs=refs.replace(a,b)
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{TITLE}</title><style>{fonts_css()}</style><link rel="stylesheet" href="book_es.css"></head><body>
<div class="pg cream cover"><img src="cover.png"></div>
<div class="pg cream half"><div><p>{TITLE}</p><small>DRA. BRÍZIA LACERDA</small></div></div>
<div class="pg black frontis"><img class="fill" src="assets/bw-front.jpg"><div class="cap"><p>{AUTHOR}</p><small>Fonoaudióloga · Especialista en voz · Cantante · Vocal coach</small></div></div>
<div class="pg cream titlep"><div class="k">Dra. Brízia Lacerda</div><div class="t">Voz,<br>Canto<br><i>y Ciencia</i></div><div class="s">{SUB}</div><div class="a">FONOAUDIOLOGÍA APLICADA A LA VOZ</div></div>
{CREDITOS}
<div class="pg black quote"><div class="q">El cantante hace de sí mismo su instrumento.</div><div class="src">{src(9)}</div></div>
<section class="toc"><h1>Índice</h1>{toc_html()}</section>
{SOBRE_LIVRO}
{SOBRE_AUTORA}
{body}
{refs}
{AUDIOS}
<div class="pg cream cover"><img src="back.png"></div>
</body></html>'''
open("book_es.html","w",encoding="utf-8").write(html)
print("ok", len(toc), sum(len(t[3]) for t in toc))
