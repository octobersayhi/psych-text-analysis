# psych-text-analysis — 迴旋升級系統

> **版本**：v0.2  
> **日期**：2026-06-16  
> **理論基礎**：普遍發展律——不均等與組合發展（Vygotsky 文化歷史學派核心命題）  
> **核心功能**：戰略導航——回答「在哪裡、往哪去、何時停」  
> **方法論注入來源**：ECC SPIRAL.md v2.1 + EME SPIRAL.md v1.1 + 三層發生學資料庫規格書  
> **配套文件**：`GRANDPLAN.md`（地圖，含三層數據模型）、`AGENTS.md`（交通規則）、`SCHEMA.md`（三層 Schema）、`TASKLOG.md`（里程表）

---

## 一、為什麼需要 SPIRAL

### 1.1 只有 12 本書——更需要方向感

大語料庫（如 EME MECW 的 6,759 篇）的危險是「永遠索引不完」。小語料庫的危險恰好相反——「很快就索引完了，然後不知道做什麼」。SPIRAL 的 M-E-G 引擎強制每個循環產出**下一步假說**，防止專案在 Phase 1 完成後停滯。

### 1.2 本專案的不均等是先天性的

```
corpus 文獻獲取          ████████████████  ✅ 12/12
結構化索引              ░░░░░░░░░░░░░░░░  ⬜ 0/200 條目
D1–D10 維度標記          ░░░░░░░░░░░░░░░░  ⬜
編譯庫 + Prefix         ░░░░░░░░░░░░░░░░  ⬜
Segment 註記（Layer 1）  ░░░░░░░░░░░░░░░░  ⬜
DCA 深度分析            ░░░░░░░░░░░░░░░░  ⬜
Event Layer（Layer 2）   ░░░░░░░░░░░░░░░░  ⬜
α₁ 制度脈絡基線          ░░░░░░░░░░░░░░░░  ⬜
Problem Space（Layer 3） ░░░░░░░░░░░░░░░░  ⬜
tt 頻譜分析             ░░░░░░░░░░░░░░░░  ⬜
跨學派比較              ░░░░░░░░░░░░░░░░  ⬜
```

不均等不可消除（也**不應**消除——它是創造性張力的來源）。SPIRAL 做的是**組合**：用已成熟的 corpus + system-template 基礎設施，直接跳躍式拉動 DCA 分析，無需走「學 Python → 寫腳本 → 做分析」的線性路徑。

### 1.3 文獻分析 SPIRAL 與場景分析 SPIRAL 有何不同

| | ECC SPIRAL | psych-text-analysis SPIRAL |
|:---|:---|:---|
| **操作對象** | 架空敘事場景 | 真實理論文獻 |
| **M-E-G 的 M** | T-SALC 三層頻譜測量 | 文獻結構化索引 + 三層數據完整性（segment/event/problem-space 覆蓋率） |
| **M-E-G 的 E** | DCA 因果追蹤（場景級） | DCA 理論危機分析（文獻級）+ 三層解釋鏈（segment→event→problem_domain） |
| **M-E-G 的 G** | 假說生成（敘事方向） | 假說生成（理論演化路徑 + 三層深化方向） |
| **Phase Gate** | 以場景覆蓋率為進度 | 以文獻條目覆蓋率 + 三層數據成熟度為進度 |

---

## 二、核心機制

### 2.1 M-E-G 迴旋引擎

```
┌─────────────────────────────────────────┐
│           M-E-G 迴旋引擎                  │
│                                         │
│  MEASURE ──→ EXPLAIN ──→ GENERATE       │
│  索引完整性    DCA 分析     假說生成       │
│  元數據校驗    因果追蹤      新數據需求     │
│     │                       │           │
│     └── 新數據注入 ←────────┘           │
│         （分辨率 +1）                    │
└─────────────────────────────────────────┘
```

**M（Measure）**：在當前分辨率上測量文獻索引與三層數據的完整性。
- 條目覆蓋率（多少章節已轉為獨立條目）
- Schema 合規率（Frontmatter 必填欄位填充率）
- 概念標記率（多少條目有 `key_concepts` 標記）
- D1–D10 維度標記率（多少條目有 `dimension_tags`）
- Segment 覆蓋率（多少關鍵段落已建立 segment 註記）
- Event 覆蓋率（多少 DCA 產出已格式化為 Event Schema）
- Problem Domain 覆蓋率（多少問題域已有獨立節點）
- 日期覆蓋率（多少條目有精確日期）

**E（Explain）**：使用 DCA + 三層解釋鏈追蹤理論演化。
- 選取當前 Phase 中資訊密度最高的文獻
- 應用 DCA：Crisis→Lag→Alternative→Direction→New Crisis
- 不解釋「全文」，只解釋「危機鏈」
- **三層疊加**：將 DCA 產出映射到三層鏈路——哪些 segment 構成此 crisis？對應哪個 event？歸屬於哪個 problem domain？

**G（Generate）**：生成假說——「什麼新數據/新分析能深化這個危機鏈？」
- 需要攝取哪些補充文獻？
- 需要哪些制度脈絡來理解文獻的社會條件？
- 當前分析的盲點是什麼？
- **三層疊加**：當前分析在哪一層最薄弱？需要深化 segment 註記？還是需要建立新的 problem domain？

### 2.2 Phase Gate 體系

| Phase Gate | M（測量指標） | E（解釋產物） | G（假說產物） |
|:---|:---|:---|:---|
| **Gate 0→1** | corpus 就位（12 冊） | — | 索引策略 + D1–D10 標記方針 |
| **Gate 1→2** | >50 條目，D1–D10 標記率 >60%，首批 segment 試點（5–10 個） | 概念共現網絡初探 + 維度分佈熱圖 | DCA 優先級清單 + segment 深化方向 |
| **Gate 2→3** | compiled-corpus.json 生成 | 首批 5 篇 DCA 分析 → 格式化為 Event Schema | 制度脈絡研究假說 + 首批 problem domain 候選 |
| **Gate 3→4** | α₁ 制度脈絡 >50 條目，首批 problem domain 節點（≥5） | 制度重力 × 理論張力解釋 + problem domain 關係拓撲 | tt 信號維度定義 + 對位分析假說 |
| **Gate 4→5** | tt 頻譜產出，segment temporal_dynamics 與 tt 時間軸對齊 | tt 長波/短波的 DCA 解釋 + segment→event 鏈路驗證 | 跨學派比較假說 + 新 problem domain 需求 |
| **Gate 5→6** | 三層整合查詢鏈路完整（problem_domain→event→segment） | Vygotsky × Psychoanalysis 平行概念分析 + 對位報告 | 新文獻需求 + 方法論種子 |

---

## 三、GPS 坐標（當前位置）

```
Phase 0 完成（corpus 就位）
├── corpus/vygotsky       ██ ✅ 7 冊
├── corpus/psychoanalysis  ██ ✅ 5 冊
├── system-template        ██ ✅ 4 腳本
└── 方法論文檔             ██ ✅ 6 份根文件

▼ 下一步：Gate 0→1
Phase 1 目標：結構化索引 + D1–D10 維度標記
├── 將每本書的章節拆分為獨立條目
├── 每個條目有 Frontmatter + 摘要 + dimension_tags
├── 目標：~200 條目 + D1–D10 標記率 >60%
├── 首批 segment 試點（5–10 個關鍵段落）
└── 預估：每冊 15-20 章 × 12 冊
```

### 當前 GPS

```
{
  "phase_gate": "0→1",
  "phase_name": "結構化索引 + 維度標記",
  "corpus_status": "12/12 ✅",
  "entries_status": "0/~200 ⬜",
  "dimension_tag_rate": "0% ⬜",
  "segment_status": "0 ⬜",
  "next_action": "建立 index/documents-raw/ 首個條目（含 dimension_tags）"
}
```

---

## 四、停止條件（何時算夠）

每個 Phase Gate 有明確的停止條件——不是「做完」，而是「夠了」：

| 停止類型 | 條件 | 範例 |
|:---|:---|:---|
| **飽和（文件級）** | 新增條目不再帶來新概念 | 第 N+1 章的 `key_concepts` 全部已存在於前 N 章 |
| **飽和（Segment 級）** | 新增 segment 不再帶來新的 genetic_status 或 dialectical_structure | 第 N+1 個 segment 的 concept_event 完全可被前 N 個 segment 覆蓋 |
| **飽和（Problem Domain 級）** | 新增 problem domain 不再揭示新的關係拓撲類型 | 所有四種 relation_topology 均已出現至少一次 |
| **方法論瓶頸** | 現有方法無法回答當前問題 | DCA 的 Crisis→Direction 鏈在某一環節無法繼續 |
| **外部依賴** | 需要人類判斷或新數據 | 需要獲取版權受限的新文獻 |
| **Phase Gate 達標** | M 指標達標 + E 產出完成 | 日期覆蓋 >80% AND 首批 5 篇 DCA 完成 |

---

## 五、Aufheben（揚棄）生命週期

每個 Phase 的產物有三種結局：

```
產物
├── seed    → 晉升為 docs/method/seeds/（可復用模板）
├── archive  → 歸檔為 docs/archive/（歷史記錄）
└── discard  → 廢棄（錯誤方向，但記錄在證偽水滴中）
```
