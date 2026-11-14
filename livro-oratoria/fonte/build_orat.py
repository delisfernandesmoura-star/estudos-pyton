import re, json, os
TITLE="Voz, Palco e Presença"
SUB="Oratória com ciência, da preparação vocal à grande apresentação"
AUTHOR="Dra. Brízia Lacerda"
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")).zfill(2) if pages.get(k) else ""
body="\n".join(open(f"part{i}.html",encoding="utf-8").read() for i in (1,2,3))
if os.path.exists("extra1.html"):
    e1=open("extra1.html",encoding="utf-8").read(); i=body.index('<section class="part" id="parte-3">'); j=body.rindex('</section>',0,i); body=body[:j]+e1+"\n"+body[j:]
if os.path.exists("extra2.html"):
    e2=open("extra2.html",encoding="utf-8").read(); a='<h2 class="chapter" id="cap-14">'; body=body.replace(a,e2+"\n"+a,1)
_n=[0]
def _ren(m):
    _n[0]+=1; return f'<h2 class="chapter" id="cap-{_n[0]}"><span class="chapter-num">Capítulo {_n[0]}</span>'
body=re.sub(r'<h2 class="chapter" id="cap-[\w]+"><span class="chapter-num">Capítulo [\w]+</span>',_ren,body)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: et al\.)?, \d{4}(?:; [A-ZÀ-Ý][A-ZÀ-Ý .;\-]*(?: et al\.)?, \d{4})*)\)', r'<span class="cit">(\1)</span>', body)
used=set()
def figrep(m):
    n,cap=m.group(1),m.group(2)
    if n in used or not os.path.exists(f"img/{n}.png"): print("fig skip",n); return ""
    used.add(n); tall=' tall' if n in ("f-aparelho","f-postura") else ''
    return f'<figure class="fig{tall}"><img src="img/{n}.png" alt=""><figcaption>{cap}</figcaption></figure>'
body=re.sub(r'<figure class="fig" data-fig="([\w-]+)">\s*<figcaption>(.*?)</figcaption>\s*</figure>',figrep,body,flags=re.S)
ICON='<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#B8975A" stroke-width="1.9" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Áudio de apoio disponível na plataforma onde você adquiriu este livro</span></p>'
body=re.sub(r'(<div class="box exercicio">.*?)(</div>)',lambda m:m.group(1)+AUDIO+"\n"+m.group(2),body,flags=re.S)
# chapter openers
CH={}
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3); CH[num]=re.sub(r"<[^>]+>","",title)
    return f'<header class="ch-open" id="{cid}"><div class="ch-n">{num:02d}</div><div class="ch-k">Capítulo {num}</div><h2>{title}</h2></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m:chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)
# part openers
PH={"parte-1":("bw-back.jpg","50% 22%"),"parte-2":("bw-p3.jpg","50% 25%"),"parte-3":("bw-q2.jpg","50% 22%"),"parte-4":("bw-q3.jpg","50% 20%")}
NUM={"parte-1":"I","parte-2":"II","parte-3":"III","parte-4":"IV"}
def popen(m):
    sid=m.group(1); inner=m.group(2)
    lab=re.search(r'<p class="part-label">(.*?)</p>',inner).group(1)
    tit=re.search(r'<h1 class="part-title">(.*?)</h1>',inner).group(1)
    sub=re.search(r'<p class="part-sub">(.*?)</p>',inner,re.S).group(1)
    img,pos=PH[sid]
    return (f'<section class="part" id="{sid}">\n<div class="pg black popen"><div class="ph"><img src="assets/{img}" style="object-position:{pos}"></div>'
            f'<div class="tx"><div class="num">{NUM[sid]}</div><div class="lab">{lab}</div><h1>{tit}</h1><div class="sub">{sub}</div></div></div>')
body=re.sub(r'<section class="part" id="(parte-\d)">\s*<div class="part-opener">(.*?)</div>',popen,body,flags=re.S)
# quote pages from the author's own destaques
dest={}
for m in re.finditer(r'<header class="ch-open" id="cap-(\d+)">(.*?)(?=<header class="ch-open"|</section>)',body,re.S):
    d=re.search(r'<p class="destaque">(.*?)</p>',m.group(2),re.S)
    if d: dest[int(m.group(1))]=re.sub(r"<[^>]+>","",d.group(1)).strip()
PHOTO={3:"bw-p1.jpg",9:"bw-p2.jpg",13:"bw-front.jpg"}
for n in (1,3,5,7,9,11,13,15):
    if n not in dest: continue
    t=dest[n]; src=f"Capítulo {n} · {CH[n]}"; lg=" l" if len(t)>95 else ""
    if n in PHOTO: q=f'<div class="pg black quote photo"><div class="ph"><img src="assets/{PHOTO[n]}"></div><div class="tx"><div class="q{lg}">{t}</div><div class="src">{src}</div></div></div>\n'
    else: q=f'<div class="pg black quote"><div class="q{lg}">{t}</div><div class="src">{src}</div></div>\n'
    nxt=f'<header class="ch-open" id="cap-{n+1}">'
    if nxt in body: body=body.replace(nxt,q+nxt,1)
def fonts_css():
    css=""
    for w,st in ((400,"normal"),(500,"normal"),(400,"italic"),(500,"italic")):
        css+=f"@font-face{{font-family:Bodoni;font-weight:{w};font-style:{st};src:url(file://{F}bodoni-moda/files/bodoni-moda-latin-{w}-{st}.woff2)}}\n"
    for w in (300,400,500,600,700):
        css+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}inter/files/inter-latin-{w}-normal.woff2)}}\n"
    css+=f"@font-face{{font-family:Inter;font-style:italic;font-weight:400;src:url(file://{F}inter/files/inter-latin-400-italic.woff2)}}\n"
    return css
toc=[]
for m in re.finditer(r'<section class="part" id="(parte-\d)">.*?<div class="lab">(.*?)</div><h1>(.*?)</h1>(.*?)</section>',body,re.S):
    sid,lab,tit,rest=m.groups()
    chs=[(c.group(1),c.group(2),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="ch-n">(\d+)</div><div class="ch-k">.*?</div><h2>(.*?)</h2>',rest)]
    toc.append((sid,lab,tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>Sobre este livro</span><span class="p">{pg("sobre-livro")}</span></div>',f'<div class="fm"><span>Sobre a autora</span><span class="p">{pg("sobre-autora")}</span></div>']
    for sid,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="k">{lab}</span><span class="t">{tit}</span><span class="p">{pg(sid)}</span></div>')
        for cid,n,t in chs: o.append(f'<div class="row"><span class="n">{n}</span><span class="t">{t}</span><span class="p">{pg(cid)}</span></div>')
    o.append(f'<div class="fm" style="margin-top:6mm"><span>Apêndice · A estante da oratória</span><span class="p">{pg("estante")}</span></div>')
    o.append(f'<div class="fm"><span>Referências</span><span class="p">{pg("referencias")}</span></div>')
    return "\n".join(o)
SOBRE_LIVRO='''<section class="fsec" id="sobre-livro"><div class="kick">Apresentação</div><h1>Sobre este livro</h1><div class="rule"></div>
<p class="lead">Antes do discurso, existe a voz. Antes do palco, existe o cuidado.</p>
<p>Existem livros excelentes sobre oratória. Durante anos, eu li, estudei e testei os mais influentes do mundo, dos guias do TED aos clássicos de Dale Carnegie, dos estudos sobre mensagens que ficam na memória às técnicas para falar de improviso. Ao mesmo tempo, eu me aprofundei na literatura brasileira de voz e expressividade, que é a base do meu trabalho como fonoaudióloga.</p>
<p>Este livro é o resultado dessa curadoria. Eu reuni o que esses autores têm de mais útil, passei cada ideia pelo filtro da fonoaudiologia e organizei tudo em um guia prático, na ordem em que a voz precisa ser cuidada: primeiro o instrumento, depois a preparação vocal, em seguida a técnica de comunicação e, por fim, o palco e o treino. Você não precisa ler dezenas de livros para chegar ao essencial: eu fiz esse caminho e trago aqui o que realmente funciona, com o crédito de cada fonte.</p>
<p>Ao longo dos capítulos, os quadros <strong>Da estante</strong> apresentam a técnica central de cada obra de referência, seguida do <strong>filtro da fonoaudióloga</strong>: o que vale adotar, o que adaptar e o que evitar para proteger a sua voz. No final, o apêndice <strong>A estante da oratória</strong> resume cada livro para consulta rápida.</p>
<h3>Para quem é este livro</h3>
<div class="publico">
<div><b>Quem fala em público</b><span>Palestrantes, líderes, advogados, vendedores, religiosos e criadores de conteúdo.</span></div>
<div><b>Professores</b><span>Quem usa a voz por horas, todos os dias, e precisa dela saudável e expressiva.</span></div>
<div><b>Quem quer perder o medo</b><span>Preparação, respiração e treino para transformar o nervosismo em presença.</span></div>
<div><b>Fonoaudiólogos e treinadores</b><span>Base técnica, curadoria de referências e um roteiro de treinamento para quem prepara outras pessoas.</span></div>
</div>
<div class="aviso-aud"><b>Áudios dos exercícios</b>Os áudios referidos neste livro estão disponíveis na plataforma onde o livro digital foi adquirido.</div>
<div class="box aviso"><p class="box-title">Aviso</p><p>Este livro tem finalidade educativa e não substitui a avaliação de um médico otorrinolaringologista ou de um fonoaudiólogo. Os exercícios são indicados para vozes saudáveis. Rouquidão persistente, dor, falhas na voz ou cansaço vocal frequente exigem avaliação profissional. As obras citadas são apresentadas em resumo e paráfrase, com crédito aos seus autores, e não substituem a leitura dos originais.</p></div>
</section>'''
SOBRE_AUTORA='''<div class="pg cream autora" id="sobre-autora"><div class="ph"><img src="assets/bw-autora.jpg"></div><div class="tx">
<div class="kick">A autora</div><h1>Dra. Brízia<br>Lacerda</h1><div class="rule"></div>
<p>Fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. Atua como cantora, vocal coach, pesquisadora, escritora e palestrante.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos, cantores e profissionais que usam a voz para trabalhar. É autora de <em>Voz, Canto e Ciência</em>.</p>
<p>Mãe e esposa, acredita que comunicar bem começa por cuidar bem do próprio instrumento.</p>
<div class="sig">Brízia Lacerda</div></div></div>'''
CRED=f'''<div class="cred"><p><strong>{TITLE}</strong><br>{SUB}</p>
<p>Autora: {AUTHOR}<br>Versão para impressão e revisão da autora · 2026</p>
<p>© 2026 {AUTHOR}. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>Projeto gráfico, capa e ilustrações originais. Fotografias: acervo da autora.</p>
<p>Esta obra tem finalidade educativa e não substitui a avaliação de médico otorrinolaringologista ou de fonoaudiólogo.</p></div>'''
REFS=open("refs.html",encoding="utf-8").read()
ESTANTE=open("estante.html",encoding="utf-8").read() if os.path.exists("estante.html") else ""
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{TITLE}</title><style>{fonts_css()}</style><link rel="stylesheet" href="orat.css"></head><body>
<div class="pg cream cover"><img src="cover.png"></div>
<div class="pg cream half"><div><p>{TITLE}</p><small>DRA. BRÍZIA LACERDA</small></div></div>
<div class="pg black frontis"><img class="fill" src="assets/bw-q1.jpg"><div class="cap"><p>{AUTHOR}</p><small>Fonoaudióloga · Especialista em voz · Palestrante</small></div></div>
<div class="pg cream titlep"><div class="k">Dra. Brízia Lacerda</div><div class="t">Voz,<br>Palco e<br><i>Presença</i></div><div class="s">{SUB}</div><div class="a">FONOAUDIOLOGIA APLICADA À ORATÓRIA</div></div>
{CRED}
<div class="pg black quote"><div class="q">Antes do discurso, existe a voz.</div><div class="src">Sobre este livro</div></div>
<section class="toc"><h1>Sumário</h1>{toc_html()}</section>
{SOBRE_LIVRO}
{SOBRE_AUTORA}
{body}
{ESTANTE}
{REFS}
<div class="pg cream cover"><img src="back.png"></div>
</body></html>'''
open("orat.html","w",encoding="utf-8").write(html)
print("ok",len(toc),sum(len(t[3]) for t in toc),sorted(used),sorted(dest))
