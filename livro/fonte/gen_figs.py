import math
AZ="#142033"; BO="#430F1C"; GO="#C8AD80"; MA="#F7F3EA"; BL="#742235"
FONT="font-family:Inter,Helvetica,Arial,sans-serif"

def svg(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>text{{{FONT};fill:{AZ}}}</style>{body}</svg>'

# ---------- 1. registros ----------
def registros():
    w,h=680,230
    b=[]
    b.append(f'<text x="340" y="26" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="2" style="fill:{GO}">EXTENSÃO DA VOZ</text>')
    # axis
    b.append(f'<line x1="40" y1="60" x2="640" y2="60" stroke="{AZ}" stroke-width="1.5"/>')
    b.append(f'<polygon points="640,55 650,60 640,65" fill="{AZ}"/>')
    b.append(f'<text x="40" y="48" font-size="12">grave</text><text x="640" y="48" text-anchor="end" font-size="12">agudo</text>')
    bands=[("BASAL",40,190,AZ,"ranger de porta · relaxamento"),("MODAL",150,470,BO,"voz de peito · fala"),("ELEVADO",400,640,GO,"voz de cabeça")]
    y=80
    for name,x1,x2,c,desc in bands:
        tc = AZ if c==GO else MA
        b.append(f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="38" rx="19" fill="{c}"/>')
        b.append(f'<text x="{(x1+x2)/2}" y="{y+24}" text-anchor="middle" font-size="14" font-weight="700" letter-spacing="2" style="fill:{tc}">{name}</text>')
        b.append(f'<text x="{x1+6}" y="{y+56}" font-size="11.5" style="fill:{AZ}">{desc}</text>')
        y+=0
        y+=0
        # stagger vertically
        y+=0
    return svg(w,h,"".join(b))

def registros_stag():
    w,h=680,320
    b=[f'<text x="340" y="26" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="2" style="fill:{GO}">OS TRÊS REGISTROS</text>']
    b.append(f'<line x1="40" y1="282" x2="640" y2="282" stroke="{AZ}" stroke-width="1.5"/><polygon points="640,277 650,282 640,287" fill="{AZ}"/>')
    b.append(f'<text x="40" y="304" font-size="12">grave</text><text x="640" y="304" text-anchor="end" font-size="12">agudo</text>')
    rows=[("BASAL",40,200,AZ,MA,"semelhante ao ranger de uma porta · musculatura relaxada"),("MODAL",140,500,BO,MA,"voz de peito · a nossa voz natural, da fala"),("ELEVADO",420,640,GO,AZ,"voz de cabeça · laringe elevada")]
    y=50
    for n,x1,x2,c,tc,d in rows:
        b.append(f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="40" rx="20" fill="{c}"/>')
        b.append(f'<text x="{(x1+x2)/2}" y="{y+25}" text-anchor="middle" font-size="14" font-weight="700" letter-spacing="2" style="fill:{tc}">{n}</text>')
        tx = x1 if x1<300 else x2
        anc = "start" if x1<300 else "end"
        b.append(f'<text x="{tx}" y="{y+58}" text-anchor="{anc}" font-size="11.5">{d}</text>')
        y+=58+18
    return svg(w,h,"".join(b))

# ---------- 2. extensão das vozes ----------
def extensao():
    # notas na notação do material: DO1..; semitone index from DO1
    names=["DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SI"]
    def idx(n,o): return names.index(n)+12*(o-1)
    white=[0,2,4,5,7,9,11]
    octs=5; wkw=15.0; x0=30; ky=0
    W=x0*2+octs*7*wkw
    H=330
    b=[f'<text x="{W/2}" y="22" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="2" style="fill:{GO}">EXTENSÃO APROXIMADA DAS VOZES</text>']
    def xc(s):
        o,n=divmod(s,12)
        if n in white: return x0+(o*7+white.index(n))*wkw+wkw/2
        # black key: between neighbours
        return x0+(o*7+white.index(n-1))*wkw+wkw
    ranges=[("Soprano",idx("DO",3),idx("FA",5),BO),("Mezzo",idx("LA",2),idx("SI",4),BL),("Contralto",idx("MI",2),idx("LA",4),"#8a5a66"),
            ("Tenor",idx("DO",2),idx("RE",4),AZ),("Barítono",idx("SOL",1),idx("LA",3),"#2d4268"),("Baixo",idx("DO",1),idx("FA",3),"#4a6290")]
    y=44
    for name,a,z,c in ranges:
        xa,xz=xc(a)-wkw/2,xc(z)+wkw/2
        b.append(f'<rect x="{xa}" y="{y}" width="{xz-xa}" height="26" rx="13" fill="{c}"/>')
        b.append(f'<text x="{(xa+xz)/2}" y="{y+17.5}" text-anchor="middle" font-size="12" font-weight="600" style="fill:{MA}">{name}</text>')
        y+=34
    ky=y+6
    # keyboard
    for o in range(octs):
        for i in range(7):
            x=x0+(o*7+i)*wkw
            b.append(f'<rect x="{x}" y="{ky}" width="{wkw}" height="74" fill="#fff" stroke="{AZ}" stroke-width="0.8"/>')
    for o in range(octs):
        for i in (0,1,3,4,5):
            x=x0+(o*7+i)*wkw+wkw*0.68
            b.append(f'<rect x="{x}" y="{ky}" width="{wkw*0.64}" height="46" fill="{AZ}" rx="1.5"/>')
    for o in range(octs):
        x=x0+o*7*wkw
        b.append(f'<text x="{x+wkw/2}" y="{ky+90}" text-anchor="middle" font-size="10.5" font-weight="600">DO{o+1}</text>')
        b.append(f'<line x1="{x+wkw/2}" y1="{ky+74}" x2="{x+wkw/2}" y2="{ky+78}" stroke="{AZ}"/>')
    return svg(W,ky+100,"".join(b))

# ---------- 3. ciclo glótico ----------
def fold_panel(cx,cy,post,mid,ant,label,num):
    # lumen background circle
    out=[f'<circle cx="{cx}" cy="{cy}" r="78" fill="{AZ}"/>']
    top=-62; bot=60
    def side(sgn):
        # outer edge
        p=f'M {cx+sgn*0.6},{cy+top} C {cx+sgn*34},{cy-52} {cx+sgn*56},{cy-14} {cx+sgn*52},{cy+16} C {cx+sgn*49},{cy+42} {cx+sgn*30},{cy+62} {cx+sgn*max(post,6)+sgn*10},{cy+bot+4} '
        p+=f'L {cx+sgn*post},{cy+bot} Q {cx+sgn*mid},{cy-2} {cx+sgn*ant},{cy+top} Z'
        return p
    for s in (-1,1):
        out.append(f'<path d="{side(s)}" fill="#E9D8C9" stroke="{GO}" stroke-width="1.2"/>')
    out.append(f'<text x="{cx}" y="{cy+112}" text-anchor="middle" font-size="13" font-weight="700" style="fill:{BO}">{num}</text>')
    out.append(f'<text x="{cx}" y="{cy+130}" text-anchor="middle" font-size="12.5">{label}</text>')
    return "".join(out)

def ciclo():
    w,h=700,300
    b=[f'<text x="350" y="24" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="2" style="fill:{GO}">O CICLO GLÓTICO</text>']
    b.append(f'<text x="350" y="42" text-anchor="middle" font-size="11" style="fill:{AZ}">vista superior · frente da laringe para cima</text>')
    panels=[(90,0,2,0.6,"Fase fechada","1"),(260,14,5,1.4,"Fase de abertura","2"),(430,30,16,4,"Fase aberta","3"),(600,12,3,0.9,"Fase de fechamento","4")]
    # avoid overlaps by scaling: panels width 156 each (r=78) -> spacing 170 ok
    for cx,post,mid,ant,lab,num in panels:
        b.append(fold_panel(cx,128,post,mid,ant,lab,num))
    # arrows between
    for x in (172,342,512):
        b.append(f'<path d="M {x},128 l 12,0 m -5,-5 l 5,5 l -5,5" stroke="{GO}" stroke-width="2" fill="none"/>')
    return svg(w,h,"".join(b))

# ---------- 4. laringe ----------
def laringe():
    w,h=660,360
    cx=250
    def hw(y):
        # half width of the lumen at height y
        pts=[(30,60),(90,58),(120,50),(132,34),(140,30),(150,36),(165,20),(172,12),(180,14),(200,32),(240,40),(300,38),(340,32)]
        for (y1,a),(y2,b2) in zip(pts,pts[1:]):
            if y1<=y<=y2: return a+(b2-a)*(y-y1)/(y2-y1)
        return pts[-1][1]
    L=[(cx-hw(y),y) for y in range(30,341,5)]
    R=[(cx+hw(y),y) for y in range(340,29,-5)]
    lumen="M "+" L ".join(f"{x:.1f},{y}" for x,y in L+R)+" Z"
    body=[]
    # tissue block
    body.append(f'<rect x="{cx-120}" y="20" width="240" height="330" rx="22" fill="#EADFCB" stroke="{GO}" stroke-width="1.5"/>')
    body.append(f'<path d="{lumen}" fill="{AZ}"/>')
    # epiglottis
    body.append(f'<path d="M {cx-52},{44} C {cx-62},{70} {cx-60},{104} {cx-56},{128}" stroke="{BO}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    # thyroid cartilage hint (anterior = left)
    body.append(f'<path d="M {cx-120},96 C {cx-134},150 {cx-132},210 {cx-118},250" stroke="{BO}" stroke-width="9" fill="none" stroke-linecap="round" opacity="0.55"/>')
    # cricoid
    body.append(f'<ellipse cx="{cx-98}" cy="270" rx="18" ry="30" fill="none" stroke="{BO}" stroke-width="7" opacity="0.55"/>')
    for sgn in (-1,1):
        for yy,wd in ((136,16),(168,14)):
            x0=cx+sgn*hw(yy)
            body.append(f'<polygon points="{x0},{yy-7} {x0-sgn*wd},{yy} {x0},{yy+7}" fill="{GO}"/>')
    # zone brackets right
    zones=[("SUPRAGLOTE",36,150,"acima das pregas vocais"),("GLOTE",150,182,"espaço entre as pregas vocais"),("INFRAGLOTE",182,334,"abaixo das pregas vocais")]
    for name,y1,y2,d in zones:
        bx=cx+140
        body.append(f'<path d="M {bx},{y1} L {bx+10},{y1} L {bx+10},{y2} L {bx},{y2}" stroke="{GO}" stroke-width="2" fill="none"/>')
        ym=(y1+y2)/2
        body.append(f'<text x="{bx+20}" y="{ym}" font-size="13" font-weight="700" letter-spacing="1.5" style="fill:{BO}">{name}</text>')
        body.append(f'<text x="{bx+20}" y="{ym+16}" font-size="11">{d}</text>')
    # left labels
    body.append(f'<text x="{cx-136}" y="120" text-anchor="end" font-size="11">cartilagem</text><text x="{cx-136}" y="134" text-anchor="end" font-size="11">tireoide</text>')
    body.append(f'<text x="{cx-62}" y="30" text-anchor="end" font-size="11">epiglote</text>')
    body.append(f'<text x="{cx-120}" y="318" text-anchor="end" font-size="11">cricoide</text>')
    body.append(f'<text x="{cx}" y="{h-6}" text-anchor="middle" font-size="11" style="fill:{AZ}">corte lateral esquemático · frente à esquerda</text>')
    return svg(w,h,"".join(body))

# ---------- 5. respiração ----------
def torso(cx,cy,mode,label,num):
    o=[]
    # silhouette
    o.append(f'<circle cx="{cx}" cy="{cy-96}" r="20" fill="none" stroke="{AZ}" stroke-width="2"/>')
    o.append(f'<path d="M {cx-8},{cy-76} L {cx-8},{cy-64} M {cx+8},{cy-76} L {cx+8},{cy-64}" stroke="{AZ}" stroke-width="2"/>')
    shoulder_y = cy-64 - (10 if mode==1 else 0)
    o.append(f'<path d="M {cx-8},{cy-64} C {cx-36},{cy-62} {cx-52},{shoulder_y} {cx-54},{shoulder_y+14} L {cx-48},{cy+10} C {cx-48},{cy+44} {cx-44},{cy+76} {cx-40},{cy+96} L {cx+40},{cy+96} C {cx+44},{cy+76} {cx+48},{cy+44} {cx+48},{cy+10} L {cx+54},{shoulder_y+14} C {cx+52},{shoulder_y} {cx+36},{cy-62} {cx+8},{cy-64}" fill="none" stroke="{AZ}" stroke-width="2"/>')
    # highlight zones
    hl={1:(cx,cy-40,30,16,GO),2:(cx,cy-12,38,18,GO),3:(cx,cy+52,32,22,GO),4:(cx,cy+10,44,50,GO)}
    x,y,rx,ry,c=hl[mode]
    o.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" opacity="0.75"/>')
    if mode==1:
        o.append(f'<path d="M {cx-60},{cy-70} l 0,-14 m -5,6 l 5,-6 l 5,6 M {cx+60},{cy-70} l 0,-14 m -5,6 l 5,-6 l 5,6" stroke="{BO}" stroke-width="2" fill="none"/>')
    if mode==4:
        o.append(f'<path d="M {cx-52},{cy+8} l -14,0 m 6,-5 l -6,5 l 6,5 M {cx+52},{cy+8} l 14,0 m -6,-5 l 6,5 l -6,5" stroke="{BO}" stroke-width="2" fill="none"/>')
        o.append(f'<path d="M {cx},{cy+78} l 0,10 m -5,-5 l 5,5 l 5,-5" stroke="{BO}" stroke-width="2" fill="none"/>')
    if mode==3:
        o.append(f'<path d="M {cx},{cy+78} l 0,14 m -5,-6 l 5,6 l 5,-6" stroke="{BO}" stroke-width="2" fill="none"/>')
    o.append(f'<text x="{cx}" y="{cy+122}" text-anchor="middle" font-size="13" font-weight="700" style="fill:{BO}">{num}</text>')
    o.append(f'<text x="{cx}" y="{cy+140}" text-anchor="middle" font-size="12.5">{label}</text>')
    return "".join(o)

def respiracao():
    w,h=700,330
    b=[f'<text x="350" y="24" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="2" style="fill:{GO}">OS QUATRO TIPOS DE RESPIRAÇÃO</text>']
    labels=[(1,"Clavicular"),(2,"Torácica"),(3,"Abdominal"),(4,"Completa")]
    for i,(m,l) in enumerate(labels):
        b.append(torso(95+i*170,150,m,l,str(m)))
    return svg(w,h,"".join(b))

figs={"fig-registros":registros_stag(),"fig-extensao-vozes":extensao(),"fig-ciclo-glotico":ciclo(),"fig-laringe":laringe(),"fig-respiracao":respiracao()}
for n,s in figs.items():
    open(f"img/{n}.svg","w",encoding="utf-8").write(s)
print("svgs ok")
