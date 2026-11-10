#!/usr/bin/env python3
"""講義建置與檢查工具（只用標準函式庫）。

  handout.py new w01-l2 --slug cpu-vs-gpu --title "…" --date 2026-11-17 \\
             --theme "W1 AI 工廠全景與 GPU 基礎" --question "…"
      由版型建立 00_study_plan/w01/w01-l2_cpu-vs-gpu.html
  handout.py fill FILE     把 <div class="q" data-qid=… data-kind=…></div> 空殼換成題庫內容
  handout.py check FILE…   結構、題庫、連結、用語檢查；有「錯誤」就不能交付
  handout.py sync [FILE…]  把版型的 CSS／JS 同步到既有講義（不給檔名則同步全部）
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL / "assets" / "template.html"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr",
        "path", "rect", "circle", "line", "ellipse", "polygon", "polyline", "use", "stop"}
SECTIONS = ["warmup", "pretest", "hook", "concepts", "worked", "myths", "pitch", "exit", "wrap", "glossary", "sources"]
BLOCKS = ("STYLE", "SCRIPT")
# 常見的簡體專用字；出現在正文代表沒有轉成繁體（出處與術語表的 repo 用語欄除外）
SIMPLIFIED = set(
    "这个们来时为说国会学对发经动进样关现实点业开种问间题长体质产车门马书义习飞华单卖双变听头审导层属岁师带归当录径忆态总恶战"
    "戏户护报择据损换数设计网络显调优势异构块储杂复压缩闭讲训练标识别传输处写读电脑软连线运营销图库选项试验证历记虽则应该虑么"
    "还没过给让从与两"
)


def repo_root() -> Path:
    for p in Path(__file__).resolve().parents:
        if (p / "00_study_plan").is_dir():
            return p
    sys.exit("找不到 00_study_plan/，請在 repo 內執行")


ROOT = repo_root()
PLAN = ROOT / "00_study_plan"


def load_bank() -> dict[str, dict]:
    bank = {}
    for f in sorted((PLAN / "question_bank").glob("*.json")):
        for q in json.loads(f.read_text(encoding="utf-8")):
            bank[q["id"]] = q
    return bank


def block(text: str, name: str) -> tuple[int, int]:
    m = re.search(rf"<!-- HANDOUT:{name}:BEGIN[^>]*-->.*?<!-- HANDOUT:{name}:END -->", text, re.S)
    if not m:
        sys.exit(f"找不到 HANDOUT:{name} 區塊標記")
    return m.span()


# ---------- new ----------

def cmd_new(args) -> int:
    m = re.match(r"^(w\d{2})-l\d$", args.lesson)
    if not m:
        sys.exit("課號格式應為 w01-l2")
    dt.date.fromisoformat(args.date)
    out = PLAN / m.group(1) / f"{args.lesson}_{args.slug}.html"
    if out.exists() and not args.force:
        sys.exit(f"{out.relative_to(ROOT)} 已存在；要覆寫請加 --force")
    text = TEMPLATE.read_text(encoding="utf-8")
    for k, v in {"LESSON": args.lesson, "DATE": args.date, "TITLE": args.title,
                 "WEEK_THEME": args.theme, "CORE_QUESTION": args.question}.items():
        text = text.replace("{{" + k + "}}", html.escape(v, quote=False))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"已建立 {out.relative_to(ROOT)}")
    return 0


# ---------- fill ----------

Q_RE = re.compile(r'<div class="q"([^>]*)>(.*?)</div>', re.S)


def render_q(attrs: str, bank: dict, errors: list[str]) -> str:
    qid = re.search(r'data-qid="([^"]+)"', attrs)
    kind = re.search(r'data-kind="([PQR])"', attrs)
    if not qid or not kind:
        errors.append(f'題目空殼缺 data-qid 或 data-kind（P/Q/R）：<div class="q"{attrs}>')
        return f'<div class="q"{attrs}></div>'
    qid, kind = qid.group(1), kind.group(1)
    q = bank.get(qid)
    if q is None:
        errors.append(f"題庫沒有 {qid}")
        return f'<div class="q" data-qid="{qid}" data-kind="{kind}"></div>'
    e = lambda s: html.escape(s, quote=False)
    out = [f'<div class="q" data-qid="{qid}" data-kind="{kind}" data-type="{q["type"]}">',
           f'<p class="q-text">{e(q["q"])}</p>']
    if kind != "P":  # 預測題不放答案
        lang = ' lang="en"' if q["type"] == "pitch" and re.search(r"[A-Za-z]{4,} [A-Za-z]{4,} [A-Za-z]{2,}", q["answer"]) else ""
        out.append(f'<aside class="q-answer"><p{lang}>{e(q["answer"])}</p><ul>')
        out += [f"<li>{e(k)}</li>" for k in q["keypoints"]]
        src = e(q["source"]) + (f"（{e(q['asof'])}）" if q.get("asof") else "")
        out.append(f'</ul><p class="q-src">出處：{src}</p></aside>')
    out.append("</div>")
    return "\n".join(out)


def cmd_fill(args) -> int:
    bank = load_bank()
    rc = 0
    for name in args.files:
        f = Path(name)
        text = f.read_text(encoding="utf-8")
        errors: list[str] = []
        new, n = Q_RE.subn(lambda m: render_q(m.group(1), bank, errors), text)
        f.write_text(new, encoding="utf-8")
        print(f"{f.name}: 已帶入 {n} 題")
        for e in errors:
            print(f"錯誤  {e}")
            rc = 1
    return rc


# ---------- sync ----------

def cmd_sync(args) -> int:
    tpl = TEMPLATE.read_text(encoding="utf-8")
    files = [Path(f) for f in args.files] or sorted(PLAN.glob("w*/w*-l*.html"))
    for f in files:
        text = f.read_text(encoding="utf-8")
        for name in BLOCKS:
            a, b = block(tpl, name)
            c, d = block(text, name)
            text = text[:c] + tpl[a:b] + text[d:]
        f.write_text(text, encoding="utf-8")
        print(f"已同步 {f.name}")
    return 0


# ---------- check ----------

class Tree(HTMLParser):
    """夠用的結構解析：記錄每個元素的 tag、屬性、所在 section、文字。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[dict] = []
        self.nodes: list[dict] = []
        self.errors: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "text": "", "own": "", "parent": self.stack[-1] if self.stack else None,
                "line": self.getpos()[0], "children": []}
        if node["parent"]:
            node["parent"]["children"].append(node)
        self.nodes.append(node)
        if tag in ("script", "style"):
            self.skip += 1
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1]["tag"] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag in ("script", "style"):
            self.skip -= 1
        if not self.stack or self.stack[-1]["tag"] != tag:
            open_tag = self.stack[-1]["tag"] if self.stack else "（無）"
            self.errors.append(f"第 {self.getpos()[0]} 行：</{tag}> 對不上，目前開著的是 <{open_tag}>")
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i]["tag"] == tag:
                    del self.stack[i:]
                    break
            return
        self.stack.pop()

    def handle_data(self, data):
        if self.skip:
            return
        for n in self.stack:
            n["text"] += data
        if self.stack:
            self.stack[-1]["own"] += data


def cls(n: dict) -> set[str]:
    return set((n["attrs"].get("class") or "").split())


def inside(n: dict, pred) -> bool:
    p = n["parent"]
    while p:
        if pred(p):
            return True
        p = p["parent"]
    return False


def descendants(n: dict):
    for c in n["children"]:
        yield c
        yield from descendants(c)


def check_file(f: Path, bank: dict, tpl: str) -> tuple[list[str], list[str]]:
    E: list[str] = []
    W: list[str] = []
    text = f.read_text(encoding="utf-8")
    if "{{" in text:
        E.append("還有未替換的 {{…}} 佔位符")
    if re.search(r"TODO|待補|…</p></div>\s*</section>", text):
        W.append("可能還有未完成的佔位內容（TODO／待補／只有「…」的段落）")
    t = Tree()
    t.feed(text)
    E += t.errors[:8]
    if t.stack:
        E.append("有標籤沒關：" + "、".join(f"<{n['tag']}>（第 {n['line']} 行）" for n in t.stack[:5]))
    nodes = t.nodes
    root = next((n for n in nodes if n["tag"] == "html"), None)
    lesson = (root or {"attrs": {}})["attrs"].get("data-lesson", "")
    if not root or root["attrs"].get("lang") != "zh-Hant":
        E.append('<html> 需要 lang="zh-Hant"')
    if not re.match(r"^w\d{2}-l\d$", lesson):
        E.append("data-lesson 格式應為 w01-l2")
    elif not f.name.startswith(lesson + "_"):
        E.append(f"檔名應以 {lesson}_ 開頭")
    try:
        dt.date.fromisoformat((root or {"attrs": {}})["attrs"].get("data-date", ""))
    except ValueError:
        E.append("data-date 需為 YYYY-MM-DD")

    sec = {n["attrs"].get("id"): n for n in nodes if n["tag"] == "section"}
    for s in SECTIONS:
        if s not in sec:
            E.append(f'缺少 <section id="{s}">')
    if E and any("缺少 <section" in e for e in E):
        return E, W

    def qs(section: str, kind: str) -> list[dict]:
        return [n for n in descendants(sec[section]) if "q" in cls(n) and n["attrs"].get("data-kind") == kind]

    def is_filled(n: dict) -> bool:
        return any("q-text" in cls(c) for c in n["children"])

    all_q = [n for n in nodes if n["tag"] == "div" and "q" in cls(n)]
    for n in all_q:
        qid = n["attrs"].get("data-qid", "")
        if qid not in bank:
            E.append(f"第 {n['line']} 行：題庫沒有 {qid or '（缺 data-qid）'}")
        elif not is_filled(n):
            E.append(f"第 {n['line']} 行：{qid} 還是空殼，請執行 handout.py fill")

    pre = qs("pretest", "P")
    if len(pre) != 3:
        E.append(f"STEP 2 預測題要剛好 3 題（目前 {len(pre)}）")
    for n in pre:
        q = bank.get(n["attrs"].get("data-qid", ""))
        if q and (q["lesson"] != lesson or q["use"] != "pre"):
            E.append(f"{q['id']} 不是本課 use=pre 的題，不能當預測題")
        if any("q-answer" in cls(c) for c in descendants(n)):
            E.append(f"預測題 {n['attrs'].get('data-qid')} 不可以帶答案")

    ex = qs("exit", "Q")
    ex_ids = [n["attrs"].get("data-qid") for n in ex]
    if not 9 <= len(ex) <= 11:
        E.append(f"STEP 8 要 9–11 題：3 題預測題重答＋6–8 題課後題（目前 {len(ex)}）")
    for n in pre:
        if n["attrs"].get("data-qid") not in ex_ids:
            E.append(f"預測題 {n['attrs'].get('data-qid')} 沒有在 STEP 8 重答")
    post_here = [i for i in ex_ids if i in bank and bank[i]["use"] == "post" and bank[i]["lesson"] == lesson]
    if len(post_here) < 6:
        E.append(f"STEP 8 需要至少 6 題本課 use=post 的題（目前 {len(post_here)}）")
    types = {bank[i]["type"] for i in ex_ids if i in bank}
    if len(types) < 4:
        W.append(f"STEP 8 只有 {len(types)} 種題型，建議至少 4 種（含一題 calc 或 scenario）")
    if len(set(ex_ids)) != len(ex_ids):
        E.append("STEP 8 有重複的題號")

    warm = qs("warmup", "R")
    if lesson != "w01-l1":
        if len(warm) < 2:
            E.append(f"STEP 1 需要至少 2 題先前課次的複習題（目前 {len(warm)}）")
        for n in warm:
            q = bank.get(n["attrs"].get("data-qid", ""))
            if q and q["lesson"] == lesson:
                E.append(f"STEP 1 的 {q['id']} 是本課的題，暖身要用先前課次的題")

    concepts = [n for n in descendants(sec["concepts"]) if n["tag"] == "article" and "concept" in cls(n)]
    if not 3 <= len(concepts) <= 5:
        E.append(f"核心概念要 3–5 個（目前 {len(concepts)}）；超過 5 個代表這一課塞太多")
    for i, c in enumerate(concepts, 1):
        d = list(descendants(c))
        if not any("claim" in cls(n) for n in d):
            E.append(f"概念 {i} 缺一句主張（.claim）")
        figs = [n for n in d if n["tag"] == "figure" and "fig" in cls(n)]
        if not figs:
            E.append(f"概念 {i} 缺圖（figure.fig）")
        for fg in figs:
            fd = list(descendants(fg))
            if not any(n["tag"] == "figcaption" for n in fd):
                E.append(f"概念 {i} 的圖缺 figcaption")
            if len(fd) < 4:
                E.append(f"概念 {i} 的圖是空的")
        if not any(n["tag"] == "details" and "check" in cls(n) for n in d):
            E.append(f"概念 {i} 缺檢查點（details.check）")
    n_analogy = sum(1 for n in nodes if {"callout", "analogy"} <= cls(n))
    if n_analogy < 2:
        E.append(f"全課至少要 2 個類比（.callout.analogy），目前 {n_analogy}")
    for n in nodes:
        if "num" in cls(n) and n["tag"] == "div" and not any("s" in cls(c) for c in n["children"]):
            E.append(f"第 {n['line']} 行：數字卡缺出處與時點（.s）")

    if not any("story" in cls(n) for n in descendants(sec["hook"])):
        E.append("STEP 3 缺情境（.callout.story）")
    if not any(n["tag"] == "details" and "check" in cls(n) for n in descendants(sec["worked"])):
        E.append("STEP 5 的解題步驟要收在 details.check 裡，讓讀者先自己算")
    n_myth = sum(1 for n in descendants(sec["myths"]) if {"callout", "warn"} <= cls(n))
    if n_myth < 2:
        E.append(f"STEP 6 至少 2 個誤解（.callout.warn），目前 {n_myth}")
    en = [n for n in descendants(sec["pitch"]) if n["attrs"].get("lang") == "en"]
    words = sum(len(re.findall(r"[A-Za-z']+", n["text"])) for n in en)
    if not 80 <= words <= 200:
        E.append(f'STEP 7 的英文講法（lang="en"）要 80–200 字（目前 {words}）')
    rows = [n for n in descendants(sec["glossary"]) if n["tag"] == "tr" and inside(n, lambda p: p["tag"] == "tbody")]
    if len(rows) < 5:
        E.append(f"術語表至少 5 列（目前 {len(rows)}）")

    repo_links = [n for n in nodes if n["tag"] == "a" and "repo" in cls(n)]
    if not any(inside(n, lambda p: p is sec["sources"]) for n in repo_links):
        E.append("出處區至少要有一個 repo 連結（a.repo[data-path]）")
    for n in repo_links:
        path = n["attrs"].get("data-path", "")
        if not path or not (ROOT / path).exists():
            E.append(f"第 {n['line']} 行：repo 路徑不存在：{path}")
    for n in nodes:
        a = n["attrs"]
        if n["tag"] == "img" and not (a.get("src") or "").startswith("data:"):
            E.append(f"第 {n['line']} 行：不要用外部圖片（講義必須單檔可開）；改用 HTML／SVG 元件畫")
        if n["tag"] == "script" and a.get("src"):
            E.append(f"第 {n['line']} 行：不要載入外部 script")
        if n["tag"] == "link" and a.get("rel") == "stylesheet":
            E.append(f"第 {n['line']} 行：不要載入外部樣式表")
        if n["tag"] == "a" and "repo" not in cls(n):
            href = a.get("href") or ""
            if href and not href.startswith(("#", "https://")):
                E.append(f"第 {n['line']} 行：連結 {href} 請改用 a.repo[data-path]（repo 檔案）或 https 網址")
        if n["tag"] == "svg" and "diagram" not in cls(n):
            W.append(f"第 {n['line']} 行：SVG 請加 class=\"diagram\" 才會跟著深淺色主題")
        if n["tag"] == "svg" and "viewBox" not in a and "viewbox" not in a:
            E.append(f"第 {n['line']} 行：SVG 缺 viewBox")
        style = a.get("style") or ""
        if re.search(r"#[0-9a-fA-F]{3,8}\b|rgb\(", style) or re.search(r"#[0-9a-fA-F]{3,8}\b", a.get("fill") or "" + (a.get("stroke") or "")):
            W.append(f"第 {n['line']} 行：寫死的顏色在深色模式會出問題，改用 var(--accent) 等變數或既有 class")

    for name in BLOCKS:
        a, b = block(tpl, name)
        c, d = block(text, name)
        if tpl[a:b] != text[c:d]:
            W.append(f"{name} 區塊與版型不同，請執行 handout.py sync")

    def exempt(n: dict) -> bool:
        return (n is sec["sources"] or n is sec["glossary"] or "q-src" in cls(n)
                or n["attrs"].get("lang") == "zh-Hans" or n["tag"] in ("code", "script", "style"))
    body = "".join(n["own"] for n in nodes if not exempt(n) and not inside(n, exempt))
    simp = sorted({ch for ch in body if ch in SIMPLIFIED})
    if simp:
        W.append("正文疑似有簡體字：" + "".join(simp[:30]) + "（引用原文請包在 lang=\"zh-Hans\" 的元素裡）")
    main = next((n for n in nodes if n["tag"] == "main"), None)
    n_cjk = len(re.findall(r"[一-鿿]", main["text"] if main else ""))
    if n_cjk < 2200:
        W.append(f"正文只有約 {n_cjk} 個中文字，內容可能太薄（建議 2,500–6,000）")
    if n_cjk > 6500:
        W.append(f"正文約 {n_cjk} 個中文字，超過一課 45 分鐘能讀完的量（建議 2,500–6,000）")
    if len(text.encode()) > 400_000:
        W.append("檔案超過 400 KB")
    return E, W


def cmd_check(args) -> int:
    bank = load_bank()
    tpl = TEMPLATE.read_text(encoding="utf-8")
    rc = 0
    for name in args.files:
        f = Path(name)
        E, W = check_file(f, bank, tpl)
        print(f"== {f.name}")
        for w in W:
            print(f"警告  {w}")
        for e in E:
            print(f"錯誤  {e}")
        print(f"{len(E)} 個錯誤、{len(W)} 個警告" + ("" if E else "　✔ 可以交付"))
        rc |= bool(E)
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new")
    p.add_argument("lesson")
    p.add_argument("--slug", required=True, help="英文小寫加連字號，如 cpu-vs-gpu")
    p.add_argument("--title", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--theme", required=True, help="當週主題，如「W1 AI 工廠全景與 GPU 基礎」")
    p.add_argument("--question", required=True, help="syllabus.md 該課的核心問題")
    p.add_argument("--force", action="store_true")
    p.set_defaults(fn=cmd_new)
    p = sub.add_parser("fill")
    p.add_argument("files", nargs="+")
    p.set_defaults(fn=cmd_fill)
    p = sub.add_parser("check")
    p.add_argument("files", nargs="+")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("sync")
    p.add_argument("files", nargs="*")
    p.set_defaults(fn=cmd_sync)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
