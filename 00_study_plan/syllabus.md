# 課綱：AI Infra GTM 實戰班 —— 從晶片到客戶

> 課程代號 `AIF-GTM-12` · 12 週 · 2026-11-16（一）開課 → 2027-02-04（四）結業 · 課綱版本 v1.0（2026-11-10 訂）
>
> 本檔是整個讀書計畫的**單一事實來源**：講義（`course-handout` skill）與測驗（`quiz-coach` skill）都依本檔的課號、日期、指定閱讀與核心問題產生。要調整進度，先改這裡。

## 一、課程資訊

| 項目 | 內容 |
| --- | --- |
| 學員目標 | 12 週內具備應徵外商 **Technical Marketing Manager（TMM）/ AI Evangelist（EVG）/ Product Marketing Manager（PMM）/ Technical Account Manager（TAM）** 的能力，領域為 AI infrastructure、GPU、data center |
| 教材主體 | 本 repo（簡體中文技術文章，約 600 篇）＋ 下方指定書目與官方文件 |
| 授課方式 | 自學 ＋ Claude 伴讀：每課一份視覺化講義（HTML）、每天閉卷小考、每週累積測驗 |
| 每週投入 | 預設 **約 13 小時**：平日 5 天 × 90 分鐘 ＋ 週六 3 小時 ＋ 週日 2.5 小時 |
| 教學語言 | 講義與測驗以**繁體中文**書寫，專有名詞一律附**英文原文**；每週至少一項英文口說或寫作產出（外商面試以英文進行） |
| 時區與假期 | Asia/Taipei；元旦（2027-01-01）當週減量；春節（除夕 2027-02-05）前結業 |

> **預設值可以改**：開課日、每週時數、是否考 NVIDIA 認證，都是我替你先做的假設。要改時告訴 Claude「把開課日改成 X」或「我每週只有 8 小時」，由它依第八節的規則重排本檔日期。

## 二、學習成果（結業時你要能做到）

| 編號 | 學習成果 | 對應職缺 | 驗收方式 |
| --- | --- | --- | --- |
| LO1 | 徒手在白板畫出 AI 工廠五層架構（晶片 → 節點 → 叢集網路 → 資料中心 → 軟體與工作負載），說出每層的瓶頸與關鍵指標 | 全部 | 期中考 1、Capstone |
| LO2 | 用數字說話：VRAM、KV Cache、tokens/s、kW/rack、TCO、$/M tokens 的 back-of-envelope 估算 | TMM、TAM | 期中考 2、作業 A4/A8 |
| LO3 | 比較並給建議：NVIDIA vs AMD vs ASIC、InfiniBand vs Ethernet、氣冷 vs 液冷、不同推論引擎——依客戶情境下結論 | TMM、PMM | 作業 A3/A9、期末考 |
| LO4 | 產出技術行銷資產：positioning、battlecard、solution brief、benchmark 判讀、launch plan、demo script | PMM、TMM | 作品集 |
| LO5 | 處理客戶技術對話：discovery、故障分級（triage）、RCA、QBR | TAM | 作業 A5/A6/A11 |
| LO6 | 任何一個主題都能用英文講 60 秒 / 5 分鐘 / 20 分鐘三種長度 | EVG、全部 | 每週錄音、Capstone |
| LO7 | 面試就緒：履歷與 LinkedIn、6 件作品集、8 則 STAR 故事、通過兩輪模擬面試 | 全部 | W12 |

職缺拆解與能力缺口分析見 [career_targets.md](career_targets.md)。

## 三、每週節奏

| 時段 | 內容 | 時間 | 學習科學依據 |
| --- | --- | --- | --- |
| 週一～週四（L1–L4 技術課） | ① 暖身回想：到期的間隔複習題（10 分）→ ② 課前預測題（5 分）→ ③ 讀講義＋指定閱讀（45 分）→ ④ 課後閉卷小考（15 分）→ ⑤ 一句話總結＋英文 60 秒口說（15 分） | 90 分 | 提取練習、生成效應、間隔、精緻化 |
| 週五（L5 職能課） | GTM／客戶面技能課（45 分）＋ 本週四課交錯複習（30 分）＋ 作業啟動（15 分） | 90 分 | 交錯練習 |
| 週六 | **週測**（累積、閉卷、45 分）→ 訂正與錯題回爐（30 分）→ 作業（105 分） | 3 小時 | 累積測驗、回饋 |
| 週日 | 作業完成並繳交（90 分）→ Teach-back：不看稿把本週內容講給「客戶」聽，錄音（30 分）→ 產業動態 30 分 | 2.5 小時 | 教中學、反思 |

每課的步驟順序不能調換：**先考、再學、再考**。為什麼這樣排、每個步驟對應兩本書的哪個原則，寫在 [assessment.md](assessment.md) 第一節。

## 四、授課內容與主題

讀法說明：

- 課號格式 `wNN-lK`（第 NN 週第 K 課）。**必讀**一定要在該課讀完；`選讀` 有餘力再看。
- 路徑皆指向本 repo 的簡體中文原文；台灣用語與英文對照見 [glossary.md](glossary.md)。
- repo 文章中的價格、模型、財報數字多為 2026 年 8–9 月時點，引用時依原文標示口徑（廠商口徑 / 獨立實測）與日期。

### 第一階段：地基——從晶片到資料中心（W1–W4）

#### W1（11/16–11/22）AI 工廠全景與 GPU 基礎

本週要能回答的面試題：*"Why do AI workloads need GPUs, and what limits a GPU's performance?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 11/16 一 | w01-l1 | AI 工廠全景：token 經濟與五層堆疊 | 資料中心為什麼被叫做「工廠」？一座 Token 工廠的收入與成本怎麼算？ | [Token Factory 圖文講解](../99_misc/token_factory_talk/talk-illustrated.md)；[硬體架構門戶 §1](../01_hardware_architecture/README.md) |
| 11/17 二 | w01-l2 | CPU vs GPU：為什麼 AI 需要大量平行運算 | CPU 與 GPU 的設計取捨差在哪？哪類工作負載 GPU 反而不划算？ | [GPU 特性](../01_hardware_architecture/nvidia/understand_gpu_architecture/01_gpu_characteristics.md)；[GPU 程式設計導論](../02_gpu_programming/02_cuda/01_gpu_programming_introduction.md) |
| 11/18 三 | w01-l3 | GPU 內部與世代演進：SM、Tensor Core、V100 → A100 → Blackwell | 每一代 GPU 到底進步了什麼？Tensor Core 為什麼是分水嶺？ | [NVIDIA GPU 架構門戶](../01_hardware_architecture/nvidia/README.md)；[A100 架構](../01_hardware_architecture/nvidia/understand_gpu_architecture/07_a100_architecture.md) |
| 11/19 四 | w01-l4 | 記憶體才是瓶頸：VRAM、HBM 與頻寬 | 為什麼 LLM 推論常被記憶體頻寬卡住而不是算力？HBM 為什麼缺貨？ | [GPU 記憶體](../01_hardware_architecture/nvidia/understand_gpu_architecture/02_gpu_memory.md)；[HBM 演進](../01_hardware_architecture/performance/01_hbm_evolution.md) |
| 11/20 五 | w01-l5 | 職能課：四種職缺在做什麼＋定位（positioning）入門 | TMM、PMM、EVG、TAM 的日常與產出差在哪？什麼叫「定位」？ | [career_targets.md](career_targets.md)；*Obviously Awesome* Part 1 |

- 選讀：[V100 架構](../01_hardware_architecture/nvidia/understand_gpu_architecture/03_tesla_v100.md)、[HBF vs HBM](../09_inference_system/hbf-vs-hbm.md)、[哈佛 CS2680 Intro to GPUs（PDF）](../10_ai_related_course/cs2680_modern_ai_systems/10_llm_serving_basics_2a.pdf)
- **作業 A1**（11/22 日 繳交）：一頁英文 explainer《Why GPUs for AI》＋ 90 秒英文錄音。
- **週測 W1**：11/21（六）。

#### W2（11/23–11/29）伺服器內部：互連與機櫃級系統

面試題：*"Walk me through the data path inside an 8-GPU server. Where are the bottlenecks?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 11/23 一 | w02-l1 | PCIe：拓撲、世代與頻寬 | Root Complex、Switch、Endpoint 各是什麼？Gen4/5/6 一條 lane 多快？ | [PCIe 總覽](../01_hardware_architecture/pcie/01_pcie_comprehensive_guide.md)；[PCIe/NVLink 速度速查](../01_hardware_architecture/performance/05_pcie_nvlink_speed_reference.md) |
| 11/24 二 | w02-l2 | NVLink / NVSwitch：GPU 之間的高速公路 | 有了 PCIe 為什麼還要 NVLink？scale-up 與 scale-out 差在哪？ | [NVLink 入門](../01_hardware_architecture/nvlink/nvlink_intro.md)；[NVLink-C2C](../01_hardware_architecture/superchips/nvlink_c2c.md) |
| 11/25 三 | w02-l3 | 資料路徑：DMA、GPUDirect、NUMA | 「繞過 CPU」到底省了什麼？NUMA 配錯會掉多少效能？ | [GPUDirect RDMA 與 Storage](../01_hardware_architecture/gpudirect/01_gpudirect_technology.md)；[AI 基礎設施延遲金字塔](../01_hardware_architecture/performance/ai_latency_pyramid.md) |
| 11/26 四 | w02-l4 | 從 8-GPU 節點到機櫃級系統：GB300 NVL72 | 為什麼部署單位從「伺服器」變成「機櫃」？這對客戶機房意味著什麼？ | [GB300 NVL72 架構解析](../01_hardware_architecture/superchips/nvidia_gb300.md) |
| 11/27 五 | w02-l5 | 職能課：Feature → Benefit → Proof 與 message house | 規格表怎麼翻譯成客戶聽得懂的價值？ | *Obviously Awesome* Part 2–3 |

- 選讀：[PCIe 拓撲層級](../01_hardware_architecture/pcie/06_pcie_topology_hierarchy.md)、[DMA engine](../01_hardware_architecture/dma/01_dma_engine.md)、[PCIe domain 與 NUMA](../01_hardware_architecture/performance/04_pcie_domain_numa.md)、[CXL 總覽](../01_hardware_architecture/pcie/08_cxl_interconnect_overview.md)
- **作業 A2**（11/29）：一頁比較《機櫃級液冷系統 vs 8-GPU 氣冷節點》，含三種客戶情境的建議（battlecard v0）。
- **週測 W2**：11/28（六），含 W1 回爐題。

#### W3（11/30–12/06）叢集網路與高效能通訊

面試題：*"InfiniBand or Ethernet for a 1,000-GPU cluster? How would you advise the customer?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo / 外部） |
| --- | --- | --- | --- | --- |
| 11/30 一 | w03-l1 | RDMA 與 InfiniBand 基礎 | RDMA 為什麼快？Subnet Manager 在做什麼？ | [IB 網路架構與協定](../03_ai_cluster_ops/02_infiniband/01_ib_network_theory.md) |
| 12/01 二 | w03-l2 | Ethernet for AI：RoCE、無損乙太網與 IB 的取捨 | RoCEv2 需要哪些條件才「無損」？兩大陣營各自的賣點？ | [GPUDirect RDMA 驗證](../01_hardware_architecture/gpudirect/04_gpudirect_rdma_verification.md)；外部：NVIDIA Spectrum-X 與 Ultra Ethernet Consortium 官方概覽（見第五節） |
| 12/02 三 | w03-l3 | NCCL 與集合通訊：網路如何決定訓練擴展性 | AllReduce 是什麼？NVLink 與跨節點頻寬差幾倍？ | [NCCL 理論](../03_ai_cluster_ops/03_nccl/01_nccl_theory.md)；[NCCL 通訊路徑逐層壓測](../03_ai_cluster_ops/03_nccl/06_nccl_path_benchmark.md) |
| 12/03 四 | w03-l4 | DPU 與叢集網路拓撲：四張網與 fat-tree | 運算網、儲存網、管理網、對外網各走什麼？DPU 卸載了什麼？ | [DPU 程式設計門戶](../02_dpu_programming/README.md)；[叢集維運門戶](../03_ai_cluster_ops/README.md) |
| 12/04 五 | w03-l5 | 職能課：競品分析與 battlecard | 一張好用的 battlecard 長什麼樣？怎麼寫 objection handling？ | *Loved* Part 1（PMM 的四項基本功） |

- 選讀：[DOCA 程式設計入門](../02_dpu_programming/doca/doca_programming_guide.md)、[NCCL 基準測試方法論](../03_ai_cluster_ops/03_nccl/04_nccl_benchmark.md)
- **作業 A3**（12/06）：《InfiniBand vs Ethernet for AI》battlecard，含 3 則 objection handling。
- **週測 W3**：12/05（六）。

#### W4（12/07–12/13）資料中心：電力、散熱與 TCO ｜ 期中考 1

面試題：*"A customer has 2 MW available. What can they build, and what will a token cost them?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo / 外部） |
| --- | --- | --- | --- | --- |
| 12/07 一 | w04-l1 | 電力：從 kW/rack 到 GW 園區 | 電從電網到晶片經過哪些環節？PUE 怎麼算？為什麼電力成了天花板？ | [資料中心建設熱潮（SemiAnalysis 解讀）](../03_ai_cluster_ops/05_datacenter/china-dc-boom-semianalysis.md)；*The Datacenter as a Computer* Ch.4 |
| 12/08 二 | w04-l2 | 散熱：氣冷極限、DLC、浸沒式與 CDU | 單櫃多少 kW 之後氣冷撐不住？液冷導入要改機房哪些東西？ | *The Datacenter as a Computer* Ch.4–5；[GPU 功耗管理](../02_gpu_programming/04_profiling/04_power_management.md) |
| 12/09 三 | w04-l3 | TCO 與單位經濟：CapEx、OpEx、折舊、$/M tokens | 一座推論叢集的成本結構？每百萬 token 成本怎麼從硬體一路算出來？ | [推論叢集單位經濟](../09_inference_system/cost_analysis/deepseek_inference_cluster_unit_economics.md)；[商業模式與財務](../99_misc/token_factory_talk/references/03-business-model-and-finance.md) |
| 12/10 四 | w04-l4 | 產能與商業模式：Goodput、算力租賃 vs Token 工廠 | 「可售產能」為什麼不等於機器極限？neocloud 的財報怎麼讀？ | [Token 工廠的產能怎麼算](../99_misc/token_factory_talk/cluster-capacity-measurement.md)；[上市公司財報證據](../99_misc/token_factory_talk/references/06-listed-companies.md) |
| 12/11 五 | w04-l5 | 期中考前交錯複習＋職能課：executive summary 寫法 | 怎麼把一張試算表濃縮成主管 30 秒看得懂的三句話？ | W1–W4 錯題；*Made to Stick* 前言與 Ch.1（Simple） |

- 選讀：*The Datacenter as a Computer* Ch.6（Modeling Costs）
- **期中考 1**：12/12（六），範圍 W1–W4，90 分鐘（取代該週週測）。
- **作業 A4**（12/13）：1 MW 推論叢集 TCO 試算表＋一頁 executive summary（英文）。

### 第二階段：軟體堆疊與工作負載（W5–W8）

#### W5（12/14–12/20）GPU 軟體堆疊與叢集維運

面試題（TAM）：*"A customer reports training throughput dropped 30% overnight. How do you triage?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 12/14 一 | w05-l1 | 軟體堆疊：Driver → CUDA → Container Toolkit → 框架 | 容器裡的程式怎麼用到宿主機的 GPU？版本不對會出什麼事？ | [NVIDIA GPU 容器環境](../02_gpu_programming/01_environment/01_nvidia_container_setup.md)；[Container Toolkit 解析](../04_cloud_native_ai_platform/k8s/01_nvidia_container_toolkit_analysis.md) |
| 12/15 二 | w05-l2 | 看得見：nvidia-smi、DCGM 與 GPU 利用率迷思 | GPU-Util 100% 代表算力用滿嗎？該看哪些指標？ | [GPU 利用率是誤導性指標](../03_ai_cluster_ops/01_gpu_ops/02_gpu_utilization_myth.md)；[DCGM 監控](../03_ai_cluster_ops/01_gpu_ops/05_dcgm_monitoring.md) |
| 12/16 三 | w05-l3 | 出事了：健康檢查、Xid 與驅動故障排查 | 一張卡「掉了」的排查順序？哪些要直接走 RMA？ | [GPU 叢集健康檢查](../03_ai_cluster_ops/01_gpu_ops/06_gpu_health_check.md)；[驅動故障速查](../03_ai_cluster_ops/01_gpu_ops/08_gpu_driver_troubleshooting.md) |
| 12/17 四 | w05-l4 | 效能驗收：nvbandwidth、NCCL test 與交付驗收 | 新叢集交付時要跑哪些測試才算驗收？數字多少算正常？ | [nvbandwidth 最佳實踐](../02_gpu_programming/04_profiling/01_nvbandwidth_best_practices.md)；[NCCL 基準測試](../03_ai_cluster_ops/03_nccl/04_nccl_benchmark.md) |
| 12/18 五 | w05-l5 | 職能課：TAM 的工作——triage、escalation、RCA | 嚴重度怎麼分級？RCA 報告的固定結構？壞消息怎麼講？ | *The Trusted Advisor* Ch.1–8（信任方程式） |

- 選讀：[nvidia-smi 場景速查](../03_ai_cluster_ops/01_gpu_ops/03_nvidia_smi_guide.md)、[GPU 忙不忙怎麼判斷](../03_ai_cluster_ops/01_gpu_ops/09_gpu_busy_check.md)、[PCIe AER 監控](../01_hardware_architecture/pcie/04_pcie_aer_monitoring.md)、[NVLink 診斷](../01_hardware_architecture/nvlink/nvlink_diagnostics.md)
- **作業 A5**（12/20）：情境題「GPU fallen off the bus」的 RCA 報告＋給客戶的英文 status update email。
- **週測 W5**：12/19（六）。

#### W6（12/21–12/27）雲原生 AI 平台與排程

面試題：*"How would you let 50 data scientists share 32 GPUs fairly?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 12/21 一 | w06-l1 | Kubernetes 上的 GPU：Device Plugin 與 GPU Operator | K8s 怎麼知道節點有幾張 GPU？`nvidia.com/gpu: 1` 背後發生什麼？ | [K8s Device Plugin 解析](../04_cloud_native_ai_platform/k8s/02_nvidia_k8s_device_plugin_analysis.md)；[GPU 管理基礎理論](../04_cloud_native_ai_platform/gpu_manager/01_basic_theory.md) |
| 12/22 二 | w06-l2 | GPU 共享與虛擬化：MIG、Time-slicing、MPS、HAMi | 四種切法的隔離性與適用情境？ | [GPU 虛擬化](../04_cloud_native_ai_platform/gpu_manager/02_virtualization.md)；[MIG 實作](../01_hardware_architecture/nvidia/mig_hands_on.md) |
| 12/23 三 | w06-l3 | 排程：Gang、拓撲感知與 Slurm vs Kubernetes | 訓練工作為什麼要「全有或全無」？HPC 與雲原生兩派怎麼選？ | [GPU 排程問題](../03_ai_cluster_ops/04_gpu_scheduling/01_gpu_scheduling_problem.md)；[Gang Scheduling](../03_ai_cluster_ops/04_gpu_scheduling/02_gang_scheduling_for_training.md) |
| 12/24 四 | w06-l4 | AI 儲存：平行檔案系統、3FS、GDS | 訓練與推論對儲存的需求差在哪？checkpoint 多大、多久存一次？ | [儲存門戶](../04_cloud_native_ai_platform/storage/README.md)；[GDS 基礎](../01_hardware_architecture/gpudirect/03_gds_basics.md) |
| 12/25 五 | w06-l5 | 職能課：discovery 與 solution mapping | 第一次客戶會議該問哪 10 個問題？怎麼從痛點對到參考架構？ | *Mastering Technical Sales* 中 Discovery 相關章節 |

- 選讀：[拓撲感知排程](../03_ai_cluster_ops/04_gpu_scheduling/03_topology_aware_scheduling.md)、[GPU 共享排程](../03_ai_cluster_ops/04_gpu_scheduling/04_gpu_sharing_scheduling.md)、[KAI vs HAMi](../04_cloud_native_ai_platform/gpu_manager/hami/KAI_vs_HAMi_Comparison.md)、[3FS 設計筆記](../04_cloud_native_ai_platform/storage/deepseek_3fs/01_deepseek_3fs_design_notes.md)
- **作業 A6**（12/27）：客戶 discovery 問題清單（20 題，分技術／商務／決策流程）＋一張參考架構圖。
- **週測 W6**：12/26（六）。

#### W7（12/28–01/03）LLM 基礎與訓練／微調工作負載（元旦週，減量）

面試題：*"Explain to a CFO why the same GPU serves 10x more users with one model than another."*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 12/28 一 | w07-l1 | Transformer 與 token：模型到底在算什麼 | 一個 token 走過模型要做哪些運算？參數量與記憶體怎麼對應？ | [Transformer 架構詳解](../06_llm_theory_and_fundamentals/llm_basic_concepts/transformer/transformer_architecture.md)；[Token 入門](../06_llm_theory_and_fundamentals/llm_basic_concepts/token/llm_token_intro.md) |
| 12/29 二 | w07-l2 | 模型為什麼越來越大卻越來越便宜：Scaling laws、MoE、量化 | MoE 的「稀疏啟動」省了什麼？INT4 量化犧牲了什麼？ | [MoE 圖解](../06_llm_theory_and_fundamentals/llm_basic_concepts/moe/mixture_of_experts_moe_visual_guide.zh-CN.md)；[量化圖解](../06_llm_theory_and_fundamentals/llm_basic_concepts/quantization/visual_guide_to_quantization.md) |
| 12/30 三 | w07-l3 | 訓練 vs 微調 vs RAG：工作負載特徵與硬體需求 | 三種做法各要多少 GPU、多久、什麼網路？客戶該選哪個？ | [SFT 實戰指南](../05_model_training_and_fine_tuning/sft_example/README.md)；[RAG 方案比較](../07_rag_and_tools/rag_basics/rag_comparison.md) |
| 12/31 四 | w07-l4 | 平行策略：DP / TP / PP / EP | 模型大到一張卡放不下時怎麼拆？每種拆法吃哪一種頻寬？ | [平行策略](../09_inference_system/parallelism/parallelism_strategies.md)（搭配同目錄 `parallelism_visual.html`） |
| 01/01 五 | w07-l5 | 職能課：說故事——SUCCESs 與類比庫（元旦，可移至 01/02） | 怎麼讓非技術聽眾記住一個技術概念？ | *Made to Stick* Ch.2–6 |

- 選讀：[Scaling Laws](../06_llm_theory_and_fundamentals/llm_basic_concepts/scaling_laws/scaling_laws.md)、[LLM 架構演進史](../06_llm_theory_and_fundamentals/llm_basic_concepts/architecture_evolution/llm_architecture_evolution.md)、[哈佛 CS2680 Intro to LLM（PDF）](../10_ai_related_course/cs2680_modern_ai_systems/09_llm_serving_basics_1.pdf)、*AI Engineering* Ch.2、Ch.7
- **作業 A7**（01/03）：類比庫 10 則（每個核心概念一個生活類比＋一句英文 soundbite）＋ 5 分鐘 lightning talk 錄影。
- **週測 W7**：01/02（六）。

#### W8（01/04–01/10）推論系統與 Token 經濟學 ｜ 期中考 2

面試題：*"Size an on-prem deployment for 500 concurrent users on a 70B-class model. State your assumptions."*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 01/04 一 | w08-l1 | 一次推論發生什麼：Prefill、Decode 與 KV Cache | 為什麼輸出 token 比輸入 token 貴？KV Cache 佔多少記憶體？ | [Prefill/Decode 計算](../09_inference_system/prefill_decode/prefill_decode_qkv_calculation.md)；[七張圖講透 KV Cache](../06_llm_theory_and_fundamentals/llm_basic_concepts/architecture_evolution/kv_cache_seven_charts.md) |
| 01/05 二 | w08-l2 | 推論引擎：Continuous batching、PagedAttention 與引擎生態 | 引擎替你做了哪三件事？vLLM、SGLang、TensorRT-LLM、NIM 怎麼定位？ | [Continuous Batching](../09_inference_system/prefill_decode/continuous_batching.md)；[PagedAttention](../09_inference_system/kv_cache/01_concepts/01_basic/02_paged_attention.md) |
| 01/06 三 | w08-l3 | 指標與容量規劃：TTFT、ITL、Goodput、VRAM 估算 | 客戶的 SLO 怎麼換算成 GPU 張數？ | [效能評估指標體系](<../09_inference_system/reference_design/05-性能评估指标体系.md>)；[LLM 記憶體分析](../09_inference_system/memory_calc/memory_analysis.md) |
| 01/07 四 | w08-l4 | 降本技術地圖：量化、投機解碼、prefix caching、PD 分離 | 每一招省的是算、存、傳還是時間？哪些能疊加？ | [核心推論最佳化技術](<../09_inference_system/reference_design/03-核心推理优化技术深度解析.md>)；[圖解投機解碼](../09_inference_system/model_optimization/illustrated-speculative-decoding.md) |
| 01/08 五 | w08-l5 | 期中考前交錯複習＋職能課：定價與 $/token 的講法 | API 定價為什麼輸入輸出差這麼多？怎麼對客戶解釋自建 vs 買 API？ | [LLM API 定價分析](../09_inference_system/cost_analysis/llm_api_pricing_analysis.md) |

- 選讀：[KV Cache 基礎](../09_inference_system/kv_cache/01_concepts/01_basic/01_kv_cache_basics.md)、[Prefix Caching](../09_inference_system/kv_cache/01_concepts/02_prefix_caching/02_prefix_caching.md)、[HBM KV 池與併發](../09_inference_system/kv_cache/01_concepts/10_capacity_planning/01_hbm_kv_pool_concurrency.md)、[哈佛 CS2680 LLM serving III（PDF）](../10_ai_related_course/cs2680_modern_ai_systems/11_llm_serving_basics_3.pdf)、*AI Engineering* Ch.9
- **期中考 2**：01/09（六），範圍 W1–W8（W5–W8 佔 70%），100 分鐘，含 15 分鐘口頭 sizing。
- **作業 A8**（01/10）：sizing 提案——金融客戶地端部署 70B 等級模型、500 同時使用者：硬體建議、假設清單、風險。

### 第三階段：市場、競爭與上場（W9–W12）

#### W9（01/11–01/17）產業地圖與競爭格局

面試題：*"Who is our biggest competitive threat in the next 24 months and why?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo / 外部） |
| --- | --- | --- | --- | --- |
| 01/11 一 | w09-l1 | NVIDIA 全棧與路線圖：從晶片到軟體訂閱 | NVIDIA 的護城河有哪幾層？一年一代的節奏對客戶採購的影響？ | [DeepSeek × Blackwell 寬 EP 最佳化](../09_inference_system/vllm/hardware_optimization/deepseek_blackwell_wide_ep.md)；外部：最近一場 GTC keynote 與最近一季法說（見第五節） |
| 01/12 二 | w09-l2 | 挑戰者：AMD、Intel、雲端自研 ASIC、華為昇騰 | 各家的切入點？客戶什麼時候會認真考慮非 NVIDIA 方案？ | [TPU 101](../01_hardware_architecture/tpu/tpu_101.md)；[GPGPU vs NPU 對比](<../01_hardware_architecture/nvidia/GPGPU_vs_NPU_大模型推理训练对比.md>) |
| 01/13 三 | w09-l3 | 供應鏈：先進封裝、HBM 三雄、ODM/OEM 與台灣的角色 | 一台 AI 伺服器從晶圓到機房經過誰的手？瓶頸在哪一站？ | [HBM 演進](../01_hardware_architecture/performance/01_hbm_evolution.md)（W1 回爐）；外部：一家 ODM/OEM 最近一季法說 |
| 01/14 四 | w09-l4 | 買方地圖：Hyperscaler、Neocloud、Sovereign AI、Enterprise | 四類買家的採購邏輯與決策者各是誰？ | [AI Factory 生態](../99_misc/token_factory_talk/references/02-ai-factory-ecosystem.md)；[上市公司財報證據](../99_misc/token_factory_talk/references/06-listed-companies.md)（W4 回爐） |
| 01/15 五 | w09-l5 | 職能課：市場區隔、ICP 與 TAM/SAM/SOM | 怎麼定義 ideal customer profile？技術採用生命週期怎麼用？ | *Crossing the Chasm* Part 1 |

- 選讀：[AMX vs Tensor Core](../01_hardware_architecture/performance/03_amx_vs_tensorcore.md)、[NPU 程式設計門戶](../02_npu_programming/README.md)、[Jevons 悖論與需求](../99_misc/token_factory_talk/references/05-jevons-demand-future.md)
- **作業 A9**（01/17）：完整 battlecard——選一家目標公司的一項產品，對兩個競品，含 ICP、勝負情境、陷阱題。
- **週測 W9**：01/16（六）。

#### W10（01/18–01/24）Benchmark、PoC 與技術行銷內容

面試題（TMM）：*"A competitor claims 2x our performance. How do you respond?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo / 外部） |
| --- | --- | --- | --- | --- |
| 01/18 一 | w10-l1 | Benchmark 判讀：MLPerf 與「口徑」陷阱 | 一則效能宣稱要追問哪五件事？ | [KV Cache 效能分析方法論](../09_inference_system/kv_cache/08_methodology/01_kv-cache-perf-methodology.md)；外部：MLCommons MLPerf Inference 規則概覽 |
| 01/19 二 | w10-l2 | 自己量：負載產生、Goodput 與壓測工具 | 怎麼設計一次可重現、可對外發表的量測？ | [叢集產能評估框架](../99_misc/token_factory_talk/references/10-cluster-capacity-assessment.md)；[參數量 vs 吞吐](../99_misc/token_factory_talk/references/11-parameter-vs-throughput.md) |
| 01/20 三 | w10-l3 | PoC 設計與驗收：成功準則與檢查清單 | PoC 為什麼常常「技術成功、商務失敗」？ | [實施建議與最佳實踐](<../09_inference_system/reference_design/07-实施建议与最佳实践.md>)；[實施檢查清單](<../09_inference_system/reference_design/13-实施检查清单.md>) |
| 01/21 四 | w10-l4 | 技術內容寫作：solution brief、reference architecture、demo script | 每種文件的讀者、長度與固定結構？ | [推論服務架構設計](<../09_inference_system/reference_design/06-推理服务架构设计.md>)；[演講提綱範例](../99_misc/token_factory_talk/outline.md) |
| 01/22 五 | w10-l5 | 職能課：產品上市（launch）與 sales enablement | Launch tier 怎麼分？業務真正會用的教材長什麼樣？ | *Loved* Part 2–3 |

- 選讀：[LLM 評估體系](../06_llm_theory_and_fundamentals/llm_basic_concepts/evaluation/llm_evaluation.md)、[不同叢集規模的技術選型](<../09_inference_system/reference_design/04-不同集群规模的技术选型策略.md>)
- **作業 A10**（01/24）：2 頁英文 solution brief ＋ 一則公開 benchmark 宣稱的批判性解讀（500 字）。
- **週測 W10**：01/23（六）。

#### W11（01/25–01/31）需求端：Agentic AI 與企業落地 ｜ 期末考

面試題（EVG）：*"Where will inference demand come from over the next three years?"*

| 日期 | 課號 | 主題 | 核心問題 | 必讀（repo） |
| --- | --- | --- | --- | --- |
| 01/25 一 | w11-l1 | Agent 為什麼吃掉 token：Agent 迴圈與基礎設施堆疊 | 一個 Agent 任務比一次對話多耗幾倍 token？對推論平台提出什麼新要求？ | [AI Agent 基礎設施堆疊](../08_agentic_system/agent_infra/01_ai-agent-infra-stack.md)；[Agent 工作負載的 serving](../09_inference_system/agent_serving/agent-workload-serving.md) |
| 01/26 二 | w11-l2 | RAG 與企業知識：架構與硬體需求 | RAG 管線的每一段各吃什麼資源？向量庫要不要 GPU？ | [RAG 方案比較](../07_rag_and_tools/rag_basics/rag_comparison.md)（W7 回爐）；[Embedding 門戶](../06_llm_theory_and_fundamentals/llm_basic_concepts/embedding/README.md) |
| 01/27 三 | w11-l3 | 企業落地：FDE 案例、ROI 與常見失敗模式 | 企業 AI 專案卡在哪？怎麼跟客戶談 ROI？ | [FDE 落地指南](../11_ai_native_everything/fde/fde-ai-landing-guide.md)；[FDE 百例分析](../11_ai_native_everything/fde/fde-100-cases-analysis.md) |
| 01/28 四 | w11-l4 | 總複習：五層架構一張圖＋全課程數字速查表 | 不看任何資料，能不能在 15 分鐘內重畫整張地圖？ | 自己的錯題本與 W1–W11 講義 |
| 01/29 五 | w11-l5 | 職能課：account plan、QBR 與面試 STAR 故事定稿 | QBR 的固定議程？8 則 STAR 故事各對應哪種題型？ | *The Trusted Advisor* Ch.9–14 |

- 選讀：[AI Agent 基礎設施的崛起](../08_agentic_system/agent_infra/02_the-rise-of-ai-agent-infrastructure.md)、[MCP 深入](../08_agentic_system/mcp/docs/01_deep_dive_into_mcp_and_the_future_of_ai_tooling.md)、[Forward Deployed Engineer](../11_ai_native_everything/fde/forward-deployed-engineer.md)、*AI Engineering* Ch.6
- **期末考**：01/30（六），範圍 W1–W11，120 分鐘。
- **作業 A11**（01/31）：Capstone 講稿與投影片初稿＋二選一：launch plan（PMM 路線）或 account plan / QBR 簡報（TAM 路線）。

#### W12（02/01–02/04）Capstone 週

| 日期 | 內容 |
| --- | --- |
| 02/01 一 | 作品集定稿（挑 6 件）、履歷與 LinkedIn 更新、錯題本總清 |
| 02/02 二 | Capstone 彩排（錄影自評一次）＋ 全課程間隔複習題最後一輪 |
| 02/03 三 | **Capstone 發表**：20 分鐘英文技術演講＋ 10 分鐘 Q&A（Claude 扮演聽眾提問），全程錄影 |
| 02/04 四 | **模擬面試 × 2**：TMM/PMM 場（技術深度＋定位題）、TAM 場（情境處理＋行為面試）＋ 課程回顧 |
| 02/05 起 | 春節。課後間隔複習日：02/15、03/01、04/01（各 30 分鐘，由 `quiz-coach` 出到期題） |

## 五、指定閱讀書目

### 5.1 必讀（納入測驗範圍）

| 類別 | 書目 / 資料 | 使用週次 | 讀哪些 |
| --- | --- | --- | --- |
| 技術 | 本 repo 各課「必讀」文章 | 每週 | 見第四節各課表格 |
| 技術 | Barroso、Hölzle、Ranganathan，*The Datacenter as a Computer*（3rd ed.，開放取用電子書） | W4 | Ch.4 Data Center Basics、Ch.5 Energy and Power Efficiency；選讀 Ch.6 Modeling Costs |
| 技術 | Chip Huyen，*AI Engineering*（O'Reilly，2025） | W7、W8、W11 | Ch.2、Ch.7、Ch.9、Ch.6（依各週選讀標示） |
| 行銷 | April Dunford，*Obviously Awesome* | W1–W2 | 全書（約 200 頁，兩週讀完） |
| 行銷 | Martina Lauchengco，*Loved: How to Rethink Marketing for Tech Products* | W3、W10 | Part 1–3 |
| 行銷 | Geoffrey Moore，*Crossing the Chasm*（3rd ed.，中譯《跨越鴻溝》） | W9 | Part 1 |
| 溝通 | Chip Heath、Dan Heath，*Made to Stick*（中譯《創意黏力學》） | W4、W7 | 前言、Ch.1–6 |
| 客戶 | David Maister 等，*The Trusted Advisor* | W5、W11 | Ch.1–14 |
| 客戶 | John Care，*Mastering Technical Sales: The Sales Engineer's Handbook* | W6 | Discovery、Demo、PoC 相關章節 |

### 5.2 選讀與延伸

- 學習方法：*Make It Stick*（中譯《超牢記憶法》）、Daniel Willingham《學生為什麼不喜歡上學？》——本課程的測驗制度就是照這兩本書設計的，讀過會更清楚為什麼每天要先考再學。
- 技術延伸：repo 內的[書單](../99_misc/book-recommendations.md)、[KV Cache 八講](../10_ai_related_course/kv_cache_course/README.md)（想把推論講到專家等級時再讀）。
- 產業動態（每週日 30 分鐘，挑一則做 3 句摘要）：最近一場 NVIDIA GTC keynote、NVIDIA／AMD／一家 ODM 或 OEM／一家 neocloud 的最近一季法說逐字稿、SemiAnalysis 公開文章、MLCommons 最新一輪 MLPerf 結果、NVIDIA Spectrum-X 與 Ultra Ethernet Consortium 官方概覽、Uptime Institute 年度調查摘要。

### 5.3 認證（選配，建議）

| 認證 | 時點 | 說明 |
| --- | --- | --- |
| NVIDIA-Certified Associate: AI Infrastructure and Operations（NCA-AIIO） | W8 結束後（建議 01/11–01/17 之間報考） | 線上監考、50 題、60 分鐘、US$125（NVIDIA 官網口徑，查於 2026-11-10；有第三方網站標 US$135，**報名前請到官網複核**）。範圍與 W1–W6 高度重疊，是履歷上最直接的「懂 AI infra」訊號 |
| NVIDIA-Certified Professional 系列（AI Infrastructure / AI Operations / AI Networking） | 結業後視目標職缺選考 | 專業級，偏實作；費用第三方資料不一致（US$200–400），以官網為準 |

## 六、作業與考試日期總表

| 日期 | 星期 | 項目 | 範圍 / 內容 | 佔比 |
| --- | --- | --- | --- | --- |
| 2026-11-15 前 | — | 前測（不計分） | [診斷前測](quizzes/00_diagnostic_pretest.md)：全課程 24 題，建立基準線 | 0% |
| 每個上課日 | 一～五 | 每日小考 × 55 | 當課預測題＋課後題＋到期複習題 | 合計 20% |
| 11/21、11/28、12/05、12/19、12/26、01/02、01/16、01/23 | 六 | 週測 × 8 | 累積，本週 60%＋舊週 40% | 合計 20% |
| 11/22、11/29、12/06、12/13、12/20、12/27、01/03、01/10、01/17、01/24、01/31 | 日 | 作業 A1–A11 | 見各週 | 合計 25% |
| 2026-12-12 | 六 | 期中考 1 | W1–W4，90 分鐘 | 5% |
| 2027-01-09 | 六 | 期中考 2 | W1–W8，100 分鐘（含口頭 sizing） | 5% |
| 2027-01-30 | 六 | 期末考 | W1–W11，120 分鐘 | 10% |
| 2027-02-03 | 三 | Capstone 發表 | 20 分鐘英文演講＋ Q&A | 10% |
| 2027-02-04 | 四 | 模擬面試 × 2 | TMM/PMM 場、TAM 場 | 5% |

題型、配分與各次考試的出題藍圖見 [assessment.md](assessment.md)。

## 七、評分標準與規定

### 7.1 成績組成

| 項目 | 佔比 | 計分方式 |
| --- | --- | --- |
| 每日小考 | 20% | 每題 0–3 分自評＋Claude 複評；去掉最低 5 次後平均 |
| 週測 | 20% | 8 次平均；每次 25 題 |
| 作業（作品集） | 25% | 11 份，各以 4 向度評分規準（rubric）給 0–4 級，見 assessment.md 第六節 |
| 期中考 × 2 | 10% | 各 5% |
| 期末考 | 10% | — |
| Capstone ＋ 模擬面試 | 15% | 演講 10%、面試 5% |

### 7.2 等第與結業門檻

| 總分 | 等第 | 意義 |
| --- | --- | --- |
| ≥ 90 | A | 可以直接投遞目標職缺，技術面試有餘裕 |
| 80–89 | B | **結業門檻**。可以投遞，面試前針對弱項再補一輪 |
| 70–79 | C | 知識有了但還不穩，延長 2 週做間隔複習與口說再考期末 |
| < 70 | — | 回到最弱的階段重修 |

除總分外，還要同時滿足：作品集 6 件完成、Capstone 與兩場模擬面試都有錄影、STAR 故事 8 則定稿。

### 7.3 規定

1. **閉卷**。小考、週測、期中期末一律不看講義、不查資料、不問 AI。看了答案再作答不算提取練習，分數也失去校準的意義。
2. **先作答，再看答案**。每題先寫下答案與信心（1 猜的 / 2 大概 / 3 確定），才能展開參考答案。Claude 出題時不會在你作答前透露答案。
3. **答錯是預期內的事**。課前預測題的正確率通常很低，這正是它有效的原因；預測題不計入成績。
4. **精熟門檻**：週測 < 70% 時，隔天先補考錯題（換題幹的同概念題）才進新課；單一概念連錯兩次，進入「回爐清單」並在下一份講義開頭重教。
5. **間隔複習不可跳過**。每天開場的到期題是整個制度的核心，時間不夠時寧可縮短閱讀也不跳過它。
6. **補課**：整個課程有 3 張「請假券」，每張可把一天的課順延到當週週末；用完之後每缺一天，該日小考以 0 分計。連續缺 3 天以上，請 Claude 依第八節重排進度，不要硬追。
7. **作業遲交**：48 小時內繳交以 9 折計；超過 48 小時仍要交（作品集需要它），但以 7 折計。
8. **英文產出**：每週至少一段英文錄音；作業 A1、A4、A8、A10 與 Capstone 必須用英文。
9. **數字要有出處**。作業與口說引用的任何數字都要說得出來源與時點；說不出來的數字在評分時視同沒說。
10. **進度要落地**：每次上課結束，由 Claude 更新 [progress.md](progress.md) 與 `progress/state.json` 並 commit、push。雲端工作階段的容器是暫時的，沒 push 的進度會消失。

## 八、進度調整規則（給 Claude 的指示）

學員要求改期或調整負荷時照下列規則改本檔，並同步更新 progress.md：

- **開課日順延 N 週**：第四、六節所有日期整體平移；若結業日落在春節（2027-02-05 至 02-10）之後，W12 排在春節後第一個完整週。
- **每週時數降到 8 小時左右**：每週保留 L1–L3 ＋ L5，L4 改為下一週的 L1，總週數由 12 增為 15；每日小考與週測不刪。
- **每週時數達 20 小時以上**：W1+W2、W5+W6、W9+W10 各併為一週，總週數降為 9；週測改為每 5 課一次。
- **提前面試**：以目標職缺對照 career_targets.md 第三節的能力矩陣，優先完成該職缺標為「核心」的週次，其餘改為選讀。
- 任何調整都不能拿掉三樣東西：每日到期複習題、課前預測題、週累積測驗。
