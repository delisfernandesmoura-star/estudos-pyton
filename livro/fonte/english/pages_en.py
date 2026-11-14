import subprocess, json, re
toc=json.load(open("toc.json"))["toc"]
n=int(re.search(r"Pages:\s+(\d+)",subprocess.check_output(["pdfinfo","book_en.pdf"]).decode()).group(1))
txt=[re.sub(r"\s+","",subprocess.check_output(["pdftotext","-f",str(i),"-l",str(i),"book_en.pdf","-"]).decode()).lower() for i in range(1,n+1)]
def norm(s): return re.sub(r"\s+","",re.sub(r"<[^>]+>","",s)).lower()
P={}
def find(key,pred,frm=0):
    for i in range(frm,n):
        if pred(txt[i]): P[key]=i+1; return i
    print("nf",key); return frm
tocp=find("toc",lambda t:"contents" in t[:30])
c=find("sobre-livro",lambda t:"aboutthisbook" in t[:60],tocp+1)
c=find("sobre-autora",lambda t:t.startswith("theauthor"),c)
for sid,lab,tit,chs in toc:
    c=find(sid,lambda t,L=norm(lab),T=norm(tit): (L+T) in t and len(t)<900,c)
    for cid,num,t in chs:
        c=find(cid,lambda tx,N=int(num),T=norm(t): tx.startswith(f"{N:02d}chapter{N}") and T[:20] in tx[:200],c)
c=find("referencias",lambda t:"references" in t[:30],c)
find("audios",lambda t:"exerciseaudio" in t[:80],c)
json.dump(P,open("pages.json","w")); print(P)
