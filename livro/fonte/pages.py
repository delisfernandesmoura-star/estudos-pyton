import subprocess, json, re
toc=json.load(open("toc.json"))["toc"]
n=int(re.search(r"Pages:\s+(\d+)",subprocess.check_output(["pdfinfo","book.pdf"]).decode()).group(1))
txt=[]
for i in range(1,n+1):
    t=subprocess.check_output(["pdftotext","-f",str(i),"-l",str(i),"-layout","book.pdf","-"]).decode()
    txt.append(re.sub(r"\s+"," ",t).lower())
def norm(s): return re.sub(r"\s+"," ",re.sub(r"<[^>]+>","",s)).lower().strip()
pages={}
# find toc page(s) to skip
tocpg=[i for i,t in enumerate(txt) if "sumário" in t and "sobre este livro" in t][0]
start=tocpg+1
def find(key,pred,frm):
    for i in range(frm,n):
        if pred(txt[i]): pages[key]=i+1; return i
    print("not found",key); return frm
i=find("sobre-livro",lambda t:t.startswith("sobre este livro") ,start)
i=find("sobre-autora",lambda t:t.startswith("sobre a autora"),i)
cur=i
for sid,label,title,chs in toc:
    cur=find(sid,lambda t,L=norm(label),T=norm(title): L in t[:60] and T in t[:160] and len(t)<700,cur)
    for cid,num,t in chs:
        cur=find(cid,lambda tx,T=norm(t),N=num: ("capítulo "+N) in tx[:40] and T[:30] in tx[:200],cur)
for sid,label,title,chs in toc: pages[sid]=pages[chs[0][0]]-1
find("referencias",lambda t:t.startswith("referências"),cur)
json.dump(pages,open("pages.json","w"))
print(pages)
