# 讀書計畫：AI Infra GTM 實戰班

用這個 repo 當教材，12 週內準備好應徵外商 **Technical Marketing Manager／AI Evangelist／Product Marketing Manager／Technical Account Manager**（AI infrastructure、GPU、data center）。

- 期間：2026-11-16（一）開課 → 2027-02-04（四）結業，春節前完成
- 投入：每週約 13 小時（平日 90 分鐘 × 5，週六 3 小時，週日 2.5 小時）
- 方法：每課一份視覺化講義；每天先考、再學、再考；題目依 1-3-7-14-30 天的間隔回來（依《Make It Stick》與《學生為什麼不喜歡上學？》設計）

本目錄是這個 fork 專屬的內容，以繁體中文撰寫；repo 其餘部分是上游的簡體中文技術文章。

## 文件

| 檔案 | 內容 |
| --- | --- |
| [syllabus.md](syllabus.md) | **課綱**：每週主題、55 課的核心問題與指定閱讀、書目、作業與考試日期、評分標準與規定 |
| [assessment.md](assessment.md) | **測驗內容**：設計原則、七種題型、每日小考流程、間隔排程、期中期末藍圖、評分規準、各週必考概念、題庫格式 |
| [career_targets.md](career_targets.md) | 四種職缺的工作內容與要求、每週對各職缺的重要性、作品集規劃、開課前清單 |
| [glossary.md](glossary.md) | 術語對照：English／台灣用語／repo 用語，以及全課程縮寫表 |
| [progress.md](progress.md) | 進度、成績、作業、回爐清單 |
| [quizzes/00_diagnostic_pretest.md](quizzes/00_diagnostic_pretest.md) | 診斷前測（24 題，開課前做） |
| `question_bank/` | 題庫（每週一個 JSON 檔） |
| `wNN/` | 各週講義。已有：[W1](w01/README.md) |

## 每天怎麼用

在 Claude Code 裡對 Claude 說一句話就好，它會依 `.claude/skills/` 裡的兩個技能照流程做：

| 你說 | Claude 做的事 | 技能 |
| --- | --- | --- |
| 「準備今天的課」「做 w01-l2 的講義」 | 讀課綱與指定文章 → 出題入庫 → 產生講義 HTML → 檢查 | `course-handout` |
| 「開始今天的小考」「考我到期的題目」 | 一題一題問、你答完才評分、記錄並排下次複習 | `quiz-coach` |
| 貼上講義頁面的 `AIFQ1\|…` 成績字串 | 入帳，抽查自評有沒有偏鬆 | `quiz-coach` |
| 「出這週的週測」「期中考」 | 依藍圖組卷、監考、評分 | `quiz-coach` |
| 「批改我的作業 A3」 | 依評分規準給級分與修改建議 | `quiz-coach` |
| 「我的進度如何？哪裡最弱？」 | 統計得分率、校準、回爐清單 | `quiz-coach` |
| 「模擬面試，TAM 場」 | 英文角色扮演＋書面回饋 | `quiz-coach` |

一天的固定順序（90 分鐘）：

1. 暖身回想：到期的複習題（10 分）
2. 預測題：還沒學先猜（5 分）
3. 讀講義＋必讀文章（45 分）
4. 課後閉卷小考（15 分）
5. 一句話總結、自己的類比、英文 60 秒錄音（15 分）

兩種上課方式可以混用：在講義頁面上自己作答再貼成績給 Claude（自助），或全程在對話裡由 Claude 口頭考（較嚴格，建議每週至少兩天這樣做）。

## 幾件要知道的事

- **進度要 push 才會留下來。** 在雲端工作階段上課時，容器是暫時的。每次結束前請 Claude commit、push；而且每個新的工作階段會開在新的分支上，所以要把前一次的分支合併回 `main`，下一次才看得到進度。嫌麻煩的話，改在本機用 Claude Code 上課，進度就留在本機的 repo 裡。
- **講義可以用便宜一點的模型產生。** 兩個技能把流程、版型與檢查都固定下來了，品質主要由腳本的檢查把關。建議講義用 Opus 等級的模型；單純的抽考與入帳用更小的模型也可以。
- **數字有時效。** repo 文章裡的價格、模型、財報數字多為 2026 年 8–9 月時點，講義會標出時點與口徑。面試前引用任何數字，請回到原始出處確認。
- **課綱的預設值可以改。** 開課日、每週時數、是否考認證都寫在 syllabus.md 開頭；告訴 Claude 你要怎麼改，它會依課綱第八節的規則重排。

## 維護工具

```bash
# 題庫檢查、到期題目、統計
python3 .claude/skills/quiz-coach/scripts/quiz.py lint
python3 .claude/skills/quiz-coach/scripts/quiz.py due
python3 .claude/skills/quiz-coach/scripts/quiz.py stats

# 講義檢查；版型更新後同步到所有講義
python3 .claude/skills/course-handout/scripts/handout.py check 00_study_plan/w01/*.html
python3 .claude/skills/course-handout/scripts/handout.py sync
```
