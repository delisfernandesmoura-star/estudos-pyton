import math
INK="#2B2622"; CREAM="#F7F0E4"; GOLD="#C29A55"; CORAL="#E8907A"; SAGE="#8FB59A"; MUST="#E6B450"; LAV="#B3A3D6"; PEACH="#F4C9A8"; SOFT="#7a7068"; WHITE="#FFFFFF"; ROSE="#F2A7A0"
FONT="font-family:Nunito,Arial,sans-serif"
def svg(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>text{{{FONT};fill:{INK}}} .t{{font-family:Fredoka,Nunito,sans-serif;font-size:17px;font-weight:600;fill:{INK}}} .l{{font-size:14px;font-weight:700}} .s{{font-size:12.5px;fill:{SOFT};font-weight:600}}</style>{body}</svg>'
def T(x,y,t,cls="l",a="middle",fill=None): return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{a}"{(" style=\"fill:"+fill+"\"") if fill else ""}>{t}</text>'
def note(x,y,c=GOLD,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="7" ry="5.4" transform="rotate(-22)" fill="{c}"/><path d="M6 -2 L6 -30 Q16 -24 18 -14" stroke="{c}" stroke-width="2.6" fill="none" stroke-linecap="round"/></g>'
def arrow(x1,y1,x2,y2,c=GOLD,w=2.4):
    a=math.atan2(y2-y1,x2-x1);L=10
    return f'<path d="M{x1},{y1} L{x2},{y2} M{x2-L*math.cos(a-.5):.1f},{y2-L*math.sin(a-.5):.1f} L{x2},{y2} L{x2-L*math.cos(a+.5):.1f},{y2-L*math.sin(a+.5):.1f}" stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'

def kid(cx,top,s=1,skin="#E0A980",hair="#3b2a20",hs="bun",shirt=MUST,pants=CORAL,mouth="sing",arms="open",prop=None,shoes=INK):
    o=[f'<g transform="translate({cx},{top}) scale({s})" stroke-linecap="round" stroke-linejoin="round">']
    # back hair
    if hs=="long": o.append(f'<path d="M-46 40 C-52 100,-50 150,-38 170 L38 170 C50 150,52 100,46 40 Z" fill="{hair}"/>')
    # legs
    o.append(f'<path d="M-20 200 L-22 262 M20 200 L22 262" stroke="{pants}" stroke-width="18"/>')
    o.append(f'<ellipse cx="-24" cy="266" rx="14" ry="7" fill="{shoes}"/><ellipse cx="24" cy="266" rx="14" ry="7" fill="{shoes}"/>')
    # arms
    if arms=="open":
        o.append(f'<path d="M-30 120 L-62 96 M30 120 L62 96" stroke="{skin}" stroke-width="12"/><path d="M-30 118 L-50 106 M30 118 L50 106" stroke="{shirt}" stroke-width="16"/>')
    elif arms=="down":
        o.append(f'<path d="M-32 118 L-42 180 M32 118 L42 180" stroke="{skin}" stroke-width="12"/><path d="M-32 116 L-38 146 M32 116 L38 146" stroke="{shirt}" stroke-width="16"/>')
    elif arms=="belly":
        o.append(f'<path d="M-32 118 L-38 150 L-6 168 M32 118 L38 150 L6 168" stroke="{skin}" stroke-width="12" fill="none"/><path d="M-32 116 L-37 142 M32 116 L37 142" stroke="{shirt}" stroke-width="16"/>')
    elif arms=="mic":
        o.append(f'<path d="M-32 118 L-42 180 M32 118 L44 128 L20 100" stroke="{skin}" stroke-width="12" fill="none"/><path d="M-32 116 L-38 146 M32 116 L42 126" stroke="{shirt}" stroke-width="16"/>')
        o.append(f'<rect x="12" y="76" width="9" height="30" rx="4" fill="{INK}" transform="rotate(-20 16 92)"/><circle cx="12" cy="74" r="9" fill="{SOFT}"/>')
    elif arms=="throat":
        o.append(f'<path d="M-32 118 L-42 180 M32 118 L36 140 L8 104" stroke="{skin}" stroke-width="12" fill="none"/><path d="M-32 116 L-38 146 M32 116 L36 134" stroke="{shirt}" stroke-width="16"/>')
    # body
    o.append(f'<path d="M-34 108 C-34 100,-24 96,0 96 C24 96,34 100,34 108 L30 206 L-30 206 Z" fill="{shirt}"/>')
    # neck
    o.append(f'<rect x="-8" y="82" width="16" height="18" rx="6" fill="{skin}"/>')
    # head
    o.append(f'<circle cx="0" cy="50" r="42" fill="{skin}"/>')
    # hair front
    if hs=="bun":
        o.append(f'<circle cx="0" cy="2" r="18" fill="{hair}"/><path d="M-42 50 C-44 14,-16 4,0 6 C20 4,44 14,42 48 C34 30,20 24,0 24 C-18 24,-34 30,-42 50 Z" fill="{hair}"/>')
    elif hs=="short":
        o.append(f'<path d="M-43 52 C-46 10,-10 0,4 4 C30 2,48 22,42 50 C38 36,28 26,10 26 C-6 34,-28 30,-43 52 Z" fill="{hair}"/>')
    elif hs=="long":
        o.append(f'<path d="M-44 60 C-48 12,-12 2,2 4 C30 4,48 20,44 60 C38 34,22 22,-4 24 C-20 30,-36 40,-44 60 Z" fill="{hair}"/>')
    elif hs=="curly":
        for a in range(0,360,30):
            r=math.radians(a); o.append(f'<circle cx="{40*math.cos(r):.1f}" cy="{36+34*math.sin(r)-6:.1f}" r="15" fill="{hair}"/>')
        o.append(f'<circle cx="0" cy="54" r="36" fill="{skin}"/>')
    # face
    o.append(f'<circle cx="-14" cy="52" r="3.6" fill="{INK}"/><circle cx="14" cy="52" r="3.6" fill="{INK}"/>')
    o.append(f'<circle cx="-24" cy="64" r="6" fill="{ROSE}" opacity=".7"/><circle cx="24" cy="64" r="6" fill="{ROSE}" opacity=".7"/>')
    if mouth=="sing": o.append(f'<ellipse cx="0" cy="70" rx="7" ry="9" fill="#7a2f2a"/>')
    elif mouth=="smile": o.append(f'<path d="M-10 66 Q0 76 10 66" stroke="{INK}" stroke-width="3" fill="none"/>')
    elif mouth=="o": o.append(f'<circle cx="0" cy="70" r="5" fill="#7a2f2a"/>')
    elif mouth=="hum": o.append(f'<path d="M-8 70 L8 70" stroke="{INK}" stroke-width="3"/>')
    elif mouth=="blow": o.append(f'<ellipse cx="0" cy="70" rx="5" ry="4" fill="#7a2f2a"/>')
    if prop=="headphones":
        o.append(f'<path d="M-46 52 C-46 0,46 0,46 52" stroke="{INK}" stroke-width="6" fill="none"/><rect x="-54" y="42" width="14" height="24" rx="6" fill="{INK}"/><rect x="40" y="42" width="14" height="24" rx="6" fill="{INK}"/>')
    o.append('</g>')
    return "".join(o)
LIA=dict(skin="#B9784F",hair="#2a1a12",hs="curly",shirt=MUST,pants=CORAL)
THEO=dict(skin="#F1C9A5",hair="#6b4426",hs="short",shirt=SAGE,pants="#5f5a55")
BIA=dict(skin="#D9A07A",hair="#2b1d16",hs="long",shirt=LAV,pants="#4b4642")

def F_lia():  return svg(300,330, kid(150,30,1,mouth="sing",arms="open",**LIA)+note(240,90)+note(262,150,CORAL,.9)+note(56,110,SAGE,.8))
def F_theo(): return svg(300,330, kid(150,30,1,mouth="o",arms="throat",prop="headphones",**THEO)+f'<path d="M222 70 q10 -8 20 0 q10 8 20 0" stroke="{GOLD}" stroke-width="3" fill="none"/><path d="M222 92 q10 -8 20 0 q10 8 20 0" stroke="{CORAL}" stroke-width="3" fill="none"/>')
def F_bia():  return svg(300,330, kid(150,30,1,mouth="sing",arms="mic",**BIA)+note(240,80,LAV)+note(60,100,GOLD,.9))
def F_turma():
    b=kid(130,60,.9,mouth="sing",arms="open",**LIA)+kid(300,30,1.0,mouth="sing",arms="down",**THEO)+kid(470,40,.97,mouth="sing",arms="mic",**BIA)
    for x,y,c,s in [(60,80,GOLD,1),(560,70,CORAL,1),(210,40,SAGE,.8),(390,30,LAV,.8),(300,20,GOLD,.7)]: b+=note(x,y,c,s)
    return svg(600,330,b)

def F_casa():
    b=[T(300,26,"ONDE MORA A VOZ","t")]
    b.append(f'<path d="M200 300 C 190 250, 196 220, 210 196 C 180 180, 160 140, 170 100 C 180 60, 230 40, 270 46 C 320 52, 346 90, 340 132 C 352 140, 356 150, 344 156 C 350 168, 344 176, 336 178 C 338 192, 330 204, 312 206 C 300 230, 300 262, 304 300 Z" fill="{PEACH}" stroke="{INK}" stroke-width="2.5"/>')
    b.append(f'<path d="M200 300 L 160 330 M304 300 L 360 330" stroke="{INK}" stroke-width="2.5"/>')
    b.append(f'<circle cx="300" cy="108" r="4" fill="{INK}"/><path d="M322 176 q-8 4 -16 0" stroke="{INK}" stroke-width="2.5" fill="none"/>')
    b.append(f'<rect x="246" y="222" width="34" height="46" rx="12" fill="{GOLD}" opacity=".9"/><path d="M252 246 L263 241 L252 236 M274 246 L263 241 L274 236" stroke="{WHITE}" stroke-width="2.4" fill="none"/>')
    b.append(f'<path d="M282 244 L400 220" stroke="{GOLD}" stroke-width="1.6"/>'+T(408,214,"Laringe","l","start")+T(408,232,"a “casinha” da voz,","s","start")+T(408,248,"dentro do pescoço","s","start"))
    b.append(f'<path d="M262 270 L262 318" stroke="{SOFT}" stroke-width="1.4" stroke-dasharray="4 4"/>'+T(262,336,"o ar vem dos pulmões","s"))
    return svg(600,350,"".join(b))

def F_cortinas():
    b=[T(320,26,"AS CORTININHAS DA VOZ","t")]
    def pan(cx,closed,lab,sub):
        o=[f'<rect x="{cx-110}" y="50" width="220" height="200" rx="26" fill="{CREAM}" stroke="{INK}" stroke-width="2.5"/>',f'<rect x="{cx-100}" y="58" width="200" height="12" rx="6" fill="{GOLD}"/>']
        gap=4 if closed else 46
        o.append(f'<path d="M{cx-100} 70 C {cx-80} 120, {cx-70} 180, {cx-100} 240 L{cx-gap} 240 C {cx-gap-10} 180, {cx-gap-6} 120, {cx-gap} 70 Z" fill="{CORAL}"/>')
        o.append(f'<path d="M{cx+100} 70 C {cx+80} 120, {cx+70} 180, {cx+100} 240 L{cx+gap} 240 C {cx+gap+10} 180, {cx+gap+6} 120, {cx+gap} 70 Z" fill="{CORAL}"/>')
        if closed:
            for k in range(3): o.append(f'<path d="M{cx-8} {120+k*40} q8 -6 16 0" stroke="{WHITE}" stroke-width="2.4" fill="none"/>')
            o+= [note(cx+130,90,GOLD,.9)]
        else:
            o.append(arrow(cx,226,cx,96,SAGE,3))
        o.append(T(cx,280,lab)+T(cx,298,sub,"s"))
        return "".join(o)
    b.append(pan(170,False,"Respirando","as cortininhas abrem e o ar passa"))
    b.append(pan(470,True,"Falando e cantando","elas se encostam e vibram"))
    return svg(640,310,"".join(b))

def F_balao():
    b=[T(300,26,"A BARRIGA BALÃO","t")]
    b.append(kid(170,50,.95,mouth="smile",arms="belly",**LIA))
    b.append(f'<ellipse cx="170" cy="200" rx="40" ry="34" fill="{SAGE}" opacity=".55"/>')
    b.append(f'<g transform="translate(420,150)"><ellipse cx="0" cy="0" rx="62" ry="74" fill="{CORAL}"/><path d="M0 74 L-8 88 L8 88 Z" fill="{CORAL}"/><path d="M0 88 C10 120,-10 140,6 170" stroke="{INK}" stroke-width="2" fill="none"/><ellipse cx="-22" cy="-30" rx="12" ry="20" fill="{WHITE}" opacity=".45"/></g>')
    b.append(arrow(260,150,340,150,GOLD,3))
    b.append(T(300,334,"Puxe o ar pelo nariz: a barriga enche como um balão.","s")+T(300,352,"Solte devagar: o balão murcha sem pressa.","s"))
    return svg(600,364,"".join(b))

def F_arvore():
    b=[T(300,26,"FIRME COMO UMA ÁRVORE","t")]
    b.append(f'<circle cx="300" cy="120" r="88" fill="{SAGE}" opacity=".45"/><circle cx="250" cy="100" r="50" fill="{SAGE}" opacity=".5"/><circle cx="352" cy="96" r="54" fill="{SAGE}" opacity=".5"/>')
    b.append(kid(300,60,.95,mouth="smile",arms="open",**THEO))
    for dx in (-60,-30,0,30,60):
        b.append(f'<path d="M{300+dx*0.3} 314 C {300+dx*0.6} 330, {300+dx} 336, {300+dx*1.4} 350" stroke="#8a6a4a" stroke-width="4" fill="none" stroke-linecap="round"/>')
    b.append(f'<path d="M180 316 L420 316" stroke="#8a6a4a" stroke-width="3"/>')
    for t,y,yy in [("cabeça leve, como uma copa",110,110),("ombros soltos",150,150),("joelhos destravados",260,260),("pés firmes, como raízes",330,316)]:
        b.append(f'<path d="M370 {yy} L440 {y}" stroke="{GOLD}" stroke-width="1.4"/>'+f'<circle cx="370" cy="{yy}" r="3.4" fill="{GOLD}"/>'+T(446,y+4,t,"s","start"))
    return svg(640,360,"".join(b))

def F_termometro():
    b=[T(320,26,"O TERMÔMETRO DO VOLUME","t")]
    levels=[("Sussurro","segredos",SAGE),("Fala tranquila","conversa",MUST),("Voz forte","apresentação, palco",CORAL),("Grito","só em emergência!","#C9473F")]
    b.append(f'<rect x="80" y="60" width="44" height="240" rx="22" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/><circle cx="102" cy="300" r="34" fill="#C9473F" stroke="{INK}" stroke-width="2.5"/>')
    for i,(n,d,c) in enumerate(levels):
        y=250-i*56
        b.append(f'<rect x="88" y="{y}" width="28" height="52" rx="6" fill="{c}"/>')
        b.append(f'<path d="M126 {y+26} L176 {y+26}" stroke="{INK}" stroke-width="1.6"/>'+T(186,y+24,n,"l","start")+T(186,y+42,d,"s","start"))
    b.append(f'<g transform="translate(470,80)"><rect x="0" y="0" width="140" height="200" rx="20" fill="{CREAM}" stroke="{GOLD}" stroke-width="2"/>'+T(70,34,"Dica","t")+T(70,66,"Na maior parte","s")+T(70,84,"do dia, fique","s")+T(70,102,"no verde e no","s")+T(70,120,"amarelo.","s")+T(70,150,"O vermelho cansa","s")+T(70,168,"e machuca a voz.","s")+'</g>')
    return svg(640,350,"".join(b))

def F_agua():
    b=[T(300,26,"ÁGUA: A MELHOR AMIGA DA VOZ","t")]
    b.append(f'<g transform="translate(200,60)"><rect x="0" y="30" width="110" height="220" rx="30" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/><rect x="30" y="0" width="50" height="36" rx="10" fill="{GOLD}"/><path d="M6 120 C 40 108, 70 132, 104 118 L104 220 C104 236 94 246 80 246 L30 246 C16 246 6 236 6 220 Z" fill="{SAGE}" opacity=".6"/><circle cx="40" cy="160" r="5" fill="{WHITE}"/><circle cx="64" cy="190" r="4" fill="{WHITE}"/><circle cx="50" cy="214" r="6" fill="{WHITE}"/></g>')
    for i,(x,y) in enumerate([(370,110),(400,170),(380,230)]):
        b.append(f'<path d="M{x} {y-24} C {x+14} {y-4}, {x+14} {y+12}, {x} {y+12} C {x-14} {y+12}, {x-14} {y-4}, {x} {y-24} Z" fill="{SAGE}"/>')
    b.append(T(470,120,"Goles pequenos","l","start")+T(470,138,"ao longo do dia","s","start")+T(470,180,"Antes e depois","l","start")+T(470,198,"de cantar","s","start")+T(470,240,"Água em temperatura","l","start")+T(470,258,"ambiente","s","start"))
    return svg(640,320,"".join(b))

def icon(kind,x,y,c):
    if kind=="agua": return f'<path d="M{x} {y-22} C {x+16} {y}, {x+16} {y+14}, {x} {y+14} C {x-16} {y+14}, {x-16} {y}, {x} {y-22} Z" fill="{c}"/>'
    if kind=="sono": return f'<path d="M{x+10} {y-18} A 18 18 0 1 0 {x+14} {y+12} A 14 14 0 1 1 {x+10} {y-18} Z" fill="{c}"/>'
    if kind=="fruta": return f'<circle cx="{x}" cy="{y}" r="16" fill="{c}"/><path d="M{x} {y-16} q4 -10 12 -10" stroke="{SAGE}" stroke-width="3" fill="none"/>'
    if kind=="aquec": return f'<path d="M{x-16} {y} q8 -12 16 0 q8 12 16 0" stroke="{c}" stroke-width="4" fill="none"/><path d="M{x-16} {y+12} q8 -12 16 0 q8 12 16 0" stroke="{c}" stroke-width="4" fill="none"/>'
    if kind=="grito": return f'<path d="M{x-18} {y-8} L{x} {y-8} L{x+18} {y-20} L{x+18} {y+20} L{x} {y+8} L{x-18} {y+8} Z" fill="{c}"/><path d="M{x+24} {y-12} l8 -6 M{x+26} {y} l10 0 M{x+24} {y+12} l8 6" stroke="{c}" stroke-width="3"/>'
    if kind=="barulho": return "".join(f'<path d="M{x-18+k*12} {y+14} L{x-18+k*12} {y-4-k*5}" stroke="{c}" stroke-width="6" stroke-linecap="round"/>' for k in range(4))
    if kind=="pigarro": return f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="{c}" stroke-width="4"/><path d="M{x-8} {y-6} l16 12 M{x+8} {y-6} l-16 12" stroke="{c}" stroke-width="4"/>'
    if kind=="frio": return "".join(f'<path d="M{x} {y} l{16*math.cos(math.radians(a)):.1f} {16*math.sin(math.radians(a)):.1f}" stroke="{c}" stroke-width="3.4" stroke-linecap="round"/>' for a in range(0,360,60))
    return ""
def F_amigos():
    b=[T(320,26,"AMIGOS E VILÕES DA VOZ","t")]
    b.append(f'<rect x="20" y="44" width="290" height="270" rx="24" fill="{SAGE}" opacity=".25"/><rect x="330" y="44" width="290" height="270" rx="24" fill="{CORAL}" opacity=".22"/>')
    b.append(T(165,76,"Amigos")+T(475,76,"Vilões"))
    A=[("agua","Beber água",SAGE),("sono","Dormir bem",LAV),("fruta","Frutas e comida leve",CORAL),("aquec","Aquecer a voz",GOLD)]
    V=[("grito","Gritar",CORAL),("barulho","Falar no barulho",MUST),("pigarro","Pigarrear",CORAL),("frio","Ar-condicionado forte",LAV)]
    for i,(k,t,c) in enumerate(A): y=118+i*52; b.append(icon(k,70,y,c)+T(104,y+5,t,"l","start"))
    for i,(k,t,c) in enumerate(V): y=118+i*52; b.append(icon(k,380,y,c)+T(414,y+5,t,"l","start"))
    return svg(640,330,"".join(b))

def F_semaforo():
    b=[T(320,26,"O SEMÁFORO DA VOZ","t")]
    b.append(f'<rect x="60" y="50" width="110" height="270" rx="30" fill="{INK}"/>')
    rows=[(SAGE,"Verde: voz tranquila","Siga cantando e se cuidando."),(MUST,"Amarelo: atenção","Voz cansada ou rouca depois de usar muito: descanse, beba água."),("#C9473F","Vermelho: hora de pedir ajuda","Rouquidão por mais de 2 semanas, dor ou perda de voz: procure um fonoaudiólogo.")]
    for i,(c,t,d) in enumerate(rows):
        y=96+i*82; b.append(f'<circle cx="115" cy="{y}" r="30" fill="{c}"/>')
        b.append(T(200,y-6,t,"l","start"))
        words=d.split(); line="";lines=[]
        for w in words:
            if len(line+w)>46: lines.append(line); line=""
            line+=w+" "
        lines.append(line)
        for j,l in enumerate(lines): b.append(T(200,y+14+j*16,l.strip(),"s","start"))
    return svg(640,340,"".join(b))

def card(title,sub,inner,w=600,h=340):
    return svg(w,h,T(w/2,26,title,"t")+inner+T(w/2,h-30,sub,"s"))
def F_abelha():
    i=kid(170,50,.85,mouth="hum",arms="down",**LIA)
    i+=f'<g transform="translate(420,140)"><ellipse cx="0" cy="0" rx="40" ry="28" fill="{MUST}"/><path d="M-14 -26 L-14 26 M6 -28 L6 28" stroke="{INK}" stroke-width="8"/><ellipse cx="-8" cy="-34" rx="20" ry="13" fill="{WHITE}" opacity=".85" stroke="{INK}" stroke-width="1.5"/><ellipse cx="14" cy="-36" rx="18" ry="12" fill="{WHITE}" opacity=".85" stroke="{INK}" stroke-width="1.5"/><circle cx="34" cy="-4" r="4" fill="{INK}"/></g>'
    i+=f'<path d="M250 150 q 20 -16 40 0 q 20 16 40 0 q20 -16 40 0" stroke="{GOLD}" stroke-width="3" fill="none" stroke-dasharray="6 6"/>'
    return card("A ABELHINHA","Boca fechada, lábios soltos: “mmmmm”, como uma abelha voando.",i)
def F_motor():
    i=kid(170,50,.85,mouth="blow",arms="down",**THEO)
    i+=f'<g transform="translate(420,150)"><rect x="-70" y="-24" width="120" height="40" rx="18" fill="{CORAL}"/><circle cx="-40" cy="22" r="16" fill="{INK}"/><circle cx="30" cy="22" r="16" fill="{INK}"/><rect x="-30" y="-46" width="54" height="26" rx="8" fill="{CORAL}"/></g>'
    for k in range(3): i+=f'<path d="M{240+k*16} {130+k*10} q8 -6 16 0" stroke="{GOLD}" stroke-width="3" fill="none"/>'
    return card("O MOTORZINHO","Lábios soltos vibrando: “brrrr”, como um carrinho de brinquedo.",i)
def F_canudo():
    i=kid(220,50,.85,mouth="blow",arms="down",**BIA)
    i+=f'<path d="M226 120 L330 70" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"/><path d="M226 120 L330 70" stroke="{WHITE}" stroke-width="2" stroke-dasharray="8 8"/>'
    i+=f'<g transform="translate(420,170)"><path d="M-50 -60 L50 -60 L40 60 L-40 60 Z" fill="{WHITE}" stroke="{INK}" stroke-width="2.5"/><path d="M-46 -10 L46 -10 L40 60 L-40 60 Z" fill="{SAGE}" opacity=".6"/><circle cx="-14" cy="6" r="6" fill="{WHITE}"/><circle cx="10" cy="-2" r="4" fill="{WHITE}"/><circle cx="18" cy="18" r="5" fill="{WHITE}"/></g>'
    return card("O CANUDINHO","Cante uma melodia soprando por um canudo, com bolhas suaves na água.",i)
def F_sirene():
    i=kid(150,50,.85,mouth="o",arms="open",**THEO)
    i+=f'<path d="M260 230 C 320 230, 330 80, 400 80 C 470 80, 480 230, 540 230" stroke="{CORAL}" stroke-width="5" fill="none" stroke-linecap="round"/>'+arrow(520,224,540,230,CORAL,4)
    i+=T(400,64,"agudo","s")+T(270,256,"grave","s")+T(540,256,"grave","s")
    return card("A SIRENE","Deslize a voz do grave para o agudo e volte, sem pular e sem forçar.",i)
def F_bocejo():
    i=kid(200,50,.85,mouth="sing",arms="open",**BIA)
    i+=f'<path d="M300 110 q 30 -20 60 0" stroke="{LAV}" stroke-width="4" fill="none"/><path d="M310 140 q 30 -20 60 0" stroke="{LAV}" stroke-width="4" fill="none"/>'+T(430,120,"“aaaah...”","l","start")+T(430,140,"garganta aberta","s","start")+T(430,158,"e relaxada","s","start")
    return card("O BOCEJO","Boceje de verdade, sentindo a garganta abrir e a laringe descer.",i)
def F_escada():
    b=[T(320,26,"A ESCADA DOS SONS","t")]
    names=["dó","ré","mi","fá","sol"]
    for k,n in enumerate(names):
        x=80+k*96; y=260-k*40
        b.append(f'<rect x="{x}" y="{y}" width="96" height="{40*(k+1)}" fill="{[SAGE,MUST,CORAL,LAV,GOLD][k]}" opacity=".85"/>')
        b.append(T(x+48,y+26,n,"l"))
    b.append(kid(150,40,.55,mouth="sing",arms="open",**LIA))
    b.append(arrow(180,180,540,40,INK,2)+arrow(560,60,560,250,SOFT,2))
    b.append(T(320,312,"Suba e desça a escada com a voz, um degrau de cada vez.","s"))
    return svg(640,330,"".join(b))
def F_ouvido():
    b=[T(300,26,"OUVIR ANTES DE CANTAR","t")]
    b.append(f'<path d="M260 230 C 200 230, 190 160, 210 120 C 230 70, 300 60, 330 100 C 360 140, 330 170, 310 180 C 290 192, 300 220, 280 236 Z" fill="{PEACH}" stroke="{INK}" stroke-width="3"/><path d="M262 130 C 280 110, 310 120, 304 146 C 300 164, 276 160, 280 184" stroke="{INK}" stroke-width="3" fill="none"/>')
    for k in range(3): b.append(f'<path d="M{120-k*24} {120-k*14} q -20 40 0 80" stroke="{GOLD}" stroke-width="4" fill="none" transform="translate({k*0},0)"/>')
    b.append(note(70,110,CORAL)+note(110,200,LAV,.9))
    b.append(T(420,120,"1. Escute","l","start")+T(420,150,"2. Cante por dentro","l","start")+T(420,180,"3. Cante em voz alta","l","start")+T(420,210,"4. Compare","l","start"))
    return svg(600,270,"".join(b))

def F_faixas():
    names=["Dó","Ré","Mi","Fá","Sol","Lá","Si"]
    W=640; x0=30; wk=400/22
    b=[T(W/2,26,"ONDE A VOZ FICA CONFORTÁVEL","t")]
    rows=[("4 a 7 anos","Ré3 a Lá3 · cerca de 5 notas",1,5,SAGE),("8 a 12 anos","Dó3 a Ré4 · cerca de uma oitava",0,8,MUST),("12 a 17 anos","depende da muda",0,14,CORAL)]
    y=52
    for lab,sub,a,z,c in rows:
        xa=x0+a*wk; xz=x0+(z+1)*wk
        b.append(f'<rect x="{xa}" y="{y}" width="{xz-xa}" height="26" rx="13" fill="{c}"/>'+T(xz+10,y+13,lab,"l","start")+T(xz+10,y+29,sub,"s","start"))
        y+=46
    ky=y+10
    for i in range(22):
        b.append(f'<rect x="{x0+i*wk}" y="{ky}" width="{wk}" height="70" fill="{WHITE}" stroke="{INK}" stroke-width="1"/>')
    for i in range(21):
        if i%7 in (0,1,3,4,5): b.append(f'<rect x="{x0+i*wk+wk*0.66}" y="{ky}" width="{wk*0.66}" height="44" fill="{INK}" rx="1.5"/>')
    for i in range(0,22,7): b.append(T(x0+i*wk+wk/2,ky+88,"Dó"+str(3+i//7),"s"))
    b.append(T(W/2-60,ky+112,"Faixas aproximadas, em que o Dó3 é o Dó central do piano. Cada criança é única.","s"))
    return svg(W,ky+124,"".join(b))

def F_muda(boys=True):
    W=640;H=330
    b=[T(W/2,26,("A MUDA VOCAL NOS MENINOS" if boys else "A MUDA VOCAL NAS MENINAS"),"t")]
    x0,x1,y0,y1=90,600,60,260
    b.append(f'<path d="M{x0} {y0} L{x0} {y1} L{x1} {y1}" stroke="{INK}" stroke-width="2" fill="none"/>')
    b.append(T(x0-10,y0+10,"agudo","s","end")+T(x0-10,y1,"grave","s","end"))
    ages=["10","11","12","13","14","15","16","17"]
    for i,a in enumerate(ages):
        x=x0+20+i*((x1-x0-40)/7); b.append(T(x,y1+20,a,"s"))
    b.append(T((x0+x1)/2,y1+44,"idade (anos) · as idades variam de pessoa para pessoa","s"))
    def X(i): return x0+20+i*((x1-x0-40)/7)
    if boys:
        top=[86,90,104,140,160,164,166,168]; bot=[150,156,172,206,226,232,236,238]
    else:
        top=[84,86,90,96,100,102,102,102]; bot=[150,152,158,164,170,172,172,172]
    pts_top=" ".join(f"{X(i):.1f},{t}" for i,t in enumerate(top)); pts_bot=" ".join(f"{X(i):.1f},{t}" for i,t in reversed(list(enumerate(bot))))
    b.append(f'<polygon points="{pts_top} {pts_bot}" fill="{SAGE if boys else LAV}" opacity=".55"/>')
    b.append(f'<polyline points="{pts_top}" fill="none" stroke="{INK}" stroke-width="2"/>')
    if boys:
        b.append(f'<rect x="{X(2)-14}" y="{y0-6}" width="{X(5)-X(2)+28}" height="{y1-y0+6}" fill="{CORAL}" opacity=".12"/>'+T((X(2)+X(5))/2,y0+6,"fase de maior mudança","s"))
        b.append(arrow(X(1),112,X(6),196,GOLD,2.4)+T(X(6)+8,190,"desce cerca de","s","start")+T(X(6)+8,206,"uma oitava","s","start"))
    else:
        b.append(f'<rect x="{X(2)-14}" y="{y0-6}" width="{X(5)-X(2)+28}" height="{y1-y0+6}" fill="{CORAL}" opacity=".12"/>'+T((X(2)+X(5))/2,y0+6,"fase de maior mudança","s"))
        b.append(arrow(X(1),118,X(6),140,GOLD,2.4)+T(X(6)+8,150,"desce cerca de","s","start")+T(X(6)+8,166,"3 a 4 semitons","s","start"))
    b.append(T(W/2,H-4,"Esquema ilustrativo da extensão confortável: a faixa colorida.","s"))
    return svg(W,H,"".join(b))

figs={"lia":F_lia(),"theo":F_theo(),"bia":F_bia(),"turma":F_turma(),"casa-da-voz":F_casa(),"cortininhas":F_cortinas(),"balao":F_balao(),"arvore":F_arvore(),"termometro":F_termometro(),
"agua":F_agua(),"amigos-viloes":F_amigos(),"semaforo":F_semaforo(),"abelhinha":F_abelha(),"motorzinho":F_motor(),"canudinho":F_canudo(),"sirene":F_sirene(),"bocejo":F_bocejo(),"escada":F_escada(),
"muda-meninos":F_muda(True),"muda-meninas":F_muda(False),"faixas-idade":F_faixas(),"ouvido":F_ouvido()}
for n,s in figs.items(): open(f"img/{n}.svg","w",encoding="utf-8").write(s)
print(len(figs))
