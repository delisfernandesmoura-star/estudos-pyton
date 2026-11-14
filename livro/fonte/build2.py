import re, json, os
TITLE="Voz, Canto e Ciência"
SUB="Saúde vocal, técnica vocal e inspiração: fonoaudiologia aplicada à voz cantada e falada"
AUTHOR="Dra. Brízia Lacerda"
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")).zfill(2) if pages.get(k) else ""
AUD=str(pages.get("audios","")) or "final"

old=open("/tmp/work/book/build.py",encoding="utf-8").read()
ADD='''<li>ELME, M. M.; FERNANDES, A. J. Canto popular e padronização vocal. In: CONGRESSO DA ASSOCIAÇÃO NACIONAL DE PESQUISA E PÓS-GRADUAÇÃO EM MÚSICA (ANPPOM), 24., 2014, São Paulo. <em>Anais</em> [...]. São Paulo: ANPPOM, 2014.</li>
<li>GARCIA, M. <em>Traité complet de l’art du chant</em>. Paris, 1847.</li>
<li>LOVETRI, J. 2003. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>MARIZ, J. 2013. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>POPEIL, L. 2012. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>SADOLIN, C. <em>Complete Vocal Technique</em>. Copenhagen: Shout Publishing, 2012.</li>
<li>SCHUTTE, H. K. 1993. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>SPIVEY, N. 2008. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>TITZE, I. R.; WORLEY, A. S.; STORY, B. H. Source-vocal tract interaction in female operatic singing and theater belting. <em>Journal of Singing</em>, v. 67, n. 5, p. 561–572, 2011.</li>
<li>VENEZIANO, N. 2008. <span class="pend">[dados completos da obra a confirmar]</span></li>
<li>WELLS, 2006. <span class="pend">[dados completos da obra a confirmar]</span></li>
'''
REFS=re.search(r"REFS='''(.*?)'''",old,re.S).group(1)
import html as _h
items=re.findall(r"<li>.*?</li>",REFS.split("<h3>")[0],re.S)+[x for x in re.findall(r"<li>.*?</li>",ADD,re.S)]
items=sorted(set(items),key=lambda x: re.sub(r"<[^>]+>","",x).upper())
REFS=re.sub(r"<ul>.*?</ul>","<ul>\n"+"\n".join(items)+"\n</ul>",REFS,count=1,flags=re.S)
parts=[open(f"/tmp/work/book/part{i}.html",encoding="utf-8").read() for i in (1,2,3,4)]
body="\n".join(parts)

# ---- citations ----
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: ET AL\.)?, \d{4})\)', r'<span class="cit">(\1)</span>', body)
# ---- figure renames ----
for a,b in [("fig-registros","f-registros"),("fig-extensao-vozes","f-extensao"),("fig-laringe","f-laringe-corte"),("fig-ciclo-glotico","f-ciclo"),("fig-respiracao","f-respiracao")]:
    body=body.replace(f"img/{a}.svg",f"img/{b}.png")
body=re.sub(r'img/(f-[a-z-]+)\.svg',r'img/\1.png',body)
def fig(name,cap,cls=""):
    return f'<figure class="fig {cls}"><img src="img/{name}.png" alt=""><figcaption>{cap}</figcaption></figure>\n'
def ins_before(anchor,html):
    global body
    assert anchor in body, anchor[:50]
    body=body.replace(anchor,html+anchor,1)
def ins_after(anchor,html):
    global body
    assert anchor in body, anchor[:50]
    body=body.replace(anchor,anchor+html,1)
ins_before('<p>O processo de produção da voz inicia-se', fig("f-aparelho","O aparelho fonador: do pulmão aos lábios, todas as estruturas que participam da produção da voz.","tall"))
ins_after('aproveitamento' if False else 'e assim são produzidas as vogais e as consoantes para a formação das palavras.</p>', fig("f-fonte-filtro","O modelo fonte-filtro: as pregas vocais geram o som básico, e o trato vocal o transforma na voz que ouvimos."))
ins_before('<p>A cinta abdominal é composta', fig("f-diafragma","Na inspiração, o diafragma desce e as costelas se abrem; na expiração, o diafragma relaxa e sobe."))
ins_before('<p>Alguns são abaixadores ou elevadores da laringe', fig("f-laringe-frente","A laringe vista de frente: osso hioide, cartilagens tireoide e cricoide e o início da traqueia."))
ins_after('volte a essa posição antes de começar.</p>\n</div>', fig("f-postura","O ponto de partida: orelha, ombro, quadril, joelho e tornozelo alinhados, com as costas apoiadas na parede.","tall"))
ins_before('<h3>Intensidade da voz</h3>', fig("f-bascula","No movimento de báscula, o músculo cricotireóideo inclina a cartilagem tireoide e alonga as pregas vocais."))
ins_before('<h3>Ontogenia vocal</h3>', fig("f-ondas","Frequência e intensidade: a altura do som depende da frequência; o volume, da amplitude da vibração."))
ins_before('<p>A produção do <strong>fry relaxado</strong>', fig("f-fry","No fry, os pulsos glóticos ficam espaçados e irregulares."))
ins_before('<div class="box origem">', fig("f-twang","O twang: base da língua elevada, constrição ariepiglótica e a sensação de brilho na face.","tall"))
ins_before('<h3>O yodel e a música <em>country</em></h3>', fig("f-yodel","O yodel alterna, de forma intencional, os registros modal e elevado."))
ins_before('<p>O vibrato é aplicado nas finalizações', fig("f-vibrato","O vibrato: uma oscilação regular da frequência em torno da nota."))
ins_before('<p>Os melismas têm seu fundamento', fig("f-melisma","No melisma, uma única sílaba percorre várias notas."))
ins_before('<p>Vendo-se a grosso modo', fig("f-apogiatura","A apogiatura: uma nota vizinha que antecede e valoriza a nota principal."))
body=body.replace("A expressão de “choro” funciona como uma imagem facilitadora para chegar a esse ajuste.","A expressão de “choro” funciona como uma imagem facilitadora para chegar a esse ajuste. Veja o movimento de báscula no Capítulo 10.")

# ---- audio notes ----
ICON='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#B8975A" stroke-width="1.9" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Áudio deste exercício disponível para download · veja a página {AUD}</span></p>'
body=re.sub(r'(<div class="box exercicio">.*?)(</div>)', lambda m: m.group(1)+AUDIO+"\n"+m.group(2), body, flags=re.S)
m=re.search(r'<h3>Desaquecimento vocal</h3>.*?</ul>',body,re.S)
body=body[:m.end()]+"\n"+AUDIO.replace("deste exercício","dos exercícios de desaquecimento")+body[m.end():]

# ---- chapter openers ----
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3)
    return f'<header class="ch-open" id="{cid}"><div class="ch-n">{num:02d}</div><div class="ch-k">Capítulo {num}</div><h2>{title}</h2></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m: chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)

# ---- part openers ----
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

# ---- quote pages ----
def qpage(text,src,photo=None,long=False):
    if photo:
        return f'<div class="pg black quote photo"><div class="ph"><img src="assets/{photo}"></div><div class="tx"><div class="q">{text}</div><div class="src">{src}</div></div></div>\n'
    return f'<div class="pg black quote"><div class="q{" l" if long else ""}">{text}</div><div class="src">{src}</div></div>\n'
QUOTES=[("cap-2","Nenhum exercício de canto deve ser desconfortável.","Capítulo 2 · Aquecimento e desaquecimento vocal",None,False),
        ("cap-4","O ar é o combustível da produção da voz.","Capítulo 4 · Higiene vocal e orientação vocal","bw-q1.jpg",False),
        ("cap-7","O timbre é a personalidade da voz.","Capítulo 6 · Terminologias do canto",None,False),
        ("cap-8","A impressão vocal é como a impressão digital.","Capítulo 7 · Classificação vocal","bw-q2.jpg",False),
        ("cap-9","Aprender a cantar é, inicialmente, aprender a respirar.","Capítulo 9 · Respiração e apoio",None,False),
        ("cap-10","A voz só existe a partir do momento em que a expiração pulmonar fornece uma pressão suficiente para fazer nascer e manter o som laríngeo.","Capítulo 9 · Respiração e apoio",None,True),
        ("cap-11","É preciso ter sempre a impressão de que se pode fazer mais.","Capítulo 9 · Respiração e apoio","bw-q3.jpg",False),
        ("cap-15","O vibrato oferece à voz uma riqueza expressiva, com grande poder emocional.","Capítulo 15 · Vibrato",None,False),
        ("cap-20","Cada pessoa é única e atingirá cores de som e efeitos únicos.","Capítulo 20 · Cores do som e efeitos",None,False),
        ("cap-21","A voz serve ao texto.","Capítulo 21 · Belting",None,False)]
for cid,t,s,ph,lg in QUOTES:
    a=f'<header class="ch-open" id="{cid}">'
    assert a in body, cid
    body=body.replace(a,qpage(t,s,ph,lg)+a,1)

def fonts_css():
    css=""
    for w,st in ((400,"normal"),(500,"normal"),(400,"italic"),(500,"italic")):
        css+=f"@font-face{{font-family:Bodoni;font-weight:{w};font-style:{st};src:url(file://{F}bodoni-moda/files/bodoni-moda-latin-{w}-{st}.woff2)}}\n"
    for w in (300,400,500,600,700):
        css+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}inter/files/inter-latin-{w}-normal.woff2)}}\n"
    return css

# ---- TOC ----
toc=[]
for m in re.finditer(r'<section class="part" id="(parte-\d)">.*?<div class="lab">(.*?)</div><h1>(.*?)</h1>(.*?)</section>',body,re.S):
    sid,lab,tit,rest=m.groups()
    chs=[(c.group(1),c.group(2),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="ch-n">(\d+)</div><div class="ch-k">.*?</div><h2>(.*?)</h2>',rest)]
    toc.append((sid,lab,tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>Sobre este livro</span><span class="p">{pg("sobre-livro")}</span></div>',
       f'<div class="fm"><span>Sobre a autora</span><span class="p">{pg("sobre-autora")}</span></div>']
    for sid,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="k">{lab}</span><span class="t">{tit}</span><span class="p">{pg(sid)}</span></div>')
        for cid,n,t in chs:
            o.append(f'<div class="row"><span class="n">{n}</span><span class="t">{t}</span><span class="p">{pg(cid)}</span></div>')
    o.append(f'<div class="fm" style="margin-top:6mm"><span>Referências</span><span class="p">{pg("referencias")}</span></div>')
    o.append(f'<div class="fm"><span>Áudios dos exercícios</span><span class="p">{pg("audios")}</span></div>')
    return "\n".join(o)

SOBRE_LIVRO=f'''<section class="fsec" id="sobre-livro"><div class="kick">Apresentação</div><h1>Sobre este livro</h1><div class="rule"></div>
<p class="lead">A voz é, ao mesmo tempo, o instrumento mais íntimo e o mais exigido que temos — para cantar, para ensinar, para vender, para liderar, para acolher.</p>
<p>Este livro nasceu para quem quer entender como a voz funciona e aprender a usá-la com técnica, expressão e segurança. O conteúdo reúne e atualiza o material didático organizado pela Dra. Brízia Lacerda a partir da prática clínica e do ensino do canto, de estudos e de referências da literatura científica e da pedagogia vocal. As fontes aparecem de forma discreta ao longo dos capítulos, com a lista completa ao final.</p>
<h3>Para quem é este livro</h3>
<div class="publico">
<div><b>Quem quer aprender a cantar</b><span>Respiração, apoio, registros, classificação vocal e exercícios para treinar com segurança.</span></div>
<div><b>Professores de canto</b><span>Terminologia, fisiologia, estilos e ornamentos organizados para consulta e para a sala de aula.</span></div>
<div><b>Quem quer se comunicar bem</b><span>Cuidados com a voz falada, hidratação, higiene vocal e orientações para quem fala em público.</span></div>
<div><b>Fonoaudiólogos</b><span>Avaliação do cantor, fatores de risco, hábitos inadequados e a base fisiológica da fonação.</span></div>
</div>
<h3>Como o livro está organizado</h3>
<p><strong>Parte I · Saúde Vocal</strong> trata da avaliação, do aquecimento e desaquecimento, da postura, da higiene vocal e dos fatores que protegem ou ameaçam a voz. <strong>Parte II · Fundamentos do Canto</strong> apresenta a terminologia, a classificação vocal, os estilos de canto, a respiração e a fisiologia da fonação. <strong>Parte III · Ornamentos Vocais</strong> explora fry, twang, yodel, vibrato, melismas, cry e apogiatura. <strong>Parte IV · Técnicas Avançadas</strong> apresenta as funções vocais, as cores do som, os efeitos e o belting.</p>
<p>Os exercícios trazem o símbolo de um fone de ouvido: todos têm áudio de apoio, que você pode baixar pelo QR code e pelo site indicados na página {AUD}.</p>
<div class="box aviso"><p class="box-title">Aviso</p><p>Este livro tem finalidade educativa e não substitui a avaliação de um médico, de um fonoaudiólogo ou de um professor de canto. Sintomas como rouquidão persistente, dor ou perda da voz exigem avaliação profissional.</p></div>
</section>'''

SOBRE_AUTORA=f'''<div class="pg cream autora" id="sobre-autora"><div class="ph"><img src="assets/bw-autora.jpg"></div><div class="tx">
<div class="kick">A autora</div><h1>Dra. Brízia<br>Lacerda</h1><div class="rule"></div>
<p>Fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. Atua como cantora, vocal coach, pesquisadora, escritora e palestrante, e é autora de artigo científico publicado.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos, cantores e profissionais que buscam desenvolver conhecimento e prática sobre voz.</p>
<p>Mãe e esposa, leva para o ensino da voz o mesmo cuidado com que enxerga a vida: a voz como expressão da pessoa inteira — corpo, emoção e propósito.</p>
<div class="sig">Brízia Lacerda</div>
</div></div>'''

CREDITOS=f'''<div class="cred">
<p><strong>{TITLE}</strong><br>{SUB}</p>
<p>Autora: {AUTHOR}<br>Versão para impressão e revisão da autora · 2026</p>
<p>© 2026 {AUTHOR}. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>Projeto gráfico, capa e ilustrações originais. Fotografias: acervo da autora.</p>
<p>Este livro tem finalidade educativa e não substitui a avaliação de profissionais de saúde.</p>
</div>'''

AUDIOS='''<div class="pg black audiopg" id="audios"><div class="k">Material complementar</div><h1>Áudios dos<br>exercícios</h1>
<p>Todos os exercícios deste livro têm áudio de apoio, gravado para que você pratique com a referência certa de som, ritmo e afinação. Aponte a câmera do celular para o QR code ou acesse o endereço abaixo para baixar o material completo.</p>
<div class="qr"><div class="box">[QR CODE]</div><div class="url">[endereço do site]<small>ACESSO EXCLUSIVO PARA LEITORES</small></div></div></div>'''

refs=open('refs_final.html',encoding='utf-8').read() if True else REFS.replace('<section class="refs" id="referencias">','<section class="refs" id="referencias"><div class="kick">Fontes</div>').replace("<h1>Referências</h1>","<h1>Referências</h1><div class=\"rule\"></div>")

html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{TITLE}</title><style>{fonts_css()}</style><link rel="stylesheet" href="book2.css"></head><body>
<div class="pg cream cover"><img src="cover.png"></div>
<div class="pg cream half"><div><p>{TITLE}</p><small>DRA. BRÍZIA LACERDA</small></div></div>
<div class="pg black frontis"><img class="fill" src="assets/bw-front.jpg"><div class="cap"><p>{AUTHOR}</p><small>Fonoaudióloga · Especialista em voz · Cantora · Vocal coach</small></div></div>
<div class="pg cream titlep"><div class="k">Dra. Brízia Lacerda</div><div class="t">Voz,<br>Canto<br><i>e Ciência</i></div><div class="s">{SUB}</div><div class="a">FONOAUDIOLOGIA APLICADA À VOZ</div></div>
{CREDITOS}
<div class="pg black quote"><div class="q">O cantor faz de si mesmo o seu instrumento.</div><div class="src">Capítulo 9 · Respiração e apoio</div></div>
<section class="toc"><h1>Sumário</h1>{toc_html()}</section>
{SOBRE_LIVRO}
{SOBRE_AUTORA}
{body}
{refs}
{AUDIOS}
<div class="pg cream cover"><img src="back.png"></div>
</body></html>'''
open("book2.html","w",encoding="utf-8").write(html)
print("ok", len(toc), sum(len(t[3]) for t in toc))
json.dump({"body":body,"sobre_livro":SOBRE_LIVRO,"sobre_autora":SOBRE_AUTORA,"creditos":CREDITOS,"refs":refs,"audios":AUDIOS},open("parts.json","w"),ensure_ascii=False)
