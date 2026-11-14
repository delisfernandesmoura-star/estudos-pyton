import json,re
d=json.load(open("parts.json"))
b=d["body"]
# audio note: plain text
b=re.sub(r'<p class="audio">.*?<span>(.*?)</span></p>',r'<div class="audio">♪ \1</div>',b,flags=re.S)
b=b.replace("veja a página 136","veja a página “Áudios dos exercícios”, no final do livro")
# part openers
def popen(m):
    img=m.group(1); inner=m.group(2)
    lab=re.search(r'<div class="lab">(.*?)</div>',inner).group(1); tit=re.search(r'<h1>(.*?)</h1>',inner).group(1)
    sub=re.search(r"<div class=\"sub\">(.*?)(?:</div>|$)",inner,re.S).group(1); it=re.search(r"<div class=\"intro\">(.*?)(?:</div>|$)",inner,re.S)
    o=f'<h1 class="part-title"><span class="part-label">{lab}</span>{tit}</h1>\n<div class="part-sub">{sub}</div>\n'
    if it: o+=f'<div class="part-intro">{it.group(1)}</div>\n'
    o+=f'<div class="part-photo"><img src="assets/{img}" alt="Dra. Brízia Lacerda"/></div>\n'
    return o
b=re.sub(r'<div class="pg black popen"><div class="ph"><img src="assets/(.*?)" style="[^"]*"></div><div class="tx">(.*?)</div></div>',popen,b,flags=re.S)
# quote pages
b=re.sub(r'<div class="pg black quote photo"><div class="ph"><img src="assets/[^"]*"></div><div class="tx"><div class="q">(.*?)</div><div class="src">(.*?)</div></div></div>',r'<div class="quote-ep"><div class="q">\1</div><div class="src">\2</div></div>',b,flags=re.S)
b=re.sub(r'<div class="pg black quote"><div class="q[^"]*">(.*?)</div><div class="src">(.*?)</div></div>',r'<div class="quote-ep"><div class="q">\1</div><div class="src">\2</div></div>',b,flags=re.S)
# chapter headers back to h2
b=re.sub(r'<header class="ch-open" id="(cap-\d+)"><div class="ch-n">\d+</div><div class="ch-k">(.*?)</div><h2>(.*?)</h2></header>',r'<h2 class="chapter" id="\1"><span class="chapter-num">\2</span>\3</h2>',b)
b=re.sub(r'</?section[^>]*>','',b)
def p2div(t): return re.sub(r'<p class="([^"]+)">(.*?)</p>',r'<div class="\1">\2</div>',t,flags=re.S)
b=p2div(b)
sl=p2div(re.sub(r'</?section[^>]*>','',d["sobre_livro"])).replace('<div class="kick">Apresentação</div>','').replace('<div class="rule"></div>','').replace('<h1>','<h1 class="front">').replace("página 136","página “Áudios dos exercícios”, no final do livro")
sa=d["sobre_autora"]
sa_txt=re.search(r'<div class="rule"></div>(.*?)<div class="sig">',sa,re.S).group(1)
sa='<h1 class="front">Sobre a autora</h1>\n<div class="autora-photo"><img src="assets/bw-autora.jpg" alt="Dra. Brízia Lacerda"/></div>\n'+sa_txt
cred=re.sub(r'<div class="cred">','<div class="creditos">',d["creditos"])
cred=p2div(cred.replace('<div class="ph">','<div class="cip">'))
refs=p2div(re.sub(r'</?section[^>]*>','',d["refs"])).replace('<div class="kick">Fontes</div>','').replace('<div class="rule"></div>','').replace('<h1>Referências</h1>','<h1 class="front">Referências</h1>')
aud=d["audios"]
aud=('<h1 class="front">Áudios dos exercícios</h1>\n<p>Todos os exercícios deste livro têm áudio de apoio, gravado para que você pratique com a referência certa de som, ritmo e afinação. Aponte a câmera do celular para o QR code ou acesse o endereço abaixo para baixar o material completo.</p>\n<div class="qr-ep">[QR CODE]<br/>[endereço do site]</div>')
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Voz, Canto e Ciência</title></head><body>
<h1 class="front">Créditos</h1>{cred}
<div class="epigrafe"><div class="q">O cantor faz de si mesmo o seu instrumento.</div><div class="src">Capítulo 9 · Respiração e apoio</div></div>
{sl}
{sa}
{b}
{refs}
{aud}
</body></html>'''
open("epub2.html","w",encoding="utf-8").write(html); print("ok")
