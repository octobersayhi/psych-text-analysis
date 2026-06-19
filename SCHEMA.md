# psych-text-analysis — Frontmatter Schema

> **版本**：v0.2  
> **日期**：2026-06-16  
> **適用範圍**：`index/documents-raw/*.md`（結構化後的個別文獻條目）+ 三層發生學數據（Segment / Event / Problem Space）  
> **方法論注入來源**：ECC SCHEMA.md v0.4 + EME MECW SCHEMA.md v0.1 + 三層發生學資料庫規格書

---

## 零、十維度標記系統（Dimension Tags）

連接文件級 Frontmatter 與三層發生學的索引框架。每個文獻條目可標記 1–3 個維度，對應的文本切片（segment）則做更細緻的概念事件註記。

| 代碼 | 維度名稱 | 核心概念 | 文本發生學操作 |
|------|---------|---------|--------------|
| D1 | 雙重刺激法 | double stimulation, mediation | 追蹤從實驗方法到理論核心的演化 |
| D2 | 科學概念/抽象 | scientific concept, everyday concept, abstraction | 提取「科學概念 vs 日常概念」的定義變形 |
| D3 | 自主記憶 | voluntary memory, logical memory, mnemotechnics | 標註「記憶」從工具中介到語義重組的軌跡 |
| D4 | 文藝心理學 | catharsis, artistic emotion, dvoistvennost' | 標註 catharsis 的消失/轉化，與 perezhivanie 的接合缺口 |
| D5 | 內在言語 | inner speech, egocentric speech, semantic system | 追蹤從自我中心言語過渡的完整論證鏈 |
| D6 | 最近發展區 | ZPD, scaffolding | 標註 ZPD 從教學概念到發展動力學的語義擴展 |
| D7 | 缺陷學/神經 | defectology, compensation, systemic reorganization | 提取缺陷補償、系統重組的臨床論證 |
| D8 | 年齡/危機理論 | age periods, crisis, transition | 提取每個年齡轉折點的危機敘事弧線 |
| D9 | 情感/意志/Perezhivanie | perezhivanie, affect, will, Spinoza's affectus | 標註情感維度從 James/Freud 到晚期 Spinoza 的轉向 |
| D10 | 哲學方法論 | cultural-historical method, dialectics, genetic principle | 標註 Hegel/Marx/Spinoza 術語的 Vygotsky 化轉譯 |

---

## 一、必填欄位

| 欄位 | 類型 | 說明 | 範例 |
|------|------|------|------|
| `id` | string | 唯一標識符，格式 `{corpus}-{short-title}` | `vygotsky-thinking-speech-ch7` |
| `title` | string | 文獻條目標題（章節級） | `"Thinking and Speech, Chapter 7: Thought and Word"` |
| `author` | string | 標準化作者名 | `L. S. Vygotsky` |
| `year` | integer | 寫作/發表年份 | `1934` |
| `corpus` | enum | 所屬子語料庫 | `vygotsky` / `psychoanalysis` |
| `doc_type` | enum | 文獻類型 | `chapter` / `article` / `letter` / `notebook` / `case_study` / `monograph` |
| `status` | enum | 處理狀態 | `raw` / `indexed` / `annotated` / `analyzed` |

---

## 二、推薦欄位

| 欄位 | 類型 | 說明 | 範例 |
|------|------|------|------|
| `source_volume` | string | 來源書目（對應 corpus/ 中的檔案） | `vol-1-problems-of-general-psychology` |
| `concepts` | list | 本條目涉及的核心概念 | `["inner_speech", "word_meaning", "egocentric_speech"]` |
| `key_figures` | list | 本條目涉及的核心人物（非作者） | `["Jean Piaget", "Kurt Lewin"]` |
| `language` | string | 原文語言 | `ru` / `de` / `en` / `fr` |
| `translator` | string | 英譯者（如適用） | `Norris Minick` |
| `date_precision` | enum | 日期精度 | `exact` / `year_only` / `approximate` / `unknown` |
| `original_publication` | string | 原始發表資訊 | `"First published in Russian, 1934"` |

---

## 三、分析欄位（DCA Phase 3+ 使用）

| 欄位 | 類型 | 說明 |
|------|------|------|
| `theoretical_position` | enum | `critique` / `synthesis` / `polemic` / `clinical_observation` / `methodology` / `literature_review` |
| `dca_crisis` | string | 本條目回應的理論危機（Phase 3+） |
| `dca_direction` | string | 本條目提出的理論方向（Phase 3+） |
| `tt_signal` | float | 理論張力強度（Phase 5+，由頻譜計算） |
| `cross_references` | list | 與其他條目的交叉引用 |
| `dimension_tags` | list | 所屬理論維度（D1–D10，見第零節）。連接文件級索引與三層發生學。 |

---

## 四、日期格式

| 規則 | 說明 | 範例 |
|------|------|------|
| 精確日期 | `YYYY-MM-DD` | `1934-06-11`（Vygotsky 逝世） |
| 年月 | `YYYY-MM` | `1912-09`（Spielrein 論文發表） |
| 僅年份 | `YYYY` | `1934` |
| 模糊 | `date_raw` 保留原始字串，`year` 提取四位年份 | `date_raw: "Summer 1911"`, `year: 1911` |
| 未知 | `year: null`, `date_precision: unknown` | — |

---

## 五、作者標準化

| 原始值 | 標準化後 |
|--------|---------|
| `L. S. Vygotsky` | `L. S. Vygotsky` |
| `Lev Vygotsky` | `L. S. Vygotsky` |
| `Sigmund Freud` | `Sigmund Freud` |
| `Sabina Spielrein` | `Sabina Spielrein` |
| `C. G. Jung` | `Carl Gustav Jung` |
| `Sabina Spielrein; Ruth I. Cape (ed.); Raymond Burt (trans.)` | `Sabina Spielrein`（編輯/譯者記入 `editor`/`translator` 欄位） |

---

## 六、概念標記標準化（受控詞表初版）

### Vygotsky 系

`inner_speech` `egocentric_speech` `zone_of_proximal_development` `higher_mental_functions` `mediation_by_signs` `scientific_concepts` `spontaneous_concepts` `psychological_systems` `subtext` `consciousness` `volition` `functional_systems` `instrumental_act` `intermental_to_intramental` `defectology` `child_development` `word_meaning` `sense_vs_meaning` `internalization` `semiotic_mediation` `cultural-historical_theory`

### 精神分析系（含橋樑人物）

`destruction_as_cause_of_becoming` `reproductive_drive` `death_drive` `libido` `unconscious` `transference` `countertransference` `oedipus_complex` `castration_anxiety` `penis_envy` `object_relations` `schizophrenia` `dementia_praecox` `psychoanalytic_case_study` `free_association` `dream_interpretation` `resistance` `repression` `sublimation` `infantile_sexuality` `psychosexual_development` `narcissism` `melancholia`
`life_space` `field_theory` `topological_psychology` `vector_psychology` `hodological_space` `psychological_regions` `locomotion` `boundaries` `structural_change` `person_environment_dynamics` `contemporaneity_principle` `concreteness_principle` `constructive_method` `galileian_mode_of_thought` `quasi_physical_facts` `quasi_social_facts` `quasi_conceptual_facts`

### 跨學派橋接概念

`development` `language_acquisition` `symbolism` `mythology` `creativity` `destruction_and_creation` `affect` `consciousness_vs_unconscious` `social_mediation` `trauma`

---

## 七、與來源 corpus/ YAML meta 的關係

`corpus/` 中的 `-meta.yaml` 是**書級**元數據（整本書的 `key_concepts`、`key_figures`、`chapter_outline`）。

`index/documents-raw/` 中的 Frontmatter 是**條目級**元數據（章節/文章級的 `concepts`、`key_figures`、`theoretical_position`）。

兩者是上下游關係：書級 meta → 指導章節拆分 → 條目級 Frontmatter。

---

## 八、驗證規則

| 規則 | 檢查方式 |
|------|---------|
| `id` 唯一 | `validate-schema.py` 自動檢查 |
| `doc_type` 合法 | 僅接受六種枚舉值 |
| `corpus` 合法 | 僅接受 `vygotsky` / `psychoanalysis` |
| `year` 合理 | 1800–2030（超出範圍需人工確認） |
| `concepts` 來自受控詞表 | 非強制，但標記為 `⚠ unmapped_concept` |
| `status` 合法 | 僅接受四種枚舉值 |

---

## 九、三層發生學資料庫總覽

本章及其後三節定義**三層發生學資料庫（Three-Layer Genetic Database）**的 Schema。此資料庫記錄的不是靜態概念，而是「概念生成過程」的動態數據。三層結構如下：

```
第三層：Problem Space ─── 問題域為獨立節點，記錄跨傳統共享的理論問題
    ↑ 問題域定義「誰與誰共享什麼問題」
第二層：Event Layer ─── 系統級相變事件（危機、質變、湧現、揚棄、螺旋回歸）
    ↑ 事件聚合多個文本切片的概念變形
第一層：Textual Genesis ─── 文本切片級概念事件（微生成、個體發生、系統發生、社會發生）
```

### 數據流方向

| 方向 | 內容 | 接口字段 |
|------|------|---------|
| **向上聚合** | 多個 segment 的 concept_event 聚合為 event；多個 event 定義 problem domain 的張力結構 | `concept_event.quality_change=true` → 註冊 `event_id`；`event.problem_domains` → 指向 `problem_domain_id` |
| **向下穿透** | 從 problem domain 可查詢相關 event；從 event 可查詢構成它的 segments | `event.source_segments` → `segment_id[]`；`problem_domain.event_links` → `event_id[]` |

### 數據存放位置

| 層 | 存放位置 | 格式 |
|:---|---------|------|
| Layer 1（Segment） | `index/segments/{corpus}/{doc_id}/` | 每個 segment 一個 `.yaml` 或 JSON |
| Layer 2（Event） | `analysis/events/{event_id}.yaml` | 每個 event 一個 YAML |
| Layer 3（Problem Space） | `analysis/problem-spaces/{problem_domain_id}.yaml` | 每個 problem domain 一個 YAML |

---

## 十、第一層：文本發生學（Segment Layer Schema）

### 10.1 目的

不是提取「概念是什麼」，而是記錄「概念在這個文本切片中**正在變成什麼**」。文本切片（segment）可以是段落、手稿頁、講義論證單元或整份文獻的關鍵節點。

### 10.2 數據字段

```yaml
segment_id: vyg_1934_tos_ch6_p245_para3
source_text:
  title: "文獻標題"
  author: "L. S. Vygotsky"
  date_composed: "1934-01"          # 寫作年代
  date_published: 1934               # 出版年代
  version: "手稿/定稿/編輯版/英譯版"
  archive_location: "family_archive_zavershneva_2006"  # 檔案來源

genetic_level: microgenesis | ontogenesis | phylogenesis | sociogenesis

concept_event:
  target_concept: "znachenie_slova"           # 目標概念
  genetic_status: germination | maturity | transition | qualitative_leap | crisis | emergence | sublatation | regression | interruption
  previous_phase: "前一階段的概念身份"
  next_phase: "下一階段的概念身份（若可推論）"
  quality_change: true                        # 是否發生非連續性質變
  dialectical_structure:
    thesis: "正題"
    antithesis: "反題（文本中出現的自我否定或內在矛盾）"
    synthesis: "合題（若文本中嘗試綜合）"

temporal_dynamics:
  linear_date: "1934-01"
  spiral_level: 1 | 2 | 3                    # 1=首次提出, 2=螺旋回歸, 3=再次回歸更高抽象
  spiral_position: "return_to_language_problem_with_consciousness_tools"
  internal_tempo: accelerating | stalling | rupture

problem_space_anchor:
  core_question: "語言如何組織意識"
  dimension_tags: ["D1_method", "D5_concept_evolution", "D9_affective"]
```

### 10.3 發生學層級（Genetic Levels）

| 層級 | 時間尺度 | 來源 |
|------|---------|------|
| **微生成（Microgenesis）** | 分鐘/小時/單次實驗內的概念變形 | Vygotsky；Werner |
| **個體發生（Ontogenesis）** | 個體思想傳記中的概念演化（年/階段） | Vygotsky；Piaget |
| **系統發生（Phylogenesis）** | 文明史/人類學尺度（百年/千年） | Vygotsky；Marx 歷史唯物主義 |
| **社會發生（Sociogenesis）** | 學派/制度/出版史中的概念擴散 | Vygotsky；Moscovici |

### 10.4 發生學狀態（Genetic Statuses）

`germination`（萌芽） → `maturity`（成熟） → `transition`（過渡） → `qualitative_leap`（質變） → `crisis`（危機） → `emergence`（湧現） → `sublatation`（揚棄） → `regression`（回歸） → `interruption`（中斷）

### 10.5 與上層接口

- 每個 `concept_event` 若 `quality_change=true`（即發生 `qualitative_leap` 或 `crisis`），必須在 Event Layer 註冊一個 `event_id`
- `problem_space_anchor.core_question` 指向 Problem Space 的 `problem_statement`

---

## 十一、第二層：事件層（Event Layer Schema）

### 11.1 目的

記錄理論系統的**相變（Phase Transition）**。不是記錄「誰做了什麼」，而是記錄「理論地殼在何處斷裂、新大陸在何處湧現」。

### 11.2 核心事件類型

| 類型 | 定義 | 來源 |
|------|------|------|
| **crisis** | 舊系統瓦解，新系統尚未成形，系統處於高張力混沌 | Vygotsky；Bachelard |
| **qualitative_leap** | 概念發生非連續、不可逆的理論身份跳躍 | Vygotsky；Hegel |
| **emergence** | 新質從舊質交互中不可還原地湧現 | Vygotsky；Prigogine |
| **sublatation** | 舊概念被克服，但核心要素被保存並提升至更高層次 | Hegel；Vygotsky |
| **spiral_return** | 同一問題以更高抽象層次、帶著新工具重新出現 | Vygotsky；Hegel |

### 11.3 數據字段

```yaml
event_id: crisis_1932_semantic_turn
event_type: crisis | qualitative_leap | emergence | sublatation | spiral_return

system_state_before:
  dominant_paradigm: "cultural_historical_toolism"
  core_operator: "orudie_znak"
  stable_relations:
    - "orudie -> deyatelnost -> kulturniy_razvitie"

crisis_symptoms:
  - "舊系統無法解決的內在矛盾（如 znak_ne_mozhet_obyasnit_vnutrennee_soznanie）"

transition_mechanism: dialectical_negation | conceptual_harvesting | political_deformation | experimental_breakthrough

system_state_after:
  emergent_paradigm: "semantic_system_dynamics"
  core_operator: "smyslovaya_sistema"
  stable_relations:
    - "slovo -> znachenie -> smysl -> soznanie"

spiral_relation:
  returns_to: "problem_yazyk_i_mysl_1928"
  returns_with:
    - "spinoza_affectus"
    - "hegel_aufhebung"
  new_level: higher_abstraction | deeper_concretion | broader_integration

temporal_span:
  onset_date: "1932-03"
  peak_date: "1934-01"
  closure_date: "1934-06"

source_segments:
  - "指向 Layer 1 的 segment_id 列表"
problem_domains:
  - "指向 Layer 3 的 problem_domain_id 列表"
```

### 11.4 過渡機制（Transition Mechanisms）

| 機制 | 定義 | 範例 |
|------|------|------|
| `dialectical_negation` | 辯證否定：舊命題被內在矛盾推翻 | Vygotsky 超越工具中介走向語義系統 |
| `conceptual_harvesting` | 概念採集：從其他傳統攝取概念碎片重新熔鑄 | Vygotsky 對 Pavlov 第二信號系統的轉化 |
| `political_deformation` | 政治變形：外部意識形態壓力迫使理論轉向 | 蘇聯體制對精神分析的壓制 |
| `experimental_breakthrough` | 實驗突破：新實驗證據強制理論重組 | 雙重刺激法的實驗發現 |

### 11.5 與其他層的關係

- **向下**：聚合多個 Layer 1 的 `concept_event`（當多個概念同時經歷質變時，標記為系統級事件）
- **向上**：`problem_domains` 指向 Layer 3，說明「這次相變發生在哪些問題域的交會處」

---

## 十二、第三層：問題共享領域（Problem Space Layer Schema）

### 12.1 目的

將「問題域」從人物/文本中解放出來，作為**獨立節點**。記錄 Vygotsky 如何從多個斷裂的、平行的、甚至彼此不知對方的傳統中**採集概念碎片並重新熔鑄**。

### 12.2 核心概念

| 術語 | 定義 | 來源 |
|------|------|------|
| **問題域（Problem Domain）** | 跨傳統共享的理論問題，獨立於任何單一學者 | 本框架原創 |
| **關係拓撲（Relation Topology）** | 學者與問題域的連結類型 | 本框架原創 |
| **概念採集（Harvesting）** | Vygotsky 讀取某傳統、轉化其概念碎片 | 類比 Marx 的古典政治經濟學批判 |
| **概念移民鏈（Mediator Chain）** | 概念通過中介者從 A 傳統移到 B 傳統 | 基於女性學者網絡研究 |
| **對位/共振（Counterpoint/Resonance）** | 兩學者共享問題域但從相反端點進入 | 本框架原創 |
| **負片證據（Negative Evidence）** | 無直接文獻，但概念結構同構+機構重疊+策略性沉默 | Zavershneva 檔案考古 |

### 12.3 關係拓撲類型

| 類型 | 標記 | 定義 | 實例 |
|------|------|------|------|
| 直接合作 | `collaborative` | 共同實驗、共同授課、理論共構 | Luria, Leontiev, Zeigarnik |
| 機構共存 | `copresence` | 同一機構/城市，共享學術空氣 | Bakhtin 圈, Spielrein, Schmidt |
| 單向攝取/轉化 | `harvesting` | Vygotsky 讀他、轉化他 | Pavlov, Piaget, Freud, Spinoza, Marx |
| 平行問題域 | `parallel` | 無直接文本接觸，處理同一問題 | Tynyanov, Werner |

### 12.4 對位類型（Resonance Types）

| 類型 | 定義 | 實例 |
|------|------|------|
| **互補對位** | 兩端點拼合為完整光譜 | Spielrein（無意識→意識）與 Vygotsky（意識→無意識） |
| **鏡像對位** | 方向相反，結構同構 | Spielrein「自閉語言」vs Vygotsky「自我中心言語」 |
| **螺旋回歸** | 同一問題在更高層次重現 | 1928「語言與思維」→1934「語言與思維」 |

### 12.5 數據字段

```yaml
problem_domain_id: PD_language_consciousness
problem_statement: "語言如何組織意識與心理現實"

approaches:
  - scholar: "學者名"
    approach_vector: "理論端點描述"
    key_concepts:
      - "概念列表"
    relation_topology: collaborative | copresence | harvesting | parallel
    directionality: bidirectional | unidirectional | null
    harvesting_sources:
      - source: "pavlov_vtoraya_signalya_sistema"
        original_fragment: "原始概念碎片"
        vygotsky_transmutation: "Vygotsky 的轉化描述"
        mechanism: analogical_translation | dialectical_inversion | dialectical_elevation
    textual_traces:
      direct_citations:
        - "直接引用"
      conceptual_echoes:
        - "結構同構概念"
      strategic_silences:
        - "應引用但沉默的人物"
      mediator_chain:
        - "lewin -> zeigarnik -> vygotsky_circle"

contrastive_pairs:
  - pair_id: "對位對標識"
    scholar_a: "學者A"
    vector_a: "方向A"
    scholar_b: "學者B"
    vector_b: "方向B"
    resonance_type: complementary | mirror | spiral
    synthetic_gap: "統合缺口描述"

event_links:
  - "指向 Layer 2 的 event_id"
```

### 12.6 關鍵作者清單

此層的 `approaches[].scholar` 可引用以下人物（不限於此）：

**直接合作**：Vygotsky, Luria, Leontiev, Zeigarnik, Birenbaum, Kaulina, Bozhovich, Morozova, Levina, Slavina
**機構共存**：Bakhtin, Voloshinov, Medvedev, V. Schmidt, Blonsky
**單向攝取**：Marx, Hegel, Spinoza, Freud, Piaget, Pavlov, Lewin, Köhler, Wertheimer
**平行問題域**：Jakobson, Tynyanov, Mandelstam, Werner, Spielrein

---

## 十三、跨層接口與數據流

### 13.1 ID 引用協議

```
第一層（Segment）      第二層（Event）         第三層（Problem Space）
                                                                 
segment_id ──(聚合)──→ event_id ──(指向)──→ problem_domain_id
                         ↑                        │
                         │  (source_segments)      │  (event_links)
                         └────────────────────────┘
```

| 路徑 | 接口 | 方向 |
|------|------|:----:|
| Segment → Event | 若 `concept_event.quality_change=true`，在 event 的 `source_segments` 中註冊該 `segment_id` | ↑ |
| Segment → Problem Space | `problem_space_anchor.core_question` 的文字匹配 `problem_statement` | ↑ |
| Event → Problem Space | `event.problem_domains[]` 指向 `problem_domain_id` | ↑ |
| Problem Space → Event | `problem_domain.event_links[]` 指向 `event_id` | ↓ |
| Event → Segment | `event.source_segments[]` 指向 `segment_id` | ↓ |

### 13.2 查詢模式

| 模式 | SQL 類比 | 用途 |
|------|---------|------|
| 向上追溯 | `segment → event → problem_domain` | 從文本痕跡到問題域 |
| 向下穿透 | `problem_domain → event → segment` | 從問題域到具體文本證據 |
| 橫向共振 | `problem_domain.approaches[].scholar` | 同一問題域內不同學者的對位分析 |
| 時間切片 | `segment.temporal_dynamics.linear_date` | 按時間軸查詢概念演化 |
| 螺旋軌跡 | `segment.temporal_dynamics.spiral_level` | 查詢概念回歸的模式 |
