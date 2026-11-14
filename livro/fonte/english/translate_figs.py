import re,glob,os
M={
'O APARELHO FONADOR':'THE VOCAL APPARATUS','Cavidade nasal':'Nasal cavity','Palato':'Palate','Cavidade oral e língua':'Oral cavity and tongue','Faringe':'Pharynx','Epiglote':'Epiglottis','Laringe e pregas vocais':'Larynx and vocal folds','Traqueia':'Trachea','Pulmões':'Lungs','Diafragma':'Diaphragm',
'APOGIATURA: A NOTA VIZINHA QUE ORNAMENTA':'APPOGGIATURA: THE NEIGHBORING NOTE THAT ADORNS','nota vizinha':'neighboring note','nota principal':'main note','a mesma nota, sem ornamento':'the same note, unornamented','A apogiatura “apoia” a nota principal a partir de um intervalo de segunda.':'The appoggiatura “leans” on the main note from a step above or below.',
'TENSÃO E ALONGAMENTO: O MOVIMENTO DE BÁSCULA':'TENSION AND LENGTHENING: THE CRICOTHYROID TILT','Repouso':'At rest','pregas vocais mais curtas · sons graves':'shorter vocal folds · lower pitches','Báscula':'Tilted','a tireoide inclina para a frente · pregas alongadas · agudos':'the thyroid tilts forward · longer folds · higher pitches','cartilagem tireoide':'thyroid cartilage','cricoide':'cricoid','aritenoide':'arytenoid','prega':'vocal','vocal':'fold','músculo cricotireóideo':'cricothyroid muscle',
'O CICLO GLÓTICO':'THE GLOTTIC CYCLE','vista superior · a frente da laringe está para cima':'seen from above · the front of the larynx faces up','Fase fechada':'Closed phase','Fase de abertura':'Opening phase','Fase aberta':'Open phase','Fase de fechamento':'Closing phase',
'QUOCIENTE DE FECHAMENTO (CQ)':'CLOSED QUOTIENT (CQ)','Canto lírico':'Classical singing','parte do ciclo glótico em que as pregas vocais permanecem fechadas':'share of the glottic cycle during which the vocal folds stay closed',
'DIAFRAGMA: INSPIRAÇÃO E EXPIRAÇÃO':'THE DIAPHRAGM: INHALATION AND EXHALATION','ar entra':'air in','Inspiração':'Inhalation','diafragma desce e se achata':'the diaphragm descends and flattens','ar sai':'air out','Expiração':'Exhalation','diafragma relaxa e sobe':'the diaphragm relaxes and rises',
'EXTENSÃO APROXIMADA DAS VOZES':'APPROXIMATE VOICE RANGES','Barítono':'Baritone','Baixo':'Bass','DO1':'C2','DO2':'C3','DO3':'C4','DO4':'C5','DO5':'C6',
'FONTE E FILTRO: COMO NASCE A VOZ':'SOURCE AND FILTER: HOW VOICE IS BORN','Fonte':'Source','as pregas vocais vibram:':'the vocal folds vibrate:','um som “cru”, como um zumbido':'a “raw” sound, like a buzz','Filtro':'Filter','faringe, boca e nariz':'pharynx, mouth and nose','amplificam e moldam o som':'amplify and shape the sound','Voz':'Voice','o som rico em harmônicos':'the harmonically rich sound','que chega ao ouvinte':'that reaches the listener',
'REGISTRO MODAL E FRY':'MODAL REGISTER AND FRY','pulsos regulares e próximos':'regular, closely spaced pulses','pulsos espaçados e irregulares':'widely spaced, irregular pulses',
'A LARINGE EM CORTE':'THE LARYNX IN CROSS-SECTION','SUPRAGLOTE':'SUPRAGLOTTIS','acima das pregas vocais':'above the vocal folds','GLOTE':'GLOTTIS','entre as pregas vocais':'between the vocal folds','INFRAGLOTE':'INFRAGLOTTIS','abaixo das pregas vocais':'below the vocal folds','epiglote':'epiglottis','corte lateral esquemático':'schematic side section',
'A LARINGE VISTA DE FRENTE':'THE LARYNX, FRONT VIEW','Osso hioide':'Hyoid bone','Membrana tireo-hióidea':'Thyrohyoid membrane','Proeminência (pomo de Adão)':'Laryngeal prominence (Adam’s apple)','Cartilagem tireoide':'Thyroid cartilage','Cartilagem cricoide':'Cricoid cartilage','Traqueia (anéis cartilagíneos)':'Trachea (cartilage rings)',
'O MEGAFONE E O MEGAFONE INVERTIDO':'THE MEGAPHONE AND THE INVERTED MEGAPHONE','laringe':'larynx','boca':'mouth','faringe estreita · boca aberta em sino':'narrow pharynx · bell-shaped mouth','faringe ampla · boca menor':'wide pharynx · smaller mouth opening',
'MELISMA: VÁRIAS NOTAS EM UMA ÚNICA SÍLABA':'MELISMA: MANY NOTES ON A SINGLE SYLLABLE','Uma sílaba sustentada, enquanto a melodia percorre várias notas.':'One sustained syllable while the melody travels through several notes.',
'A ESCALA DE METAL':'THE METAL SCALE','não metálica':'non-metallic','meio metálica':'half-metallic','metálica':'metallic','muito metálica':'fully metallic','mais metal':'more metal',
'FREQUÊNCIA E INTENSIDADE':'FREQUENCY AND INTENSITY','Grave · frequência baixa':'Low · lower frequency','Agudo · frequência alta':'High · higher frequency','Fraco · menor amplitude':'Soft · smaller amplitude','Forte · maior amplitude':'Loud · larger amplitude','A altura depende da frequência de vibração; o volume, da amplitude.':'Pitch depends on the frequency of vibration; loudness, on its amplitude.',
'O PONTO DE PARTIDA':'THE STARTING POSITION','parede':'wall','orelha':'ear','ombro':'shoulder','quadril':'hip','joelho':'knee','tornozelo':'ankle','costelas abertas,':'ribs open,','ombros relaxados,':'shoulders relaxed,','joelhos soltos':'knees soft',
'OS TRÊS REGISTROS':'THE THREE REGISTERS','grave':'low','agudo':'high','ELEVADO':'ELEVATED','ranger de porta · musculatura relaxada':'creaking door · relaxed muscles','voz de peito · a voz da fala':'chest voice · our speaking voice','voz de cabeça · laringe elevada':'head voice · raised larynx',
'OS QUATRO TIPOS DE RESPIRAÇÃO':'THE FOUR TYPES OF BREATHING','Torácica':'Thoracic','Completa':'Complete',
'TWANG: BRILHO E “VOZ DE MÁSCARA”':'TWANG: BRIGHTNESS AND “MASK” RESONANCE','sensação de “máscara”':'“mask” sensation','brilho percebido na face':'brightness felt in the face','constrição ariepiglótica':'aryepiglottic constriction','estreitamento acima das':'narrowing just above the','pregas vocais':'vocal folds','base da língua elevada':'raised tongue base',
'O VIBRATO':'VIBRATO','nota':'pitch','1 segundo · cerca de 5 a 7 oscilações no canto lírico':'1 second · about 5 to 7 oscillations in classical singing','A frequência oscila em torno da nota, de forma regular e controlada.':'The frequency oscillates around the note in a regular, controlled way.',
'YODEL: A QUEBRA ENTRE REGISTROS':'YODEL: THE BREAK BETWEEN REGISTERS','registro elevado (voz de cabeça)':'elevated register (head voice)','registro modal (voz de peito)':'modal register (chest voice)','Cada ponto dourado é uma “quebra” intencional de registro.':'Each gold dot is an intentional register “break”.',
}
for f in sorted(glob.glob("/tmp/work/book2/img/f-*.svg")):
    s=open(f,encoding="utf-8").read()
    def rep(m):
        t=m.group(2)
        return m.group(1)+M.get(t,t)+m.group(3)
    s=re.sub(r'(<text[^>]*>)(.*?)(</text>)',rep,s)
    open("/tmp/work/en/img/"+os.path.basename(f),"w",encoding="utf-8").write(s)
left=set()
for f in glob.glob("/tmp/work/en/img/*.svg"):
    for t in re.findall(r'<text[^>]*>(.*?)</text>',open(f,encoding="utf-8").read()):
        if re.search(r'[ãõçáéíóúâêô]',t): left.add(t)
print("untranslated with accents:",left)
