import re
s=open('/tmp/work/en/build_en.py',encoding='utf-8').read()
R=[('TITLE="Voice, Singing and Science"','TITLE="Voz, Canto y Ciencia"'),
('SUB="Vocal health, vocal technique and inspiration: speech-language pathology applied to the singing and speaking voice"','SUB="Salud vocal, técnica vocal e inspiración: fonoaudiología aplicada a la voz cantada y hablada"'),
('AUTHOR="Dr. Brízia Lacerda"','AUTHOR="Dra. Brízia Lacerda"'),
('or "at the end of the book"','or "final"'),
('/tmp/work/en/part','/tmp/work/es/part'),
('"The vocal apparatus: from the lungs to the lips, every structure involved in producing the voice."','"El aparato fonador: de los pulmones a los labios, todas las estructuras que participan en la producción de la voz."'),
('"The source–filter model: the vocal folds generate the basic sound, and the vocal tract turns it into the voice we hear."','"El modelo fuente-filtro: los pliegues vocales generan el sonido básico y el tracto vocal lo transforma en la voz que oímos."'),
('"On inhalation, the diaphragm descends and the ribs open; on exhalation, the diaphragm relaxes and rises."','"En la inspiración, el diafragma desciende y las costillas se abren; en la espiración, el diafragma se relaja y sube."'),
('"The larynx seen from the front: hyoid bone, thyroid and cricoid cartilages, and the top of the trachea."','"La laringe vista de frente: hueso hioides, cartílagos tiroides y cricoides y el inicio de la tráquea."'),
('"The Starting Position: ear, shoulder, hip, knee and ankle in line, with your back against the wall."','"El Punto de Partida: oreja, hombro, cadera, rodilla y tobillo alineados, con la espalda apoyada en la pared."'),
('"In the cricothyroid tilt, the cricothyroid muscle tips the thyroid cartilage forward and lengthens the vocal folds."','"En el movimiento de báscula, el músculo cricotiroideo inclina el cartílago tiroides y alarga los pliegues vocales."'),
('"Frequency and intensity: pitch depends on frequency; loudness, on the amplitude of vibration."','"Frecuencia e intensidad: la altura depende de la frecuencia; el volumen, de la amplitud de la vibración."'),
('"In fry, the glottal pulses become widely spaced and irregular."','"En el fry, los pulsos glóticos se vuelven espaciados e irregulares."'),
('"Twang: a raised tongue base, aryepiglottic constriction and a sensation of brightness in the face."','"El twang: base de la lengua elevada, constricción ariepiglótica y sensación de brillo en la cara."'),
('"The yodel deliberately alternates between the modal and elevated registers."','"El yodel alterna intencionalmente los registros modal y elevado."'),
('"Vibrato: a regular oscillation of frequency around the note."','"El vibrato: una oscilación regular de la frecuencia en torno a la nota."'),
('"In a melisma, a single syllable travels through several notes."','"En el melisma, una sola sílaba recorre varias notas."'),
('"The appoggiatura: a neighboring note that precedes and enhances the main note."','"La apoyatura: una nota vecina que antecede y realza la nota principal."'),
("Audio for this exercise available for download · see page {AUD}","Audio de este ejercicio disponible para descargar · ver página {AUD}"),
('"for this exercise","for the cool-down exercises"','"de este ejercicio","de los ejercicios de enfriamiento"'),
("' See the cricothyroid tilt in Chapter 10.'","' Consulta el movimiento de báscula en el Capítulo 10.'"),
('<div class="ch-k">Chapter {num}</div>','<div class="ch-k">Capítulo {num}</div>'),
('<span class="chapter-num">Chapter (\\d+)</span>','<span class="chapter-num">Capítulo (\\d+)</span>'),
('f"Chapter {n} · {CH[n]}"','f"Capítulo {n} · {CH[n]}"'),
('"No singing exercise should ever be uncomfortable."','"Ningún ejercicio de canto debe ser incómodo."'),
('"Air is the fuel of voice production."','"El aire es el combustible de la producción de la voz."'),
('"Timbre is the personality of the voice."','"El timbre es la personalidad de la voz."'),
('"A vocal signature is as unique as a fingerprint."','"La huella vocal es como la huella digital."'),
('"Learning to sing is, first of all, learning to breathe."','"Aprender a cantar es, ante todo, aprender a respirar."'),
('"The voice exists only when the breath from the lungs provides enough pressure to give birth to the laryngeal sound — and to sustain it."','"La voz solo existe a partir del momento en que la espiración pulmonar aporta la presión suficiente para hacer nacer y mantener el sonido laríngeo."'),
('"Always leave yourself the feeling that you could give a little more."','"Hay que tener siempre la impresión de que se puede dar más."'),
('"Vibrato gives the voice expressive richness and great emotional power."','"El vibrato ofrece a la voz una riqueza expresiva de gran poder emocional."'),
('"Every person is unique — and will reach unique sound colors and effects."','"Cada persona es única y alcanzará colores de sonido y efectos únicos."'),
('"The voice serves the text."','"La voz está al servicio del texto."'),
('About This Book</span>','Sobre este libro</span>'),('About the Author</span>','Sobre la autora</span>'),('<span>References</span>','<span>Referencias</span>'),('<span>Exercise Audio</span>','<span>Audios de los ejercicios</span>'),
('lang="en"','lang="es"'),('book_en.css','book_es.css'),('book_en.html','book_es.html'),
('<small>DR. BRÍZIA LACERDA</small>','<small>DRA. BRÍZIA LACERDA</small>'),
('Speech-language pathologist · Voice specialist · Singer · Vocal coach','Fonoaudióloga · Especialista en voz · Cantante · Vocal coach'),
('<div class="k">Dr. Brízia Lacerda</div><div class="t">Voice,<br>Singing<br><i>and Science</i></div>','<div class="k">Dra. Brízia Lacerda</div><div class="t">Voz,<br>Canto<br><i>y Ciencia</i></div>'),
('SPEECH-LANGUAGE PATHOLOGY APPLIED TO THE VOICE','FONOAUDIOLOGÍA APLICADA A LA VOZ'),
('>Singers are their own instrument.<','>El cantante hace de sí mismo su instrumento.<'),
('<h1>Contents</h1>','<h1>Índice</h1>'),
]
for a,b in R:
    assert a in s, a[:60]; s=s.replace(a,b)
def block(name,new):
    global s
    m=re.search(name+r"=f?'''.*?'''",s,re.S); assert m, name
    s=s[:m.start()]+new+s[m.end():]
for name in ("SOBRE_LIVRO","SOBRE_AUTORA","CREDITOS","AUDIOS","REFSR"):
    pass
FB=open('/tmp/work/es/frontmatter_es.py',encoding='utf-8').read()
blocks=dict(re.findall(r"#--(\w+)\n(.*?)\n#--end",FB,re.S))
for k,v in blocks.items():
    if k=="R":
        m=re.search(r"R=\[\(.*?\n\]\n",s,re.S); assert m; s=s[:m.start()]+v+"\n"+s[m.end():]
    else: block(k,v)
open('/tmp/work/es/build_es.py','w',encoding='utf-8').write(s)
p=open('/tmp/work/en/pages_en.py',encoding='utf-8').read()
for a,b in [('book_en.pdf','book_es.pdf'),('"contents" in t[:30]','"índice" in t[:30]'),('"aboutthisbook"','"sobreestelibro"'),('t.startswith("theauthor")','t.startswith("laautora")'),('f"{N:02d}chapter{N}"','f"{N:02d}capítulo{N}"'),('"references" in t[:30]','"referencias" in t[:30]'),('"exerciseaudio"','"audiosdelosejercicios"')]:
    assert a in p,a; p=p.replace(a,b)
open('/tmp/work/es/pages_es.py','w',encoding='utf-8').write(p)
r=open('/tmp/work/en/render_en.js',encoding='utf-8').read().replace('/tmp/work/en/','/tmp/work/es/').replace('book_en','book_es')
open('/tmp/work/es/render_es.js','w',encoding='utf-8').write(r)
print("ok")
