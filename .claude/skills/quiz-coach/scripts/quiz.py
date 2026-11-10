#!/usr/bin/env python3
"""題庫與間隔複習排程工具（只用標準函式庫）。

題庫：  00_study_plan/question_bank/*.json
狀態：  00_study_plan/progress/state.json   （由本工具維護，不要手改）

常用指令：
  quiz.py lint                         檢查所有題庫檔
  quiz.py due [--date D] [--max 8]     列出到期的複習題（不含答案）
  quiz.py lesson w01-l1 [--use pre]    列出某課的題目（不含答案）
  quiz.py show ID [--answer]           顯示單題；加 --answer 才顯示答案與給分要點
  quiz.py record ID SCORE [--conf C]   登記一題成績（0-3），更新 Leitner 盒
  quiz.py import "AIFQ1|..."           匯入講義頁面「複製成績」產生的字串
  quiz.py compose weekly --week 3      組週測卷，輸出 Markdown
  quiz.py compose exam --weeks 1-4 --n 40 --name midterm1
  quiz.py render d00 --out FILE        把整個題庫檔轉成 Markdown 試卷
  quiz.py stats                        成績、盒分布、校準、回爐清單
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
MASTERED_INTERVAL = 60
TYPES = {"recall", "explain", "compare", "calc", "scenario", "pitch", "draw"}
ROLES = {"TMM", "PMM", "EVG", "TAM"}
USES = {"pre", "post", "bank"}
ID_RE = re.compile(r"^(w\d{2}-l\d|d00)-q\d{2}$")
TYPE_ZH = {
    "recall": "回想", "explain": "解釋", "compare": "比較", "calc": "計算",
    "scenario": "情境", "pitch": "定位", "draw": "畫圖",
}
WEEKLY_MIN = {"calc": 3, "scenario": 3, "compare": 4}


def repo_root() -> Path:
    for p in Path(__file__).resolve().parents:
        if (p / "00_study_plan").is_dir():
            return p
    sys.exit("找不到 00_study_plan/，請在 repo 內執行")


ROOT = repo_root()
PLAN = ROOT / "00_study_plan"
BANK_DIR = PLAN / "question_bank"
STATE = PLAN / "progress" / "state.json"


def rel(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


# ---------- 讀寫 ----------

def load_bank() -> dict[str, dict]:
    bank: dict[str, dict] = {}
    for f in sorted(BANK_DIR.glob("*.json")):
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            sys.exit(f"{f.name} 不是合法 JSON：{e}")
        for q in items:
            q["_file"] = f.name
            if q.get("id") in bank:
                sys.exit(f"題號重複：{q['id']}（{f.name} 與 {bank[q['id']]['_file']}）")
            bank[q["id"]] = q
    return bank


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"version": 1, "items": {}, "sessions": []}


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def parse_date(s: str | None) -> dt.date:
    return dt.date.fromisoformat(s) if s else dt.date.today()


def week_of(q: dict) -> int:
    m = re.match(r"w(\d{2})", q["lesson"])
    return int(m.group(1)) if m else 0


# ---------- lint ----------

def cmd_lint(args) -> int:
    errors, warns = [], []
    seen: dict[str, str] = {}
    per_lesson: dict[str, Counter] = defaultdict(Counter)
    files = sorted(BANK_DIR.glob("*.json"))
    if not files:
        errors.append("question_bank/ 裡沒有題庫檔")
    for f in files:
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: JSON 解析失敗 {e}")
            continue
        if not isinstance(items, list):
            errors.append(f"{f.name}: 最外層必須是陣列")
            continue
        for i, q in enumerate(items):
            where = f"{f.name}[{i}] {q.get('id', '?')}"
            for key in ("id", "lesson", "type", "level", "roles", "tags", "use",
                        "q", "answer", "keypoints", "source"):
                if key not in q:
                    errors.append(f"{where}: 缺欄位 {key}")
            qid = q.get("id", "")
            if not ID_RE.match(qid):
                errors.append(f"{where}: 題號格式應為 w01-l1-q01 或 d00-q01")
            elif not qid.startswith(q.get("lesson", "")):
                errors.append(f"{where}: 題號與 lesson 不一致")
            if qid in seen:
                errors.append(f"{where}: 題號與 {seen[qid]} 重複")
            seen[qid] = f.name
            if q.get("type") not in TYPES:
                errors.append(f"{where}: type 必須是 {sorted(TYPES)}")
            if q.get("level") not in (1, 2, 3):
                errors.append(f"{where}: level 必須是 1、2、3")
            if q.get("use") not in USES:
                errors.append(f"{where}: use 必須是 pre / post / bank")
            if not set(q.get("roles", [])) <= ROLES or not q.get("roles"):
                errors.append(f"{where}: roles 必須是 {sorted(ROLES)} 的非空子集")
            kp = q.get("keypoints", [])
            if not (2 <= len(kp) <= 4):
                errors.append(f"{where}: keypoints 需 2–4 點（目前 {len(kp)}）")
            if len(q.get("q", "")) < 8 or len(q.get("answer", "")) < 8:
                errors.append(f"{where}: 題幹或答案過短")
            src = q.get("source", "")
            path = re.split(r"[（(#\s]", src, maxsplit=1)[0]
            if src.startswith("外部："):
                pass
            elif not path or not (ROOT / path).exists():
                errors.append(f"{where}: source 路徑不存在：{path or src}（外部資料請以「外部：」開頭）")
            if re.search(r"\d{2,}", q.get("answer", "")) and not q.get("asof") and q.get("type") in ("recall", "calc"):
                warns.append(f"{where}: 答案含數字但沒有 asof（時點與口徑）")
            per_lesson[q.get("lesson", "?")][q.get("use", "?")] += 1
    for lesson, c in sorted(per_lesson.items()):
        if lesson == "d00":
            continue
        total = sum(c.values())
        if c["pre"] != 3:
            warns.append(f"{lesson}: 預測題應為 3 題（目前 {c['pre']}）")
        if not (6 <= c["post"] <= 8):
            warns.append(f"{lesson}: 課後題應為 6–8 題（目前 {c['post']}）")
        if total < 10:
            warns.append(f"{lesson}: 每課建議 10–12 題入庫（目前 {total}）")
    for w in warns:
        print(f"警告  {w}")
    for e in errors:
        print(f"錯誤  {e}")
    print(f"\n{len(seen)} 題、{len(files)} 個檔；{len(errors)} 個錯誤、{len(warns)} 個警告")
    return 1 if errors else 0


# ---------- 顯示 ----------

def fmt_q(q: dict, n: int | None = None, answer: bool = False) -> str:
    head = f"{n}. " if n is not None else ""
    out = [f"{head}[{q['id']}｜{TYPE_ZH[q['type']]}｜L{q['level']}] {q['q']}"]
    if answer:
        out.append(f"   參考答案：{q['answer']}")
        for k in q["keypoints"]:
            out.append(f"   ・{k}")
        out.append(f"   出處：{q['source']}" + (f"（{q['asof']}）" if q.get("asof") else ""))
    return "\n".join(out)


def cmd_show(args) -> int:
    bank = load_bank()
    if args.id not in bank:
        sys.exit(f"沒有這題：{args.id}")
    print(fmt_q(bank[args.id], answer=args.answer))
    st = load_state()["items"].get(args.id)
    if st:
        print(f"   狀態：第 {st['box']} 盒，下次 {st['due']}，已作答 {len(st['hist'])} 次")
    return 0


def cmd_lesson(args) -> int:
    bank = load_bank()
    qs = [q for q in bank.values() if q["lesson"] == args.lesson and (not args.use or q["use"] == args.use)]
    if not qs:
        sys.exit(f"題庫裡沒有 {args.lesson} 的題目（先用 course-handout skill 產生該課）")
    for i, q in enumerate(sorted(qs, key=lambda x: x["id"]), 1):
        print(fmt_q(q, i, answer=args.answer))
    return 0


def due_items(bank: dict, state: dict, today: dt.date) -> list[tuple[int, str]]:
    out = []
    for qid, st in state["items"].items():
        if qid in bank and dt.date.fromisoformat(st["due"]) <= today:
            overdue = (today - dt.date.fromisoformat(st["due"])).days
            out.append((st["box"], -overdue, qid))
    out.sort()
    return [(b, qid) for b, _, qid in out]


def cmd_due(args) -> int:
    bank, state = load_bank(), load_state()
    today = parse_date(args.date)
    items = due_items(bank, state, today)
    if not items:
        print(f"{today} 沒有到期的複習題。")
        return 0
    # 交錯：同一課的題不連續出現
    picked, last_lesson, pool = [], None, items[:]
    while pool and len(picked) < args.max:
        idx = next((i for i, (_, q) in enumerate(pool) if bank[q]["lesson"] != last_lesson), 0)
        b, qid = pool.pop(idx)
        picked.append((b, qid))
        last_lesson = bank[qid]["lesson"]
    print(f"{today} 到期 {len(items)} 題，本次出 {len(picked)} 題（盒號低的優先、不同課交錯）：\n")
    for i, (b, qid) in enumerate(picked, 1):
        print(fmt_q(bank[qid], i) + f"  〔第 {b} 盒〕")
    return 0


# ---------- 登記成績 ----------

def apply_score(state: dict, qid: str, score: int, conf: int | None, day: dt.date, kind: str) -> str:
    it = state["items"].get(qid)
    if kind == "P":  # 預測題：只留紀錄，不進排程
        state.setdefault("pretest", []).append([day.isoformat(), qid, score, conf])
        return "預測題，僅記錄"
    if it is None:
        it = {"box": 1, "due": day.isoformat(), "last": None, "hist": []}
        state["items"][qid] = it
        first = True
    else:
        first = False
    box = it["box"]
    if score >= 3:
        mastered = box == 5 and not first
        box = min(5, box if first else box + 1)
        interval = MASTERED_INTERVAL if mastered else INTERVALS[box]
    elif score == 2:
        interval = INTERVALS[box]
    else:
        box, interval = 1, INTERVALS[1]
    it.update(box=box, last=day.isoformat(), due=(day + dt.timedelta(days=interval)).isoformat())
    it["hist"].append([day.isoformat(), kind, score, conf])
    flag = ""
    if conf == 3 and score <= 1:
        flag = "  ⚠ 高估（信心 3 卻答錯）→ 回爐"
    elif conf == 1 and score == 3:
        flag = "  ☆ 低估（其實會了）→ 排一次口說"
    return f"第 {box} 盒，下次 {it['due']}{flag}"


def cmd_record(args) -> int:
    bank, state = load_bank(), load_state()
    if args.id not in bank:
        sys.exit(f"沒有這題：{args.id}")
    if not 0 <= args.score <= 3:
        sys.exit("分數必須是 0–3")
    msg = apply_score(state, args.id, args.score, args.conf, parse_date(args.date), args.kind)
    save_state(state)
    print(f"{args.id}: {args.score} 分 → {msg}")
    return 0


def cmd_import(args) -> int:
    """格式：AIFQ1|<lesson>|<YYYY-MM-DD>|id:kind:score:conf;id:kind:score:conf;..."""
    bank, state = load_bank(), load_state()
    parts = args.payload.strip().split("|")
    if len(parts) != 4 or parts[0] != "AIFQ1":
        sys.exit("格式不對，應為 AIFQ1|課號|日期|題號:類別:分數:信心;...")
    _, lesson, day_s, body = parts
    day = parse_date(args.date or day_s)
    total = mx = 0
    for chunk in filter(None, body.split(";")):
        try:
            qid, kind, score, conf = chunk.split(":")
            score, conf = int(score), (int(conf) or None)
        except ValueError:
            print(f"略過無法解析的片段：{chunk}")
            continue
        if qid not in bank:
            print(f"略過題庫沒有的題號：{qid}")
            continue
        msg = apply_score(state, qid, score, conf, day, kind)
        print(f"{qid} [{kind}] {score} 分 → {msg}")
        if kind != "P":
            total, mx = total + score, mx + 3
    state["sessions"].append({"date": day.isoformat(), "kind": "daily", "ref": lesson, "score": total, "max": mx})
    save_state(state)
    if mx:
        print(f"\n{lesson} 計分題 {total}/{mx}（{total / mx:.0%}），已寫入 state.json")
    return 0


def cmd_session(args) -> int:
    state = load_state()
    state["sessions"].append({"date": parse_date(args.date).isoformat(), "kind": args.kind,
                              "ref": args.ref, "score": args.score, "max": args.max})
    save_state(state)
    print(f"已登記 {args.kind} {args.ref}: {args.score}/{args.max}")
    return 0


# ---------- 組卷 ----------

def priority(q: dict, state: dict) -> tuple:
    st = state["items"].get(q["id"])
    if st is None:
        return (1, 0)          # 沒考過：次優先
    last = st["hist"][-1][2]
    return (0 if last < 3 else 2, st["box"])  # 上次沒滿分的最優先


def pick(pool: list[dict], n: int, state: dict, rng: random.Random, chosen: set[str]) -> list[dict]:
    pool = [q for q in pool if q["id"] not in chosen]
    rng.shuffle(pool)
    pool.sort(key=lambda q: priority(q, state))
    out = pool[:n]
    chosen.update(q["id"] for q in out)
    return out


def compose_weekly(bank: dict, state: dict, week: int, n: int, rng: random.Random) -> list[dict]:
    chosen: set[str] = set()
    this = [q for q in bank.values() if week_of(q) == week]
    prev = [q for q in bank.values() if week_of(q) == week - 1]
    older = [q for q in bank.values() if 0 < week_of(q) < week - 1]
    n_prev = min(4, len(prev)) if week > 1 else 0
    n_old = min(6, len(older)) if week > 2 else 0
    n_this = n - n_prev - n_old
    out: list[dict] = []
    lessons = sorted({q["lesson"] for q in this})
    per = max(1, n_this // max(1, len(lessons)))
    for les in lessons:  # 每課平均
        out += pick([q for q in this if q["lesson"] == les], per, state, rng, chosen)
    out += pick(this, n_this - len(out), state, rng, chosen)
    out += pick(prev, n_prev, state, rng, chosen)
    by_week: dict[int, list[dict]] = defaultdict(list)
    for q in older:
        by_week[week_of(q)].append(q)
    old_out: list[dict] = []
    for w in sorted(by_week):  # 每個舊週至少一題
        if len(old_out) < n_old:
            old_out += pick(by_week[w], 1, state, rng, chosen)
    old_out += pick(older, n_old - len(old_out), state, rng, chosen)
    out += old_out
    # 題型下限：盡量從同週未選的題替換
    for typ, need in WEEKLY_MIN.items():
        have = sum(1 for q in out if q["type"] == typ)
        spare = [q for q in this if q["type"] == typ and q["id"] not in chosen]
        while have < need and spare:
            victim = next((q for q in out if week_of(q) == week and q["type"] == "recall"), None)
            if victim is None:
                break
            new = spare.pop()
            out[out.index(victim)] = new
            chosen.discard(victim["id"])
            chosen.add(new["id"])
            have += 1
    rng.shuffle(out)  # 交錯
    return out


def to_markdown(title: str, intro: str, qs: list[dict]) -> str:
    lines = [f"# {title}", "", intro, ""]
    for i, q in enumerate(qs, 1):
        lines += [
            f"## 第 {i} 題　`{q['id']}`｜{TYPE_ZH[q['type']]}",
            "",
            q["q"],
            "",
            "我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿",
            "",
            "<details>",
            "<summary>作答後才展開：參考答案與給分要點</summary>",
            "",
            q["answer"],
            "",
        ]
        lines += [f"- {k}" for k in q["keypoints"]]
        lines += ["", f"出處：`{q['source']}`" + (f"（{q['asof']}）" if q.get("asof") else ""),
                  "", "</details>", ""]
    lines += ["---", "", "作答完把每題的「題號、得分 0–3、信心 1–3」交給 Claude 入帳（`quiz-coach` skill）。", ""]
    return "\n".join(lines)


def cmd_compose(args) -> int:
    bank, state = load_bank(), load_state()
    rng = random.Random(args.seed)
    if args.kind == "weekly":
        if not args.week:
            sys.exit("weekly 需要 --week")
        qs = compose_weekly(bank, state, args.week, args.n or 25, rng)
        title = f"W{args.week} 週測"
        name = f"w{args.week:02d}_weekly"
        intro = "> 閉卷、45 分鐘。每題先寫答案與信心，再展開參考答案自評 0–3 分。"
    else:
        m = re.match(r"(\d+)-(\d+)$", args.weeks or "")
        if not m:
            sys.exit("exam 需要 --weeks 1-4 這種範圍")
        lo, hi = int(m.group(1)), int(m.group(2))
        pool = [q for q in bank.values() if lo <= week_of(q) <= hi]
        chosen: set[str] = set()
        qs = []
        weeks = sorted({week_of(q) for q in pool})
        per = max(1, (args.n or 40) // max(1, len(weeks)))
        for w in weeks:
            qs += pick([q for q in pool if week_of(q) == w], per, state, rng, chosen)
        qs += pick(pool, (args.n or 40) - len(qs), state, rng, chosen)
        rng.shuffle(qs)
        name = args.name or f"exam_w{lo:02d}-w{hi:02d}"
        title = f"{name}（W{lo}–W{hi}）"
        intro = "> 閉卷、限時。大題結構與配分依 assessment.md 第五節，本檔提供題目池。"
    if not qs:
        sys.exit("題庫裡沒有符合範圍的題目")
    out = Path(args.out).resolve() if args.out else PLAN / "quizzes" / f"{name}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(to_markdown(title, intro, qs), encoding="utf-8")
    types = Counter(q["type"] for q in qs)
    print(f"已產生 {rel(out)}：{len(qs)} 題；題型 " +
          "、".join(f"{TYPE_ZH[t]} {c}" for t, c in types.most_common()))
    if args.kind == "weekly":
        for typ, need in WEEKLY_MIN.items():
            if types[typ] < need:
                print(f"警告  {TYPE_ZH[typ]}題只有 {types[typ]} 題（下限 {need}），題庫需要補這類題")
        if len(qs) < (args.n or 25):
            print(f"警告  題庫不足，只組出 {len(qs)} 題")
    return 0


def cmd_render(args) -> int:
    bank = load_bank()
    qs = sorted((q for q in bank.values() if q["_file"] == f"{args.set}.json"), key=lambda q: q["id"])
    if not qs:
        sys.exit(f"沒有 question_bank/{args.set}.json 或檔內無題目")
    out = Path(args.out).resolve() if args.out else PLAN / "quizzes" / f"{args.set}.md"
    title = args.title or f"{args.set} 題庫"
    intro = args.intro or "> 閉卷。每題先寫答案與信心，再展開參考答案自評 0–3 分。"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(to_markdown(title, intro, qs), encoding="utf-8")
    print(f"已產生 {rel(out)}：{len(qs)} 題")
    return 0


# ---------- 統計 ----------

def cmd_stats(args) -> int:
    bank, state = load_bank(), load_state()
    today = parse_date(args.date)
    items = state["items"]
    print(f"## 學習狀態（{today}）\n")
    print(f"- 題庫 {len(bank)} 題；已進入排程 {len(items)} 題；今天到期 {len(due_items(bank, state, today))} 題")
    boxes = Counter(it["box"] for it in items.values())
    print("- 盒分布：" + "、".join(f"第 {b} 盒 {boxes.get(b, 0)}" for b in range(1, 6)))

    def table(title: str, keyfn) -> None:
        agg: dict = defaultdict(lambda: [0, 0, 0])
        for qid, it in items.items():
            if qid not in bank:
                continue
            for _, kind, score, _ in it["hist"]:
                a = agg[keyfn(bank[qid])]
                a[0] += 1
                a[1] += score
                a[2] += 3
        if not agg:
            return
        print(f"\n### {title}\n\n| 分類 | 作答次數 | 得分率 |\n| --- | --- | --- |")
        for k in sorted(agg):
            n, s, m = agg[k]
            print(f"| {k} | {n} | {s / m:.0%} |")

    table("依週次", lambda q: f"W{week_of(q):02d}" if week_of(q) else "前測")
    table("依題型", lambda q: TYPE_ZH[q["type"]])

    over, under, weak = [], [], []
    for qid, it in items.items():
        if qid not in bank:
            continue
        _, _, score, conf = it["hist"][-1]
        if conf == 3 and score <= 1:
            over.append(qid)
        if conf == 1 and score == 3:
            under.append(qid)
        if sum(1 for h in it["hist"] if h[2] <= 1) >= 2:
            weak.append(qid)
    n_conf = sum(1 for it in items.values() for h in it["hist"] if h[3])
    n_over = sum(1 for it in items.values() for h in it["hist"] if h[3] == 3 and h[2] <= 1)
    print(f"\n### 校準\n\n- 有填信心的作答 {n_conf} 次，其中「信心 3 卻得 0–1 分」{n_over} 次"
          + (f"（{n_over / n_conf:.0%}）" if n_conf else ""))
    if over:
        print("- 高估（最近一次）：" + "、".join(over))
    if under:
        print("- 低估（最近一次）：" + "、".join(under))
    print("\n### 回爐清單（同一題答錯兩次以上）\n")
    if weak:
        for qid in weak:
            print(f"- `{qid}` {bank[qid]['q'][:40]}…")
    else:
        print("- 目前沒有")
    if state["sessions"]:
        print("\n### 最近 10 次測驗\n\n| 日期 | 類別 | 範圍 | 得分 |\n| --- | --- | --- | --- |")
        for s in state["sessions"][-10:]:
            pct = f"（{s['score'] / s['max']:.0%}）" if s["max"] else ""
            print(f"| {s['date']} | {s['kind']} | {s['ref']} | {s['score']}/{s['max']}{pct} |")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("lint").set_defaults(fn=cmd_lint)

    p = sub.add_parser("due")
    p.add_argument("--date")
    p.add_argument("--max", type=int, default=8)
    p.set_defaults(fn=cmd_due)

    p = sub.add_parser("lesson")
    p.add_argument("lesson")
    p.add_argument("--use", choices=sorted(USES))
    p.add_argument("--answer", action="store_true")
    p.set_defaults(fn=cmd_lesson)

    p = sub.add_parser("show")
    p.add_argument("id")
    p.add_argument("--answer", action="store_true")
    p.set_defaults(fn=cmd_show)

    p = sub.add_parser("record")
    p.add_argument("id")
    p.add_argument("score", type=int)
    p.add_argument("--conf", type=int, choices=[1, 2, 3])
    p.add_argument("--date")
    p.add_argument("--kind", default="R", choices=["P", "Q", "R", "W", "E"],
                   help="P 預測 / Q 課後 / R 間隔複習 / W 週測 / E 考試")
    p.set_defaults(fn=cmd_record)

    p = sub.add_parser("import")
    p.add_argument("payload")
    p.add_argument("--date")
    p.set_defaults(fn=cmd_import)

    p = sub.add_parser("session", help="登記一次週測或考試的總分")
    p.add_argument("kind", choices=["weekly", "midterm", "final", "assignment", "pretest"])
    p.add_argument("ref")
    p.add_argument("score", type=float)
    p.add_argument("max", type=float)
    p.add_argument("--date")
    p.set_defaults(fn=cmd_session)

    p = sub.add_parser("compose")
    p.add_argument("kind", choices=["weekly", "exam"])
    p.add_argument("--week", type=int)
    p.add_argument("--weeks")
    p.add_argument("--n", type=int)
    p.add_argument("--name")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--out")
    p.set_defaults(fn=cmd_compose)

    p = sub.add_parser("render")
    p.add_argument("set")
    p.add_argument("--out")
    p.add_argument("--title")
    p.add_argument("--intro")
    p.set_defaults(fn=cmd_render)

    p = sub.add_parser("stats")
    p.add_argument("--date")
    p.set_defaults(fn=cmd_stats)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
