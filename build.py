from douyu import get_real_url as douyu

OUTPUT_PATH = "C:\\Users\\sanch\\Desktop\\"
NAME = "live"

urls = {
    "douyu": douyu
}

slist = {
    "douyu": {
        "贝拉": "3276456"
    }
}

fl = open(OUTPUT_PATH+NAME+".m3u","w",encoding="utf-8")
fl.write("#EXTM3U\n")

for platform in slist:
    for streamer in slist[platform]:
        fl.write("#EXTINF:-1,"+streamer)
        fl.write("\n"+urls[platform](slist[platform][streamer])+"\n")

