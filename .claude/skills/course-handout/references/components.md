# 圖表元件目錄

講義的所有視覺都用版型內建的元件組成，不引用外部圖片、不寫自訂 CSS。這樣每份講義單檔就能開，在手機、深色模式下都正常，十二週的風格也一致。

每張圖都包在 `figure.fig` 裡，並且一定有 `figcaption`：第一句說這張圖要讀者看出什麼，接著寫資料來源與時點。

```html
<figure class="fig">
  <!-- 元件放這裡，可以放兩個（例如公式＋橫條） -->
  <figcaption><b>圖 2</b>　要讀者看出什麼。出處，時點，口徑。</figcaption>
</figure>
```

## 怎麼選

| 你要表達的是 | 用 | 例子 |
| --- | --- | --- |
| 上下分層、誰疊在誰上面 | `stack` | 軟體堆疊、五層架構、網路分層 |
| 先後順序、資料怎麼流 | `flow` | 一次推論的步驟、供電鏈、排查順序 |
| 兩個選項的取捨 | `vs` | InfiniBand vs Ethernet、氣冷 vs 液冷 |
| 幾個要背的關鍵數字 | `nums` | 頻寬、功率、倍數 |
| 比例或大小比較 | `bars` | 成本結構、各世代頻寬 |
| 一條公式，各項有不同性質 | `formula` | 收入公式、KV Cache 大小、PUE |
| 隨時間演進 | `timeline` | GPU 世代、HBM 世代 |
| 多維度對照 | 表格 | 四種 GPU 共享方式 × 四個面向 |
| 以上都不合適的空間關係 | `svg.diagram` | 拓撲圖、曲線示意、晶片內部配置 |

優先用前八種。它們是用 HTML 排的，文字會自動換行、手機上會自動改成直排。SVG 的文字不會換行，容易重疊，只在真的需要畫線、畫位置關係時才用。

一個概念一張圖就夠。圖的作用是讓讀者一眼看到結構；塞太多格子的圖，還不如一張表。

## stack：層疊

寫的時候**由下往上**排（第一個 `.layer` 在最底層），CSS 會反轉顯示。四欄依序是編號、名稱、技術、指標；`.wk` 是名稱下方的小註；`.hl` 強調其中一層。

```html
<div class="stack">
  <div class="layer"><span class="n">①</span><span class="name">驅動程式<span class="wk">宿主機</span></span><span class="tech">NVIDIA driver</span><span class="metric">nvidia-smi</span></div>
  <div class="layer hl"><span class="n">②</span><span class="name">Container Toolkit</span><span class="tech">把裝置與函式庫掛進容器</span><span class="metric">--gpus all</span></div>
  <div class="layer"><span class="n">③</span><span class="name">CUDA 函式庫<span class="wk">容器內</span></span><span class="tech">libcudart、cuDNN</span><span class="metric">版本需相容</span></div>
</div>
```

三到六層最好讀。

## flow：流程

`.node` 與 `.arrow` 交替。節點內用 `<b>` 寫名稱、`<small>` 寫補充。`.hl`（綠）與 `.warm`（橘）用來標出重點或瓶頸。手機上自動變成由上往下。

```html
<div class="flow">
  <div class="node"><b>電網</b><small>高壓</small></div><span class="arrow"></span>
  <div class="node"><b>變壓與 UPS</b><small>轉換損耗</small></div><span class="arrow"></span>
  <div class="node warm"><b>機櫃 PDU</b><small>130 kW／櫃</small></div><span class="arrow"></span>
  <div class="node hl"><b>GPU</b></div>
</div>
```

最多五個節點；更長的流程拆成兩列或改用編號清單。

## vs：對照

左 `.side.a`（灰）放舊的或基準，右 `.side.b`（綠）放新的或主角。內容用 `dl`，兩邊的 `dt` 要一一對應，讀者才能橫向比較。

```html
<div class="vs">
  <div class="side a"><h4>Time-slicing</h4>
    <dl><dt>隔離</dt><dd>無</dd><dt>彈性</dt><dd>高</dd><dt>適合</dt><dd>開發測試</dd></dl></div>
  <div class="side b"><h4>MIG</h4>
    <dl><dt>隔離</dt><dd>硬體層級</dd><dt>彈性</dt><dd>固定切法</dd><dt>適合</dt><dd>多租戶推論</dd></dl></div>
</div>
```

三個以上的選項改用表格。

## nums：數字卡

每張卡三行：`.v` 數字、`.l` 這個數字是什麼、`.s` 出處與時點。**`.s` 不可省略**，`check` 會擋。加 `.warm` 變橘色，用來標示「壞消息」類的數字。

```html
<div class="nums">
  <div class="num"><div class="v">2039 GB/s</div><div class="l">A100 的 HBM2e 記憶體頻寬</div><div class="s">repo：01_hbm_evolution.md，規格 2026-11 核對</div></div>
  <div class="num warm"><div class="v">~0.5 ms</div><div class="l">讀一遍單層 1.07 GB KV Cache 的時間</div><div class="s">同上，估算值</div></div>
</div>
```

一組二到四張。數字要帶單位；倍數用 ×、÷ 開頭。

## bars：橫條

`style="--v:60"` 代表條長 60%。三欄：標籤、條、數值文字。`.warm` 橘色、`.mute` 灰色、預設綠色。比較絕對數值時，把最大值當 100 自己換算，並在數值欄寫真實數字。

```html
<div class="bars">
  <div class="bar warm"><span>折舊</span><i style="--v:60"></i><span>60%</span></div>
  <div class="bar mute"><span>網路</span><i style="--v:10"></i><span>10%</span></div>
  <div class="bar"><span>電費</span><i style="--v:8"></i><span>8%</span></div>
</div>
```

數值相差超過一百倍時橫條會看不見短的那條，改用 `nums` 或表格，並用文字說出倍數。

## formula：公式

每一項一個 `.term`，下方 `<small>` 寫單位或性質；運算符號用 `.op`。`.skill`（綠底）與 `.money`（灰框）可以用來把項目分成兩類。

```html
<div class="formula">
  <span class="term">機房總用電</span><span class="op">÷</span>
  <span class="term skill">IT 設備用電</span><span class="op">＝</span>
  <span class="term">PUE<small>越接近 1 越好</small></span>
</div>
```

## timeline：時間軸

```html
<div class="timeline">
  <div class="tick"><b>V100</b><small>2017 · Volta</small>首次加入 Tensor Core</div>
  <div class="tick"><b>A100</b><small>2020 · Ampere</small>MIG、HBM2e</div>
  <div class="tick"><b>H100</b><small>2022 · Hopper</small>…</div>
</div>
```

年份與規格從原文取，不要憑記憶填。

## 表格

包在 `.tbl` 裡才能在手機上橫向捲動。欄數不超過五欄；每格不超過兩行。

```html
<div class="tbl"><table>
  <thead><tr><th>方式</th><th>隔離</th><th>適合</th></tr></thead>
  <tbody><tr><td>MIG</td><td>硬體</td><td>多租戶</td></tr></tbody>
</table></div>
```

## svg.diagram：自己畫

規則：

- 一律 `class="diagram"`、`viewBox="0 0 720 高度"`（高度 200–360），加 `role="img"` 與 `aria-label`。不要寫 `width`／`height` 屬性。
- 顏色只用 class 或 CSS 變數，不寫色碼：方塊 `class="box"`（可加 `hl`、`warm`），線 `class="wire"`（可加 `hl`），文字預設 14px，次要文字 `class="sub"`。需要其他顏色時寫 `style="stroke:var(--warm)"`、`style="fill:var(--accent)"`。可用變數：`--ink --muted --line --surface --accent --accent-soft --warm --warm-soft --cust --bad`。
- 文字不會自動換行。中文字每個約佔 14px 寬，方塊寬度要算過；一個方塊內最多兩行（主文字＋`sub`）。文字與文字之間至少留 8px。
- 方塊用 `rx="8"` 圓角。箭頭用線加一個小三角 `polygon`，或直接在文字裡用「→」。
- 示意性的曲線（沒有照真實數據畫）要在圖內或圖說寫「示意圖，非等比例」。

```html
<svg class="diagram" viewBox="0 0 720 220" role="img" aria-label="兩張 GPU 經由 NVLink 直接互連，另經 PCIe 連到 CPU">
  <rect class="box" x="290" y="20" width="140" height="48" rx="8"/>
  <text x="360" y="49" text-anchor="middle">CPU</text>
  <rect class="box hl" x="120" y="140" width="160" height="56" rx="8"/>
  <text x="200" y="166" text-anchor="middle">GPU 0</text>
  <text class="sub" x="200" y="184" text-anchor="middle">HBM</text>
  <rect class="box hl" x="440" y="140" width="160" height="56" rx="8"/>
  <text x="520" y="166" text-anchor="middle">GPU 1</text>
  <text class="sub" x="520" y="184" text-anchor="middle">HBM</text>
  <path class="wire" d="M330 68 L210 140 M390 68 L510 140"/>
  <text class="sub" x="232" y="100">PCIe</text>
  <path class="wire hl" d="M280 168 L440 168"/>
  <text x="360" y="160" text-anchor="middle" style="fill:var(--accent)">NVLink</text>
</svg>
```

畫完一定要截圖看，SVG 是最容易出現文字重疊的地方。

## 提示框

不是圖，但常和圖搭配：

```html
<div class="callout analogy"><b>類比</b><p>…</p></div>       <!-- 橘：連到讀者已懂的東西 -->
<div class="callout customer"><b>對客戶</b><p>…</p></div>    <!-- 紫：現場可以直接說的話 -->
<div class="callout warn"><b>誤解：…</b><p>…</p></div>       <!-- 紅：STEP 6 用 -->
<div class="callout story"><b>情境</b><p>…</p></div>         <!-- STEP 3 用 -->
<details class="check"><summary>問題？</summary><p>答案。</p></details>
```

好的類比有兩個條件：讀者本來就熟，而且對應關係講得出來（「廚房是 GPU、便當是 token」）。只有氣氛相似的類比會誤導，寧可不放。

## 引用 repo 既有的互動視覺化

repo 裡有一些現成的互動 HTML（例如 `09_inference_system/prefill_decode/prefill_decode_visual.html`、`09_inference_system/parallelism/parallelism_visual.html`、`06_llm_theory_and_fundamentals/llm_basic_concepts/transformer/transformer_block_visual.html`）。不要嵌入，用 repo 連結指過去，並告訴讀者要看哪一步：

```html
<p>想看動起來的版本：<a class="repo" data-path="09_inference_system/prefill_decode/prefill_decode_visual.html"></a>（需下載後用瀏覽器開啟，逐步按到第 4 步）。</p>
```
