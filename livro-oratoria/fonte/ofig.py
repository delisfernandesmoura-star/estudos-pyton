import sys,math
sys.path.insert(0,"/tmp/work/book2")
from gen2 import svg,title,label,arrow,INK,GOLD,GL,GM,GRAY,CREAM,SOFT
def recursos():
    b=[title(320,24,"Os recursos vocais")]
    items=[("Intensidade","volume e projeção","força, presença"),("Altura","grave e agudo","autoridade, emoção"),("Velocidade","ritmo da fala","energia ou calma"),("Pausa","o silêncio que organiza","reflexão, impacto"),("Ênfase","a palavra que importa","foco, sentido"),("Entonação","a melodia da frase","intenção, emoção")]
    for i,(a,c,e) in enumerate(items):
        x=20+(i%3)*206; y=46+(i//3)*124
        b.append(f'<rect x="{x}" y="{y}" width="190" height="108" fill="#fff" stroke="{GOLD}" stroke-width="1"/>')
        b.append(f'<text x="{x+16}" y="{y+30}" style="font-family:Bodoni;font-size:20px;fill:{INK}">{a}</text>')
        b.append(label(x+16,y+52,c,"start","s"))
        b.append(f'<path d="M{x+16} {y+68} H{x+174}" stroke="{GL}"/>'+label(x+16,y+90,"efeito: "+e,"start","l"))
    # wave
    d="M20 330 "+" ".join(f"Q{30+i*40} {330-(18 if i%2==0 else -18)*(1+0.6*math.sin(i))} {40+i*40} 330" for i in range(15))
    b.append(f'<path d="{d}" stroke="{GOLD}" stroke-width="1.6" fill="none"/>')
    b.append(label(320,368,"Variar os recursos com intenção é o que dá música e sentido à fala.","middle","s"))
    return svg(640,380,"".join(b))
def estrutura():
    b=[title(320,24,"A estrutura da fala")]
    cols=[("Abertura","conexão e promessa","história, pergunta ou dado"),("Desenvolvimento","a ideia, passo a passo","pontos, exemplos, provas"),("Fechamento","síntese e chamada","o que levar e o que fazer")]
    for i,(a,c,d) in enumerate(cols):
        x=20+i*210; w=190
        b.append(f'<rect x="{x}" y="50" width="{w}" height="170" fill="{"#fff" if i!=1 else GL}" stroke="{GOLD}"/>')
        b.append(f'<text x="{x+w/2}" y="90" text-anchor="middle" style="font-family:Bodoni;font-size:22px;fill:{INK}">{a}</text>')
        b.append(label(x+w/2,120,c,"middle","l")+label(x+w/2,146,d,"middle","s"))
        b.append(f'<text x="{x+w/2}" y="196" text-anchor="middle" style="font-family:Bodoni;font-size:28px;fill:{GOLD}">{["I","II","III"][i]}</text>')
        if i<2: b.append(arrow(x+w+2,135,x+w+18,135))
    b.append(f'<path d="M20 252 H620" stroke="{GOLD}"/>')
    b.append(label(320,280,"Uma ideia central atravessa as três partes.","middle","l"))
    return svg(640,296,"".join(b))
def microfone():
    b=[title(320,24,"Distância e ângulo do microfone")]
    def face(x,y):
        return f'<path d="M{x} {y-60} C{x+40} {y-60},{x+52} {y-20},{x+50} {y+10} L{x+58} {y+22} L{x+48} {y+26} C{x+50} {y+44},{x+40} {y+58},{x+20} {y+60} L{x} {y+90}" stroke="{INK}" stroke-width="1.6" fill="none"/>'
    def mic(x,y,ang,l=60):
        return f'<g transform="translate({x},{y}) rotate({ang})"><rect x="0" y="-9" width="{l}" height="18" rx="4" fill="{INK}"/><ellipse cx="-4" cy="0" rx="12" ry="14" fill="{GRAY}" stroke="{INK}"/></g>'
    b.append(face(60,130)+mic(140,155,15)+f'<path d="M110 160 L128 158" stroke="{GOLD}" stroke-dasharray="3 3"/>'+label(110,250,"De mão: 3 a 5 cm,","middle","l")+label(110,268,"levemente abaixo da boca","middle","s"))
    b.append(face(280,130)+f'<path d="M330 156 C352 160,366 150,372 140" stroke="{INK}" stroke-width="2.4" fill="none"/><circle cx="332" cy="156" r="5" fill="{INK}"/>'+label(330,250,"Headset: ao lado da boca,","middle","l")+label(330,268,"fora do fluxo de ar","middle","s"))
    b.append(face(500,130)+f'<rect x="515" y="208" width="10" height="16" rx="3" fill="{INK}"/>'+label(540,250,"Lapela: no centro do peito,","middle","l")+label(540,268,"um palmo abaixo do queixo","middle","s"))
    b.append(label(320,306,"Fale sempre na mesma direção do microfone e deixe o som fazer o esforço por você.","middle","s"))
    return svg(640,320,"".join(b))
def plano():
    b=[title(320,24,"Plano de 8 semanas")]
    ph=[("1–2","Instrumento","higiene, respiração"),("3–4","Preparação","aquecimento, articulação"),("5–6","Expressão","recursos vocais, presença"),("7–8","Palco","mensagem, ensaio, apresentação")]
    b.append(f'<path d="M70 100 H570" stroke="{GOLD}" stroke-width="1.4"/>')
    for i,(s,a,d) in enumerate(ph):
        x=95+i*150
        b.append(f'<circle cx="{x}" cy="100" r="30" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.4"/><text x="{x}" y="108" text-anchor="middle" style="font-family:Bodoni;font-size:20px;fill:{INK}">{s}</text>')
        b.append(label(x,62,"semanas","middle","s")+f'<text x="{x}" y="164" text-anchor="middle" style="font-family:Bodoni;font-size:19px;fill:{INK}">{a}</text>')
        w=d.split(", "); b.append(label(x,188,w[0],"middle","s")+label(x,206,w[1] if len(w)>1 else "","middle","s"))
    b.append(label(320,244,"A cada semana, a voz é cuidada antes de ser exigida.","middle","l"))
    return svg(640,260,"".join(b))
for n,f in {"f-recursos":recursos,"f-estrutura":estrutura,"f-microfone":microfone,"f-plano":plano}.items():
    open(f"img/{n}.svg","w").write(f())
print("ok")
