# psych-text-analysis — 心理學文本分析引擎

> **版本**：v0.1  
> **日期**：2026-06-15  
> **定位**：基於 Vygotsky 文化歷史學派與精神分析經典文獻的**結構化文本分析系統**——不是電子書架，是自帶方法論的研究引擎  
> **核心語料**：Vygotsky 全集（7 冊）+ 精神分析經典（5 冊）= 12 冊，~13.3 MB  
> **方法論來源**：ECC 多世界線比較認知系統（兩年開發經驗的萃取注入）

---

## 一句話

> 用 Vygotsky 的方法論分析 Vygotsky 和精神分析的文本——從索引到頻譜，從 DCA 到證偽。

---

## 目錄結構

```
psych-text-analysis/
├── README.md                     # 本文件
├── GRANDPLAN.md                  # 架構總綱（雙世界線、五公理、Phase Gate）
├── AGENTS.md                     # AI Agent 協作協議
├── SPIRAL.md                     # 研究迴旋導航（M-E-G 引擎）
├── GENERAL-PRINCIPLES.md         # 方法論十九原則（Vygotsky《思維與言語》第七章）
├── SCHEMA.md                     # Frontmatter 規範
├── TASKLOG.md                    # 進度追蹤
│
├── corpus/                       # 📚 來源文獻（12 冊，含結構化 YAML meta）
│   ├── vygotsky/                 # Vygotsky 全集 7 冊
│   └── psychoanalysis/           # 精神分析經典 5 冊
│
├── system-template/              # 🔧 基礎設施腳本
│   └── scripts/
│       ├── build-compiled-db.py  # 編譯 SSOT JSON
│       ├── build-prefix.py       # 生成 AI Prefix
│       ├── validate-schema.py    # Frontmatter 校驗
│       └── query.py              # CLI 查詢
│
├── index/                        # 📊 索引層
│   ├── data/                     # 編譯庫 + Prefix（腳本生成）
│   └── documents-raw/            # 結構化後的個別文獻
│
├── analysis/                     # 🔬 分析層
│   ├── dca/                      # DCA 理論演化分析產出
│   └── spectrum/                 # tt（理論張力）頻譜產出
│
└── docs/method/                  # 📖 方法論文檔
    ├── falsifications/           # 證偽水滴
    └── seeds/                    # 方法論種子
```

---

## 快速開始

```bash
# 1. 查看語料庫
ls corpus/vygotsky/ corpus/psychoanalysis/

# 2. 校驗文獻結構
python system-template/scripts/validate-schema.py

# 3. 建立編譯庫
python system-template/scripts/build-compiled-db.py

# 4. 查詢
python system-template/scripts/query.py stats
python system-template/scripts/query.py search "inner speech"

# 5. 生成 AI Prefix
python system-template/scripts/build-prefix.py
```

---

## 核心方法論（從 ECC 注入）

| 模組 | 用途 |
|------|------|
| **SSOT Frontmatter** | YAML 元數據為唯一真實來源——每本書的 `key_concepts`、`key_figures`、`chapter_outline` 在 meta 中定義 |
| **DCA 遞歸引擎** | Crisis→Lag→Alternative→Direction→New Crisis——追蹤精神分析理論分裂與演化 |
| **T-SALC 頻譜** | Butterworth 長波/短波分解——tt（理論張力）信號 |
| **SPIRAL M-E-G** | Measure→Explain→Generate——強制每個 Phase 產出下一步假說 |
| **證偽方法論** | 結構化記錄每個假說的證偽——防止確認偏誤 |
| **Vygotsky 十九原則** | 語法≠語義、心理主詞≠語法主詞、只有數學無歧義……**

## 與 ECC 的關係

本專案**不屬於** ECC/EME 兩院制蘇維埃體系。它是一個獨立的心理學文本分析專案，從 ECC 萃取並注入了以下經驗：

- `system-template/` 基礎設施（SSOT + 編譯 DB + AI Prefix）
- `GENERAL-PRINCIPLES.md` 方法論原則（原生來自 Vygotsky）
- DCA / T-SALC / SPIRAL 方法論框架
- 證偽水滴與方法論種子體系

---

## 許可

本專案僅包含公開發表學術文獻的結構化索引與元數據。原始文獻版權歸屬原出版社與作者。
