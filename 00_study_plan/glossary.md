# 術語對照表：English ／ 台灣用語 ／ repo 用語

> 本 repo 的文章以簡體中文與中國大陸用語撰寫，外商面試則用英文。這張表讓你讀 repo 時對得上、開口時說得出。
>
> **面試時一律說英文原文**；中文只是幫助理解。每份講義的術語區會把該課新詞加進來，由 `course-handout` skill 維護。

## 一、最容易卡住的用語差異

| English | 台灣用語 | repo 用語（簡中） | 備註 |
| --- | --- | --- | --- |
| inference | 推論 | 推理 | 台灣業界兩者都聽得到，正式文件用「推論」 |
| compute / computing power | 運算、算力 | 算力 | — |
| GPU memory / VRAM | 顯示記憶體、GPU 記憶體 | 显存 | — |
| memory (RAM) | 記憶體 | 内存 | repo 的「内存」是主記憶體，不是儲存 |
| storage | 儲存 | 存储 | — |
| cache | 快取 | 缓存 | KV Cache 直接說英文 |
| bandwidth | 頻寬 | 带宽 | — |
| throughput | 吞吐量 | 吞吐 | — |
| latency | 延遲 | 延迟、时延 | — |
| cluster | 叢集 | 集群 | — |
| scheduling / scheduler | 排程、排程器 | 调度、调度器 | — |
| server | 伺服器 | 服务器 | — |
| data center | 資料中心 | 数据中心 | — |
| rack | 機櫃 | 机柜、机架 | — |
| chip | 晶片 | 芯片 | — |
| network | 網路 | 网络 | — |
| switch | 交換器 | 交换机 | — |
| NIC | 網路卡 | 网卡 | — |
| optical transceiver | 光收發模組 | 光模块 | — |
| hardware / software | 硬體 / 軟體 | 硬件 / 软件 | — |
| kernel | 核心 | 内核 | CUDA 的 kernel 指 GPU 上執行的函式，直接說英文 |
| thread / process | 執行緒 / 行程 | 线程 / 进程 | — |
| parallel / serial | 平行 / 循序 | 并行 / 串行 | — |
| interface | 介面 | 接口 | — |
| driver | 驅動程式 | 驱动 | — |
| container | 容器 | 容器 | — |
| virtualization | 虛擬化 | 虚拟化 | — |
| fine-tuning | 微調 | 微调 | — |
| quantization | 量化 | 量化 | — |
| token | token（官方譯「詞元」少用） | token、词元 | 直接說英文 |
| AI agent | AI 代理、智慧代理 | 智能体 | 直接說 agent |
| LLM | 大型語言模型 | 大语言模型、大模型 | — |
| optimization | 最佳化 | 优化 | — |
| default | 預設 | 默认 | — |
| file / document | 檔案 / 文件 | 文件 / 文档 | 陷阱：repo 的「文件」是 file |
| program | 程式 | 程序 | — |
| byte / bit | 位元組 / 位元 | 字节 / 比特、位 | — |
| digital / data | 數位 / 資料 | 数字 / 数据 | — |
| liquid cooling | 液冷 | 液冷 | — |
| cold plate | 水冷板、冷板 | 冷板 | — |
| power / electricity | 電力 | 电力 | — |
| depreciation | 折舊 | 折旧 | — |
| gross margin | 毛利率 | 毛利率 | — |
| utilization | 使用率、利用率 | 利用率 | — |
| offload | 卸載 | 卸载 | — |
| topology | 拓撲 | 拓扑 | — |
| heterogeneous | 異質 | 异构 | — |
| bare metal | 裸機 | 裸金属 | — |
| sovereign AI | 主權 AI | 主权 AI | — |
| compute leasing | 算力租賃 | 算力租赁 | — |
| AIDC（AI data center） | AI 資料中心、AI 算力中心 | 智算中心 | repo 常見「智算中心」 |

## 二、課程核心縮寫（依出現週次）

| 縮寫 | 全名 | 一句話 | 週 |
| --- | --- | --- | --- |
| SM | Streaming Multiprocessor | GPU 內的基本運算單元 | W1 |
| HBM | High Bandwidth Memory | 疊在 GPU 旁的高頻寬記憶體 | W1 |
| VRAM | Video RAM | GPU 上的記憶體 | W1 |
| PCIe | Peripheral Component Interconnect Express | 伺服器內部的通用高速匯流排 | W2 |
| NUMA | Non-Uniform Memory Access | 多處理器下記憶體存取遠近有別 | W2 |
| DMA | Direct Memory Access | 裝置不經 CPU 搬資料 | W2 |
| RDMA | Remote Direct Memory Access | 跨機器直接讀寫對方記憶體 | W3 |
| IB | InfiniBand | 為 HPC 與 AI 設計的低延遲網路 | W3 |
| RoCE | RDMA over Converged Ethernet | 在乙太網上跑 RDMA | W3 |
| NCCL | NVIDIA Collective Communications Library | 多 GPU 集合通訊函式庫 | W3 |
| DPU | Data Processing Unit | 把網路、儲存、安全工作從主機 CPU 卸載的晶片 | W3 |
| PUE | Power Usage Effectiveness | 機房總用電 ÷ IT 設備用電 | W4 |
| DLC | Direct Liquid Cooling | 冷卻液直接流過晶片上的冷板 | W4 |
| CDU | Coolant Distribution Unit | 液冷迴路的分配與熱交換設備 | W4 |
| TCO | Total Cost of Ownership | 總持有成本 | W4 |
| CapEx / OpEx | Capital / Operating Expenditure | 資本支出 / 營運支出 | W4 |
| SLO / SLA | Service Level Objective / Agreement | 服務水準目標 / 協議 | W4 |
| DCGM | Data Center GPU Manager | NVIDIA 的 GPU 監控工具 | W5 |
| RCA | Root Cause Analysis | 根因分析 | W5 |
| RMA | Return Merchandise Authorization | 故障品退換流程 | W5 |
| MIG | Multi-Instance GPU | 把一張 GPU 硬切成多個隔離的實例 | W6 |
| MPS | Multi-Process Service | 讓多個行程共用一張 GPU 的執行環境 | W6 |
| GDS | GPUDirect Storage | 儲存裝置直接把資料送進 GPU 記憶體 | W6 |
| MoE | Mixture of Experts | 每個 token 只啟動部分參數的模型架構 | W7 |
| LoRA | Low-Rank Adaptation | 只訓練少量附加參數的微調法 | W7 |
| RAG | Retrieval-Augmented Generation | 先檢索再生成 | W7 |
| TP / PP / EP / DP | Tensor / Pipeline / Expert / Data Parallelism | 四種把模型或資料拆到多張卡的方式 | W7 |
| TTFT | Time To First Token | 首個 token 的等待時間 | W8 |
| ITL / TPOT | Inter-Token Latency / Time Per Output Token | 相鄰輸出 token 的間隔 | W8 |
| TPS | Tokens Per Second | 每秒 token 數 | W8 |
| PD | Prefill–Decode disaggregation | 把 prefill 與 decode 分到不同機器 | W8 |
| ASIC | Application-Specific Integrated Circuit | 特定用途晶片 | W9 |
| CoWoS | Chip-on-Wafer-on-Substrate | 台積電的先進封裝技術 | W9 |
| ODM / OEM | Original Design / Equipment Manufacturer | 代工設計製造商 / 品牌系統廠 | W9 |
| ICP | Ideal Customer Profile | 理想客戶輪廓 | W9 |
| TAM / SAM / SOM | Total Addressable / Serviceable Available / Serviceable Obtainable Market | 三層市場規模（注意與職稱 TAM 同縮寫） | W9 |
| PoC | Proof of Concept | 概念驗證 | W10 |
| GTM | Go-To-Market | 上市與銷售策略 | W10 |
| MCP | Model Context Protocol | 模型連接外部工具與資料的協定 | W11 |
| FDE | Forward Deployed Engineer | 駐點在客戶端做落地的工程師 | W11 |
| QBR | Quarterly Business Review | 每季與客戶的業務檢討會 | W11 |
| STAR | Situation, Task, Action, Result | 行為面試的回答結構 | W11 |
