import re, json, os
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")) if pages.get(k) else ""
body="\n".join(open(f,encoding="utf-8").read() for f in ("part1.html","part2.html","part3.html"))
used=set()
def figrep(m):
    name=m.group(1); cap=m.group(2)
    if name in used or not os.path.exists(f"img/{name}.png"): return ""
    used.add(name)
    return f'<figure class="fig"><img src="img/{name}.png" alt=""><figcaption>{cap}</figcaption></figure>'
body=re.sub(r'<figure class="fig" data-fig="([\w-]+)">\s*<figcaption>(.*?)</figcaption>\s*</figure>',figrep,body,flags=re.S)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: et al\.)?, \d{4}(?:; [A-ZÀ-Ý][A-ZÀ-Ý .\-]*(?: et al\.)?, \d{4})*)\)', r'<span class="cit">(\1)</span>', body)
body=re.sub(r'<div class="linhas" data-n="(\d+)"></div>',lambda m:'<div class="linhas">'+'<div></div>'*int(m.group(1))+'</div>',body)
ICON='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8a6a2e" stroke-width="2" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Áudio de apoio disponível na plataforma onde você adquiriu este livro.</span></p>'
body=re.sub(r'(<div class="box praticar">.*?)(</div>)',lambda m:m.group(1)+AUDIO+m.group(2),body,flags=re.S)
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3)
    return f'<header class="ch-open" id="{cid}"><div class="k kick">Capítulo {num}</div><h2>{title}</h2></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m:chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)
def popen(m):
    n=int(m.group(1)); inner=m.group(2)
    g=lambda c:(re.search(rf'<(?:p|h1) class="{c}">(.*?)</(?:p|h1)>',inner,re.S) or [None,""])[1]
    q=g("part-quote")
    return (f'<section class="part" id="parte-{n}">\n<div class="pg popen"><div class="txt"><div class="lab kick">{g("part-label")}</div><div class="num">{n:02d}</div><h1>{g("part-title")}</h1><div class="sub">{g("part-sub")}</div></div>'
            +(f'<div class="q">{q}</div>' if q else '')+f'<div class="art"><img src="img/op{n}.png"></div></div>')
body=re.sub(r'<section class="part" id="parte-(\d)">\s*<div class="part-opener">(.*?)</div>',popen,body,flags=re.S)
toc=[]
for m in re.finditer(r'<section class="part" id="parte-(\d)">.*?<h1>(.*?)</h1>(.*?)</section>',body,re.S):
    n,tit,rest=m.groups()
    chs=[(c.group(1),re.search(r'\d+',c.group(2)).group(0),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="k kick">(.*?)</div><h2>(.*?)</h2>',rest)]
    toc.append((int(n),tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>Uma carta para você</span><span class="p">{pg("carta")}</span></div>',f'<div class="fm"><span>Como usar este livro</span><span class="p">{pg("como-usar")}</span></div>']
    for n,tit,chs in toc:
        o.append(f'<div class="part"><span class="n">{n:02d}</span><span class="t">{tit}</span><span class="p">{pg("parte-"+str(n))}</span></div>')
        for cid,num,t in chs: o.append(f'<div class="row"><span class="t">{num}. {t}</span><span class="p">{pg(cid)}</span></div>')
    for k,t in (("referencias","Referências"),("sobre-autora","Sobre a autora")):
        o.append(f'<div class="fm"><span>{t}</span><span class="p">{pg(k)}</span></div>')
    return "\n".join(o)
def fonts():
    c=""
    for w in (400,500,600,700):
        for st in ("normal","italic"): c+=f"@font-face{{font-family:Lora;font-weight:{w};font-style:{st};src:url(file://{F}lora/files/lora-latin-{w}-{st}.woff2)}}\n"
    for w in (400,500,600,700):
        for st in ("normal","italic"): c+=f"@font-face{{font-family:Bodoni;font-weight:{w};font-style:{st};src:url(file://{F}bodoni-moda/files/bodoni-moda-latin-{w}-{st}.woff2)}}\n"
    for w in (400,600): c+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}inter/files/inter-latin-{w}-normal.woff2)}}\n"
    return c
CARTA='''<section class="fsec" id="carta"><h1>Uma carta para você</h1>
<div class="carta"><div class="ph"><img src="autora.jpg"></div><div>
<p>Eu sou a Brízia. Sou fonoaudióloga, especialista em voz, cantora e professora de canto. Todos os dias encontro pessoas que guardaram, durante anos, a mesma vontade: cantar.</p>
<p>Talvez você seja uma delas. Construiu uma carreira, cuidou da família, realizou muita coisa. E agora, com mais tempo e mais liberdade, decidiu que chegou a sua vez.</p>
</div></div>
<p>Este livro é um convite para transformar esse desejo em prática: aprender técnica, conhecer a sua voz de hoje, escolher um repertório que conte a sua história e viver a música com prazer, seja num sarau com amigos, num coral, numa banda ou no casamento de alguém que você ama.</p>
<p>Ele também foi escrito para quem ensina: professores de canto, regentes e educadores que acompanham pessoas nessa fase tão rica da vida.</p>
<p>Aqui não há promessas milagrosas. Há conhecimento, cuidado e muita alegria. A sua voz tem uma história. Agora ela vai cantar.</p>
<div class="sig">Com carinho, Brízia</div>
</section>'''
COMO='''<section class="fsec" id="como-usar"><h1>Como usar este livro</h1>
<p>Os capítulos são curtos e podem ser lidos na ordem ou conforme o seu interesse. Os exercícios cabem na sua rotina: em casa, na aula, no ensaio. Ao longo do livro, você vai encontrar:</p>
<div class="legend">
<div class="lg praticar"><b>Para praticar</b>Exercícios passo a passo, com áudio de apoio.</div>
<div class="lg historia"><b>Uma história</b>Helena, Ricardo e Lúcia contam a experiência deles.</div>
<div class="lg atv"><b>Sua vez</b>Espaços para escrever e planejar.</div>
<div class="lg saiba"><b>Bom saber</b>Informações curtas e úteis.</div>
<div class="lg ciencia"><b>Por trás da ciência</b>A base fonoaudiológica, com as fontes.</div>
<div class="lg professor"><b>Para o professor</b>Orientações para quem ensina.</div>
</div>
<div class="aviso"><b>Áudios dos exercícios</b>Os áudios referidos neste livro estão disponíveis na plataforma onde o livro digital foi adquirido. Lá você encontra a referência de som, ritmo e afinação de cada exercício dos quadros “Para praticar”, para ouvir quantas vezes quiser.</div>
</section>
<section class="fsec" id="personagens"><h1>Quem caminha com você</h1>
<p>Três pessoas vão compartilhar a experiência delas ao longo destas páginas. Talvez você se reconheça em alguma.</p>
<div class="perfis">
<div class="perfil"><div class="mono">H</div><div><b>Helena, 58 anos</b><span>Deixou o mundo corporativo depois de uma carreira brilhante. Sempre cantou no carro e no chuveiro. Agora faz aulas e está preparando um sarau para os amigos.</span></div></div>
<div class="perfil"><div class="mono">R</div><div><b>Ricardo, 63 anos</b><span>Engenheiro, reencontrou os amigos da juventude e voltou a tocar violão e a cantar na banda deles.</span></div></div>
<div class="perfil"><div class="mono">L</div><div><b>Lúcia, 54 anos</b><span>Empresária, descobriu uma nova cor na voz depois da menopausa. Quer cantar no casamento da filha.</span></div></div>
</div>
<div class="aviso"><b>Um combinado importante</b>Este é um livro educativo. Os exercícios são para vozes saudáveis, como prática de canto. Ele não faz diagnóstico, não indica tratamento e não substitui a avaliação de um médico otorrinolaringologista e de um fonoaudiólogo. Se você percebe alguma alteração na voz, na respiração ou na audição, converse com esses profissionais antes de começar. E respeite sempre o seu corpo: diante de tontura, dor ou cansaço, faça uma pausa.</div>
</section>'''
REFS=open("/tmp/work/senior/build_senior.py",encoding="utf-8").read().split("REFS='''")[1].split("'''")[0]
AUTORA='''<section class="fsec" id="sobre-autora"><h1>Sobre a autora</h1>
<div class="carta"><div class="ph"><img src="autora2.jpg"></div><div>
<p><strong>Dra. Brízia Lacerda</strong> é fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. É cantora, vocal coach, pesquisadora, escritora e palestrante.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos e cantores. É autora de <em>Voz, Canto e Ciência</em> e de <em>Minha voz cresce comigo</em>.</p>
<p>Mãe e esposa, acredita que cada fase da vida tem a sua própria música, e que é sempre hora de cantá-la.</p></div></div>
</section>'''
CRED='''<div class="cred" id="cred">
<p><strong>Agora é a Minha Vez</strong><br>O prazer de cantar na melhor fase da vida</p>
<p>Autora: Dra. Brízia Lacerda<br>Versão para impressão e revisão da autora · 2026</p>
<p>© 2026 Dra. Brízia Lacerda. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>Projeto gráfico, capa e ilustrações originais. Os personagens são fictícios.</p>
<p>Esta obra tem finalidade exclusivamente educativa e não substitui a avaliação, o diagnóstico ou o tratamento realizados por médico otorrinolaringologista, fonoaudiólogo ou outros profissionais de saúde.</p></div>'''
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Agora é a Minha Vez</title><style>{fonts()}</style><link rel="stylesheet" href="vez.css"></head><body>
<div class="pg"><img class="fill" src="cover.png"></div>
{CRED}
<section class="toc" id="sumario"><h1>Sumário</h1>{toc_html()}</section>
{CARTA}
{COMO}
{body}
{REFS}
{AUTORA}
<div class="pg"><img class="fill" src="back.png"></div>
</body></html>'''
open("vez.html","w",encoding="utf-8").write(html)
print("ok",len(toc),sum(len(t[2]) for t in toc),sorted(used))
