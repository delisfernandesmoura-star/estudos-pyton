import re, json, os
F="/tmp/work/fonts/node_modules/@fontsource/"
pages=json.load(open("pages.json")) if os.path.exists("pages.json") else {}
def pg(k): return str(pages.get(k,"")) if pages.get(k) else ""
AUD=str(pages.get("audios","")) or "final"
body="\n".join(open(f,encoding="utf-8").read() for f in ("part1.html","part2.html","part3.html"))
# figures: once each except characters
used=set()
def figrep(m):
    name=m.group(1); cap=m.group(2)
    if name in used and name not in ("lia","theo","bia","turma"): return ""
    used.add(name)
    cls="fig char" if name in ("lia","theo","bia") else "fig"
    return f'<figure class="{cls}"><img src="img/{name}.png" alt=""><figcaption>{cap}</figcaption></figure>'
body=re.sub(r'<figure class="fig" data-fig="([\w-]+)">\s*<figcaption>(.*?)</figcaption>\s*</figure>',figrep,body,flags=re.S)
body=re.sub(r'(?<![>\w])\(((?:[A-ZÀ-Ý][A-ZÀ-Ý .;&\'\-]*)(?: et al\.| ET AL\.)?, \d{4})\)', r'<span class="cit">(\1)</span>', body)
# interactive bits
body=re.sub(r'<div class="linhas" data-n="(\d+)"></div>',lambda m:'<div class="linhas">'+'<div></div>'*int(m.group(1))+'</div>',body)
body=re.sub(r'<div class="desenho" data-h="(\d+)">',lambda m:f'<div class="desenho" style="height:{m.group(1)}mm">',body)
# audio notes in brincar boxes
ICON='<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#a87a1e" stroke-width="2.2" stroke-linecap="round"><path d="M3 15v-3a9 9 0 0 1 18 0v3"/><rect x="2.5" y="14.5" width="4.6" height="7" rx="1.6"/><rect x="16.9" y="14.5" width="4.6" height="7" rx="1.6"/></svg>'
AUDIO=f'<p class="audio">{ICON}<span>Tem áudio deste exercício! Veja a página {AUD}.</span></p>'
body=re.sub(r'(<div class="box brincar">.*?)(</div>)',lambda m:m.group(1)+AUDIO+m.group(2),body,flags=re.S)
COL={1:"#E8907A",2:"#8FB59A",3:"#E6B450",4:"#B3A3D6",5:"#C29A55"}
PART_OF={}
def chap(m):
    cid,num,title=m.group(1),int(m.group(2)),m.group(3)
    c=COL[PART_OF.get(num,1)]
    return f'<header class="ch-open" id="{cid}"><div class="n" style="background:{c}">{num}</div><div><div class="k">Capítulo {num}</div><h2>{title}</h2></div></header>'
# map chapters to parts
for sm in re.finditer(r'<section class="part" id="parte-(\d)">(.*?)</section>',body,re.S):
    for cm in re.finditer(r'id="cap-(\d+)"',sm.group(2)): PART_OF[int(cm.group(1))]=int(sm.group(1))
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>\s*<p>',lambda m:chap(m)+'\n<p class="lead">',body)
body=re.sub(r'<h2 class="chapter" id="(cap-\d+)"><span class="chapter-num">Capítulo (\d+)</span>(.*?)</h2>',chap,body)
ART={1:"lia",2:"agua",3:"turma",4:"theo",5:"bia"}
def popen(m):
    n=int(m.group(1)); inner=m.group(2)
    lab=re.search(r'<p class="part-label">(.*?)</p>',inner).group(1)
    tit=re.search(r'<h1 class="part-title">(.*?)</h1>',inner).group(1)
    sub=re.search(r'<p class="part-sub">(.*?)</p>',inner,re.S).group(1)
    w="120mm" if ART[n] in ("turma",) else "92mm"
    return (f'<section class="part" id="parte-{n}">\n<div class="pg popen" style="background:{COL[n]}"><div><div class="num">{n}</div><div class="lab">{lab}</div><h1>{tit}</h1><div class="sub">{sub}</div></div>'
            f'<div class="art" style="width:{w}"><img src="img/{ART[n]}.png"></div></div>')
body=re.sub(r'<section class="part" id="parte-(\d)">\s*<div class="part-opener">(.*?)</div>',popen,body,flags=re.S)
toc=[]
for m in re.finditer(r'<section class="part" id="parte-(\d)">.*?<div class="lab">(.*?)</div><h1>(.*?)</h1>(.*?)</section>',body,re.S):
    n,lab,tit,rest=m.groups()
    chs=[(c.group(1),c.group(2),re.sub(r"<[^>]+>","",c.group(3))) for c in re.finditer(r'<header class="ch-open" id="(cap-\d+)"><div class="n"[^>]*>(\d+)</div><div><div class="k">.*?</div><h2>(.*?)</h2>',rest)]
    toc.append((int(n),lab,tit,chs))
json.dump({"toc":toc},open("toc.json","w"),ensure_ascii=False)
def toc_html():
    o=[f'<div class="fm"><span>Olá! Uma carta para você</span><span class="p">{pg("carta")}</span></div>',f'<div class="fm"><span>Como usar este livro</span><span class="p">{pg("como-usar")}</span></div>']
    for n,lab,tit,chs in toc:
        o.append(f'<div class="part"><span class="dot" style="background:{COL[n]}"></span><span class="t">{lab} · {tit}</span><span class="p">{pg("parte-"+str(n))}</span></div>')
        for cid,num,t in chs: o.append(f'<div class="row"><span class="t">{num}. {t}</span><span class="p">{pg(cid)}</span></div>')
    o.append(f'<div class="fm" style="margin-top:5mm"><span>Referências</span><span class="p">{pg("referencias")}</span></div>')
    o.append(f'<div class="fm"><span>Áudios dos exercícios</span><span class="p">{pg("audios")}</span></div>')
    o.append(f'<div class="fm"><span>Sobre a autora</span><span class="p">{pg("sobre-autora")}</span></div>')
    return "\n".join(o)
def fonts():
    c=""
    for w in (400,500,600,700): c+=f"@font-face{{font-family:Fredoka;font-weight:{w};src:url(file://{F}fredoka/files/fredoka-latin-{w}-normal.woff2)}}\n"
    for w in (400,600,700,800):
        for st in ("normal","italic"): c+=f"@font-face{{font-family:Nunito;font-weight:{w};font-style:{st};src:url(file://{F}nunito/files/nunito-latin-{w}-{st}.woff2)}}\n"
    return c
CARTA=f'''<section class="fsec" id="carta"><h1>Olá! Que bom<br>ter você aqui.</h1>
<div class="carta"><div class="ph"><img src="autora.jpg"></div><div>
<p>Eu sou a Brízia. Sou fonoaudióloga, especialista em voz, cantora e professora de canto. Passo os meus dias ajudando pessoas de todas as idades a usar a voz com alegria e saúde.</p>
<p>A sua voz é um instrumento que mora dentro de você, que cresce junto com você e que é só seu: não existe outra igual no mundo. Neste livro, vamos descobrir onde ela mora, como ela funciona e como cuidar dela para cantar, falar e brincar a vida inteira.</p>
<p>Você vai encontrar brincadeiras, exercícios, desafios e espaços para escrever e desenhar. Faça junto com seu professor, com a sua família ou com seus amigos. E lembre: cantar nunca deve doer.</p>
<div class="sig">Com carinho, Brízia</div></div></div>
</section>'''
COMO='''<section class="fsec" id="como-usar"><h1>Como usar este livro</h1>
<p>Este livro foi feito para ser usado a quatro mãos: <strong>a criança ou o adolescente</strong> lê, brinca e faz os exercícios; <strong>o professor, o regente, o fonoaudiólogo ou a família</strong> encontra, nos quadros especiais, a explicação técnica e as orientações para conduzir cada atividade com segurança.</p>
<p>Ele une duas visões que se completam: a do <strong>canto</strong>, que ensina a usar a voz com arte e técnica, e a da <strong>fonoaudiologia</strong>, que garante que ela cresça saudável, especialmente durante a muda vocal.</p>
<div class="legend">
<div style="background:#FBE7C2"><b>Vamos brincar</b>Exercícios e brincadeiras para fazer. Muitos têm áudio de apoio.</div>
<div style="background:#fff;border:2px dashed #E8907A"><b>Sua vez!</b>Espaços para escrever, marcar e desenhar no próprio livro.</div>
<div style="background:#E1EDE3"><b>Você sabia?</b>Curiosidades sobre a voz.</div>
<div style="background:#FADCD3"><b>Cuidado!</b>Alertas importantes de saúde vocal.</div>
<div style="background:#fff;border:2px solid #C29A55"><b>Para o professor</b>Orientações didáticas para quem conduz a aula.</div>
<div style="background:#ECE6F5"><b>Por trás da ciência</b>A base fonoaudiológica e científica, para adultos.</div>
</div>
<h3>Conheça a turma</h3>
<div class="turma"><div><img src="img/lia.png"><b>Lia</b><span>8 anos · adora cantar no coral da escola</span></div><div><img src="img/theo.png"><b>Theo</b><span>12 anos · a voz dele está começando a mudar</span></div><div><img src="img/bia.png"><b>Bia</b><span>15 anos · canta numa banda e quer cuidar da voz</span></div></div>
</section>'''
REFS='''<section class="refs" id="referencias"><h1>Referências</h1>
<ul>
<li>ALVES, M.; KRÜGER, E.; PILLAY, B.; VAN LIERDE, K.; VAN DER LINDE, J. The effect of hydration on voice quality in adults: a systematic review. <em>Journal of Voice</em>, v. 33, n. 1, p. 125.e13–125.e28, 2019.</li>
<li>BEHLAU, M. (org.). <em>Voz: o livro do especialista</em>. Rio de Janeiro: Revinter, 2001. v. 1.</li>
<li>COOKSEY, J. M. <em>Working with adolescent voices</em>. St. Louis: Concordia, 2000.</li>
<li>GACKLE, L. <em>Finding Ophelia’s voice, opening Ophelia’s heart</em>: nurturing the adolescent female voice. Dayton: Heritage Music Press, 2011.</li>
<li>PHILLIPS, K. H. <em>Teaching kids to sing</em>. 2. ed. Boston: Schirmer, 2014.</li>
<li>TITZE, I. R. <em>Principles of voice production</em>. Englewood Cliffs: Prentice Hall, 1994.</li>
<li>TITZE, I. R. Voice training and therapy with a semi-occluded vocal tract: rationale and scientific underpinnings. <em>Journal of Speech, Language, and Hearing Research</em>, v. 49, n. 2, p. 448–459, 2006.</li>
</ul>
<p style="font-size:10pt;color:#7a7068">Leitura complementar da autora: LACERDA, B. <em>Voz, Canto e Ciência</em>: saúde vocal, técnica vocal e inspiração.</p>
</section>'''
AUDIOS='''<div class="pg audiopg" id="audios"><div class="k">MATERIAL COMPLEMENTAR</div><h1>Áudios dos<br>exercícios</h1>
<p>Todas as brincadeiras e exercícios marcados com o fone de ouvido têm áudio de apoio, para você praticar com a referência certa de som, ritmo e afinação. Peça a um adulto para apontar a câmera do celular para o QR code ou acessar o endereço abaixo.</p>
<div class="qr"><div class="bx">[QR CODE]</div><div class="url">[endereço do site]</div></div></div>'''
AUTORA='''<section class="fsec" id="sobre-autora"><h1>Sobre a autora</h1>
<div class="carta"><div class="ph"><img src="autora2.jpg"></div><div>
<p><strong>Dra. Brízia Lacerda</strong> é fonoaudióloga formada pela PUC Minas, pós-graduada e especialista em voz. É cantora, vocal coach, pesquisadora, escritora e palestrante.</p>
<p>À frente da Faculdade da Voz, reúne ciência vocal, canto, ensino e mentoria para professores de canto, fonoaudiólogos e cantores. É autora de <em>Voz, Canto e Ciência</em>.</p>
<p>Mãe e esposa, acredita que cuidar da voz desde a infância é cuidar da forma como cada pessoa vai se expressar no mundo.</p></div></div>
</section>'''
CRED='''<div class="toc" style="padding-top:150mm;font-size:9.6pt;color:#5d554c" id="cred">
<p><strong>Minha voz cresce comigo</strong><br>Técnica vocal e cuidados com a voz para crianças e adolescentes</p>
<p>Autora: Dra. Brízia Lacerda<br>Versão para impressão e revisão da autora · 2026</p>
<p>© 2026 Dra. Brízia Lacerda. Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida ou transmitida, por qualquer meio, sem autorização prévia e por escrito da autora, conforme a Lei nº 9.610/1998.</p>
<p>Projeto gráfico, capa e ilustrações originais.</p>
<p>Este livro tem finalidade educativa e não substitui a avaliação de um fonoaudiólogo ou de um médico otorrinolaringologista.</p></div>'''
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Minha voz cresce comigo</title><style>{fonts()}</style><link rel="stylesheet" href="kids.css"></head><body>
<div class="pg"><img class="fill" src="cover.png"></div>
{CRED}
<section class="toc" id="sumario"><h1>Sumário</h1>{toc_html()}</section>
{CARTA}
{COMO}
{body}
{REFS}
{AUDIOS}
{AUTORA}
<div class="pg"><img class="fill" src="back.png"></div>
</body></html>'''
open("kids.html","w",encoding="utf-8").write(html)
print("ok",len(toc),sum(len(t[3]) for t in toc))
