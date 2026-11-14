import math
INK="#1F1F1F"; GOLD="#B8975A"; GL="#EADFC8"; GM="#D6C29A"; GRAY="#CFCAC2"; CREAM="#EFE8DC"; SOFT="#6b655c"
FONT="font-family:Inter,Helvetica,Arial,sans-serif"
def svg(w,h,body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>text{{{FONT};fill:{INK}}} .t{{font-size:12px;font-weight:600;letter-spacing:2.4px;fill:{GOLD}}} .l{{font-size:13px}} .s{{font-size:11.5px;fill:{SOFT}}}</style>{body}</svg>'
def title(x,y,t,anchor="middle"): return f'<text class="t" x="{x}" y="{y}" text-anchor="{anchor}">{t.upper()}</text>'
def label(x,y,t,anchor="start",cls="l"): return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{t}</text>'
def leader(x1,y1,x2,y2): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{GOLD}" stroke-width="1"/><circle cx="{x1}" cy="{y1}" r="2.6" fill="{GOLD}"/>'
def arrow(x1,y1,x2,y2,c=GOLD,w=1.6):
    a=math.atan2(y2-y1,x2-x1); L=8
    p1=(x2-L*math.cos(a-0.45),y2-L*math.sin(a-0.45)); p2=(x2-L*math.cos(a+0.45),y2-L*math.sin(a+0.45))
    return f'<path d="M{x1},{y1} L{x2},{y2} M{p1[0]:.1f},{p1[1]:.1f} L{x2},{y2} L{p2[0]:.1f},{p2[1]:.1f}" stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'

HEAD="M 150 505 C 150 450, 140 410, 120 385 C 85 345, 78 270, 95 215 C 115 140, 185 100, 255 102 C 300 104, 322 140, 322 178 C 322 192, 318 200, 322 210 C 334 228, 352 244, 360 258 C 362 264, 352 270, 338 270 C 340 278, 344 286, 338 292 C 333 296, 334 300, 338 304 C 342 312, 336 320, 330 324 C 334 336, 334 350, 320 358 C 300 368, 280 368, 268 372 C 264 400, 272 420, 268 440 C 265 465, 262 485, 262 505"

def head_internals(hl_mask=False, hl_ae=False):
    o=[]
    # nasal cavity
    o.append(f'<path d="M 228 206 C 258 190, 306 194, 320 214 C 328 230, 300 240, 262 238 C 240 236, 226 224, 228 206 Z" fill="{GL}" stroke="{GOLD}" stroke-width="1.2"/>')
    # hard palate + velum
    o.append(f'<path d="M 318 246 L 238 243 C 226 246, 218 256, 214 270" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/>')
    # tongue
    o.append(f'<path d="M 226 336 C 222 292, 250 264, 290 263 C 312 263, 326 276, 326 290 C 312 296, 298 302, 288 314 C 272 332, 250 340, 226 336 Z" fill="{GM}" stroke="{INK}" stroke-width="1.4"/>')
    # pharynx walls
    o.append(f'<path d="M 206 212 C 196 260, 196 330, 210 410" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/>')
    # epiglottis
    o.append(f'<path d="M 240 352 C 232 360, 228 372, 232 384" stroke="{INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    # larynx & folds
    o.append(f'<path d="M 212 410 L 212 452 M 250 392 C 258 410, 258 440, 250 456" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M 213 428 L 229 432 L 213 436 Z M 249 428 L 233 432 L 249 436 Z" fill="{GOLD}"/>')
    if hl_mask:
        o.append(f'<ellipse cx="300" cy="226" rx="70" ry="44" fill="{GOLD}" opacity=".22"/><ellipse cx="300" cy="226" rx="44" ry="26" fill="{GOLD}" opacity=".28"/>')
    if hl_ae:
        o.append(f'<circle cx="236" cy="392" r="16" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 3"/>')
    return "".join(o)

def aparelho():
    w,h=680,930
    b=[title(340,30,"O aparelho fonador")]
    b.append(f'<g transform="translate(40,10)">')
    b.append(head_internals())
    b.append(f'<path d="{HEAD}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>')
    # torso
    b.append(f'<path d="M150 505 C 120 540, 70 560, 62 620 L 60 890 M 262 505 C 300 540, 344 560, 350 620 L 352 890" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>')
    # trachea
    b.append(f'<path d="M 214 456 C 212 520, 204 580, 204 630 M 248 456 C 246 520, 238 580, 238 630" stroke="{INK}" stroke-width="1.8" fill="none"/>')
    for yy in range(472,628,16):
        b.append(f'<path d="M {213-(yy-456)*0.06:.1f} {yy} L {247-(yy-456)*0.06:.1f} {yy}" stroke="{GOLD}" stroke-width="1.6"/>')
    # bronchi + lungs
    b.append(f'<path d="M 204 630 C 190 650, 170 662, 150 676 M 238 630 C 252 650, 272 662, 292 676" stroke="{INK}" stroke-width="1.8" fill="none"/>')
    b.append(f'<path d="M 196 610 C 150 600, 96 640, 92 720 C 90 780, 104 816, 150 820 C 180 822, 194 800, 196 760 Z" fill="{GL}" stroke="{INK}" stroke-width="1.6"/>')
    b.append(f'<path d="M 246 610 C 292 600, 324 640, 326 720 C 328 780, 314 816, 276 820 C 248 822, 246 800, 246 760 Z" fill="{GL}" stroke="{INK}" stroke-width="1.6"/>')
    # diaphragm
    b.append(f'<path d="M 66 860 C 110 800, 170 790, 206 812 C 240 790, 300 800, 346 860" stroke="{GOLD}" stroke-width="3" fill="none" stroke-linecap="round"/>')
    b.append('</g>')
    L=[("Cavidade nasal",(40+300,10+216),210),("Palato",(40+290,10+245),262),("Cavidade oral e língua",(40+300,10+280),310),("Faringe",(40+202,10+300),360),
       ("Epiglote",(40+232,10+372),408),("Laringe e pregas vocais",(40+250,10+432),456),("Traqueia",(40+244,10+560),560),("Pulmões",(40+318,10+720),720),("Diafragma",(40+330,10+838),838)]
    for t,(x,y),ly in L:
        b.append(leader(x,y,470,ly)); b.append(label(478,ly+4,t))
    return svg(w,h,"".join(b))

def laringe_frente():
    w,h=660,560; cx=230
    b=[title(320,30,"A laringe vista de frente")]
    b.append(f'<path d="M {cx-110} 70 C {cx-96} 112, {cx+96} 112, {cx+110} 70" stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round"/>')
    b.append(f'<path d="M {cx-110} 70 C {cx-96} 112, {cx+96} 112, {cx+110} 70" stroke="{GL}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    for dx in (-70,-35,0,35,70):
        b.append(f'<path d="M {cx+dx} {106-abs(dx)*0.12} L {cx+dx*1.05} 132" stroke="{GRAY}" stroke-width="1.2"/>')
    b.append(f'<path d="M {cx-95} 134 L {cx-18} 132 L {cx} 158 L {cx+18} 132 L {cx+95} 134 L {cx+82} 236 L {cx} 284 L {cx-82} 236 Z" fill="{GL}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>')
    b.append(f'<path d="M {cx} 158 L {cx} 280" stroke="{GOLD}" stroke-width="1.2" stroke-dasharray="4 4"/>')
    b.append(f'<path d="M {cx-70} 300 C {cx-40} 318, {cx+40} 318, {cx+70} 300 L {cx+70} 334 C {cx+40} 352, {cx-40} 352, {cx-70} 334 Z" fill="{GM}" stroke="{INK}" stroke-width="2"/>')
    y=362
    while y<520:
        b.append(f'<path d="M {cx-56} {y} C {cx-30} {y+10}, {cx+30} {y+10}, {cx+56} {y} L {cx+56} {y+14} C {cx+30} {y+24}, {cx-30} {y+24}, {cx-56} {y+14} Z" fill="#fff" stroke="{INK}" stroke-width="1.4"/>')
        y+=26
    for t,(x,y),ly in [("Osso hioide",(cx+104,86),84),("Membrana tireo-hióidea",(cx+60,120),124),("Proeminência (pomo de Adão)",(cx,152),166),("Cartilagem tireoide",(cx+78,200),210),("Cartilagem cricoide",(cx+70,318),318),("Traqueia (anéis cartilagíneos)",(cx+56,430),430)]:
        b.append(leader(x,y,410,ly)); b.append(label(418,ly+4,t))
    return svg(w,h,"".join(b))

def diafragma():
    w,h=680,430
    b=[title(340,30,"Diafragma: inspiração e expiração")]
    def panel(cx,insp):
        o=[]
        # ribcage
        o.append(f'<path d="M {cx-70} 90 C {cx-120} 120, {cx-130} 220, {cx-118} 320 M {cx+70} 90 C {cx+120} 120, {cx+130} 220, {cx+118} 320" stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
        for i in range(6):
            yy=120+i*34; sp= 1.0 + (0.06 if insp else 0)
            o.append(f'<path d="M {cx-10} {yy} C {cx-60*sp} {yy-6}, {cx-104*sp} {yy+6}, {cx-110*sp} {yy+26} M {cx+10} {yy} C {cx+60*sp} {yy-6}, {cx+104*sp} {yy+6}, {cx+110*sp} {yy+26}" stroke="{GRAY}" stroke-width="1.6" fill="none"/>')
        o.append(f'<path d="M {cx} 70 L {cx} 300" stroke="{GRAY}" stroke-width="5"/>')
        dome = 250 if insp else 200
        lung_b = dome-6
        o.append(f'<path d="M {cx-14} 112 C {cx-62} 102, {cx-102} 150, {cx-102} {lung_b-8} C {cx-80} {lung_b+4}, {cx-40} {lung_b-4}, {cx-14} {lung_b-18} Z" fill="{GL}" stroke="{INK}" stroke-width="1.4"/>')
        o.append(f'<path d="M {cx+14} 112 C {cx+62} 102, {cx+102} 150, {cx+102} {lung_b-8} C {cx+80} {lung_b+4}, {cx+40} {lung_b-4}, {cx+14} {lung_b-18} Z" fill="{GL}" stroke="{INK}" stroke-width="1.4"/>')
        o.append(f'<path d="M {cx-116} 300 C {cx-90} {dome}, {cx-30} {dome-14}, {cx} {dome+4} C {cx+30} {dome-14}, {cx+90} {dome}, {cx+116} 300" stroke="{GOLD}" stroke-width="3.2" fill="none" stroke-linecap="round"/>')
        if insp:
            o.append(arrow(cx,dome-40,cx,dome+30,GOLD,2)); o.append(arrow(cx-130,200,cx-156,200,GOLD,2)); o.append(arrow(cx+130,200,cx+156,200,GOLD,2))
            o.append(label(cx,64,"ar entra",anchor="middle",cls="s"))
        else:
            o.append(arrow(cx,dome+50,cx,dome-10,GOLD,2)); o.append(label(cx,64,"ar sai",anchor="middle",cls="s"))
        o.append(f'<text x="{cx}" y="370" text-anchor="middle" style="font-family:Inter;font-size:14px;font-weight:600;fill:{INK}">{"Inspiração" if insp else "Expiração"}</text>')
        o.append(label(cx,392,"diafragma desce e se achata" if insp else "diafragma relaxa e sobe",anchor="middle",cls="s"))
        return "".join(o)
    b.append(panel(180,True)); b.append(panel(500,False))
    return svg(w,h,"".join(b))

def postura():
    w,h=520,640
    b=[title(260,30,"O ponto de partida")]
    b.append(f'<path d="M 168 56 L 168 600" stroke="{GRAY}" stroke-width="7"/>')
    b.append(label(160,620,"parede",anchor="end",cls="s"))
    b.append(f'<path d="M 120 600 L 440 600" stroke="{GRAY}" stroke-width="2"/>')
    st=f'stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    b.append(f'<ellipse cx="236" cy="94" rx="26" ry="32" {st}/>')
    b.append(f'<path d="M 224 126 L 220 160 M 246 124 L 248 156" {st}/>')
    b.append(f'<path d="M 220 160 C 194 186, 190 250, 198 300 C 204 330, 196 352, 194 372 C 190 394, 200 412, 206 432 C 212 480, 212 530, 214 590" {st}/>')
    b.append(f'<path d="M 248 156 C 280 172, 290 214, 286 250 C 282 286, 270 312, 268 340 C 266 366, 262 392, 260 422 C 258 470, 252 522, 250 590" {st}/>')
    b.append(f'<path d="M 234 176 C 244 230, 244 290, 238 356" {st}/>')
    b.append(f'<path d="M 206 596 L 276 596" {st}/>')
    b.append(f'<path d="M 230 56 L 230 600" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="5 5"/>')
    for t,yy in [("orelha",96),("ombro",176),("quadril",352),("joelho",470),("tornozelo",586)]:
        b.append(f'<circle cx="230" cy="{yy}" r="5" fill="{GOLD}"/><path d="M 238 {yy} L 330 {yy}" stroke="{GOLD}" stroke-width="0.8"/>'); b.append(label(338,yy+4,t))
    b.append(label(338,252,"costelas abertas,",cls="s")); b.append(label(338,268,"ombros relaxados,",cls="s")); b.append(label(338,284,"joelhos soltos",cls="s"))
    return svg(w,h,"".join(b))

def bascula():
    w,h=700,380
    b=[title(350,30,"Tensão e alongamento: o movimento de báscula")]
    def rot(px,py,jx,jy,deg):
        a=math.radians(deg); dx,dy=px-jx,py-jy
        return jx+dx*math.cos(a)-dy*math.sin(a), jy+dx*math.sin(a)+dy*math.cos(a)
    def panel(cx,deg,name,desc):
        o=[]; J=(cx+40,222)
        o.append(f'<path d="M {cx-92} 262 C {cx-96} 244, {cx-40} 238, {cx+20} 218 L {cx+72} 198 L {cx+78} 272 C {cx+20} 280, {cx-60} 282, {cx-92} 262 Z" fill="{GM}" stroke="{INK}" stroke-width="1.8"/>')
        o.append(f'<path d="M {cx+50} 200 L {cx+64} 162 L {cx+76} 198 Z" fill="{GL}" stroke="{INK}" stroke-width="1.6"/>')
        P=[(cx-112,110),(cx+30,98),(cx+46,226),(cx-98,206)]
        R=[rot(x,y,*J,deg) for x,y in P]
        if deg:
            o.append(f'<path d="M {" L ".join(f"{x:.1f} {y:.1f}" for x,y in P)} Z" fill="none" stroke="{SOFT}" stroke-width="1" stroke-dasharray="4 4"/>')
        o.append(f'<path d="M {" L ".join(f"{x:.1f} {y:.1f}" for x,y in R)} Z" fill="{GL}" fill-opacity=".55" stroke="{INK}" stroke-width="2"/>')
        F=rot(cx-82,184,*J,deg); A=(cx+60,194)
        o.append(f'<path d="M {F[0]:.1f} {F[1]:.1f} L {A[0]} {A[1]}" stroke="{GOLD}" stroke-width="4.5" stroke-linecap="round"/>')
        C1=R[3]; C2=(cx-78,246)
        o.append(f'<path d="M {C1[0]:.1f} {C1[1]:.1f} L {C2[0]} {C2[1]}" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 3"/>')
        L=math.hypot(A[0]-F[0],A[1]-F[1])
        o.append(f'<text x="{cx}" y="320" text-anchor="middle" style="font-family:Inter;font-size:14px;font-weight:600;fill:{INK}">{name}</text>')
        o.append(label(cx,340,desc,anchor="middle",cls="s"))
        return "".join(o)
    b.append(panel(190,0,"Repouso","pregas vocais mais curtas · sons graves"))
    b.append(panel(510,-14,"Báscula","a tireoide inclina para a frente · pregas alongadas · agudos"))
    b.append(leader(110,130,44,96)); b.append(label(40,90,"cartilagem tireoide",cls="s"))
    b.append(leader(130,262,44,300)); b.append(label(40,314,"cricoide",cls="s"))
    b.append(leader(254,170,330,128)); b.append(label(338,124,"aritenoide",cls="s"))
    b.append(leader(560,186,640,120)); b.append(label(648,116,"prega",cls="s")); b.append(label(648,130,"vocal",cls="s"))
    b.append(leader(436,236,380,268)); b.append(label(330,282,"músculo cricotireóideo",cls="s"))
    return svg(w,h,"".join(b))

def ondas():
    w,h=680,360
    b=[title(340,30,"Frequência e intensidade")]
    def wave(x0,y0,wd,amp,cyc,col=INK):
        pts=[]
        for i in range(0,401):
            t=i/400; pts.append(f"{x0+t*wd:.1f},{y0-amp*math.sin(2*math.pi*cyc*t):.1f}")
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>' + f'<path d="M {x0} {y0} L {x0+wd} {y0}" stroke="{GRAY}" stroke-width="1"/>'
    b.append(wave(40,120,270,34,3)); b.append(label(175,182,"Grave · frequência baixa",anchor="middle"))
    b.append(wave(370,120,270,34,9)); b.append(label(505,182,"Agudo · frequência alta",anchor="middle"))
    b.append(wave(40,260,270,14,5,GOLD)); b.append(label(175,318,"Fraco · menor amplitude",anchor="middle"))
    b.append(wave(370,260,270,48,5,GOLD)); b.append(label(505,318,"Forte · maior amplitude",anchor="middle"))
    b.append(label(340,350,"A altura depende da frequência de vibração; o volume, da amplitude.",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def fonte_filtro():
    w,h=680,300
    b=[title(340,30,"Fonte e filtro: como nasce a voz")]
    # source waveform: pulse train
    pts=[]
    for i in range(0,241):
        t=i/240; ph=(t*6)%1; y=150-(40*(ph/0.7) if ph<0.7 else 40*(1-(ph-0.7)/0.3))
        pts.append(f"{40+t*160:.1f},{y:.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2"/>')
    b.append(label(120,200,"Fonte",anchor="middle")); b.append(label(120,218,"as pregas vocais vibram:",anchor="middle",cls="s")); b.append(label(120,234,"um som “cru”, como um zumbido",anchor="middle",cls="s"))
    b.append(arrow(214,130,250,130,GOLD,2))
    # filter: tube
    b.append(f'<path d="M 262 100 C 300 80, 340 150, 380 110 C 400 92, 420 98, 430 110 L 430 160 C 420 172, 400 176, 380 160 C 340 120, 300 190, 262 160 Z" fill="{GL}" stroke="{INK}" stroke-width="2"/>')
    b.append(label(346,200,"Filtro",anchor="middle")); b.append(label(346,218,"faringe, boca e nariz",anchor="middle",cls="s")); b.append(label(346,234,"amplificam e moldam o som",anchor="middle",cls="s"))
    b.append(arrow(444,130,480,130,GOLD,2))
    pts=[]
    for i in range(0,401):
        t=i/400; y=130-26*math.sin(2*math.pi*6*t)-12*math.sin(2*math.pi*12*t+0.6)-7*math.sin(2*math.pi*24*t+1.1)
        pts.append(f"{494+t*150:.1f},{y:.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    b.append(label(569,200,"Voz",anchor="middle")); b.append(label(569,218,"o som rico em harmônicos",anchor="middle",cls="s")); b.append(label(569,234,"que chega ao ouvinte",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def vibrato():
    w,h=680,280
    b=[title(340,30,"O vibrato")]
    b.append(f'<path d="M 50 140 L 640 140" stroke="{GRAY}" stroke-width="1.4" stroke-dasharray="6 5"/>')
    b.append(label(646,144,"nota",cls="s"))
    pts=[]
    for i in range(0,601):
        t=i/600; env=min(1,t*4)
        pts.append(f"{50+t*590:.1f},{140-28*env*math.sin(2*math.pi*6*t):.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{GOLD}" stroke-width="2.4"/>')
    b.append(f'<path d="M 50 210 L 640 210 M 50 204 L 50 216 M 640 204 L 640 216" stroke="{INK}" stroke-width="1.2"/>')
    b.append(label(345,232,"1 segundo · cerca de 5 a 7 oscilações no canto lírico",anchor="middle",cls="s"))
    b.append(label(345,256,"A frequência oscila em torno da nota, de forma regular e controlada.",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def pulses(irregular):
    pts=[]; x=0
    import random
    random.seed(3)
    out=[]
    while x<270:
        gap = (22 if not irregular else random.choice([42,48,30,56]))
        for k in range(0,gap):
            t=k/gap; y = -30*math.exp(-t*5)*math.cos(2*math.pi*t*3)
            out.append((x+k,y))
        x+=gap
    return out
def fry():
    w,h=680,260
    b=[title(340,30,"Registro modal e fry")]
    for i,(irr,x0,name,desc) in enumerate([(False,40,"Modal","pulsos regulares e próximos"),(True,370,"Fry","pulsos espaçados e irregulares")]):
        pts=pulses(irr)
        b.append(f'<polyline points="{" ".join(f"{x0+x:.1f},{120+y:.1f}" for x,y in pts if x<270)}" fill="none" stroke="{INK if not irr else GOLD}" stroke-width="2"/>')
        b.append(f'<path d="M {x0} 120 L {x0+270} 120" stroke="{GRAY}" stroke-width="1"/>')
        b.append(f'<text x="{x0+135}" y="196" text-anchor="middle" style="font-family:Inter;font-size:14px;font-weight:600;fill:{INK}">{name}</text>')
        b.append(label(x0+135,216,desc,anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def yodel():
    w,h=680,280
    b=[title(340,30,"Yodel: a quebra entre registros")]
    b.append(f'<rect x="50" y="70" width="580" height="50" fill="{GL}"/><rect x="50" y="160" width="580" height="50" fill="{GRAY}" opacity=".5"/>')
    b.append(label(60,92,"registro elevado (voz de cabeça)",cls="s")); b.append(label(60,232,"registro modal (voz de peito)",cls="s"))
    pts=[(50,185),(130,185),(140,95),(220,95),(230,185),(300,185),(310,95),(400,95),(410,185),(480,185),(490,95),(630,95)]
    b.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>')
    for x in (135,225,305,405,485):
        b.append(f'<circle cx="{x}" cy="140" r="5" fill="{GOLD}"/>')
    b.append(label(340,262,"Cada ponto dourado é uma “quebra” intencional de registro.",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def staff(x0,y0,wd):
    return "".join(f'<path d="M {x0} {y0+i*12} L {x0+wd} {y0+i*12}" stroke="{INK}" stroke-width="1"/>' for i in range(5))
def note(x,y,small=False,stem=True,filled=True,slash=False):
    r=(4.6 if small else 6.8); ry=r*0.72
    o=f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{ry}" transform="rotate(-20 {x} {y})" fill="{INK if filled else "#fff"}" stroke="{INK}" stroke-width="1.6"/>'
    if stem:
        L=(26 if small else 38); o+=f'<path d="M {x+r-0.6} {y-1} L {x+r-0.6} {y-L}" stroke="{INK}" stroke-width="1.5"/>'
        if small: o+=f'<path d="M {x+r-0.6} {y-L} C {x+r+8} {y-L+8}, {x+r+8} {y-L+14}, {x+r+4} {y-L+18}" stroke="{INK}" stroke-width="1.4" fill="none"/>'
        if slash: o+=f'<path d="M {x-4} {y-L+20} L {x+r+8} {y-L+6}" stroke="{INK}" stroke-width="1.4"/>'
    return o
def melisma():
    w,h=680,250
    b=[title(340,30,"Melisma: várias notas em uma única sílaba")]
    b.append(staff(40,80,600))
    ys=[110,104,98,104,110,116,110,104,98,92,98,104]
    xs=[110+i*42 for i in range(len(ys))]
    for x,y in zip(xs,ys): b.append(note(x,y))
    b.append(f'<path d="M 104 156 C 250 186, 450 186, 590 156" stroke="{GOLD}" stroke-width="1.8" fill="none"/>')
    b.append(f'<text x="104" y="206" style="font-family:Inter;font-size:18px;fill:{INK}">a ——————————————————————————</text>')
    b.append(label(340,236,"Uma sílaba sustentada, enquanto a melodia percorre várias notas.",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))
def apogiatura():
    w,h=680,250
    b=[title(340,30,"Apogiatura: a nota vizinha que ornamenta")]
    b.append(staff(60,80,560))
    b.append(note(220,98,small=True,slash=True)); b.append(note(262,104,stem=True,filled=False))
    b.append(f'<path d="M 214 120 C 230 136, 254 136, 262 122" stroke="{GOLD}" stroke-width="1.6" fill="none"/>')
    b.append(note(420,104,stem=True,filled=False))
    b.append(leader(220,90,150,150)); b.append(label(150,168,"nota vizinha",anchor="middle",cls="s"))
    b.append(leader(268,110,300,160)); b.append(label(300,178,"nota principal",anchor="middle",cls="s"))
    b.append(label(420,160,"a mesma nota, sem ornamento",anchor="middle",cls="s"))
    b.append(label(340,226,"A apogiatura “apoia” a nota principal a partir de um intervalo de segunda.",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def ressonancia():
    w,h=640,560
    b=[title(320,30,"Twang: brilho e “voz de máscara”")]
    b.append('<g transform="translate(20,0)">'); b.append(head_internals(hl_mask=True,hl_ae=True))
    b.append(f'<path d="{HEAD}" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>'); b.append('</g>')
    b.append(leader(340,206,440,170)); b.append(label(448,166,"sensação de “máscara”")); b.append(label(448,184,"brilho percebido na face",cls="s"))
    b.append(leader(256,392,440,392)); b.append(label(448,388,"constrição ariepiglótica")); b.append(label(448,406,"estreitamento acima das",cls="s")); b.append(label(448,422,"pregas vocais",cls="s"))
    b.append(leader(304,268,440,290)); b.append(label(448,294,"base da língua elevada"))
    return svg(w,h,"".join(b))

# --- restyled previous figures ---
def registros():
    w,h=680,300
    b=[title(340,30,"Os três registros")]
    b.append(f'<line x1="40" y1="262" x2="640" y2="262" stroke="{INK}" stroke-width="1.4"/><polygon points="640,257 650,262 640,267" fill="{INK}"/>')
    b.append(label(40,284,"grave",cls="s")); b.append(label(640,284,"agudo",anchor="end",cls="s"))
    rows=[("BASAL",40,200,GRAY,INK,"ranger de porta · musculatura relaxada"),("MODAL",140,500,INK,CREAM,"voz de peito · a voz da fala"),("ELEVADO",420,640,GOLD,"#fff","voz de cabeça · laringe elevada")]
    y=56
    for n,x1,x2,c,tc,d in rows:
        b.append(f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="36" rx="18" fill="{c}"/>')
        b.append(f'<text x="{(x1+x2)/2}" y="{y+23}" text-anchor="middle" style="font-family:Inter;font-size:13px;font-weight:600;letter-spacing:3px;fill:{tc}">{n}</text>')
        tx= x1 if x1<300 else x2; anc="start" if x1<300 else "end"
        b.append(label(tx,y+56,d,anchor=anc,cls="s")); y+=68
    return svg(w,h,"".join(b))

def extensao():
    names=["DO","DO#","RE","RE#","MI","FA","FA#","SOL","SOL#","LA","LA#","SI"]
    def idx(n,o): return names.index(n)+12*(o-1)
    white=[0,2,4,5,7,9,11]; octs=5; wkw=17.0; x0=40
    W=int(x0*2+octs*7*wkw)
    b=[title(W/2,26,"Extensão aproximada das vozes")]
    def xc(s):
        o,n=divmod(s,12)
        if n in white: return x0+(o*7+white.index(n))*wkw+wkw/2
        return x0+(o*7+white.index(n-1))*wkw+wkw
    R=[("Soprano",idx("DO",3),idx("FA",5),GOLD,"#fff"),("Mezzo",idx("LA",2),idx("SI",4),GM,INK),("Contralto",idx("MI",2),idx("LA",4),GL,INK),
       ("Tenor",idx("DO",2),idx("RE",4),INK,CREAM),("Barítono",idx("SOL",1),idx("LA",3),"#4a4744",CREAM),("Baixo",idx("DO",1),idx("FA",3),"#8d8881","#fff")]
    y=44
    for n,a,z,c,tc in R:
        xa,xz=xc(a)-wkw/2,xc(z)+wkw/2
        b.append(f'<rect x="{xa}" y="{y}" width="{xz-xa}" height="24" rx="12" fill="{c}"/>')
        b.append(f'<text x="{(xa+xz)/2}" y="{y+16.5}" text-anchor="middle" style="font-family:Inter;font-size:12px;font-weight:600;fill:{tc}">{n}</text>')
        y+=31
    ky=y+8
    for o in range(octs):
        for i in range(7):
            b.append(f'<rect x="{x0+(o*7+i)*wkw}" y="{ky}" width="{wkw}" height="80" fill="#fff" stroke="{INK}" stroke-width="0.8"/>')
    for o in range(octs):
        for i in (0,1,3,4,5):
            b.append(f'<rect x="{x0+(o*7+i)*wkw+wkw*0.68}" y="{ky}" width="{wkw*0.64}" height="50" fill="{INK}" rx="1.5"/>')
        b.append(f'<text x="{x0+o*7*wkw+wkw/2}" y="{ky+98}" text-anchor="middle" style="font-family:Inter;font-size:11px;font-weight:600;fill:{INK}">DO{o+1}</text>')
    return svg(W,ky+110,"".join(b))

def ciclo():
    w,h=700,300
    b=[title(350,26,"O ciclo glótico")]
    b.append(label(350,46,"vista superior · a frente da laringe está para cima",anchor="middle",cls="s"))
    def panel(cx,cy,post,mid,ant,lab,num):
        o=[f'<circle cx="{cx}" cy="{cy}" r="74" fill="{INK}"/>']
        top,bot=-60,58
        for s in (-1,1):
            p=f'M {cx+s*0.6},{cy+top} C {cx+s*34},{cy-50} {cx+s*54},{cy-14} {cx+s*50},{cy+16} C {cx+s*47},{cy+40} {cx+s*30},{cy+60} {cx+s*max(post,6)+s*10},{cy+bot+4} L {cx+s*post},{cy+bot} Q {cx+s*mid},{cy-2} {cx+s*ant},{cy+top} Z'
            o.append(f'<path d="{p}" fill="{GL}" stroke="{GOLD}" stroke-width="1.2"/>')
        o.append(f'<text x="{cx}" y="{cy+106}" text-anchor="middle" style="font-family:Inter;font-size:13px;font-weight:700;fill:{GOLD}">{num}</text>')
        o.append(f'<text x="{cx}" y="{cy+124}" text-anchor="middle" style="font-family:Inter;font-size:12.5px;fill:{INK}">{lab}</text>')
        return "".join(o)
    for cx,post,mid,ant,lab,num in [(92,0,2,0.6,"Fase fechada","1"),(262,14,5,1.4,"Fase de abertura","2"),(432,30,16,4,"Fase aberta","3"),(602,12,3,0.9,"Fase de fechamento","4")]:
        b.append(panel(cx,128,post,mid,ant,lab,num))
    for x in (172,342,512):
        b.append(arrow(x,128,x+14,128,GOLD,2))
    return svg(w,h,"".join(b))

def laringe_corte():
    w,h=660,380; cx=250
    def hw(y):
        pts=[(40,60),(100,58),(128,50),(140,34),(148,30),(158,36),(172,20),(180,12),(188,14),(208,32),(248,40),(308,38),(350,32)]
        for (y1,a),(y2,b2) in zip(pts,pts[1:]):
            if y1<=y<=y2: return a+(b2-a)*(y-y1)/(y2-y1)
        return pts[-1][1]
    L=[(cx-hw(y),y) for y in range(40,351,5)]; R=[(cx+hw(y),y) for y in range(350,39,-5)]
    lumen="M "+" L ".join(f"{x:.1f},{y}" for x,y in L+R)+" Z"
    b=[title(330,24,"A laringe em corte")]
    b.append(f'<rect x="{cx-118}" y="34" width="236" height="322" rx="24" fill="{GL}" stroke="{GOLD}" stroke-width="1.4"/>')
    b.append(f'<path d="{lumen}" fill="{INK}"/>')
    for s in (-1,1):
        for yy,wd in ((144,16),(176,14)):
            x0=cx+s*hw(yy); b.append(f'<polygon points="{x0},{yy-7} {x0-s*wd},{yy} {x0},{yy+7}" fill="{GOLD}"/>')
    b.append(f'<path d="M {cx-52} 54 C {cx-62} 80, {cx-60} 112, {cx-56} 136" stroke="{GOLD}" stroke-width="6" fill="none" stroke-linecap="round"/>')
    for name,y1,y2,d in [("SUPRAGLOTE",44,158,"acima das pregas vocais"),("GLOTE",158,190,"entre as pregas vocais"),("INFRAGLOTE",190,346,"abaixo das pregas vocais")]:
        bx=cx+138
        b.append(f'<path d="M {bx},{y1} L {bx+10},{y1} L {bx+10},{y2} L {bx},{y2}" stroke="{GOLD}" stroke-width="1.6" fill="none"/>')
        ym=(y1+y2)/2
        b.append(f'<text x="{bx+22}" y="{ym}" style="font-family:Inter;font-size:12.5px;font-weight:600;letter-spacing:2px;fill:{INK}">{name}</text>')
        b.append(label(bx+22,ym+16,d,cls="s"))
    b.append(label(cx-64,46,"epiglote",anchor="end",cls="s"))
    b.append(label(cx,374,"corte lateral esquemático",anchor="middle",cls="s"))
    return svg(w,h,"".join(b))

def respiracao():
    w,h=700,330
    b=[title(350,24,"Os quatro tipos de respiração")]
    def torso(cx,cy,mode,lab,num):
        o=[f'<circle cx="{cx}" cy="{cy-96}" r="20" fill="none" stroke="{INK}" stroke-width="1.8"/>']
        sy=cy-64-(10 if mode==1 else 0)
        o.append(f'<path d="M {cx-8},{cy-76} L {cx-8},{cy-64} M {cx+8},{cy-76} L {cx+8},{cy-64}" stroke="{INK}" stroke-width="1.8"/>')
        o.append(f'<path d="M {cx-8},{cy-64} C {cx-36},{cy-62} {cx-52},{sy} {cx-54},{sy+14} L {cx-48},{cy+10} C {cx-48},{cy+44} {cx-44},{cy+76} {cx-40},{cy+96} L {cx+40},{cy+96} C {cx+44},{cy+76} {cx+48},{cy+44} {cx+48},{cy+10} L {cx+54},{sy+14} C {cx+52},{sy} {cx+36},{cy-62} {cx+8},{cy-64}" fill="none" stroke="{INK}" stroke-width="1.8"/>')
        x,y,rx,ry={1:(cx,cy-40,30,16),2:(cx,cy-12,38,18),3:(cx,cy+52,32,22),4:(cx,cy+10,44,50)}[mode]
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{GOLD}" opacity=".55"/>')
        if mode==1: o.append(arrow(cx-60,cy-70,cx-60,cy-86,GOLD,2)+arrow(cx+60,cy-70,cx+60,cy-86,GOLD,2))
        if mode==3: o.append(arrow(cx,cy+78,cx,cy+92,GOLD,2))
        if mode==4: o.append(arrow(cx-52,cy+8,cx-68,cy+8,GOLD,2)+arrow(cx+52,cy+8,cx+68,cy+8,GOLD,2)+arrow(cx,cy+78,cx,cy+90,GOLD,2))
        o.append(f'<text x="{cx}" y="{cy+124}" text-anchor="middle" style="font-family:Inter;font-size:13px;font-weight:700;fill:{GOLD}">{num}</text>')
        o.append(f'<text x="{cx}" y="{cy+142}" text-anchor="middle" style="font-family:Inter;font-size:12.5px;fill:{INK}">{lab}</text>')
        return "".join(o)
    for i,(m,l) in enumerate([(1,"Clavicular"),(2,"Torácica"),(3,"Abdominal"),(4,"Completa")]):
        b.append(torso(95+i*170,150,m,l,str(m)))
    return svg(w,h,"".join(b))

figs={"f-aparelho":aparelho(),"f-laringe-frente":laringe_frente(),"f-diafragma":diafragma(),"f-postura":postura(),"f-bascula":bascula(),
      "f-ondas":ondas(),"f-fonte-filtro":fonte_filtro(),"f-vibrato":vibrato(),"f-fry":fry(),"f-yodel":yodel(),"f-melisma":melisma(),
      "f-apogiatura":apogiatura(),"f-twang":ressonancia(),"f-registros":registros(),"f-extensao":extensao(),"f-ciclo":ciclo(),
      "f-laringe-corte":laringe_corte(),"f-respiracao":respiracao()}
for n,s in figs.items(): open(f"img/{n}.svg","w",encoding="utf-8").write(s)
print(len(figs),"svgs")
