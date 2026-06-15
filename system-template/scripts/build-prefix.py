#!/usr/bin/env python3
"""
build-prefix.py — psych-text-analysis AI Prefix 生成器

從 index/data/compiled-corpus.json 生成濃縮索引文本，供 AI Agent 載入。

用法:
    python system-template/scripts/build-prefix.py
"""

import json, os
from collections import defaultdict

SYSTEM_NAME = "corpus"
DB_PATH = f"index/data/compiled-{SYSTEM_NAME}.json"
OUTPUT_PATH = f"index/data/{SYSTEM_NAME}-prefix.txt"

CORPUS_NAMES = {
    "vygotsky": "Vygotsky 文化歷史學派",
    "psychoanalysis": "精神分析經典",
}


def estimate_tokens(text: str) -> int:
    chinese = sum(1 for c in text if '\u4e00' <= c <= '\u9fff' or '\u3000' <= c <= '\u303f')
    return int(chinese * 0.6 + (len(text) - chinese) * 0.25)


def build():
    if not os.path.exists(DB_PATH):
        print("❌ 請先執行 build-compiled-db.py")
        return
    
    db = json.load(open(DB_PATH, 'r', encoding='utf-8'))
    entries = db.get("entries", [])
    
    prompt = f"""你是 psych-text-analysis 的心理學文本分析師。
以下是本專案的心理學文獻索引摘要（{len(entries)} 條目）。
請先查本索引定位相關條目，再讀取 index/documents-raw/ 下的對應檔案。

核心語料庫：Vygotsky 全集（7 冊）+ 精神分析經典（5 冊）= 12 冊
核心方法論：DCA（辯證反事實分析）+ T-SALC（理論張力頻譜）+ Vygotsky 十九原則"""

    lines = [prompt, "", "=" * 60]
    lines.append(f"## psych-text-analysis 索引（{len(entries)} 條目）\n")
    
    corpora = defaultdict(list)
    for e in entries:
        corpora[e.get("corpus", "?")].append(e)
    
    for corpus in sorted(corpora.keys()):
        corpus_entries = corpora[corpus]
        label = CORPUS_NAMES.get(corpus, corpus)
        lines.append(f"### {label}（{len(corpus_entries)} 條目）")
        for e in corpus_entries:
            concepts = ", ".join(e.get("concepts", [])[:5]) if e.get("concepts") else ""
            year_str = str(e.get('year', '?'))
            lines.append(f"  `{e['id']}` [{year_str}] {e.get('author','?')} — {e['title'][:80]}")
            if concepts:
                lines.append(f"    ↳ {concepts}")
        lines.append("")
    
    full = "\n".join(lines)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    open(OUTPUT_PATH, 'w', encoding='utf-8').write(full)
    print(f"✅ {OUTPUT_PATH}: {len(full):,} chars, ~{estimate_tokens(full):,} tokens")


if __name__ == "__main__":
    build()
