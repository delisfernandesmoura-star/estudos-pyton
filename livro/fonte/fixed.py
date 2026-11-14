import os, zipfile, json, glob, uuid
from PIL import Image
imgs=sorted(glob.glob("fx/img/p-*.jpg")); W,H=Image.open(imgs[0]).size
P=json.load(open("pages.json")); toc=json.load(open("toc.json"))["toc"]
out="out/voz-canto-e-ciencia_layout-fixo.epub"
z=zipfile.ZipFile(out,"w")
z.writestr(zipfile.ZipInfo("mimetype"),"application/epub+zip",compress_type=zipfile.ZIP_STORED)
z.writestr("META-INF/container.xml",'<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>',compress_type=zipfile.ZIP_DEFLATED)
man=[];spine=[]
for i,f in enumerate(imgs,1):
    n=f"p{i:03d}"
    z.write(f,f"OEBPS/img/{n}.jpg",compress_type=zipfile.ZIP_STORED)
    z.writestr(f"OEBPS/text/{n}.xhtml",f'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="pt-BR"><head><meta charset="utf-8"/><title>Página {i}</title><meta name="viewport" content="width={W}, height={H}"/><style>html,body{{margin:0;padding:0;width:{W}px;height:{H}px}}img{{display:block;width:{W}px;height:{H}px}}</style></head><body><img src="../img/{n}.jpg" alt="Página {i}"/></body></html>',compress_type=zipfile.ZIP_DEFLATED)
    props=' properties="cover-image"' if i==1 else ''
    man.append(f'<item id="i{n}" href="img/{n}.jpg" media-type="image/jpeg"{props}/><item id="{n}" href="text/{n}.xhtml" media-type="application/xhtml+xml"/>')
    spine.append(f'<itemref idref="{n}" properties="{"page-spread-right" if i%2 else "page-spread-left"}"/>')
nav=[("Capa",1),("Sumário",P["toc"]),("Sobre este livro",P["sobre-livro"]),("Sobre a autora",P["sobre-autora"])]
for sid,lab,tit,chs in toc:
    nav.append((f"{lab} · {tit}",P[sid]))
    for cid,num,t in chs: nav.append((f"Capítulo {int(num)} · {t}",P[cid]))
nav+=[("Referências",P["referencias"]),("Áudios dos exercícios",P["audios"])]
z.writestr("OEBPS/nav.xhtml",'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="pt-BR"><head><meta charset="utf-8"/><title>Sumário</title></head><body><nav epub:type="toc" id="toc"><h1>Sumário</h1><ol>'+"".join(f'<li><a href="text/p{p:03d}.xhtml">{t}</a></li>' for t,p in nav)+'</ol></nav></body></html>',compress_type=zipfile.ZIP_DEFLATED)
z.writestr("OEBPS/content.opf",f'''<?xml version="1.0" encoding="UTF-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="pt-BR" prefix="rendition: http://www.idpf.org/vocab/rendition/#"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="uid">urn:uuid:{uuid.uuid4()}</dc:identifier><dc:title>Voz, Canto e Ciência</dc:title><dc:creator>Dra. Brízia Lacerda</dc:creator><dc:language>pt-BR</dc:language><dc:rights>© 2026 Dra. Brízia Lacerda. Todos os direitos reservados.</dc:rights><meta property="dcterms:modified">2026-11-14T00:00:00Z</meta><meta property="rendition:layout">pre-paginated</meta><meta property="rendition:orientation">portrait</meta><meta property="rendition:spread">auto</meta><meta name="cover" content="ip001"/></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>{"".join(man)}</manifest><spine>{"".join(spine)}</spine></package>''',compress_type=zipfile.ZIP_DEFLATED)
z.close(); print(out, len(imgs), os.path.getsize(out)//1024,"KB")
