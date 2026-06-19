# psych-text-analysis — 架構總綱

> **版本**：v0.2  
> **日期**：2026-06-16  
> **定位**：定義心理學文本分析系統的認識論框架、世界線架構、三層數據模型、Phase Gate 路線  
> **方法論注入來源**：ECC 多世界線比較認知系統（GRANDPLAN v2.0 經驗萃取）+ 三層發生學資料庫規格書  
> **配套文件**：`SCHEMA.md`（數據 Schema，含三層發生學定義）、`SPIRAL.md`（動態導航）、`AGENTS.md`（協作協議）、`GENERAL-PRINCIPLES.md`（方法論原則）

---

## 一、核心命題

> **「Vygotsky 文化歷史學派和精神分析學派在 20 世紀初的理論演化中，存在哪些未被充分探索的平行發展、互相影響、以及結構性分歧？」**

本專案通過對兩大學派核心文獻的結構化索引與 DCA 分析，建立心理學理論演化的可計算模型。

---

## 二、雙世界線架構（適配自 ECC）

```
世界線 α₁：真實心理學史
  ├── 文獻事實基線：作者、日期、發表脈絡、引用網絡
  ├── 制度脈絡：蘇聯心理學體制、IPA 組織史、大學實驗室
  └── → ha（歷史張力時間序列，來自制度變遷與學派衝突）

世界線 γ：理論張力（EME-適配版）
  ├── Vygotsky 文獻 → tt_vyg（文化歷史學派理論張力）
  ├── 精神分析文獻 → tt_pa（精神分析理論張力）
  └── → tt = f(tt_vyg, tt_pa)（統一理論張力信號）

比較層：
  ├── ha × tt → 制度變遷與理論創新的相位差
  └── tt_vyg × tt_pa → 兩大學派的共鳴與偏離
```

### 與 ECC 的關鍵差異

| | ECC | psych-text-analysis |
|:---|:---|:---|
| **操作對象** | 架空敘事場景 | 真實理論文獻 |
| **核心信號** | zg（敘事時代精神） | tt（理論張力） |
| **β₁ 性質** | 虛構（架空小說） | 真實（歷史文獻） |
| **α₁ 密度** | 399 歷史事實條目 | 文獻元數據（日期、作者、制度脈絡） |
| **DCA 用途** | 分叉動能分析（虛構世界線） | 理論演化追蹤（真實思想史） |

---

## 三、認識論原則（五條公理，適配自 ECC）

| # | 公理 | 含義 |
|---|------|------|
| 1 | **雙世界線不可混淆** | α₁（真實心理學史）和 γ（理論張力分析）是兩個獨立的信號維度。文獻的歷史事實（誰、何時、何處）不可與理論張力（概念演化、學派衝突、範式轉移）混淆。 |
| 2 | **可能性空間優先於單一實例** | 精神分析史不僅是「Freud 的勝利敘事」——被邊緣化的替代方案（Spielrein 的毀滅本能、早期女性分析師的貢獻、俄國精神分析的被壓抑傳統）構成理論的「可能性空間」。DCA 的任務是恢復這些替代方案的可理解性。 |
| 3 | **制度重力與理論分叉動能** | 制度密度高的環境（IPA 的組織化、蘇聯心理學的意識形態控制）施加理論收斂的重力；制度崩潰或過渡期（1910 年代俄國、兩次大戰間的維也納）釋放理論分叉動能。 |
| 4 | **殘差即種子** | 兩大學派之間的「不可通約」概念（如 Vygotsky 的「內在言語」vs Freud 的「無意識」）不是需要調和的矛盾——它們標誌著不同的理論演化路徑在何處分叉。殘差考古學的任務是識別種子，而非消除差異。 |
| 5 | **DCA 構成 UCD；T-SLAC 是觀察中介** | DCA 分支樹遞歸構成理論的不均等與組合發展（UCD）模式。T-SALC 頻譜系統不是引擎——它是兩大學派之間的觀察中介，投射理論演化的頻譜。α₁ 是量度 tt 偏離的對比基準（尺），不是解釋 tt 的框架。 |

---

## 四、Phase Gate 路線

```
Phase 0: 源數據準備          ✅ 文獻已獲取（12 冊）
Phase 1: 結構化索引 + 維度標記  ⬜ documents-raw/ 條目 + D1–D10 標記
Phase 2: 編譯庫 + Prefix      ⬜ compiled-corpus.json
Phase 3: DCA + Event Layer    ⬜ 5-10 篇 DCA + 首批 event 記錄
Phase 4: α₁ + Problem Space   ⬜ 制度脈絡基線 + 首批 problem domain 節點
Phase 5: tt 頻譜 + Segment    ⬜ Butterworth 分解 + 關鍵段落 segment 註記
Phase 6: 三層整合跨學派比較    ⬜ problem_domain→event→segment 穿透查詢
```

### 各 Phase 詳情

#### Phase 0：源數據準備 🔄 擴充中

- [x] Vygotsky 全集 7 冊（含結構化 YAML meta）
- [x] 精神分析經典 5 冊（含結構化 YAML meta）
- [x] 每冊含 `key_concepts`、`key_figures`、`chapter_outline`（行號範圍）
- [x] **橋樑人物 Kurt Lewin：** Principles of Topological Psychology (1936) — 2026-06-19 新增
- [ ] 橋樑人物待補：Piaget, Pavlov, Bekhterev, Bühler 等

#### Phase 1：結構化索引 + 維度標記（下一步）

將每本書的章節拆分為獨立文獻條目，每個條目有：
- YAML Frontmatter（`id`、`title`、`author`、`year`、`concepts`、`doc_type`、`dimension_tags`）
- 正文摘要
- 與其他條目的交叉引用
- 可選的 D1–D10 維度標記（見 SCHEMA.md 第零節）

目標：~200 條目（12 冊 × 平均 15-20 章）

**三層疊加**：為首批 5–10 個關鍵段落建立 segment 層註記（`index/segments/`），作為 Layer 1 的試點。

#### Phase 2：編譯庫 + Prefix

- 執行 `build-compiled-db.py` 生成 `compiled-corpus.json`
- 執行 `build-prefix.py` 生成 AI Prefix
- 執行 `validate-schema.py` 全量校驗

#### Phase 3：DCA 深度分析 + Event Layer

選取關鍵文獻進行 DCA（辯證反事實分析）：
- Crisis：理論危機（學派分裂、概念僵局、制度壓制）
- Lag：理論滯後（某些概念為何發展停滯）
- Alternative：替代方案（被壓抑的理論路徑）
- Direction：演化方向（哪些替代方案獲得了後續發展）
- New Crisis：從 Direction 中生成的新危機

首批候選：
1. Spielrein (1912) "Destruction as the Cause of Becoming"——被 Freud/Jung 三角關係遮蔽的理論創新
2. Vygotsky (1934) "Thinking and Speech" Ch.7——內在言語與精神分析無意識的平行概念
3. Freud & the Bolsheviks——俄國精神分析在蘇聯體制下的命運

**三層疊加**：DCA 分析完成後，將產出格式化為 Layer 2 Event Schema 記錄（`analysis/events/`），包含 `system_state_before/after`、`transition_mechanism`、`temporal_span`。每個 event 記錄指向構成它的 segment_id 列表（`source_segments`）。

#### Phase 4：α₁ 制度脈絡基線 + Problem Space

- 建立制度脈絡基線：IPA 組織史、蘇聯心理學體制史、關鍵機構（Detski Dom、Moscow University）
- **三層疊加**：建立首批 Problem Domain 節點（`analysis/problem-spaces/`），至少覆蓋 5 個問題域（如 PD_language_consciousness、PD_affect_drive、PD_social_mediation）
- 為每個 problem domain 記錄關係拓撲（approaches[].relation_topology）與對位對（contrastive_pairs）

#### Phase 5：tt 頻譜分析 + Segment 深化

- 理論張力 Butterworth 分解（長波/中波/短波）
- **三層疊加**：將 tt 頻譜的時間軸與 Layer 1 Segment 的 temporal_dynamics 對齊；將 tt 波峰/波谷與 Layer 2 Event 的 temporal_span 交叉驗證
- 在 tt 波峰附近選取關鍵段落進行深度 segment 註記

#### Phase 6：三層整合跨學派比較

- Vygotsky × Psychoanalysis 平行概念分析
- **三層整合查詢**：支援從 problem_domain 向下穿透到 event 再到 segment 的完整鏈路
- 跨學派概念採集（harvesting）與概念移民鏈（mediator chain）分析
- 負片證據（negative evidence）的結構化記錄

---

## 五、模組狀態

| 模組 | 狀態 | 說明 |
|------|:---:|------|
| corpus/vygotsky | ✅ | 7 冊完整 |
| corpus/psychoanalysis | ✅ | **6 冊（擴充中，含橋樑人物 Kurt Lewin）** |
| system-template/scripts | ✅ | 4 個腳本就位 |
| SCHEMA.md | ✅ | v0.2（含三層 Schema + D1–D10 維度） |
| GENERAL-PRINCIPLES.md | ✅ | v0.1（19 原則） |
| GRANDPLAN.md | ✅ | v0.2（含三層數據模型） |
| documents-raw/ | ⬜ | Phase 1 |
| dimension_tags（D1–D10 標記） | ⬜ | Phase 1 疊加 |
| segments/ | ⬜ | Layer 1（首批試點） |
| compiled-corpus.json | ⬜ | Phase 2 |
| DCA 分析 | ⬜ | Phase 3 |
| events/ | ⬜ | Layer 2（Phase 3 疊加） |
| problem-spaces/ | ⬜ | Layer 3（Phase 4 疊加） |

---

## 六、三層數據模型（Three-Layer Genetic Database）

本節定義疊加在雙世界線架構上的**操作化數據模型**。雙世界線（α₁/γ）是認識論框架，三層數據模型是該框架的具體數據組織方式。

### 6.1 三層架構總覽

```
第三層：Problem Space（問題共享領域）
  ─ 問題域為獨立節點，跨傳統共享
  ─ 關係拓撲：collaborative / copresence / harvesting / parallel
  ─ 對位分析：互補、鏡像、螺旋
  ─ 負片證據、概念移民鏈
        ↑
        │ problem_domain.event_links → event_id
        │ event.problem_domains → problem_domain_id
        ↓
第二層：Event Layer（事件層）
  ─ 系統級相變：crisis / qualitative_leap / emergence / sublatation / spiral_return
  ─ 系統狀態前後對比
  ─ 過渡機制：dialectical_negation / conceptual_harvesting / political_deformation / experimental_breakthrough
  ─ 螺旋關係追蹤
        ↑
        │ concept_event.quality_change=true → 註冊 event_id
        │ event.source_segments → segment_id[]
        ↓
第一層：Textual Genesis（文本發生學）
  ─ 文本切片級概念事件
  ─ 四個發生學層級：microgenesis / ontogenesis / phylogenesis / sociogenesis
  ─ 九種發生學狀態：germination → maturity → ... → interruption
  ─ 辯證結構與時間動力學
  ─ D1–D10 十維度標記
```

### 6.2 與雙世界線的對應關係

| 雙世界線 | 三層數據模型 | 功能 |
|---------|-------------|------|
| α₁（真實心理學史） | Layer 1 的 `source_text` + `temporal_dynamics.linear_date` | 提供歷史事實基線 |
| α₁（制度脈絡） | Layer 3 的 `relation_topology` + `textual_traces` | 記錄制度關係與文本痕跡 |
| γ（理論張力 tt） | Layer 1 的 `concept_event.genetic_status` + Layer 2 的 `event_type` | 概念變形→系統相變的信號鏈 |
| γ（DCA 分析） | Layer 2 的 `system_state_before/after` + `transition_mechanism` | DCA 產出的結構化存儲 |
| 比較層（ha × tt） | Layer 3 的 `contrastive_pairs` + `approaches[].harvesting_sources` | 跨傳統的共振與採集分析 |

### 6.3 三層與現有 Phase Gate 的整合

| 現有 Phase | 三層建設任務 | 優先級 |
|:-----------|-------------|:------:|
| Phase 1：結構化索引 | 為每個條目標記 D1–D10 維度（嵌入 Frontmatter）；首批關鍵段落 segment 註記 | P0 |
| Phase 2：編譯庫 + Prefix | Segment 元數據納入編譯庫 | P1 |
| Phase 3：DCA 深度分析 | DCA 產出格式化為 Event Schema；建立首批 event 記錄 | P0 |
| Phase 4：α₁ 制度脈絡基線 | 建立首批 Problem Domain 節點；記錄關係拓撲 | P0 |
| Phase 5：tt 頻譜分析 | 概念 event 的時間序列對齊 tt 頻譜 | P1 |
| Phase 6：跨學派比較 | 三層整合查詢：problem_domain → event → segment | P1 |

### 6.4 三層 Schema 存放位置

| 層 | 目錄 | 格式 |
|:---|------|------|
| Layer 1（Segment） | `index/segments/{corpus}/{doc_id}/` | `.yaml` |
| Layer 2（Event） | `analysis/events/` | `.yaml` |
| Layer 3（Problem Space） | `analysis/problem-spaces/` | `.yaml` |

> 詳細的 Schema 定義（含所有字段、枚舉值、驗證規則）請見 `SCHEMA.md` 第零節（D1–D10）及第九至十三節（三層 Schema）。

---

## 七、術語體系

| 術語 | 定義 |
|------|------|
| **tt**（theoretical tension） | 理論張力——文獻中概念創新、學派衝突、範式轉移的強度信號 |
| **ha**（historical atmosphere） | 歷史氛圍——制度變遷、政治壓制、學術組織變化的時間序列 |
| **DCA**（Dialectical Counterfactual Analysis） | 辯證反事實分析——Crisis→Lag→Alternative→Direction→New Crisis |
| **T-SALC**（Three-layer Spectrum Analysis for Literary Corpora） | 三層頻譜分析——Butterworth 長波/中波/短波分解 |
| **SSOT**（Single Source of Truth） | 唯一真實來源——YAML Frontmatter 為元數據的唯一權威 |
| **SPIRAL M-E-G** | 迴旋引擎——Measure→Explain→Generate |
| **Genetic Level** | 發生學層級——概念生成的時間尺度（micro/onto/phylo/sociogenesis） |
| **Genetic Status** | 發生學狀態——概念在生成過程中的階段性標記（萌芽/成熟/質變/危機/湧現/揚棄等） |
| **Concept Event** | 概念事件——單一概念在文本切片中的動態身份 |
| **Problem Domain** | 問題域——跨傳統共享的理論問題，獨立於任何單一學者 |
| **Relation Topology** | 關係拓撲——學者與問題域的連結類型（collaborative/copresence/harvesting/parallel） |
| **Counterpoint** | 對位/共振——兩學者從相反端點進入同一問題域的結構關係 |
| **Negative Evidence** | 負片證據——無直接文獻但概念結構同構+機構重疊+策略性沉默的推論依據 |
| **Concept Harvesting** | 概念採集——從其他傳統攝取概念碎片並重新熔鑄的機制 |
| **Mediator Chain** | 概念移民鏈——概念通過中介者從 A 傳統移到 B 傳統的路徑 |
