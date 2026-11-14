import math
G="#B8904A"; GL="#D9B26A"; INK="#1E1B19"; SOFT="#6B625B"; CREAM="#F7F0E4"; LG="#E6DCCB"
def svg(w,h,body,dark=False):
    tc=CREAM if dark else INK
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><style>text{{font-family:Lora,serif;fill:{tc}}} .t{{font-size:15px;letter-spacing:4px;font-weight:600;fill:{G}}} .l{{font-size:17px;font-weight:600}} .s{{font-size:14.5px;fill:{SOFT if not dark else "#cfc6b8"};font-style:italic}} .n{{font-family:Bodoni,serif;font-size:30px;fill:{G}}}</style><g fill="none" stroke="{G}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{body[0]}</g>{body[1]}</svg>'
def T(x,y,t,c="l",a="middle"): return f'<text class="{c}" x="{x}" y="{y}" text-anchor="{a}">{t}</text>'
def note(x,y,s=1): return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="6" ry="4.5" transform="rotate(-22)" fill="{G}" stroke="none"/><path d="M5 -2 L5 -26 Q14 -20 15 -12"/></g>'
def sil(cx,top,s=1,pose="stand",arms="down"):
    o=f'<g transform="translate({cx},{top}) scale({s})">'
    o+='<circle cx="0" cy="22" r="18"/><path d="M-6 40 L-6 50 M6 40 L6 50"/>'
    o+='<path d="M-34 66 C-34 54,-20 50,0 50 C20 50,34 54,34 66"/>'
    if pose=="stand":
        o+='<path d="M-30 66 L-26 170 L26 170 L30 66"/><path d="M-16 170 L-18 270 M16 170 L18 270 M-18 270 L-30 274 M18 270 L30 274"/>'
    else:
        o+='<path d="M-30 66 L-26 166 L26 166 L30 66"/><path d="M-22 166 L-80 168 L-82 250 M18 166 L-44 170 L-46 250 M-82 250 L-94 254 M-46 250 L-58 254"/>'
    if arms=="down": o+='<path d="M-34 66 L-46 160 M34 66 L46 160"/>'
    elif arms=="belly": o+='<path d="M-34 66 L-44 120 L-8 136 M34 66 L44 120 L8 136"/>'
    elif arms=="open": o+='<path d="M-34 66 L-62 110 L-86 82 M34 66 L62 110 L86 82"/>'
    elif arms=="mic": o+='<path d="M-34 66 L-46 160 M34 66 L44 112 L14 70"/><path d="M8 62 L18 76"/><circle cx="6" cy="58" r="6"/>'
    elif arms=="lap": o+='<path d="M-34 66 L-42 130 L-70 160 M34 66 L38 130 L-30 162"/>'
    return o+'</g>'
def chair(x,y,s=1): return f'<g transform="translate({x},{y}) scale({s})"><path d="M-10 0 L60 0 M-6 0 L-10 90 M56 0 L60 90 M60 0 L64 -110"/></g>'

def F_voz_madura():
    a=[];t=[T(320,26,"A VOZ NA MATURIDADE","t")]
    for x,lab,sub,th,gap in [(170,"Antes","pregas mais volumosas",12,3),(470,"Com o tempo","pregas mais finas",5,10)]:
        a.append(f'<ellipse cx="{x}" cy="160" rx="96" ry="84"/><ellipse cx="{x}" cy="160" rx="80" ry="70" stroke="{LG}"/>')
        a.append(f'<path d="M{x-gap} 96 C{x-gap-th} 136,{x-gap-th} 186,{x-gap} 226 M{x+gap} 96 C{x+gap+th} 136,{x+gap+th} 186,{x+gap} 226" stroke-width="2.4"/>')
        a.append(f'<path d="M{x-gap-th*1.6} 110 C{x-gap-th*2.6} 150,{x-gap-th*2.6} 175,{x-gap-th*1.6} 212 M{x+gap+th*1.6} 110 C{x+gap+th*2.6} 150,{x+gap+th*2.6} 175,{x+gap+th*1.6} 212" stroke="{LG}"/>')
        t.append(T(x,284,lab)+T(x,306,sub,"s"))
    a.append('<path d="M290 160 L345 160 M335 152 L345 160 L335 168"/>')
    t.append(T(320,346,"O fechamento pode ficar menos completo e a voz, um pouco mais soprosa.","s"))
    t.append(T(320,368,"Esquema simplificado, visto de cima. Cada voz muda de um jeito.","s"))
    return svg(640,380,("".join(a),"".join(t)))

def F_postura():
    a=[sil(200,60,1,"seat","lap"),chair(165,226,1),sil(460,60,1,"stand","belly")]
    a.append(f'<path d="M200 50 L200 340 M460 50 L460 340" stroke="{LG}" stroke-dasharray="5 7"/>')
    a.append('<path d="M500 186 q24 0 24 -24"/>')
    t=[T(320,26,"POSTURA PARA CANTAR","t"),T(170,372,"Sentado: pés no chão"),T(170,394,"costas longas, ombros soltos","s"),T(460,372,"Em pé: joelhos soltos"),T(460,394,"peso bem distribuído","s"),T(532,158,"o ar","s","start"),T(532,176,"expande","s","start")]
    return svg(640,410,("".join(a),"".join(t)))

def F_escuta():
    a=[]
    a.append('<path d="M150 90 C110 90,92 126,96 160 C100 196,120 200,124 226 C128 250,150 262,168 248 C182 236,170 214,182 200 C206 170,214 132,196 108 C186 96,170 90,150 90 Z"/><path d="M150 120 C132 122,124 140,132 156 C138 168,152 166,152 180"/>')
    for r in (40,62,84): a.append(f'<path d="M{236} {170-r} A{r} {r} 0 0 1 {236} {170+r}" transform="translate(-30,0)"/>')
    tips=[("Perto do piano","ou de quem conduz o grupo"),("Sala com pouco eco","e pouco ruído de fundo"),("Aparelho auditivo","use nos ensaios, se tiver"),("Exame de audição","com otorrino e fonoaudiólogo")]
    t=[T(320,26,"OUVIR PARA AFINAR","t")]
    for i,(x,y) in enumerate(tips):
        yy=74+i*72; a.append(f'<circle cx="338" cy="{yy}" r="17"/><path d="M366 {yy+30} L610 {yy+30}" stroke="{LG}"/>')
        t.append(f'<text class="n" x="338" y="{yy+10}" text-anchor="middle" style="font-size:22px">{i+1}</text>'+T(370,yy-2,x,"l","start")+T(370,yy+19,y,"s","start"))
    return svg(640,370,("".join(a),"".join(t)))

def icon(k,x,y):
    if k=="gota": return f'<path d="M{x} {y-28} C{x+20} {y-2},{x+20} {y+16},{x} {y+18} C{x-20} {y+16},{x-20} {y-2},{x} {y-28}Z"/>'
    if k=="lua": return f'<path d="M{x+8} {y-24} A24 24 0 1 0 {x+16} {y+14} A17 17 0 1 1 {x+8} {y-24}Z"/>'
    if k=="fala": return f'<path d="M{x-26} {y-18} h40 a8 8 0 0 1 8 8 v16 a8 8 0 0 1 -8 8 h-26 l-10 10 v-10 h-4 a8 8 0 0 1 -8 -8 v-16 a8 8 0 0 1 8 -8z"/>'
    if k=="ruido": return f'<path d="M{x-24} {y-8} h12 l14 -14 v44 l-14 -14 h-12 z M{x+12} {y-12} l16 24 M{x+28} {y-12} l-16 24"/>'
    if k=="livro": return f'<path d="M{x} {y-14} C{x-10} {y-22},{x-24} {y-22},{x-28} {y-16} V{y+18} C{x-24} {y+12},{x-10} {y+12},{x} {y+20} C{x+10} {y+12},{x+24} {y+12},{x+28} {y+18} V{y-16} C{x+24} {y-22},{x+10} {y-22},{x} {y-14} Z M{x} {y-14} V{y+20}"/>'
    if k=="cruz": return f'<rect x="{x-24}" y="{y-24}" width="48" height="48" rx="10"/><path d="M{x} {y-12} V{y+12} M{x-12} {y} H{x+12}"/>'
def F_habitos():
    a=[];t=[T(320,26,"HÁBITOS QUE PROTEGEM A VOZ","t")]
    items=[("gota","Água","ao longo do dia"),("lua","Sono","voz descansada"),("fala","Conversar","sem competir com o barulho"),("ruido","Sem gritar","em festas e eventos"),("livro","Ler em voz alta","alguns minutos por dia"),("cruz","Consultas","em dia")]
    for i,(k,a1,b1) in enumerate(items):
        x=110+(i%3)*210; y=96+(i//3)*150
        a.append(f'<circle cx="{x}" cy="{y}" r="44" stroke="{LG}"/>'+icon(k,x,y)); t.append(T(x,y+72,a1)+T(x,y+93,b1,"s"))
    return svg(640,360,("".join(a),"".join(t)))

def F_aquecimento():
    st=[("Corpo","ombros e pescoço","2 min"),("Respiração","suspiros leves","2 min"),("Humming","“mmm” confortável","2 min"),("Lábios e canudo","vibrar e soprar","2 min"),("Sirenes","sobe e desce suave","1 min"),("Vogais","frases curtas","1 min")]
    a=[];t=[T(320,26,"AQUECIMENTO EM 10 MINUTOS","t")]
    for i,(x1,y1,m) in enumerate(st):
        x=40+(i%3)*200; y=70+(i//3)*96
        a.append(f'<circle cx="{x+26}" cy="{y+26}" r="24"/><path d="M{x+60} {y+62} L{x+186} {y+62}" stroke="{LG}"/>')
        t.append(f'<text class="n" x="{x+26}" y="{y+35}" text-anchor="middle" style="font-size:24px">{i+1}</text>'+T(x+62,y+20,x1,"l","start")+T(x+62,y+42,y1,"s","start")+T(x+26,y+74,m,"s"))
    t.append(T(320,282,"Tudo pode ser feito sentado. Pare diante de tontura ou desconforto.","s"))
    return svg(640,296,("".join(a),"".join(t)))

def F_extensao():
    a=[];t=[T(320,26,"SUA EXTENSÃO CONFORTÁVEL","t")]
    x0=70;n=18;w=28
    for i in range(n):
        x=x0+i*w; z=5<=i<=12
        a.append(f'<rect x="{x}" y="60" width="{w}" height="130" {"fill=\"#F1E3C4\"" if z else ""}/>')
    for i in range(n-1):
        if i%7 in (0,1,3,4,5): a.append(f'<rect x="{x0+i*w+w*0.66}" y="60" width="{w*0.66}" height="80" fill="{INK}" stroke="{INK}"/>')
    a.append(f'<path d="M{x0+5*w} 214 L{x0+13*w} 214" stroke-width="4"/><path d="M{x0+5*w} 206 V222 M{x0+13*w} 206 V222"/>')
    t.append(T(x0+9*w,246,"zona confortável")+T(x0+9*w,268,"onde a voz sai sem esforço","s")+T(x0+2.5*w,246,"explore aos poucos","s")+T(x0+15.5*w,246,"explore aos poucos","s"))
    return svg(640,290,("".join(a),"".join(t)))

def F_sinais():
    items=["Rouquidão que dura mais de 2 a 3 semanas","Dor ou ardor ao falar ou cantar","Falta de ar ao falar frases curtas","Engasgos frequentes ao comer ou beber","Perda súbita da voz","Tosse ou pigarro que não passa"]
    a=[f'<rect x="20" y="16" width="600" height="356" rx="6"/><rect x="28" y="24" width="584" height="340" rx="3" stroke="{LG}"/>'];t=[T(320,62,"SINAIS PARA PROCURAR UM PROFISSIONAL","t")]
    for i,s in enumerate(items):
        y=104+i*38; a.append(f'<circle cx="72" cy="{y-6}" r="11"/><path d="M72 {y-12} V{y-5} M72 {y-1} V{y}"/>'); t.append(T(96,y,s,"l","start"))
    t.append(T(320,344,"Procure um otorrinolaringologista e um fonoaudiólogo.","s"))
    return svg(640,386,("".join(a),"".join(t)))

def mic(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-22" y="-60" width="44" height="74" rx="22"/><path d="M-22 -30 H22 M-22 -16 H22 M-22 -44 H22" stroke="{LG}"/><path d="M-34 -14 C-34 22,34 22,34 -14"/><path d="M0 16 V60 M-24 60 H24"/></g>'
def F_palco():
    a=[f'<path d="M150 20 L60 330 M150 20 L300 330" stroke="{LG}"/><path d="M490 20 L340 330 M490 20 L580 330" stroke="{LG}"/>',f'<path d="M40 330 H600"/>',mic(320,200,1.5)+'<path d="M320 290 V330 M290 330 L320 296 L350 330"/>']
    for x,y,r in [(120,90,6),(520,110,5),(200,180,4),(450,200,4),(560,240,3)]: a.append(f'<path d="M{x} {y-r*2} V{y+r*2} M{x-r*2} {y} H{x+r*2}"/>')
    a.append(note(250,120,1.1)+note(400,100,1))
    return svg(640,350,("".join(a),T(320,346+0,"","s")))

def F_grupo():
    a=[]
    for i in range(9):
        ang=math.radians(200+i*17.5); x=320+250*math.cos(ang)*-1; y=300+170*math.sin(ang)
        x=320-250*math.cos(math.radians(i*22.5)); y=290-150*math.sin(math.radians(i*22.5))
        a.append(f'<circle cx="{x:.0f}" cy="{y-30:.0f}" r="15"/><path d="M{x-28:.0f} {y+12:.0f} C{x-28:.0f} {y-6:.0f},{x+28:.0f} {y-6:.0f},{x+28:.0f} {y+12:.0f}"/>')
    a.append(f'<circle cx="320" cy="300" r="15" fill="{G}"/><path d="M292 342 C292 322,348 322,348 342" stroke-width="2.4"/>')
    a.append(note(210,110,1)+note(430,100,1)+note(320,80,.9))
    return svg(640,360,("".join(a),T(320,26,"CANTAR EM GRUPO","t")+T(320,358,"","s")))

def F_estudio():
    a=[]
    a.append('<path d="M70 200 C70 100,230 100,230 200"/><rect x="56" y="190" width="34" height="62" rx="12"/><rect x="210" y="190" width="34" height="62" rx="12"/>')
    a.append(mic(320,170,1.3)+f'<circle cx="320" cy="120" r="46" stroke="{LG}"/><path d="M320 248 V300 M290 300 H350"/>')
    a.append('<rect x="440" y="90" width="120" height="210" rx="18"/><path d="M480 104 H520"/>')
    for i,h in enumerate([10,24,40,18,52,30,14,36,22,8]): a.append(f'<path d="M{458+i*10} {200-h/2} V{200+h/2}"/>')
    a.append(f'<circle cx="500" cy="262" r="14"/><circle cx="500" cy="262" r="6" fill="{G}"/>')
    t=T(320,26,"GRAVAR A SUA VOZ","t")+T(150,290,"fones em volume seguro","s")+T(320,330,"microfone","s")+T(500,330,"o celular já grava bem","s")
    return svg(640,346,("".join(a),t))

def F_plano():
    ph=[("1–3","Acolher","corpo, respiração, escuta"),("4–6","Explorar","extensão e afinação"),("7–9","Cantar","repertório e memória"),("10–12","Celebrar","grupo e sarau final")]
    a=['<path d="M80 110 L560 110"/>'];t=[T(320,26,"CURSO DE 12 SEMANAS","t")]
    for i,(s,n,d) in enumerate(ph):
        x=110+i*140; a.append(f'<circle cx="{x}" cy="110" r="34" fill="{CREAM}"/>')
        t.append(f'<text class="n" x="{x}" y="118" text-anchor="middle" style="font-size:21px">{s}</text>'+T(x,66,"semanas","s")+T(x,180,n)+T(x,202,d.split(" ")[0]+(" "+d.split(" ")[1] if len(d.split(" "))>3 else ""),"s")+T(x,222," ".join(d.split(" ")[2:] if len(d.split(" "))>3 else d.split(" ")[1:]),"s"))
    t.append(T(320,268,"Cada fase revisa a anterior. O ritmo é do grupo, não do calendário.","s"))
    return svg(640,282,("".join(a),"".join(t)))

# openers: gold on transparent, for black pages
def OP(n):
    a=[]
    if n==1:
        a.append(mic(250,250,3.2)+'<path d="M250 450 V520"/>')
        for r in (150,200,250): a.append(f'<path d="M{250+r*0.6} {170-r*0.5} A{r} {r} 0 0 1 {250+r*0.6} {170+r*0.5}" stroke-width="1.6"/>')
    if n==2:
        a.append('<path d="M40 260 C120 120,180 400,260 260 S400 120,460 260" stroke-width="2.4"/><path d="M40 300 C120 160,180 440,260 300 S400 160,460 300" stroke-width="1.4" opacity=".6"/><path d="M40 220 C120 80,180 360,260 220 S400 80,460 220" stroke-width="1.4" opacity=".6"/>')
    if n==3:
        for i in range(5): a.append(f'<path d="M30 {180+i*28} H470" stroke-width="1.4"/>')
        a.append('<path d="M150 380 C120 380,118 340,148 338 C176 336,180 380,150 384 C100 392,80 300,140 250 C180 214,190 170,170 130 C150 100,128 140,140 190 L170 420 C176 450,140 460,130 440" stroke-width="2.6"/>')
        a.append(note(280,262,2)+note(360,234,2)+note(430,290,2))
    if n==4:
        a.append('<path d="M60 40 L20 460 M60 40 L190 460 M440 40 L310 460 M440 40 L480 460 M250 20 L170 460 M250 20 L330 460" stroke-width="1.4"/><path d="M10 460 H490" stroke-width="2.4"/>')
        a.append(mic(250,380,1.3))
    if n==5:
        a.append('<path d="M250 80 C330 200,350 270,350 320 C350 380,305 420,250 420 C195 420,150 380,150 320 C150 270,170 200,250 80 Z" stroke-width="2.4"/><path d="M200 330 C205 360,225 380,250 384" stroke-width="1.6"/>')
    if n==6:
        a.append('<path d="M250 200 C200 170,110 170,60 190 V420 C110 400,200 400,250 430 C300 400,390 400,440 420 V190 C390 170,300 170,250 200 Z M250 200 V430" stroke-width="2.2"/>')
        a.append(note(170,150,1.8)+note(320,120,1.8))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 520" width="500" height="520"><g fill="none" stroke="{GL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{"".join(a)}</g></svg>'

FIGS={"voz-madura":F_voz_madura,"postura":F_postura,"escuta":F_escuta,"aquecimento":F_aquecimento,"extensao":F_extensao,"habitos":F_habitos,"sinais":F_sinais,"palco":F_palco,"grupo":F_grupo,"estudio":F_estudio,"plano":F_plano}
if __name__=="__main__":
    for k,f in FIGS.items(): open(f"/tmp/work/vez/img/{k}.svg","w").write(f())
    for n in range(1,7): open(f"/tmp/work/vez/img/op{n}.svg","w").write(OP(n))
    print("ok")
