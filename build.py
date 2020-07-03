from douyu import get_real_url as douyu
from huya import get_real_url as huya

OUTPUT_PATH = "C:\\Users\\sanch\\Desktop\\"
NAME = "live"

urls = {
    "douyu": douyu,
    "huya": huya
}

slist = {
    "douyu": {
        "贝拉": "3276456",
        "学姐": "4775361"
    },
    "huya": {
        "轩子":"xuanzi",
        "恩七":"en777"
    }
}

fl = open(OUTPUT_PATH+NAME+".m3u","w",encoding="utf-8")
fl.write("#EXTM3U\n")

for platform in slist:
    for streamer in slist[platform]:
        url = urls[platform](slist[platform][streamer])

        #huya 
        if isinstance(url,list):
            url = url[0]
        
        if isinstance(url,str) and url.find("未开播")!=-1:
            continue
        fl.write("#EXTINF:-1,"+streamer)
        fl.write(("\n"+url)+"\n")
