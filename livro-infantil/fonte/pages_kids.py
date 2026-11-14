import subprocess, json, re
toc=json.load(open("toc.json"))["toc"]
n=int(re.search(r"Pages:\s+(\d+)",subprocess.check_output(["pdfinfo","kids.pdf"]).decode()).group(1))
txt=[re.sub(r"\s+","",subprocess.check_output(["pdftotext","-f",str(i),"-l",str(i),"kids.pdf","-"]).decode()).lower() for i in range(1,n+1)]
def norm(s): return re.sub(r"\s+","",re.sub(r"<[^>]+>","",s)).lower()
P={}
def find(k,pred,frm=0):
    for i in range(frm,n):
        if pred(txt[i]): P[k]=i+1; return i
    print("nf",k); return frm
c=find("carta",lambda t:t.startswith("olá!quebom"))
c=find("como-usar",lambda t:t.startswith("comousarestelivro"),c)
for num,lab,tit,chs in toc:
    c=find(f"parte-{num}",lambda t,T=norm(tit):T in t and len(t)<600,c)
    for cid,nn,t in chs: c=find(cid,lambda tx,N=nn,T=norm(t):(tx.startswith(f"{N}capítulo{N}") or tx.startswith(f"capítulo{N}{N}")) and T[:15] in tx[:200],c)
c=find("referencias",lambda t:t.startswith("referências"),c)
c=find("audios",lambda t:t.startswith("materialcomplementar"),c)
find("sobre-autora",lambda t:t.startswith("sobreaautora"),c)
json.dump(P,open("pages.json","w")); print(P)
