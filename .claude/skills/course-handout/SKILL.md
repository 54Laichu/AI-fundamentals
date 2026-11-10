---
name: course-handout
description: 為 00_study_plan 讀書計畫編排一課的視覺化講義（單檔 HTML）與該課題庫。只要使用者說「做講義」「編講義」「上今天的課」「準備 w03-l2」「下一課」「產生第 N 週教材」「幫我把這篇文章變成一課」，或提到課號（wNN-lK）並想要教材，就使用本技能——即使沒有說出「講義」兩個字。也用於修改既有講義、補圖、依錯題重教某個概念。不用於出考卷、口頭抽考或登記成績（那是 quiz-coach）。
---

# course-handout：一課講義的編排流程

你在替一位正在轉職的學員編教材。他的目標是 12 週內能應徵外商的 Technical Marketing Manager、AI Evangelist、Product Marketing Manager 或 Technical Account Manager（AI infrastructure／GPU／data center）。他每天只有 90 分鐘，教材是這個 repo 裡的簡體中文技術文章——寫給工程師看的，又長又深。你的工作是把一課的指定閱讀，編成一份他能在 45 分鐘內讀完、而且**一個月後還記得**的講義。

成品是兩樣東西：`00_study_plan/question_bank/wNN.json` 裡的 10–12 題，以及 `00_study_plan/wNN/wNN-lK_<slug>.html` 一份單檔講義。

## 為什麼講義長這個樣子

版型的九個步驟不是排版偏好，是照《Make It Stick》與 Willingham《學生為什麼不喜歡上學？》排的，順序不能換：

- **先考再教**（STEP 1 暖身回想、STEP 2 預測題）。把舊知識拉出來一次，比重讀十次有效；還沒學就先猜，猜錯也會讓接下來的學習更深。所以預測題不能附答案，也不能放在內容後面。
- **一課最多五件事**（STEP 4）。工作記憶很小。原文有二十個重點時，你的價值在於挑出三到五個，其他的忍痛捨棄或放到延伸閱讀。
- **每件事配一張圖和一個類比**。人是靠「連到已經懂的東西」來理解的；圖與文字各走一條記憶通道。
- **每件事後面一個檢查點**。讀起來很順不代表會了，檢查點讓讀者發現自己其實答不出來。
- **記憶是思考的殘留物**。讀者記住的是他當時在想的東西。所以題目與檢查點要逼他想「為什麼」「差在哪」「客戶會怎樣」，不要讓他想「那個數字是多少」以外沒別的。
- **學完再考、隔幾天再考**（STEP 8 與題庫）。課後題進入 1-3-7-14-30 天的間隔排程，那是 quiz-coach 的工作；你的責任是把題目出好、放進題庫。

理解了這些，遇到版型沒規定的情況，你就知道該怎麼判斷。

## 流程

### 1. 查課綱

打開 `00_study_plan/syllabus.md`，找到該課那一列，取得：日期、主題、核心問題、必讀文章、當週主題。再看 `00_study_plan/assessment.md` 第七節該週的「必考概念」。使用者只說「今天的課」或「下一課」時，用今天日期對課綱，或看 `00_study_plan/progress.md` 最後完成到哪。

課綱沒有的課不要自己發明；跟使用者確認，或先更新課綱。

### 2. 讀原文

把必讀文章**從頭到尾讀完**（長文分段讀），不要只看標題和前幾段就動筆。邊讀邊記：

- 這一課的三到五個核心主張是什麼（對照必考概念，確定都涵蓋到）。
- 每個數字的出處、時點、口徑（廠商自己說的，還是第三方實測）。
- 原文有哪些圖表、比喻可以轉用。
- 原文沒講、但回答核心問題需要的東西——這些要標成「外部」並找可靠來源，或直接告訴使用者有缺口。

事實以原文為準。原文沒有的數字不要憑印象補；非補不可時，在圖說標明「非 repo 出處」與查閱日期。原文是簡體中文與中國大陸用語，寫進講義時轉成繁體與台灣用語（對照 `00_study_plan/glossary.md`），專有名詞第一次出現寫成「中文（English）」。

GTM 職能課（每週 L5）的來源是書而不是 repo。依課綱指定的書與章節，寫你確定的框架內容；不確定的細節不要編，改成請學員讀該章時自己找答案的檢查點。

### 3. 先出題，再寫講義

先把題目寫進題庫，原因是：題目定義了「這一課要學會什麼」，先有題目，內容才不會寫散。

在 `00_study_plan/question_bank/wNN.json` 的陣列裡加入本課 10–12 題（檔案不存在就新建一個 JSON 陣列）。欄位與出題守則見 `00_study_plan/assessment.md` 第二節與第八節，重點：

- `use`：3 題 `pre`（預測題，選「不學也猜得出一個答案、但多半會猜錯」的題）、6–8 題 `post`、其餘 `bank`（留給週測）。
- 題型至少四種，一定要有一題 `calc` 或 `scenario`，以及一題英文 `pitch`。
- `keypoints` 2–4 點，每點可獨立判斷對錯；`answer` 寫成你希望學員說得出口的樣子。
- 含數字的答案要有 `asof`（時點與口徑）。`calc` 題用假設數字時，在 `asof` 說明是假設。
- `source` 寫 repo 相對路徑（可在後面用全形括號註明段落）；書或網路資料以「外部：」開頭。

寫完執行：

```bash
python3 .claude/skills/quiz-coach/scripts/quiz.py lint
```

### 4. 建立講義檔

```bash
python3 .claude/skills/course-handout/scripts/handout.py new w01-l2 \
  --slug cpu-vs-gpu --title "CPU vs GPU：為什麼 AI 需要大量平行運算" \
  --date 2026-11-17 --theme "W1 AI 工廠全景與 GPU 基礎" \
  --question "CPU 與 GPU 的設計取捨差在哪？哪類工作負載 GPU 反而不划算？"
```

產生的檔案裡每個區段都有註解說明要放什麼。CSS 與 JS 在標記區塊內，不要改；所有視覺都用既有元件組出來。

### 5. 填內容

開始寫之前，先讀一遍示範講義 `00_study_plan/w01/w01-l1_ai-factory-overview.html` 的 `<main>` 部分，它示範了每個區段的份量與語氣。圖的寫法查 `references/components.md`。

各區段的要求：

| 區段 | 內容 | 注意 |
| --- | --- | --- |
| STEP 1 暖身 | 2–3 題**先前課次**的題目空殼（`data-kind="R"`） | 優先挑和今天主題有關聯的舊題，讓新舊知識接上；用 `quiz.py due` 看哪些到期 |
| STEP 2 預測 | 本課 3 題 `pre` 的空殼（`data-kind="P"`） | — |
| STEP 3 情境 | 一則具體情境：誰、什麼場合、問了什麼 | 150 字內；用面試或客戶現場，不要用「隨著 AI 快速發展」這種開頭 |
| STEP 4 概念 | 3–5 個 `article.concept` | 每個都有一句主張、一張圖、一個檢查點；全課至少兩個類比 |
| STEP 5 動手算 | 一題帶步驟的估算或一個完整案例 | 數字要和課後 `calc` 題不同，否則等於洩題；步驟收在 `details.check` |
| STEP 6 誤解 | 2–3 個「很多人以為…其實…」 | 選面試或客戶現場真的會出現的誤解 |
| STEP 7 英文 | 60 秒英文講法（80–200 字）、片語對照、一則反問與回應 | 寫成口語，句子短；不要逐句翻譯中文 |
| STEP 8 小考 | 3 題預測題重答＋6–8 題 `post`（都是 `data-kind="Q"`） | 只放空殼 |
| STEP 9 收尾 | 版型已備好，只需填「明天」那一行 | — |
| 術語 | 本課新詞至少 5 列 | 三欄對照：English／台灣用語／repo 用語 |
| 出處 | 必讀與引用過的文章 | repo 檔案用 `<a class="repo" data-path="…"></a>` |

題目一律只寫空殼，內容由腳本從題庫帶入，這樣題庫是唯一的版本：

```html
<div class="q" data-qid="w01-l2-q04" data-kind="Q"></div>
```

寫作語氣：像一位懂技術的前輩在跟你解釋，不是教科書。短句。先講結論再講原因。每段只講一件事。不寫「值得注意的是」「綜上所述」這類填充語。

### 6. 帶入題目、檢查、看一眼

```bash
python3 .claude/skills/course-handout/scripts/handout.py fill  00_study_plan/w01/w01-l2_cpu-vs-gpu.html
python3 .claude/skills/course-handout/scripts/handout.py check 00_study_plan/w01/w01-l2_cpu-vs-gpu.html
```

`check` 的「錯誤」全部修掉才算完成；「警告」逐條判斷，不處理的要說得出理由。

腳本檢查得了結構，檢查不了好不好讀。環境有 Playwright 時，截圖自己看一遍（桌機 900px 寬與手機 390px 寬各一張，至少看 STEP 4 的每張圖）：文字有沒有重疊或被切掉、圖是不是真的幫助理解、深色模式看不看得見。沒有 Playwright 就逐一重讀每張圖的原始碼，確認沒有寫死的寬度或顏色。

最後用讀者的眼睛問三個問題：只讀每個概念的主張句，能不能回答這一課的核心問題？有沒有哪個數字說不出來源？遮住答案，課後題是不是真的只靠這份講義就答得出來？

### 7. 收尾

- 更新 `00_study_plan/wNN/README.md`（該週門戶；不存在就照 `00_study_plan/w01/README.md` 的格式建立）：加上這一課的連結與一句話摘要。
- 本課的新術語補進 `00_study_plan/glossary.md`（已有的不重複）。
- 在 `00_study_plan/progress.md` 的「講義進度」表把這一課標為已產生。
- 把講義檔案送給使用者看（有檔案傳送工具時用它並以可渲染方式呈現），用兩三句話說明這一課的重點與建議的上課順序。有任何你無法從原文核實、或原文之間互相矛盾的地方，在這裡講明。
- 使用者要求時才 commit。訊息依 repo 慣例：`docs(study): 新增 w01-l2 講義與題庫`（Conventional Commits、中文描述、scope 用 `study`），不加任何 AI 署名行。

## 一次做多課

使用者要求「產生整週教材」時，一課一課做完整流程（出題 → 講義 → 檢查），不要先把五份講義的骨架都建好再回頭填——後面的課需要引用前面課的題號當暖身題。每完成一課回報一次進度。

## 修改既有講義

- 改題目：改題庫 JSON，再對講義執行 `fill`（會覆寫所有題目區塊）。
- 版型更新後：`handout.py sync` 會把新的 CSS／JS 套到所有講義。
- 依錯題重教：使用者某個概念連錯時，在下一份講義的 STEP 1 之後加一個 `article.concept`，換一個類比、換一張圖重講，不要原文照貼。

## 檔案位置

```
00_study_plan/
  syllabus.md  assessment.md  glossary.md  progress.md
  question_bank/wNN.json          ← 題庫（唯一版本）
  wNN/README.md                   ← 該週門戶
  wNN/wNN-lK_<slug>.html          ← 講義
.claude/skills/course-handout/
  assets/template.html            ← 版型（CSS／JS 的唯一版本）
  references/components.md        ← 圖表元件目錄，畫圖前讀
  scripts/handout.py              ← new / fill / check / sync
```
