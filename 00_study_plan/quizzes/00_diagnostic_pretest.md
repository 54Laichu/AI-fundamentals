# 診斷前測（開課前，不計分）

> 閉卷、限時 40 分鐘、共 24 題（六個領域各 4 題）。不會的題目也請寫下你的猜測——先猜再學，之後會記得更牢。每題先寫答案與信心，全部寫完才展開參考答案自評 0–3 分，再把成績交給 Claude 入帳。這份前測不計入成績；結業前會再考一次，用來衡量進步幅度。

## 第 1 題　`d00-q01`｜比較

【晶片】CPU 與 GPU 在設計目標上差在哪？各適合什麼樣的工作？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

CPU 為多工與快速的循序處理而設計：少量但很強的核心，重視單一任務的低延遲。GPU 用大規模平行架構換取高運算吞吐：大量較簡單的核心同時做同一種運算。AI 的矩陣運算高度平行，所以適合 GPU；分支多、平行度低的工作仍適合 CPU，實務上是兩者搭配的異質運算。

- CPU：少量強核心，擅長循序與多工、低延遲
- GPU：大量平行，追求吞吐
- AI 的矩陣運算高度平行，因此適合 GPU

出處：`01_hardware_architecture/nvidia/understand_gpu_architecture/01_gpu_characteristics.md`

</details>

## 第 2 題　`d00-q02`｜解釋

【晶片】為什麼 LLM 推論的速度常被「記憶體頻寬」卡住，而不是被算力卡住？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

逐字生成（decode）時，每產生一個 token 都要把模型權重與整份 KV Cache 從記憶體讀過一遍，但每次真正做的運算量相對小。於是每秒能生成幾個 token，主要取決於每秒能從 HBM 讀出多少資料。GPU 算力每代成長很快，記憶體頻寬跟不上，就成了瓶頸。

- decode 每個 token 都要讀一遍權重與 KV Cache
- 讀取的資料量大、運算量相對小
- 所以記憶體頻寬決定 tokens/s

出處：`01_hardware_architecture/performance/01_hbm_evolution.md`

</details>

## 第 3 題　`d00-q03`｜回想

【晶片】HBM 是什麼的縮寫？它和消費級顯示卡用的 GDDR 在封裝方式上差在哪？資料中心 GPU 為什麼選它？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

High Bandwidth Memory。HBM 把多層 DRAM 做 3D 堆疊，再透過矽中介層（interposer）緊貼 GPU 封裝；GDDR 則是平面排在電路板上。資料中心 GPU 選 HBM 是因為頻寬需求壓過成本考量。

- High Bandwidth Memory
- 3D 堆疊並與 GPU 封裝在一起，GDDR 是平面排在板上
- 選它是為了頻寬，代價是成本與產能

出處：`01_hardware_architecture/performance/01_hbm_evolution.md`

</details>

## 第 4 題　`d00-q04`｜比較

【晶片】訓練（training）與推論（inference）這兩種工作負載，對基礎設施的要求有什麼不同？各說兩點。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

訓練：長時間、整批的工作，追求總吞吐與擴展性，多卡多節點之間要頻繁同步，所以非常吃節點間網路；會定期寫大型 checkpoint。推論：面對即時請求，受延遲與服務水準（SLO）約束，全年無休，衡量的是每個 token 的成本；瓶頸常在記憶體容量與頻寬。

- 訓練：追求吞吐與擴展，重度依賴節點間高速網路
- 推論：受延遲與 SLO 約束，看每 token 成本
- 兩者的瓶頸與衡量指標不同

出處：`09_inference_system/reference_design/01-背景与目标.md`

</details>

## 第 5 題　`d00-q05`｜回想

【互連】NVLink 是什麼？伺服器裡已經有 PCIe 了，為什麼還需要它？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

NVLink 是 NVIDIA 專為 GPU 之間（以及 GPU 與 CPU 之間）設計的高速互連。PCIe 是通用匯流排，頻寬不足以支撐多張 GPU 之間大量交換資料；NVLink 提供高出許多的 GPU 對 GPU 頻寬，搭配 NVSwitch 可以把多張 GPU 連成一個像單一大型 GPU 的系統。

- GPU 對 GPU 的專用高速互連
- PCIe 是通用匯流排，GPU 間頻寬不夠
- 搭配 NVSwitch 把多張 GPU 連成一個域

出處：`01_hardware_architecture/nvlink/nvlink_intro.md`

</details>

## 第 6 題　`d00-q06`｜解釋

【互連】RDMA 為什麼比傳統的 TCP/IP 網路快？說出它的三個關鍵特性。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

零複製（zero copy）：資料直接在應用程式的記憶體之間傳輸，不經核心緩衝區複製。核心旁路（kernel bypass）：繞過作業系統核心，省掉上下文切換。硬體卸載：傳輸協定由網路卡處理，不佔用主機 CPU。

- 零複製
- 核心旁路
- 協定處理卸載到網路卡硬體

出處：`03_ai_cluster_ops/02_infiniband/01_ib_network_theory.md`

</details>

## 第 7 題　`d00-q07`｜比較

【互連】AI 叢集的後端網路選 InfiniBand 還是 Ethernet（RoCE）？各說出一項主要優勢與一項主要顧慮。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

InfiniBand：為 HPC 與 AI 設計，原生無損、延遲低、調校成熟；顧慮是生態較封閉、供應商選擇少、需要專門的維運技能。Ethernet（RoCE）：生態開放、供應商多、和既有資料中心網路與人員技能相容；顧慮是要靠額外的流量控制與壅塞控制機制才能做到無損，調校較費工。

- InfiniBand：原生無損與低延遲
- InfiniBand 的顧慮：生態與供應商較集中
- Ethernet：開放、多供應商、與既有網路相容，但無損需要額外調校

出處：`03_ai_cluster_ops/02_infiniband/01_ib_network_theory.md`

</details>

## 第 8 題　`d00-q08`｜回想

【互連】用一句話分別解釋 scale-up 與 scale-out，並各舉一種對應的互連技術。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

Scale-up：在單一節點或單一機櫃內，把更多 GPU 緊密連成一個更大的系統，例如 NVLink／NVSwitch。Scale-out：用網路把許多節點或機櫃連成叢集，例如 InfiniBand 或 Ethernet。

- scale-up：把單一系統做大（節點內或機櫃內）
- scale-out：把許多系統用網路連起來
- 技術對應正確：NVLink 對 scale-up，InfiniBand／Ethernet 對 scale-out

出處：`01_hardware_architecture/nvlink/nvlink_intro.md`

</details>

## 第 9 題　`d00-q09`｜回想

【資料中心】PUE 的公式是什麼？數值越接近多少越好？PUE 1.5 代表什麼？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

PUE（Power Usage Effectiveness）＝ 機房總用電 ÷ IT 設備用電。越接近 1 越好。PUE 1.5 代表每 1 瓦送進 IT 設備，機房另外要花 0.5 瓦在冷卻、配電損耗等非 IT 用途。

- 總用電 ÷ IT 設備用電
- 越接近 1 越好
- 1.5 表示有相當於 IT 用電一半的額外開銷

出處：`外部：The Datacenter as a Computer（3rd ed.）Ch.5`（定義不隨時間變動）

</details>

## 第 10 題　`d00-q10`｜解釋

【資料中心】為什麼新一代機櫃級 AI 系統幾乎都要用液冷？從單櫃功率的數量級說起。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

傳統企業機櫃約十幾 kW 以內，氣冷足以應付；機櫃級 AI 系統的單櫃功率已到 100 kW 以上。空氣能帶走的熱量有限，要靠極大的風量與風扇耗電才撐得住；液體的帶熱能力高出空氣許多，把冷卻液直接送到晶片上的冷板（DLC）才能在這種密度下散熱。

- 單櫃功率從十幾 kW 級升到 100 kW 以上
- 空氣帶熱能力不足
- 液冷（冷板直接接觸晶片）帶熱效率高，才能支撐這種密度

出處：`外部：NVIDIA NVL72 公開規格與 The Datacenter as a Computer Ch.4`（功率為數量級，查於 2026-11；精確數字依機型而異，W4 再核對）

</details>

## 第 11 題　`d00-q11`｜計算

【資料中心】某機房可供 IT 設備使用的電力是 1 MW，PUE 為 1.3。（a）機房總用電是多少？（b）若每個機櫃耗電 130 kW，最多能放幾櫃？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

（a）總用電 ＝ 1 MW × 1.3 ＝ 1.3 MW。（b）1,000 kW ÷ 130 kW ≈ 7.7，最多放 7 櫃（櫃數只能無條件捨去，實務上還要留餘裕）。

- 總用電 1.3 MW
- 最多 7 櫃
- 知道櫃數要用 IT 電力算，而不是用總用電算

出處：`外部：The Datacenter as a Computer（3rd ed.）Ch.5`（教學用假設數字）

</details>

## 第 12 題　`d00-q12`｜解釋

【資料中心】一座賣 token 的推論叢集，成本最大項通常是什麼？這對營運的首要目標有什麼含意？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

硬體折舊。以 repo 引用的白皮書案例，折舊約佔六成，電費約 8%。折舊不管機器有沒有在忙都照算，所以首要目標是把利用率與單卡吞吐拉高，讓同樣的折舊攤到更多 token 上。

- 最大項是折舊
- 電費佔比遠小於折舊
- 含意：利用率與吞吐是第一槓桿

出處：`99_misc/token_factory_talk/talk-illustrated.md（頁 07）`（2026-09，白皮書單一案例口徑）

</details>

## 第 13 題　`d00-q13`｜解釋

【軟體與維運】nvidia-smi 顯示 GPU-Util 100%，代表這張卡的算力被用滿了嗎？這個數字實際上量的是什麼？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

不代表。GPU-Util 量的是過去一段取樣時間內，「有任何 kernel 在執行」的時間比例。只要一直有工作在跑就會顯示 100%，即使只用到一小部分運算單元、甚至只是在做記憶體複製。要判斷算力是否用滿，得看更細的指標（例如 DCGM 提供的 SM 活躍度）。

- 不代表算力用滿
- 量的是取樣期間內有 kernel 在執行的時間比例
- 要看更細的指標才能判斷真實負載

出處：`03_ai_cluster_ops/01_gpu_ops/02_gpu_utilization_myth.md`

</details>

## 第 14 題　`d00-q14`｜回想

【軟體與維運】要讓容器裡的程式用到宿主機的 GPU，從宿主機到 Kubernetes 需要哪些元件？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

宿主機要裝 NVIDIA 驅動程式；NVIDIA Container Toolkit 負責在容器啟動時把 GPU 裝置與驅動函式庫掛進容器；容器映像檔內要有對應版本的 CUDA 使用者態函式庫。在 Kubernetes 上還需要 device plugin 把 GPU 回報成可排程的資源。

- 宿主機的 NVIDIA 驅動程式
- NVIDIA Container Toolkit 把裝置與函式庫注入容器
- Kubernetes 需要 device plugin 回報 GPU 資源

出處：`02_gpu_programming/01_environment/01_nvidia_container_setup.md`

</details>

## 第 15 題　`d00-q15`｜比較

【軟體與維運】MIG 與 time-slicing 都能讓多個工作共用一張 GPU。兩者在隔離性上差在哪？各適合什麼情境？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

MIG 在硬體層把一張 GPU 切成數個獨立實例，各有專屬的記憶體與運算資源，彼此隔離，適合多租戶或需要效能保證的推論服務；限制是切法固定、只有部分型號支援。Time-slicing 讓多個工作輪流使用整張 GPU，沒有記憶體隔離，會互相影響，適合開發測試這類不要求保證的輕量工作。

- MIG：硬體層級切分，記憶體與運算隔離
- time-slicing：輪流使用，沒有記憶體隔離
- 情境對應：MIG 用於多租戶與有保證需求，time-slicing 用於開發測試

出處：`04_cloud_native_ai_platform/gpu_manager/02_virtualization.md`

</details>

## 第 16 題　`d00-q16`｜情境

【軟體與維運】你是 TAM。客戶早上來信：「昨晚開始，訓練吞吐掉了 30%，程式沒改。」你的前三個動作是什麼？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

一、先回覆並界定範圍：確認收到、問清楚影響範圍（所有工作或單一工作、所有節點或特定節點）、昨晚前後有什麼變更（韌體、驅動、排程、機房事件）。二、由下往上查硬體與網路健康：GPU 是否有錯誤事件、過熱降頻、掉卡；節點間網路是否有連結降速或錯誤計數上升。三、用標準測試比對基準線（例如集合通訊的基準測試），把問題定位到單機還是網路，並約定下一次更新的時間。

- 先回應客戶並界定影響範圍與變更點
- 有順序地查 GPU 健康與網路健康
- 用基準測試對照基準線來定位，並給出下一次更新時間

出處：`03_ai_cluster_ops/README.md`

</details>

## 第 17 題　`d00-q17`｜回想

【LLM 與推論】什麼是 token？為什麼 AI 服務用它來計費？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

token 是模型處理文字的基本單位，通常是一個字、一個子詞或一個符號。模型的運算量與輸入、輸出的 token 數直接相關，而且 token 數可以精確計數，所以它同時是資訊單位、算力消耗單位與計費單位。

- 模型處理文字的基本單位（字或子詞）
- 運算量與 token 數直接相關
- 可精確計數，所以適合當計費單位

出處：`06_llm_theory_and_fundamentals/llm_basic_concepts/token/llm_token_intro.md`

</details>

## 第 18 題　`d00-q18`｜解釋

【LLM 與推論】KV Cache 是什麼？它用什麼換什麼？它的大小隨什麼成長？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

模型生成每個新 token 時都要參考前面所有 token。KV Cache 把前面 token 在注意力機制中算出的 key 與 value 存起來，之後不必重算。這是用記憶體換運算。它的大小隨上下文長度線性成長（也和層數、模型寬度、同時服務的請求數成正比），所以長上下文與高併發會很快吃光 GPU 記憶體。

- 存下先前 token 的 key／value，避免重算
- 以記憶體換運算
- 大小隨上下文長度（與併發數）線性成長

出處：`09_inference_system/kv_cache/01_concepts/01_basic/01_kv_cache_basics.md`

</details>

## 第 19 題　`d00-q19`｜回想

【LLM 與推論】TTFT 與 ITL（或 TPOT）各是什麼？分別主要由推論的哪個階段決定？

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

TTFT（Time To First Token）是送出請求到收到第一個 token 的時間，主要由排隊與 prefill（處理整段輸入）決定。ITL（Inter-Token Latency，或 TPOT，Time Per Output Token）是相鄰兩個輸出 token 的間隔，主要由 decode（逐字生成）決定。

- TTFT：到第一個 token 的時間，取決於排隊與 prefill
- ITL／TPOT：輸出 token 之間的間隔，取決於 decode
- 兩者分屬不同階段，要分開量

出處：`09_inference_system/reference_design/05-性能评估指标体系.md`

</details>

## 第 20 題　`d00-q20`｜計算

【LLM 與推論】一個 70B（700 億）參數的模型，權重以 FP16 載入需要多少記憶體？量化成 4-bit 之後呢？（只算權重）

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

FP16 每個參數 2 bytes：70×10⁹ × 2 ＝ 140 GB。4-bit 每個參數 0.5 byte：70×10⁹ × 0.5 ＝ 35 GB。實際部署還要加上 KV Cache 與執行時的額外開銷。

- FP16 約 140 GB
- 4-bit 約 35 GB
- 知道這只是權重，還要加 KV Cache 與其他開銷

出處：`09_inference_system/memory_calc/memory_analysis.md`（算術題，不隨時間變動）

</details>

## 第 21 題　`d00-q21`｜回想

【GTM 與客戶】什麼是產品定位（positioning）？說出構成定位的要素（盡量多）。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

定位是界定你的產品在哪一件特定的事情上、對哪一群特定的客戶是最好的選擇。April Dunford 的框架有五個要素：競爭替代方案（客戶不用你會用什麼）、獨特屬性（你有而對手沒有的）、價值（這些屬性為客戶帶來什麼）、目標客戶（最在意這個價值的人）、市場類別（讓價值顯而易見的參考框架）。

- 定位 ＝ 對誰、在什麼事情上、相對於誰是最佳選擇
- 說得出至少三個要素：替代方案、獨特屬性、價值、目標客戶、市場類別
- 知道起點是競爭替代方案而不是產品功能

出處：`外部：April Dunford, Obviously Awesome`（框架，不隨時間變動）

</details>

## 第 22 題　`d00-q22`｜比較

【GTM 與客戶】Product Marketing Manager 與 Technical Marketing Manager 的工作差在哪？各舉兩項典型產出。

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

PMM 決定產品對誰說什麼、怎麼上市：典型產出是 positioning 與 messaging、launch plan、battlecard、sales deck。TMM 把產品的技術事實變成可信的對外證據：典型產出是 benchmark 報告、reference architecture、技術白皮書、demo。PMM 偏策略與訊息，TMM 偏技術深度與驗證。

- PMM：定位、訊息與上市策略
- TMM：技術證據與深度內容
- 各能舉出兩項正確的典型產出

出處：`00_study_plan/career_targets.md`

</details>

## 第 23 題　`d00-q23`｜情境

【GTM 與客戶】業務轉來一則消息：「競品說他們的推論效能是我們的兩倍。」在回應之前，你要先問清楚哪些事？（至少四項）

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

一、測什麼：哪個模型、多長的輸入輸出、什麼工作負載。二、怎麼配：硬體型號與數量、軟體與驅動版本、是否做了量化或其他有損最佳化。三、量什麼：是吞吐還是延遲，有沒有服務水準限制（不設延遲上限的吞吐沒有比較意義）。四、怎麼比：是每張卡、每瓦還是每一塊錢。五、誰量的：廠商自己還是第三方，能不能重現。

- 工作負載與模型是否相同
- 硬體與軟體配置、是否量化
- 指標定義與有無 SLO 限制
- 正規化基準（每卡／每瓦／每元）與可否重現

出處：`09_inference_system/kv_cache/08_methodology/01_kv-cache-perf-methodology.md`

</details>

## 第 24 題　`d00-q24`｜定位

【GTM 與客戶】英文口說 60 秒（請錄音）：Explain to a non-technical executive what an "AI factory" is.

我的答案：＿＿＿＿　　信心（1 猜的 / 2 大概 / 3 確定）：＿＿

<details>
<summary>作答後才展開：參考答案與給分要點</summary>

參考講法："An AI factory is a data center built for one job: turning electricity into AI output. Power goes in, and tokens — the units of text, code or images a model produces — come out. Unlike a traditional data center that hosts many applications, it's measured like a production line: how many tokens it produces per watt, and at what cost. Because a site's power is fixed once it's built, efficiency is the only way to grow output — and that's what the hardware, cooling and software choices are all about."

- 有清楚的定義：電力進、token 出
- 用非技術聽眾聽得懂的比喻或對比
- 點出衡量方式（每瓦產出或每 token 成本）
- 60 秒內結束，英文流暢

出處：`99_misc/token_factory_talk/talk-illustrated.md（頁 03）`

</details>

---

作答完把每題的「題號、得分 0–3、信心 1–3」交給 Claude 入帳（`quiz-coach` skill）。
