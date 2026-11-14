import math, os
INK="#2B2622"; CREAM="#F7F0E4"; GOLD="#B8904A"; CORAL="#D9846E"; SAGE="#7FA58A"; MUST="#D9A945"; LAV="#9C8CC4"; PEACH="#F2CDAE"; SOFT="#6B625B"; WHITE="#FFFFFF"; ROSE="#E9A49A"; GRAY="#B9B4AE"; LGRAY="#E7E3DD"; NAVY="#4A4F5C"
FONT="font-family:Atkinson,Nunito,Arial,sans-serif"
def svg(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>text{{{FONT};fill:{INK}}} .t{{font-family:Fredoka,Nunito,sans-serif;font-size:21px;font-weight:600;fill:{INK};letter-spacing:.5px}} .l{{font-size:17px;font-weight:700}} .s{{font-size:15px;fill:{SOFT};font-weight:400}} .w{{fill:{WHITE}}}</style>{body}</svg>'
def T(x,y,t,cls="l",a="middle",fill=None): return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{a}"{(" style=\"fill:"+fill+"\"") if fill else ""}>{t}</text>'
def note(x,y,c=GOLD,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="7" ry="5.4" transform="rotate(-22)" fill="{c}"/><path d="M6 -2 L6 -30 Q16 -24 18 -14" stroke="{c}" stroke-width="2.6" fill="none" stroke-linecap="round"/></g>'
def arrow(x1,y1,x2,y2,c=GOLD,w=2.6):
    a=math.atan2(y2-y1,x2-x1);L=11
    return f'<path d="M{x1},{y1} L{x2},{y2} M{x2-L*math.cos(a-.5):.1f},{y2-L*math.sin(a-.5):.1f} L{x2},{y2} L{x2-L*math.cos(a+.5):.1f},{y2-L*math.sin(a+.5):.1f}" stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'

def adult(cx,top,s=1,skin="#E3B08C",hair=GRAY,hs="bob",shirt=CORAL,pants=NAVY,mouth="smile",arms="down",glasses=False,aid=False,seated=False,skirt=False,shoes=INK,beard=False):
    o=[f'<g transform="translate({cx},{top}) scale({s})" stroke-linecap="round" stroke-linejoin="round">']
    if hs=="bob": o.append(f'<path d="M-40 40 C-46 80,-44 104,-34 112 L34 112 C44 104,46 80,40 40 Z" fill="{hair}"/>')
    # legs
    if seated:
        o.append(f'<rect x="-52" y="214" width="104" height="14" rx="5" fill="{GOLD}"/><path d="M-44 228 L-48 320 M44 228 L48 320 M46 214 L52 120" stroke="{GOLD}" stroke-width="9"/>')
        o.append(f'<path d="M-18 216 L-58 218 L-60 306 M18 216 L-22 220 L-24 306" stroke="{pants}" stroke-width="22" fill="none"/>')
        o.append(f'<ellipse cx="-70" cy="310" rx="17" ry="8" fill="{shoes}"/><ellipse cx="-34" cy="310" rx="17" ry="8" fill="{shoes}"/>')
    else:
        if skirt:
            o.append(f'<path d="M-16 270 L-18 316 M16 270 L18 316" stroke="{skin}" stroke-width="13"/>')
            o.append(f'<path d="M-32 204 L-44 278 L44 278 L32 204 Z" fill="{pants}"/>')
        else:
            o.append(f'<path d="M-18 208 L-21 312 M18 208 L21 312" stroke="{pants}" stroke-width="22"/>')
        o.append(f'<ellipse cx="-24" cy="318" rx="17" ry="8" fill="{shoes}"/><ellipse cx="24" cy="318" rx="17" ry="8" fill="{shoes}"/>')
    # torso
    o.append(f'<path d="M-38 112 C-38 98,-24 92,0 92 C24 92,38 98,38 112 L34 214 L-34 214 Z" fill="{shirt}"/>')
    o.append(f'<path d="M-12 93 L0 108 L12 93" fill="{WHITE}" opacity=".35"/>')
    # arms
    S=shirt
    if arms=="down": o.append(f'<path d="M-34 104 L-44 190 M34 104 L44 190" stroke="{S}" stroke-width="18"/><circle cx="-44" cy="196" r="8" fill="{skin}"/><circle cx="44" cy="196" r="8" fill="{skin}"/>')
    elif arms=="open": o.append(f'<path d="M-34 106 L-60 150 L-84 118 M34 106 L60 150 L84 118" stroke="{S}" stroke-width="18" fill="none"/><circle cx="-86" cy="112" r="8" fill="{skin}"/><circle cx="86" cy="112" r="8" fill="{skin}"/>')
    elif arms=="belly": o.append(f'<path d="M-34 106 L-42 160 L-10 180 M34 106 L42 160 L10 180" stroke="{S}" stroke-width="18" fill="none"/><circle cx="-8" cy="180" r="8" fill="{skin}"/><circle cx="8" cy="176" r="8" fill="{skin}"/>')
    elif arms=="chest": o.append(f'<path d="M-34 106 L-44 190 M34 106 L44 150 L12 130" stroke="{S}" stroke-width="18" fill="none"/><circle cx="-44" cy="196" r="8" fill="{skin}"/><circle cx="8" cy="128" r="9" fill="{skin}"/>')
    elif arms=="folder": o.append(f'<path d="M-34 106 L-40 160 L-6 150 M34 106 L40 160 L6 150" stroke="{S}" stroke-width="18" fill="none"/><rect x="-30" y="118" width="60" height="44" rx="4" fill="{INK}"/><rect x="-24" y="124" width="48" height="32" rx="2" fill="{WHITE}" opacity=".9"/>')
    elif arms=="ear": o.append(f'<path d="M-34 104 L-44 190 M34 106 L48 130 L36 54" stroke="{S}" stroke-width="18" fill="none"/><circle cx="-44" cy="196" r="8" fill="{skin}"/><circle cx="36" cy="50" r="9" fill="{skin}"/>')
    elif arms=="lap": o.append(f'<path d="M-34 106 L-44 170 L-60 210 M34 106 L40 170 L-14 210" stroke="{S}" stroke-width="18" fill="none"/><circle cx="-62" cy="212" r="8" fill="{skin}"/><circle cx="-18" cy="212" r="8" fill="{skin}"/>')
    o.append(f'<rect x="-9" y="74" width="18" height="22" rx="7" fill="{skin}"/>')
    o.append(f'<ellipse cx="0" cy="44" rx="34" ry="38" fill="{skin}"/>')
    o.append(f'<ellipse cx="-34" cy="48" rx="6" ry="9" fill="{skin}"/><ellipse cx="34" cy="48" rx="6" ry="9" fill="{skin}"/>')
    if aid: o.append(f'<path d="M37 36 C46 36,46 56,38 58" stroke="{GOLD}" stroke-width="5" fill="none"/>')
    if hs=="bob": o.append(f'<path d="M-37 52 C-42 8,-12 -4,0 -2 C22 -4,42 10,37 52 C32 26,18 16,-2 16 C-16 18,-30 28,-37 52 Z" fill="{hair}"/>')
    elif hs=="bald": o.append(f'<path d="M-34 52 C-38 34,-36 22,-30 16 L-28 40 Z M34 52 C38 34,36 22,30 16 L28 40 Z" fill="{hair}"/><path d="M-26 12 C-14 4,14 4,26 12" stroke="{hair}" stroke-width="4" fill="none" opacity=".6"/>')
    elif hs=="wavy": o.append(f'<path d="M-38 60 C-46 6,-8 -6,6 -2 C34 0,46 22,38 60 C36 40,30 24,12 20 C2 30,-10 30,-18 22 C-28 30,-34 42,-38 60 Z" fill="{hair}"/>')
    elif hs=="bun": o.append(f'<circle cx="0" cy="-6" r="15" fill="{hair}"/><path d="M-36 48 C-38 10,-14 2,0 2 C18 2,40 12,36 48 C30 26,16 18,0 18 C-16 18,-30 26,-36 48 Z" fill="{hair}"/>')
    # face
    o.append(f'<circle cx="-12" cy="44" r="3.4" fill="{INK}"/><circle cx="12" cy="44" r="3.4" fill="{INK}"/>')
    o.append(f'<path d="M-20 32 q8 -4 15 0 M5 32 q8 -4 15 0" stroke="{hair if hs!="bald" else SOFT}" stroke-width="2.6" fill="none"/>')
    o.append(f'<path d="M-26 50 q2 4 0 7 M26 50 q-2 4 0 7" stroke="#b9805f" stroke-width="1.5" fill="none" opacity=".7"/>')
    o.append(f'<circle cx="-21" cy="58" r="5" fill="{ROSE}" opacity=".55"/><circle cx="21" cy="58" r="5" fill="{ROSE}" opacity=".55"/>')
    if glasses: o.append(f'<circle cx="-12" cy="44" r="9.5" fill="none" stroke="{INK}" stroke-width="2.2"/><circle cx="12" cy="44" r="9.5" fill="none" stroke="{INK}" stroke-width="2.2"/><path d="M-2.5 43 L2.5 43 M-21.5 42 L-32 40 M21.5 42 L32 40" stroke="{INK}" stroke-width="2"/>')
    if beard: o.append(f'<path d="M-14 58 Q0 52 14 58 Q8 62 0 61 Q-8 62 -14 58Z" fill="{hair}"/>')
    if mouth=="sing": o.append(f'<ellipse cx="0" cy="64" rx="6" ry="7.5" fill="#7a2f2a"/>')
    elif mouth=="smile": o.append(f'<path d="M-9 61 Q0 69 9 61" stroke="{INK}" stroke-width="2.8" fill="none"/>')
    elif mouth=="o": o.append(f'<circle cx="0" cy="64" r="4.5" fill="#7a2f2a"/>')
    elif mouth=="hum": o.append(f'<path d="M-7 64 L7 64" stroke="{INK}" stroke-width="2.8"/>')
    elif mouth=="calm": o.append(f'<path d="M-6 63 Q0 66 6 63" stroke="{INK}" stroke-width="2.6" fill="none"/>')
    o.append('</g>'); return "".join(o)

CELIA=dict(skin="#E6B894",hair="#D8D4CF",hs="bob",shirt=CORAL,pants=NAVY,skirt=True,glasses=True)
ANTONIO=dict(skin="#A8714C",hair="#E2DFDA",hs="bald",shirt=SAGE,pants="#5a5550",aid=True,beard=True)
MARTA=dict(skin="#D49A73",hair="#5b4032",hs="wavy",shirt=LAV,pants=INK)

def card(x,y,w,h,fill=WHITE,stroke=GOLD): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def halo(cx,cy,r,c): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity=".22"/>'

def F_celia(): return svg(340,360, halo(170,180,150,CORAL)+adult(170,24,1,mouth="sing",arms="chest",**CELIA)+note(270,90,GOLD)+note(60,120,CORAL,.9)+note(290,170,SAGE,.8))
def F_antonio(): return svg(340,360, halo(170,180,150,SAGE)+adult(170,24,1,mouth="o",arms="ear",**ANTONIO)+f'<path d="M232 60 q10 -8 20 0 q10 8 20 0 M236 84 q10 -8 20 0 q10 8 20 0" stroke="{GOLD}" stroke-width="3" fill="none"/>'+note(70,110,GOLD,.9))
def F_marta(): return svg(340,360, halo(170,180,150,LAV)+adult(170,24,1,mouth="sing",arms="open",**MARTA)+note(280,70,GOLD)+note(54,80,LAV,.9))
def F_grupo():
    b=halo(150,190,120,CORAL)+halo(320,180,130,SAGE)+halo(490,190,120,LAV)
    b+=adult(150,40,.92,mouth="sing",arms="chest",**CELIA)+adult(320,24,1,mouth="sing",arms="open",**ANTONIO)+adult(490,40,.92,mouth="sing",arms="open",**MARTA)
    for x,y,c,s in [(60,80,GOLD,1),(590,70,CORAL,1),(236,40,SAGE,.8),(410,30,LAV,.8)]: b+=note(x,y,c,s)
    return svg(640,360,b)

def F_voz_madura():
    b=[T(320,28,"A VOZ AO LONGO DA VIDA","t")]
    for i,(x,lab,sub,th,gap) in enumerate([(160,"Voz jovem","pregas mais cheias",16,2),(480,"Voz madura","pregas mais finas",9,9)]):
        b.append(card(x-140,50,280,250,WHITE))
        b.append(f'<ellipse cx="{x}" cy="160" rx="84" ry="70" fill="#f4dcd0" stroke="{CORAL}" stroke-width="2.5"/>')
        b.append(f'<path d="M{x-gap} 104 C{x-gap-th} 140,{x-gap-th} 180,{x-gap} 216" stroke="#e9b6a6" stroke-width="{th}" fill="none"/>')
        b.append(f'<path d="M{x+gap} 104 C{x+gap+th} 140,{x+gap+th} 180,{x+gap} 216" stroke="#e9b6a6" stroke-width="{th}" fill="none"/>')
        b.append(f'<path d="M{x-gap} 104 C{x-gap-th} 140,{x-gap-th} 180,{x-gap} 216 M{x+gap} 104 C{x+gap+th} 140,{x+gap+th} 180,{x+gap} 216" stroke="{CORAL}" stroke-width="1.6" fill="none"/>')
        b.append(T(x,256,lab)+T(x,280,sub,"s"))
    b.append(arrow(300,160,340,160,GOLD,3))
    b.append(T(320,332,"Com o tempo, o fechamento pode ficar menos completo: a voz tende a soar mais soprosa.","s"))
    b.append(T(320,354,"Esquema simplificado, visto de cima. Cada pessoa envelhece de um jeito.","s"))
    return svg(640,370,"".join(b))

def F_respiracao():
    b=[T(320,28,"POSTURA CONFORTÁVEL","t")]
    b.append(adult(180,60,.9,mouth="calm",arms="lap",seated=True,**CELIA))
    b.append(adult(470,50,.9,mouth="calm",arms="belly",**MARTA))
    b.append(T(160,375,"Sentado: pés no chão,","l")+T(160,396,"costas apoiadas se precisar","s"))
    b.append(T(470,375,"Em pé: joelhos soltos,","l")+T(470,396,"peso bem distribuído","s"))
    b.append(f'<path d="M520 190 q22 0 22 -22" stroke="{GOLD}" stroke-width="2.6" fill="none"/>'+T(552,160,"barriga","s","start")+T(552,178,"se expande","s","start"))
    b.append(f'<path d="M320 70 L320 390" stroke="{LGRAY}" stroke-width="2" stroke-dasharray="6 6"/>')
    return svg(640,410,"".join(b))

def F_audicao():
    b=[T(320,28,"ESCUTAR MELHOR PARA AFINAR MELHOR","t")]
    b.append(adult(150,60,.9,mouth="o",arms="ear",**ANTONIO))
    items=[("Fique perto do piano","ou de quem conduz"),("Prefira salas","com pouco eco e ruído"),("Use o aparelho auditivo","nos ensaios, se tiver"),("Avaliação auditiva","com fonoaudiólogo")]
    for i,(a,c) in enumerate(items):
        y=70+i*74
        b.append(card(300,y,300,60,WHITE,[GOLD,SAGE,CORAL,LAV][i]))
        b.append(f'<circle cx="328" cy="{y+30}" r="14" fill="{[GOLD,SAGE,CORAL,LAV][i]}"/>'+T(328,y+36,str(i+1),"l","middle",WHITE))
        b.append(T(354,y+26,a,"l","start")+T(354,y+47,c,"s","start"))
    return svg(640,380,"".join(b))

def icon(kind,x,y,c):
    if kind=="agua": return f'<path d="M{x} {y-26} C{x+18} {y-2},{x+18} {y+14},{x} {y+16} C{x-18} {y+14},{x-18} {y-2},{x} {y-26}Z" fill="{c}"/>'
    if kind=="sono": return f'<path d="M{x+8} {y-22} A22 22 0 1 0 {x+14} {y+14} A16 16 0 1 1 {x+8} {y-22}Z" fill="{c}"/>'
    if kind=="conversa": return f'<rect x="{x-24}" y="{y-20}" width="40" height="28" rx="10" fill="{c}"/><path d="M{x-14} {y+8} L{x-18} {y+18} L{x-4} {y+8}" fill="{c}"/><rect x="{x-6}" y="{y-6}" width="32" height="24" rx="9" fill="{c}" opacity=".6"/>'
    if kind=="ruido": return f'<path d="M{x-20} {y-8} L{x-8} {y-8} L{x+6} {y-20} L{x+6} {y+20} L{x-8} {y+8} L{x-20} {y+8}Z" fill="{c}"/><path d="M{x+12} {y-14} L{x+26} {y+14} M{x+26} {y-14} L{x+12} {y+14}" stroke="{c}" stroke-width="4"/>'
    if kind=="livro": return f'<path d="M{x} {y-14} C{x-10} {y-20},{x-22} {y-20},{x-26} {y-16} L{x-26} {y+16} C{x-22} {y+12},{x-10} {y+12},{x} {y+18} C{x+10} {y+12},{x+22} {y+12},{x+26} {y+16} L{x+26} {y-16} C{x+22} {y-20},{x+10} {y-20},{x} {y-14}Z" fill="{c}"/><path d="M{x} {y-14} L{x} {y+18}" stroke="{WHITE}" stroke-width="2"/>'
    if kind=="medico": return f'<rect x="{x-22}" y="{y-22}" width="44" height="44" rx="10" fill="{c}"/><path d="M{x} {y-12} L{x} {y+12} M{x-12} {y} L{x+12} {y}" stroke="{WHITE}" stroke-width="6"/>'
    return ""

def F_habitos():
    b=[T(320,28,"HÁBITOS QUE PROTEGEM A VOZ","t")]
    items=[("agua","Beber água","ao longo do dia",SAGE),("sono","Dormir bem","voz descansada",LAV),("conversa","Conversar","usar a voz faz bem",CORAL),
           ("ruido","Não gritar","sobre o barulho",GOLD),("livro","Ler em voz alta","alguns minutos",MUST),("medico","Consultas","em dia",SAGE)]
    for i,(k,a,c,col) in enumerate(items):
        x=30+(i%3)*200; y=52+(i//3)*150
        b.append(card(x,y,180,134,WHITE,col)+icon(k,x+90,y+44,col)+T(x+90,y+96,a)+T(x+90,y+118,c,"s"))
    return svg(640,350,"".join(b))

def F_aquecimento():
    b=[T(320,28,"AQUECIMENTO SUAVE · 10 MINUTOS","t")]
    steps=[("1","Corpo","ombros e pescoço","2 min",SAGE),("2","Respiração","suspiros leves","2 min",LAV),("3","Humming","“mmm” confortável","2 min",GOLD),
           ("4","Lábios e canudo","vibrar e soprar","2 min",CORAL),("5","Sirene suave","sobe e desce","1 min",MUST),("6","Vogais","frases curtas","1 min",SAGE)]
    for i,(n,a,c,t,col) in enumerate(steps):
        x=30+(i%3)*200; y=52+(i//3)*150
        b.append(card(x,y,180,134,WHITE,col)+f'<circle cx="{x+36}" cy="{y+36}" r="20" fill="{col}"/>'+T(x+36,y+43,n,"l","middle",WHITE)+T(x+164,y+42,t,"s","end"))
        b.append(T(x+90,y+90,a)+T(x+90,y+114,c,"s"))
    b.append(T(320,350,"Tudo pode ser feito sentado. Pare se sentir tontura ou desconforto.","s"))
    return svg(640,365,"".join(b))

def F_sinais():
    b=[card(20,20,600,330,"#FBF3EE",CORAL), T(320,56,"SINAIS PARA PROCURAR AVALIAÇÃO","t")]
    items=["Rouquidão que dura mais de 2 a 3 semanas","Dor ou ardor ao falar ou cantar","Falta de ar ao falar frases curtas","Engasgos frequentes ao comer ou beber","Perda súbita da voz","Tosse ou pigarro que não passa"]
    for i,t in enumerate(items):
        y=96+i*36
        b.append(f'<circle cx="62" cy="{y-6}" r="10" fill="{CORAL}"/>'+T(62,y-1,"!","l","middle",WHITE)+T(84,y,t,"l","start"))
    b.append(T(320,326,"Procure médico otorrinolaringologista e fonoaudiólogo.","l","middle",CORAL))
    return svg(640,370,"".join(b))

def F_extensao():
    b=[T(320,28,"SUA EXTENSÃO CONFORTÁVEL","t")]
    # keyboard
    x0=40; n=15; w=28
    for i in range(n):
        x=x0+i*w; inz=4<=i<=10
        b.append(f'<rect x="{x}" y="70" width="{w-2}" height="120" rx="3" fill="{"#EFE3C9" if inz else WHITE}" stroke="{GRAY}" stroke-width="1.4"/>')
    for i in range(n-1):
        if i%7 in (0,1,3,4,5):
            x=x0+i*w+w*0.66; b.append(f'<rect x="{x}" y="70" width="{w*0.62}" height="74" rx="2" fill="{INK}"/>')
    b.append(f'<path d="M{x0+4*w} 208 L{x0+11*w-2} 208" stroke="{GOLD}" stroke-width="5"/>')
    b.append(T(x0+7.5*w,236,"zona confortável","l")+T(x0+7.5*w,256,"a voz sai sem esforço","s"))
    b.append(T(x0+2*w,236,"evite forçar","s")+T(x0+13*w,236,"evite forçar","s"))
    b.append(adult(540,52,.62,mouth="sing",arms="open",**MARTA))
    b.append(T(320,290,"Comece no meio e explore aos poucos, semana após semana.","s"))
    return svg(640,310,"".join(b))

def F_coral():
    b=[T(320,28,"CORAL EM SEMICÍRCULO","t")]
    b.append(f'<path d="M80 300 Q320 140 560 300" stroke="{LGRAY}" stroke-width="40" fill="none"/>')
    people=[(110,220,CELIA,.5),(180,180,ANTONIO,.5),(250,160,MARTA,.5),(320,154,CELIA|{"shirt":MUST,"hair":"#cfc9c2","glasses":False},.5),(390,160,ANTONIO|{"shirt":LAV,"hs":"bob","hair":"#e8e4df","beard":False,"aid":False,"skirt":True,"pants":CORAL},.5),(460,180,MARTA|{"shirt":SAGE,"hair":"#9a9590"},.5),(530,220,CELIA|{"shirt":GOLD,"glasses":True,"skin":"#B87C55"},.5)]
    for x,y,p,s in people: b.append(adult(x,y-90,s,mouth="sing",arms="down",**p))
    b.append(f'<rect x="290" y="300" width="60" height="34" rx="6" fill="{INK}"/>'+T(320,356,"regente e piano à frente, ao alcance da visão e da audição","s"))
    b.append(note(80,90,GOLD)+note(560,80,CORAL))
    return svg(640,372,"".join(b))

def F_plano():
    b=[T(320,28,"CURSO DE 12 SEMANAS","t")]
    phases=[("1–3","Acolher","corpo, respiração, escuta",SAGE),("4–6","Explorar","extensão, afinação",GOLD),("7–9","Cantar","repertório, memória",CORAL),("10–12","Compartilhar","grupo, apresentação",LAV)]
    b.append(f'<path d="M60 120 L580 120" stroke="{LGRAY}" stroke-width="8" stroke-linecap="round"/>')
    for i,(s,a,c,col) in enumerate(phases):
        x=95+i*150
        b.append(f'<circle cx="{x}" cy="120" r="26" fill="{col}"/>'+T(x,126,s,"l","middle",WHITE))
        b.append(card(x-70,166,140,104,WHITE,col)+T(x,198,a)+T(x,222,c.split(", ")[0],"s")+T(x,242,c.split(", ")[1],"s"))
        b.append(T(x,84,f"Semanas","s"))
    b.append(T(320,300,"Cada fase revisa a anterior. O ritmo é do grupo, não do calendário.","s"))
    return svg(640,316,"".join(b))

FIGS={"celia":F_celia,"antonio":F_antonio,"marta":F_marta,"grupo":F_grupo,"voz-madura":F_voz_madura,"respiracao-sentado":F_respiracao,"audicao":F_audicao,"habitos":F_habitos,"aquecimento":F_aquecimento,"sinais":F_sinais,"extensao":F_extensao,"coral":F_coral,"plano":F_plano}
if __name__=="__main__":
    for k,f in FIGS.items(): open(f"/tmp/work/senior/img/{k}.svg","w").write(f())
    print(len(FIGS))
