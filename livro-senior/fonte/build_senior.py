import re, json, os
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")) if pages.get(k) else ""
AUD=str(pages.get("audios","")) or "final"
body="\n".join(open(f,encoding="utf-8").read() for f in ("part1.html","part2.html","part3.html"))
used=set()
def figrep(m):
    name=m.group(1); cap=m.group(2)
    if name in used: return ""
    used.add(name)
    cls="fig char" if name in ("celia","antonio","marta") else "fig"
    return f'<figure class="{cls}"><img src="img/{name}.png" alt=""><figcaption>{cap}</figcaption></figure>'
body=re.sub(r'<figure class="fig" data-fig="([\w-]+)">\s*<figcaption>(.*?)</figcaption>\s*</figure>',figrep,body,flags=re.S)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: et al\.)?, \d{4}(?:; [A-ZÀ-Ý][A-ZÀ-Ý .\-]*(?: et al\.)?, \d{4})*)\)', r'<span class="cit">(\1)</span>', body)
body=re.sub(r'<div class="linhas" data-n="(\d+)"></div>',lambda m:'<div class="linhas">'+'<div></div>'*int(m.group(1))+'</div>',body)
ICON='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#8a6a2e" stroke-width="2.2" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Áudio de apoio disponível na plataforma onde você adquiriu este livro.</span></p>'
body=re.sub(r'(<div class="box praticar">.*?)(</div>)',lambda m:m.group(1)+AUDIO+m.group(2),body,flags=re.S)
COL={1:"#D9846E",2:"#7FA58A",3:"#B8904A",4:"#9C8CC4",5:"#4A4F5C"}
PART_OF={}
for sm in re.finditer(r'<section class="part" id="parte-(\d)">(.*?)</section>',body,re.S):
    for cm in re.finditer(r'id="cap-(\d+)"',sm.group(2)): PART_OF[int(cm.group(1))]=int(sm.group(1))
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3)
    c=COL[PART_OF.get(num,1)]
    return f'<header class="ch-open" id="{cid}"><div class="n" style="background:{c}">{num}</div><div><div class="k">Capítulo {num}</div><h2>{title}</h2></div></header>'
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m:chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)
ART={1:"celia",2:"antonio",3:"marta",4:"grupo",5:"coral"}
QUOTE={1:"A voz amadurece com a gente. E continua sendo nossa.",2:"Pequenos cuidados, todos os dias, fazem uma grande diferença.",3:"Nunca é tarde para descobrir a própria voz cantando.",4:"Cantar junto é encontrar gente, memória e alegria.",5:"Ensinar é acolher a pessoa inteira, com tudo o que ela já viveu."}
def popen(m):
    n=int(m.group(1)); inner=m.group(2)
    lab=re.search(r'<p class="part-label">(.*?)</p>',inner).group(1)
    tit=re.search(r'<h1 class="part-title">(.*?)</h1>',inner).group(1)
    sub=re.search(r'<p class="part-sub">(.*?)</p>',inner,re.S).group(1)
    return (f'<section class="part" id="parte-{n}">\n<div class="pg popen"><div class="band" style="background:{COL[n]}"></div><div class="txt"><div class="num" style="color:{COL[n]}">{n}</div><div class="lab">{lab}</div><h1>{tit}</h1><div class="sub">{sub}</div><div class="q">“{QUOTE[n]}”</div></div>'
            f'<div class="art"><img src="img/{ART[n]}.png"></div></div>')
body=re.sub(r'<section class="part" id="parte-(\d)">\s*<div class="part-opener">(.*?)</div>',popen,body,flags=re.S)
toc=[]
for m in re.finditer(r'<section class="part" id="parte-(\d)">.*?<div class="lab">(.*?)</div><h1>(.*?)</h1>(.*?)</section>',body,re.S):
    n,lab,tit,rest=m.groups()
    chs=[(c.group(1),c.group(2),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="n"[^>]*>(\d+)</div><div><div class="k">.*?</div><h2>(.*?)</h2>',rest)]
    toc.append((int(n),lab,tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>Uma carta para você</span><span class="p">{pg("carta")}</span></div>',f'<div class="fm"><span>Como usar este livro</span><span class="p">{pg("como-usar")}</span></div>']
    for n,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="dot" style="background:{COL[n]}"></span><span class="t">{lab} · {tit}</span><span class="p">{pg("parte-"+str(n))}</span></div>')
        for cid,num,t in chs: o.append(f'<div class="row"><span class="t">{num}. {t}</span><span class="p">{pg(cid)}</span></div>')
    for k,t in (("referencias","Referências"),("sobre-autora","Sobre a autora")):
        o.append(f'<div class="fm"><span>{t}</span><span class="p">{pg(k)}</span></div>')
    return "\n".join(o)
def fonts():
    c=""
    for w in (400,700):
        for st in ("normal","italic"): c+=f"@font-face{{font-family:Atkinson;font-weight:{w};font-style:{st};src:url(file://{F}atkinson-hyperlegible/files/atkinson-hyperlegible-latin-{w}-{st}.woff2)}}\n@font-face{{font-family:Atkinson;font-weight:{w};font-style:{st};src:url(file://{F}atkinson-hyperlegible/files/atkinson-hyperlegible-latin-ext-{w}-{st}.woff2);unicode-range:U+0100-024F}}\n"
    for w in (400,700):
        for st in ("normal","italic"): c+=f"@font-face{{font-family:Atkinson;font-weight:{w};font-style:{st};src:url(file:///tmp/work/fonts/node_modules/@fontsource/inter/files/inter-latin-{w}-{st}.woff2);unicode-range:U+0030-0039}}\n"
    for w in (500,600,700):
        c+=f"@font-face{{font-family:Lora;font-weight:{w};src:url(file://{F}lora/files/lora-latin-{w}-normal.woff2)}}\n"
    c+=f"@font-face{{font-family:Lora;font-weight:500;font-style:italic;src:url(file://{F}lora/files/lora-latin-500-italic.woff2)}}\n"
    return c
CARTA='''<section class="fsec" id="carta"><h1>Uma carta<br>para você</h1>
<div class="carta"><div class="ph"><img src="autora.jpg"></div><div>
<p>Eu sou a Brízia. Sou fonoaudióloga, especialista em voz, cantora e professora de canto. Ao longo da minha caminhada, aprendi que a voz acompanha a nossa história: ela carrega as nossas memórias, as nossas canções e o nosso jeito de estar no mundo.</p>
<p>Com o passar dos anos, a voz muda, como todo o corpo. Isso é natural. E a boa notícia é que dá para continuar cantando, aprendendo e cuidando dela com prazer, respeitando o seu tempo e o seu corpo.</p>
</div></div>
<p>Este livro foi escrito para quem tem 50, 60, 70 anos ou mais e quer aprender a cantar, voltar a cantar ou simplesmente usar a voz com mais conforto. E também para quem ensina esse público: professores de canto, regentes de corais, educadores e profissionais de saúde.</p>
<p>Ele não promete milagres nem substitui uma consulta. Ele convida você a conhecer a sua voz de hoje, a praticar com segurança e a descobrir a alegria de cantar, sozinho ou em grupo.</p>
<div class="sig">Com carinho, Brízia</div>
</section>'''
COMO='''<section class="fsec" id="como-usar"><h1>Como usar este livro</h1>
<p>As letras são grandes e os capítulos são curtos, para uma leitura sem pressa. Leia na ordem ou vá direto ao tema que mais interessa. Os exercícios podem ser feitos em casa, na aula ou no coral, e quase todos podem ser feitos sentado.</p>
<p>Ao longo do livro, você vai encontrar quadros com cores diferentes:</p>
<div class="legend">
<div class="lg praticar"><b>Para praticar</b>Exercícios explicados passo a passo. Todos têm áudio de apoio.</div>
<div class="lg atv"><b>Sua vez</b>Espaços para escrever e marcar no próprio livro.</div>
<div class="lg saiba"><b>Bom saber</b>Informações curtas e úteis para o dia a dia.</div>
<div class="lg cuidado"><b>Atenção</b>Alertas de segurança e de saúde.</div>
<div class="lg professor"><b>Para o professor</b>Orientações para quem conduz aulas e corais.</div>
<div class="lg ciencia"><b>Por trás da ciência</b>A explicação fonoaudiológica, com as fontes.</div>
</div>
<div class="aviso audios"><b>Áudios dos exercícios</b>Os áudios referidos neste livro estão disponíveis na plataforma onde o livro digital foi adquirido. Lá você encontra a referência de som, ritmo e afinação de cada exercício dos quadros “Para praticar”, para ouvir quantas vezes quiser.</div>
</section>
<section class="fsec" id="personagens"><h1>Quem caminha com você</h1>
<p>Três personagens vão aparecer nas páginas deste livro. Talvez você se reconheça em algum deles.</p>
<div class="turma"><div><img src="img/celia.png"><b>Dona Célia</b><span>68 anos. Canta no coral da comunidade há muitos anos e percebeu a voz mais fina e cansada.</span></div><div><img src="img/antonio.png"><b>Seu Antônio</b><span>72 anos. Sempre quis cantar e começou depois de se aposentar. Usa aparelho auditivo.</span></div><div><img src="img/marta.png"><b>Marta</b><span>55 anos. Professora, passou pela menopausa e notou a voz mais grave.</span></div></div>
<div class="aviso"><b>Um combinado importante</b>Este é um livro educativo. Os exercícios são para vozes saudáveis, como prática de canto e de bem-estar vocal. Ele não faz diagnóstico, não indica tratamento e não substitui a avaliação de um médico otorrinolaringologista e de um fonoaudiólogo. Se você tem alguma alteração na voz, na respiração, na audição ou na deglutição, procure esses profissionais antes de começar. Respeite sempre os seus limites: pare se sentir tontura, dor ou cansaço.</div>
</section>'''
REFS='''<section class="refs" id="referencias"><h1>Referências</h1>
<ul>
<li>ALVES, M.; KRÜGER, E.; PILLAY, B.; VAN LIERDE, K.; VAN DER LINDE, J. The effect of hydration on voice quality in adults: a systematic review. <em>Journal of Voice</em>, v. 33, n. 1, p. 125.e13–125.e28, 2019.</li>
<li>BEHLAU, M. (org.). <em>Voz: o livro do especialista</em>. Rio de Janeiro: Revinter, 2001. v. 1.</li>
<li>JOHNSON, J. K.; STEWART, A. L.; ACREE, M.; NÁPOLES, A. M.; FLATT, J. D.; MAX, W. B.; GREGORICH, S. E. A community choir intervention to promote well-being among diverse older adults: results from the Community of Voices trial. <em>The Journals of Gerontology: Series B</em>, v. 75, n. 3, p. 549–559, 2020.</li>
<li>STEMPLE, J. C.; LEE, L.; D’AMICO, B.; PICKUP, B. Efficacy of vocal function exercises as a method of improving voice production. <em>Journal of Voice</em>, v. 8, n. 3, p. 271–278, 1994.</li>
<li>TITZE, I. R. <em>Principles of voice production</em>. Englewood Cliffs: Prentice Hall, 1994.</li>
<li>TITZE, I. R. Voice training and therapy with a semi-occluded vocal tract: rationale and scientific underpinnings. <em>Journal of Speech, Language, and Hearing Research</em>, v. 49, n. 2, p. 448–459, 2006.</li>
<li>ZIEGLER, A.; VERDOLINI ABBOTT, K.; JOHNS, M.; KLEIN, A.; HAPNER, E. R. Preliminary data on two voice therapy interventions in the treatment of presbyphonia. <em>The Laryngoscope</em>, v. 124, n. 8, p. 1869–1876, 2014.</li>
</ul>
<p class="comp">Leitura complementar da autora: LACERDA, B. <em>Voz, Canto e Ciência</em>: saúde vocal, técnica vocal e inspiração.</p>
</section>'''
AUDIOS='''<div class="pg audiopg" id="audios"><div class="k">MATERIAL COMPLEMENTAR</div><h1>Áudios dos<br>exercícios</h1>
<p>Todos os exercícios dos quadros “Para praticar” têm áudio de apoio, com a referência de som, ritmo e afinação. Aponte a câmera do celular para o código abaixo ou digite o endereço no navegador. Se precisar, peça ajuda a alguém de confiança: os áudios ficam todos reunidos num só lugar.</p>
<div class="qr"><div class="bx">[QR CODE]</div><div class="url">[endereço do site]</div></div></div>'''
AUTORA='''<section class="fsec" id="sobre-autora"><h1>Sobre a autora</h1>
<div class="carta"><div class="ph"><img src="autora2.jpg"></div><div>
<p><strong>Dra. Brízia Lacerda</strong> é fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. É cantora, vocal coach, pesquisadora, escritora e palestrante.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos e cantores. É autora de <em>Voz, Canto e Ciência</em> e de <em>Minha voz cresce comigo</em>.</p>
<p>Mãe e esposa, acredita que a voz acompanha cada fase da vida, e que nunca é tarde para cantar.</p></div></div>
</section>'''
CRED='''<div class="cred" id="cred">
<p><strong>A Voz Não Tem Idade</strong><br>Guia de canto e cuidados com a voz a partir dos 50 anos, para aprender e para ensinar</p>
<p>Autora: Dra. Brízia Lacerda<br>Versão para impressão e revisão da autora · 2026</p>
<p>© 2026 Dra. Brízia Lacerda. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>Projeto gráfico, capa e ilustrações originais. Os personagens são fictícios.</p>
<p>Esta obra tem finalidade exclusivamente educativa. As informações aqui contidas não substituem a avaliação, o diagnóstico ou o tratamento realizados por médico otorrinolaringologista, fonoaudiólogo ou outros profissionais de saúde.</p></div>'''
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>A Voz Não Tem Idade</title><style>{fonts()}</style><link rel="stylesheet" href="senior.css"></head><body>
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
open("senior.html","w",encoding="utf-8").write(html)
print("ok",len(toc),sum(len(t[3]) for t in toc),sorted(used))
