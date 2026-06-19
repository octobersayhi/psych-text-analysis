# psych-text-analysis — 任務日誌

> **版本**：v0.2  
> **日期**：2026-06-17  
> **功能**：追蹤執行狀態、設計決策記錄、已完成操作、跨設備上下文恢復

---

## 一、專案初始化（2026-06-15）

### ✅ 已完成

- [x] 目錄結構建立
- [x] corpus/vygotsky — 7 冊複製完成（含 YAML meta）
- [x] corpus/psychoanalysis — 5 冊複製完成（含 YAML meta）
- [x] system-template/scripts — 4 個腳本複製完成
- [x] 根文件建立：README.md、GRANDPLAN.md、AGENTS.md、SPIRAL.md、GENERAL-PRINCIPLES.md、SCHEMA.md、TASKLOG.md
- [x] .gitignore 建立
- [x] Git 初始化

---

## 二、三層發生學架構導入（2026-06-16 ~ 2026-06-17）

### 💡 核心決策：導入三層發生學資料庫

用戶提交了一份詳細的**三層發生學資料庫規格書**，內容涵蓋：

| 層 | 名稱 | 核心功能 |
|:---|------|---------|
| Layer 1 | **文本發生學（Textual Genesis）** | 文本切片級概念事件——記錄「概念正在變成什麼」 |
| Layer 2 | **事件層（Event Layer）** | 系統級相變——危機、質變、湧現、揚棄、螺旋回歸 |
| Layer 3 | **問題共享領域（Problem Space）** | 問題域為獨立節點——關係拓撲、對位分析、概念採集 |

**設計判斷**：三層架構與現有專案（雙世界線 α₁/γ + DCA + T-SALC）是**垂直互補**關係，不是取代關係。現有專案是「文件級」索引，三層是「段落/事件/問題域」級的深化。

### ✅ 已修改文件

| 文件 | v0.1 → v0.2 | 關鍵變更 |
|------|:-----------:|---------|
| **SCHEMA.md** | ✅ | 新增 D1–D10 十維度標記系統（第零節）+ 三層 Schema 定義（第九至十三節）+ 跨層接口協議 |
| **GRANDPLAN.md** | ✅ | 新增「三層數據模型」章節（第六節）+ 更新 Phase Gate 路線以包含三層建設 + 擴充術語體系 |
| **GENERAL-PRINCIPLES.md** | ✅ | 新增**原則 20：「問題域是分析的單位，不是作者」**——定義關係拓撲、對位類型、三層操作鏈 |
| **AGENTS.md** | ✅ | 新增「三層數據引用」操作規則 + 更新 ALWAYS 規則含跨層 ID 校驗 |
| **SPIRAL.md** | ✅ | 擴充 M-E-G 引擎含三層指標 + 重寫 Phase Gate 表格 + 新增三種飽和條件（文件/Segment/Problem Domain） |

### 🏗️ 當前架構總覽

```
世界線 α₁（真實心理學史）         世界線 γ（理論張力）
       │                               │
       ▼                               ▼
    ┌──────────────────────────────────────┐
    │       三層數據模型（操作化層）          │
    │                                      │
    │  Layer 3: Problem Space              │
    │    ↑ 問題域定義「誰與誰共享什麼」       │
    │  Layer 2: Event Layer                │
    │    ↑ 事件記錄「相變在何處發生」         │
    │  Layer 1: Textual Genesis            │
    │    ↑ 文本切片記錄「概念在何處變形」     │
    └──────────────────────────────────────┘
```

### 📂 新增目錄結構

```
index/
├── segments/               ⬜ Layer 1（首批試點）
│   ├── vygotsky/
│   └── psychoanalysis/
└── data/                   ⬜ 編譯庫（Phase 2）

analysis/
├── events/                 ⬜ Layer 2（Phase 3）
├── problem-spaces/         ⬜ Layer 3（Phase 4）
├── dca/                    ⬜ DCA 分析產出
└── spectrum/               ⬜ tt 頻譜產出
```

---

## 三、文獻檔案狀態

### 核心文件版本

| 文件 | 版本 | 日期 | 修改 |
|------|:---:|:---:|:----|
| README.md | v0.1 | 2026-06-15 | 初始 |
| GRANDPLAN.md | **v0.3** | 2026-06-19 | ✅ Phase 0 狀態更新——標為「擴充中」，新增橋樑人物 Lewin |
| SCHEMA.md | **v0.3** | 2026-06-19 | ✅ 新增 Lewin 系概念至精神分析詞表 |
| GENERAL-PRINCIPLES.md | **v0.2** | 2026-06-16 | ✅ 新增原則 20 |
| AGENTS.md | **v0.2** | 2026-06-16 | ✅ 三層數據引用規則 |
| SPIRAL.md | **v0.2** | 2026-06-16 | ✅ 三層 MEG + 三層飽和條件 |
| TASKLOG.md | **v0.3** | 2026-06-19 | ✅ 本文件 + 新增 Lewin 記錄 |

### 語料庫統計

| 子語料庫 | 冊數 | 總大小 | 總行數 | 章節（估計） |
|------|:---:|:---:|:---:|:---:|
| vygotsky | 7 | ~9.1 MB | ~13,311 | ~100 |
| psychoanalysis | **6** | **~4.4 MB** | **~33,293** | ~90 |
| **合計** | **13** | **~13.5 MB** | **~46,604** | **~190** |

### 模組狀態

| 模組 | 狀態 | 說明 |
|------|:---:|------|
| corpus/vygotsky | ✅ | 7 冊完整 |
| corpus/psychoanalysis | ✅ | **6 冊（擴充中，含橋樑人物 Lewin）** |
| system-template/scripts | ✅ | 4 個腳本就位 |
| SCHEMA.md | ✅ | v0.2（含三層 Schema） |
| GENERAL-PRINCIPLES.md | ✅ | v0.2（20 原則） |
| GRANDPLAN.md | ✅ | v0.2（含三層數據模型） |
| AGENTS.md | ✅ | v0.2（含三層規則） |
| SPIRAL.md | ✅ | v0.2（含三層指標） |
| TASKLOG.md | ✅ | v0.2（本文件） |
| documents-raw/ | ⬜ | Phase 1 未啟動 |
| dimension_tags（D1–D10） | ⬜ | Phase 1 疊加 |
| segments/ | ⬜ | Layer 1 未啟動 |
| compiled-corpus.json | ⬜ | Phase 2 未啟動 |
| DCA 分析 | ⬜ | Phase 3 未啟動 |
| events/ | ⬜ | Layer 2 未啟動 |
| problem-spaces/ | ⬜ | Layer 3 未啟動 |
| GitHub repo | ⬜ | 未建立 |

---

## 四、Phase Gate GPS

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

## 五、三層發生學——關鍵設計決策記錄

### 決策 1：為什麼不改寫現有 Frontmatter Schema

現有 SCHEMA.md 的 Frontmatter 是**文件級**元數據（每章/文章一個條目）。三層的 Segment Schema 是**段落級**——兩者粒度不同，應共存而非取代。Segment 註記存放在 `index/segments/` 下各自的 YAML 文件中，不嵌入 Frontmatter。

### 決策 2：D1–D10 的角色

十維度標記是連接文件級索引與三層發生學的**輕量橋樑**。在 Phase 1 索引時為每個條目標記 1–3 個維度標籤（`dimension_tags`），不需要做完整的 Segment 註記就能開始看到維度分佈。

### 決策 3：DCA 與 Event Layer 的關係

DCA 是**分析流程**（Crisis→Lag→Alternative→Direction→New Crisis），Event Layer 是**該流程的結構化輸出存儲**。DCA 分析完成後，將產出格式化為 Event Schema 記錄，存入 `analysis/events/`。

### 決策 4：Problem Space 不依賴完整 Segment 數據

Problem Domain 節點的建立不需要等所有 Segment 註記完成。Phase 3–4 就可以根據已知的學術史知識建立首批 Problem Domain，隨 Segment 數據積累逐步完善。

### 決策 5：三層建設不改變 Phase Gate 順序

三層建設疊加在現有 Phase Gate 之上，而不是取代它。每個 Phase 在完成原有任務的同時疊加對應的三層子任務。

| 現有 Phase | 疊加的三層子任務 | 優先級 |
|:-----------|-----------------|:------:|
| Phase 1：結構化索引 | D1–D10 維度標記 + 首批 segment 試點 | P0 |
| Phase 2：編譯庫 + Prefix | Segment 元數據納入編譯庫 | P1 |
| Phase 3：DCA 深度分析 | DCA 產出→Event Schema 格式化 | P0 |
| Phase 4：α₁ 制度脈絡基線 | 首批 Problem Domain 節點（≥5） | P0 |
| Phase 5：tt 頻譜分析 | Segment temporal_dynamics 對齊 tt 時間軸 | P1 |
| Phase 6：跨學派比較 | 三層整合穿透查詢 | P1 |

---

## 六、下一步行動

### 🔜 立即（Phase 1 啟動）

1. **建立 `index/documents-raw/` 目錄結構**（按 corpus + 卷組織）
2. **建立首個條目**：從 Vygotsky `vol-1-problems-of-general-psychology.md` 的 "Thinking and Speech" 第七章開始
3. **標記 D1–D10 維度**：首個條目應包含 `dimension_tags`（預估：D5 內在言語、D10 哲學方法論）
4. **腳本適配**：修改 `build-compiled-db.py` 中的 `SYSTEM_NAME`，確認路徑正確

### 🔜 短期（Phase 1–2）

5. **首批 segment 試點**：選取 "Thinking and Speech" Ch.7 中 1–2 個關鍵段落做 segment 註記
6. **GitHub repo**：建立遠端 repo 並推送當前狀態
7. **TASKLOG 更新**：每完成一個 Phase 更新本文件

### 🔜 中期（Phase 3–4）

8. **首批 DCA 分析**：Spielrein (1912)、Vygotsky (1934) Ch.7、Freud & the Bolsheviks
9. **Event Schema 格式化**：將 DCA 產出轉為 `analysis/events/` 下的 YAML
10. **首批 Problem Domain**：至少 5 個（PD_language_consciousness、PD_affect_drive、PD_social_mediation 等）

---

## 七、阻擋問題

| # | 問題 | 狀態 | 備註 |
|---|------|:---:|------|
| 1 | 腳本 `SYSTEM_NAME` 尚未適配 | ⚠️ 待處理 | `build-compiled-db.py` 中的 `SYSTEM_NAME = "corpus"` 可能需要改為 `"psych-text-analysis"` |
| 2 | `index/` 目錄尚未建立 | ⚠️ 待處理 | Phase 1 開始時需建立 `index/documents-raw/` |
| 3 | `analysis/` 目錄尚未建立 | ⚠️ 待處理 | Phase 3 開始時需建立 `analysis/events/`、`analysis/problem-spaces/` |
| 4 | GitHub 遠端 repo 未建立 | ⚠️ 待處理 | 需人類手動操作 |
| 5 | Segment Schema 無自動校驗腳本 | ⚠️ 待處理 | 現有 `validate-schema.py` 只檢查 Frontmatter，不檢查 segment/event/problem-space YAML |

---

## 八、跨設備恢復指引

在新的設備上恢復工作會話時：

1. **讀取 `GRANDPLAN.md`** → 理解雙世界線架構與三層數據模型
2. **讀取 `SPIRAL.md`** → 確認當前 GPS 坐標與 Phase Gate
3. **讀取 `AGENTS.md`** → 確認操作規則與邊界
4. **讀取 `GENERAL-PRINCIPLES.md`** → 確認方法論原則（特別是原則 20）
5. **讀取 `SCHEMA.md`** → 確認 Frontmatter 格式與三層 Schema 定義
6. **讀取 `TASKLOG.md`** → 確認當前狀態、已完成操作、下一步行動（本文件）

關鍵上下文關鍵詞：`三層發生學` `D1–D10` `Problem Space` `Event Layer` `Textual Genesis` `原則 20` `關係拓撲` `對位分析` `概念採集`

## 七、Corpus 擴充記錄

### 2026-06-19：新增 Kurt Lewin — Principles of Topological Psychology

- **背景**：Lewin 是 Vygotsky 與精神分析之間的關鍵橋樑人物（場域理論、衝突理論、拓撲心理學）
- **行動**：
  - Internet Archive OCR 全文取得（公領域，5029 行）
  - 建立 `corpus/psychoanalysis/principles-of-topological-psychology.md`（含 YAML frontmatter）
  - 建立 `corpus/psychoanalysis/principles-of-topological-psychology-meta.yaml`（含完整 chapter_outline）
  - 更新 `corpus/psychoanalysis/INDEX.md`（總數 5→6）
  - 更新 `SCHEMA.md` 第六節精神分析詞表（新增 14 個 Lewin 系概念）
  - 更新 `GRANDPLAN.md` Phase 0 狀態
  - 刪除暫存 `corpus/lewin/` 目錄
- **狀態**：✅ 完成
- **注意**：OCR 僅收錄至第 10 章（共 18 章），第 11–18 章待補
