# psych-text-analysis — 架構總綱

> **版本**：v0.1  
> **日期**：2026-06-15  
> **定位**：定義心理學文本分析系統的認識論框架、世界線架構、Phase Gate 路線  
> **方法論注入來源**：ECC 多世界線比較認知系統（GRANDPLAN v2.0 經驗萃取）  
> **配套文件**：`SPIRAL.md`（動態導航）、`AGENTS.md`（協作協議）、`GENERAL-PRINCIPLES.md`（方法論原則）

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
Phase 1: 結構化索引          ⬜ 建立 documents-raw/ 條目
Phase 2: 編譯庫 + Prefix      ⬜ compiled-corpus.json
Phase 3: DCA 深度分析         ⬜ 選取 5-10 篇關鍵文獻
Phase 4: α₁ 制度脈絡基線      ⬜ IPA 史、蘇聯心理學體制史
Phase 5: tt 頻譜分析          ⬜ 理論張力 Butterworth 分解
Phase 6: 跨學派比較           ⬜ Vygotsky × Psychoanalysis
```

### 各 Phase 詳情

#### Phase 0：源數據準備 ✅

- [x] Vygotsky 全集 7 冊（含結構化 YAML meta）
- [x] 精神分析經典 5 冊（含結構化 YAML meta）
- [x] 每冊含 `key_concepts`、`key_figures`、`chapter_outline`（行號範圍）

#### Phase 1：結構化索引（下一步）

將每本書的章節拆分為獨立文獻條目，每個條目有：
- YAML Frontmatter（`id`、`title`、`author`、`year`、`concepts`、`doc_type`）
- 正文摘要
- 與其他條目的交叉引用

目標：~200 條目（12 冊 × 平均 15-20 章）

#### Phase 2：編譯庫 + Prefix

- 執行 `build-compiled-db.py` 生成 `compiled-corpus.json`
- 執行 `build-prefix.py` 生成 AI Prefix
- 執行 `validate-schema.py` 全量校驗

#### Phase 3：DCA 深度分析

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

#### Phase 4-6：後續

詳見 `SPIRAL.md` 的 Phase Gate 定義。

---

## 五、模組狀態

| 模組 | 狀態 | 說明 |
|------|:---:|------|
| corpus/vygotsky | ✅ | 7 冊完整 |
| corpus/psychoanalysis | ✅ | 5 冊完整 |
| system-template/scripts | ✅ | 4 個腳本就位 |
| SCHEMA.md | ✅ | v0.1 |
| GENERAL-PRINCIPLES.md | ✅ | v0.1（19 原則） |
| documents-raw/ | ⬜ | Phase 1 |
| compiled-corpus.json | ⬜ | Phase 2 |
| DCA 分析 | ⬜ | Phase 3 |

---

## 六、術語體系

| 術語 | 定義 |
|------|------|
| **tt**（theoretical tension） | 理論張力——文獻中概念創新、學派衝突、範式轉移的強度信號 |
| **ha**（historical atmosphere） | 歷史氛圍——制度變遷、政治壓制、學術組織變化的時間序列 |
| **DCA**（Dialectical Counterfactual Analysis） | 辯證反事實分析——Crisis→Lag→Alternative→Direction→New Crisis |
| **T-SALC**（Three-layer Spectrum Analysis for Literary Corpora） | 三層頻譜分析——Butterworth 長波/中波/短波分解 |
| **SSOT**（Single Source of Truth） | 唯一真實來源——YAML Frontmatter 為元數據的唯一權威 |
| **SPIRAL M-E-G** | 迴旋引擎——Measure→Explain→Generate |
