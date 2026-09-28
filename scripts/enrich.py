# -*- coding: utf-8 -*-
"""OMDb 回灌: 拉取海报 + IMDb/烂番茄/Metacritic 评分, 写入 data/omdb_cache.json。
用法:
  set OMDB_KEY=你的key   (Windows)   或   export OMDB_KEY=你的key
  python scripts/enrich.py
之后再 python build.py 重新生成 index.html 即可看到海报和评分。
OMDb 免费 key: https://www.omdbapi.com/apikey.aspx (填邮箱->点确认链接, 30秒)
"""
import os, sys, json, re, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from build import DATA  # noqa

KEY = os.environ.get("OMDB_KEY", "").strip()
if not KEY:
    print("缺少 OMDB_KEY 环境变量。先去 https://www.omdbapi.com/apikey.aspx 拿免费 key。")
    sys.exit(1)

CACHE_PATH = os.path.join(HERE, "data", "omdb_cache.json")
cache = {}
if os.path.exists(CACHE_PATH):
    cache = json.load(open(CACHE_PATH, encoding="utf-8"))

def clean_title(t):
    t = re.sub(r"\s*\(.*?\)\s*", "", t)   # 去掉 (Season 1)/(Netflix) 等
    t = t.replace("*", "").strip()        # Thunderbolts*
    return t

def query(title, year, is_series):
    params = {"apikey": KEY, "t": clean_title(title),
              "type": "series" if is_series else "movie"}
    # 剧集按首播年匹配,分季标题不传年份以免第二季匹配失败
    if not (is_series and "Season" in title):
        params["y"] = str(year)
    url = "http://www.omdbapi.com/?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return json.load(r)
    except Exception as e:
        return {"Response": "False", "Error": str(e)}

def parse(j):
    if j.get("Response") != "True":
        return None
    out = {}
    poster = j.get("Poster", "")
    out["poster"] = poster if poster and poster != "N/A" else None
    imdb = j.get("imdbRating", "")
    out["imdb"] = imdb if imdb and imdb != "N/A" else None
    out["rt"] = None; out["metacritic"] = None
    for r in j.get("Ratings", []):
        if r["Source"] == "Rotten Tomatoes":
            out["rt"] = r["Value"]
        elif r["Source"] == "Metacritic":
            out["metacritic"] = r["Value"].split("/")[0]
    return out

REFRESH = os.environ.get("OMDB_REFRESH", "").strip() not in ("", "0", "false", "False")
ok = miss = 0
for d in DATA:
    if not REFRESH and d["id"] in cache and cache[d["id"]].get("poster"):
        ok += 1; continue
    j = query(d["title_en"], d["year"], d["type"] == "series")
    p = parse(j)
    if p:
        cache[d["id"]] = p; ok += 1
        print(f"  [OK] {d['title_zh']}  IMDb={p['imdb']} RT={p['rt']} MC={p['metacritic']}")
    else:
        miss += 1
        print(f"  [--] {d['title_zh']} ({d['year']}) 未匹配: {j.get('Error','no data')}")
    time.sleep(0.12)

json.dump(cache, open(CACHE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\n完成: 命中 {ok}, 未匹配 {miss}. 缓存写入 {CACHE_PATH}")
print("接着运行:  python build.py")
