# psych-text-analysis — Frontmatter Schema

> **版本**：v0.1  
> **日期**：2026-06-15  
> **適用範圍**：`index/documents-raw/*.md`（結構化後的個別文獻條目）  
> **方法論注入來源**：ECC SCHEMA.md v0.4 + EME MECW SCHEMA.md v0.1

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

### 精神分析系

`destruction_as_cause_of_becoming` `reproductive_drive` `death_drive` `libido` `unconscious` `transference` `countertransference` `oedipus_complex` `castration_anxiety` `penis_envy` `object_relations` `schizophrenia` `dementia_praecox` `psychoanalytic_case_study` `free_association` `dream_interpretation` `resistance` `repression` `sublimation` `infantile_sexuality` `psychosexual_development` `narcissism` `melancholia`

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
