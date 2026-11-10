# 目標職缺與能力地圖

> 本檔是課程的「逆向設計」起點：先看職缺要什麼，再決定每週學什麼、做什麼作品。
>
> 下列職責與要求彙整自這四類職缺常見的公開徵才條件，是通則而非特定公司的 JD。**開課前請自己收集 10 份真實 JD**（第五節），用它們校正本檔。

## 一、四種職缺在做什麼

| | Technical Marketing Manager（TMM） | Product Marketing Manager（PMM） | AI Evangelist / Developer Advocate（EVG） | Technical Account Manager（TAM） |
| --- | --- | --- | --- | --- |
| 一句話 | 把產品的技術事實變成可信的對外證據 | 決定產品對誰說什麼、怎麼上市 | 在社群與舞台上讓技術人想用你的產品 | 確保既有大客戶把產品用好、續約、擴大 |
| 主要對象 | 客戶的架構師、內部業務工程師、媒體與分析師 | 買方決策者、業務團隊、通路 | 開發者、研究者、社群 | 客戶的維運主管與工程團隊 |
| 典型產出 | benchmark 報告、reference architecture、白皮書、技術部落格、demo、競品技術比較、reviewer's guide | positioning 與 messaging、launch plan、battlecard、定價與包裝建議、sales deck、客戶案例 | 演講、教學影片、範例程式、技術文章、社群經營、把社群回饋帶回產品 | 帳戶計畫、QBR、技術健檢、升級管理、RCA、續約與擴充建議 |
| 成敗指標 | 內容被業務與客戶採用、PoC 勝率、技術宣稱站得住腳 | pipeline、勝率、上市成效、訊息一致性 | 觸及與採用（下載、活躍開發者、演講評價） | 續約率、擴充營收、客戶滿意度、重大事件處理時間 |
| 技術深度 | 很深，要能自己跑測試、讀懂架構 | 中等，要能跟工程師與客戶對話 | 深，要能現場寫與現場答 | 深且廣，偏維運與除錯 |
| 最吃重的軟實力 | 技術寫作、嚴謹 | 策略思考、跨部門協調 | 公開演講、說故事 | 信任經營、危機溝通 |

四者的共同核心：**技術講得對、對不同對象講得懂、英文講得出來**。這也是本課程 70% 時間放在技術、30% 放在表達與職能的原因。

## 二、AI infra 領域的徵才常見要求

| 類別 | 常見要求 | 本課程對應 |
| --- | --- | --- |
| 領域知識 | GPU 與加速運算、資料中心架構、伺服器、高速網路（InfiniBand / Ethernet）、儲存、液冷 | W1–W4 |
| 軟體堆疊 | Linux、容器與 Kubernetes、CUDA 生態、叢集管理與排程（Slurm / K8s） | W5–W6 |
| AI 工作負載 | LLM 訓練與推論、效能指標、benchmark（如 MLPerf）、sizing | W7–W8、W10 |
| 產業理解 | 競爭格局、供應鏈、hyperscaler / neocloud / enterprise 的需求差異 | W9、W11 |
| 行銷職能 | positioning、messaging、launch、competitive intelligence、sales enablement、content | 每週 L5 |
| 客戶職能 | discovery、PoC、troubleshooting、escalation、QBR、executive communication | W5、W6、W10、W11 的 L5 |
| 溝通 | 英文簡報與寫作、對高階主管與工程師兩種聽眾切換 | 每週英文產出、Capstone |
| 加分 | 相關認證、公開演講或內容創作紀錄、實際跑過 benchmark 或 PoC | NCA-AIIO、作品集 |

## 三、能力矩陣：每週對四種職缺的重要性

● 核心（一定要精熟）　○ 重要　· 了解即可

| 週 | 主題 | TMM | PMM | EVG | TAM |
| --- | --- | --- | --- | --- | --- |
| W1 | AI 工廠全景與 GPU 基礎 | ● | ● | ● | ● |
| W2 | 互連與機櫃級系統 | ● | ○ | ○ | ● |
| W3 | 叢集網路 | ● | ○ | ○ | ● |
| W4 | 電力、散熱、TCO | ● | ● | ○ | ○ |
| W5 | 軟體堆疊與維運 | ○ | · | ○ | ● |
| W6 | 雲原生平台與排程 | ○ | · | ○ | ● |
| W7 | LLM 基礎與訓練 | ● | ○ | ● | ○ |
| W8 | 推論系統與 token 經濟 | ● | ● | ● | ● |
| W9 | 產業與競爭 | ● | ● | ○ | ○ |
| W10 | Benchmark、PoC、技術內容 | ● | ○ | ○ | ○ |
| W11 | Agentic AI 與企業落地 | ○ | ● | ● | ○ |

提前面試或時間不夠時，依目標職缺只保證「●」的週次精熟。

## 四、作品集規劃（結業時挑 6 件）

面試官要看的是證據。每份作業都設計成可以直接放進作品集的形式：

| 作品 | 來自 | 證明什麼 | 最適合的職缺 |
| --- | --- | --- | --- |
| 英文 explainer《Why GPUs for AI》＋錄音 | A1 | 能把技術講給非技術人聽 | EVG、PMM |
| InfiniBand vs Ethernet battlecard | A3 | 競品分析與 objection handling | PMM、TMM |
| 1 MW 推論叢集 TCO 模型＋ executive summary | A4 | 用數字說話、懂客戶的錢 | TMM、PMM、TAM |
| RCA 報告＋客戶狀態更新信 | A5 | 危機溝通與技術嚴謹 | TAM |
| Discovery 問題清單＋參考架構 | A6 | 懂得先問再賣 | TAM、TMM |
| 5 分鐘 lightning talk 錄影 | A7 | 舞台表現 | EVG |
| Sizing 提案 | A8 | 能做 presales 等級的估算 | TMM、TAM |
| 完整 battlecard（含 ICP） | A9 | 策略思考 | PMM |
| Solution brief＋ benchmark 批判 | A10 | 技術寫作、不被數字唬住 | TMM |
| Launch plan 或 account plan | A11 | 能規劃而不只是執行 | PMM / TAM |
| Capstone 20 分鐘英文演講錄影 | W12 | 綜合實力 | 全部 |

建議組合：

- 投 TMM：A4、A8、A10、A3、A7、Capstone
- 投 PMM：A9、A11（launch）、A3、A4、A1、Capstone
- 投 EVG：Capstone、A7、A1、A10、A8，再加一支自己頻道的公開影片
- 投 TAM：A5、A6、A8、A11（account plan）、A4、Capstone

## 五、開課前要做的事（W0，11/10–11/15）

1. **收集 10 份真實 JD**：四種職缺各 2–3 份，存到 `00_study_plan/jd/`（一份一個 Markdown 檔）。把重複出現三次以上的關鍵字圈出來，和第二節對照；有落差就請 Claude 更新本檔與課綱。
2. **寫現況履歷的落差清單**：現有經歷中，哪些已經能對應上表的「證明什麼」，哪些完全空白。
3. **完成診斷前測**：[quizzes/00_diagnostic_pretest.md](quizzes/00_diagnostic_pretest.md)，閉卷、限時 40 分鐘，把成績交給 Claude 入帳。
4. **列出 8 則 STAR 故事的素材**：先各寫一行標題即可（一次成功、一次失敗、一次衝突、一次說服別人、一次從零學會新東西、一次處理客訴、一次跨部門合作、一次主動發起的專案），W11 才定稿。
5. **準備錄音工具**：每週都要錄英文口說，用手機即可，檔案放自己的雲端硬碟，連結記在 progress.md。

## 六、面試題型對照

| 面試關卡 | 會被問什麼 | 在哪裡練 |
| --- | --- | --- |
| 技術深度 | 「解釋 X 的運作」「X 和 Y 差在哪」 | 每日小考的 `explain`、`compare` 題 |
| 白板 | 「畫出一個 AI 叢集的架構」 | `draw` 題、期中考 1 第四大題 |
| 估算 | 「這個需求要幾張 GPU」 | `calc` 題、A8、期中考 2 口頭 sizing |
| 簡報 | 給一個題目做 15–20 分鐘演講 | A7、Capstone |
| 寫作樣本 | 交一份技術文件或行銷文件 | 作品集 |
| 情境 | 「客戶生氣了你怎麼辦」「競品說他們快兩倍」 | `scenario` 題、期末考第三、四大題 |
| 行為 | 「說一個你說服別人的經驗」 | STAR 故事、W12 模擬面試 |
| 產業觀點 | 「你怎麼看未來兩年的競爭」 | 每週日產業動態、W9 |
