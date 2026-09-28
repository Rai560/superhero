#!/usr/bin/env python3
"""超级英雄观影地图 —— GitHub 部署脚本 (Contents REST API)。
把项目文件推送到目标仓库(默认 Rai560/superhero)，GitHub Pages/Actions 自动发布。
用法:
  python deploy.py "commit message"                 # 用默认仓库和默认 token 文件
  REPO=Rai560/superhero GH_TOKEN_FILE=~/.aki/.secrets/superhero_gh_token python deploy.py "msg"
说明: 纯 REST(获取现有 sha -> base64 覆盖上传)，不依赖本地 git。
"""
import sys, os, json, base64, urllib.request, urllib.error

REPO = os.environ.get("REPO", "Rai560/superhero")
TOKEN_FILE = os.environ.get("GH_TOKEN_FILE", os.path.expanduser("~/.aki/.secrets/superhero_gh_token"))
TOKEN = open(os.path.expanduser(TOKEN_FILE)).read().strip()
BASE = os.path.dirname(os.path.abspath(__file__))
APIROOT = f"https://api.github.com/repos/{REPO}/contents/"

# 要推送的文件(相对本项目根)。生成物 index.html 也推，首发即可直接看。
FILES = [
    "build.py", "template.html", "index.html", "README.md",
    "deploy.py", "scripts/enrich.py",
    "data/omdb_cache.json", "data/logos.json", "data/banners.json",
    ".github/workflows/update.yml",
]

def api(method, path, data=None):
    req = urllib.request.Request(APIROOT + path, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "aki-superhero-deploy")
    if data is not None:
        req.data = json.dumps(data).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try: return e.code, json.load(e)
        except Exception: return e.code, {"message": str(e)}

def get_sha(repo_path):
    st, d = api("GET", repo_path.replace("\\", "/"))
    return d.get("sha") if (st == 200 and isinstance(d, dict)) else None

def push(repo_path, message):
    content = open(os.path.join(BASE, repo_path), "rb").read()
    rp = repo_path.replace("\\", "/")
    body = {"message": message, "content": base64.b64encode(content).decode()}
    sha = get_sha(rp)
    if sha:
        body["sha"] = sha
    st, d = api("PUT", rp, body)
    if st in (200, 201):
        print(f"  OK {rp} ({len(content)} bytes)")
        return True
    print(f"  FAIL {rp} [{st}]: {d.get('message')}")
    return False

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "update superhero watchlist"
    files = sys.argv[2:] if len(sys.argv) > 2 else FILES
    print(f"推送到 {REPO}（commit: {msg}）")
    ok = all(push(f, msg) for f in files)
    print(f"线上: https://{REPO.split('/')[0].lower()}.github.io/{REPO.split('/')[1]}/")
    sys.exit(0 if ok else 1)
