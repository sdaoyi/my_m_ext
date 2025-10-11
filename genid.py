import json,hashlib,os

def main():
    with open(os.path.join(os.path.dirname(__file__),"index.min.json"),"r",encoding="utf-8") as f:
        data=json.load(f)
    for ext in data:
        pkg=ext["pkg"]
        # code=ext["code"]
        for s in ext["sources"]:
            lang=s["lang"]
            genid=f"{pkg}:{lang}"
            genid=hashlib.md5(genid.encode("utf-8")).hexdigest()
            genid=str(int(genid,16))[:19]
            s['id']=genid
    with open(os.path.join(os.path.dirname(__file__),"index.min.json"),"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
if __name__=="__main__":
    main()