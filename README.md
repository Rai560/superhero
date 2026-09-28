# 漫威 & DC 超级英雄观影地图

自包含单文件网页：两大宇宙的电影 + 剧集全整理，含推荐观看顺序、官方海报、
IMDb/烂番茄/Metacritic 评分、中文简介与「是否值得看」建议。按篇章分展厅，博物馆风 UI。

线上地址：https://rai560.github.io/superhero/

## 目录结构
- `build.py` —— 核心片单数据 `DATA` + 篇章/宇宙元信息 + 生成 `index.html`
- `template.html` —— 页面模板（数据经 `/*__PAYLOAD__*/` 注入）
- `scripts/enrich.py` —— 调 OMDb 回灌海报+评分，写 `data/omdb_cache.json`
- `data/logos.json` / `data/banners.json` —— 官方 logo / 群像图（base64 内联，构建时读取）
- `index.html` —— 生成物（直接双击可看）
- `.github/workflows/update.yml` —— 每月自动刷新评分/海报 + 每次 push 自动重建部署

## 本地重建
```bash
python build.py                       # 只重建页面
export OMDB_KEY=你的key                # 刷新评分/海报（可选）
python scripts/enrich.py && python build.py
```

## 自动更新机制
GitHub Actions（`update.yml`）会在：
1. **每月 1 号**自动重跑 OMDb 刷新评分/海报 + 重建 + 部署；
2. **每次修改 `build.py` 等并 push** 时自动重建 + 部署。
所以**新片无法自动发现，需手动加**，但加完后构建/部署全自动。

---

## 如何添加一部新片（给任何 AI / 任何电脑）

在 GitHub 网页上打开 `build.py`，找到合适的 `DATA += [ ... ]` 区块，
按下面格式加**一行** `F(...)`，然后 commit。Actions 会自动补海报/评分并重新部署，
**无需在本地运行任何东西**。

### F() 字段说明
```python
F(id, zh, en, year, universe, group, tier, note, syn, type="film")
```
| 字段 | 含义 | 取值 |
|---|---|---|
| `id` | 唯一英文短标识 | 如 `"mcu-avengers-5"`，不可与现有重复 |
| `zh` | 中文片名 | 如 `"复仇者联盟5"` |
| `en` | 英文原名（**OMDb 靠它匹配，务必准确**） | 如 `"Avengers: Doomsday"` |
| `year` | 上映/首播年 | 如 `2026` |
| `universe` | 宇宙 | `"mcu"` / `"dceu"` / `"dcu"` / `"elseworlds"` |
| `group` | 阶段/分组（决定归入哪个篇章） | MCU：`"第一阶段"`~`"第六阶段"` 或 `"衍生剧集"`；DC 填如 `"DCU 电影"` |
| `tier` | 必要性 | `"core"`主线必看 / `"rec"`推荐 / `"opt"`可选 / `"skip"`衍生可跳过 |
| `note` | 「是否值得看」建议（1~2 句中文） | |
| `syn` | 剧情简介（1 句中文，不剧透结局） | |
| `type` | 类型（默认电影） | `"film"` / `"series"`剧集 / `"special"`特别篇 |

### 篇章归类规则（自动，无需手动指定）
- MCU + group 属第一~三阶段 → 「无限传奇」
- MCU + 其它阶段 → 「多元宇宙传奇」
- MCU + group 以「衍生」开头 → 「漫威衍生宇宙」
- dceu / dcu / elseworlds → 对应各自展厅

### 示例：新增《复仇者联盟5》
```python
 F("mcu-avengers-5","复仇者联盟5","Avengers: Doomsday",2026,"mcu","第六阶段","core",
   "多元宇宙传奇的收官集结，主线必看。",
   "面对跨越多元宇宙的新威胁，复仇者们再度集结。"),
```
把这行加进对应的 `DATA += [ ... ]` 区块里，commit 即可。

### 剧集匹配小贴士
分季剧集（标题含 `Season`）OMDb 不传年份匹配；括号内的备注（如 `(Netflix)`）
会被自动清理，不影响匹配。
