#!/usr/bin/env python3
"""
build-compiled-db.py — psych-text-analysis 編譯庫生成器

讀取 index/documents-raw/ 下的所有 .md 條目，提取 YAML Frontmatter + 正文摘要，
輸出為單一 compiled-corpus.json 供查詢與 Prefix 生成。

用法:
    python system-template/scripts/build-compiled-db.py
"""

import json, glob, os

SYSTEM_NAME = "corpus"
RAW_DIR = "index/documents-raw"
OUTPUT_PATH = f"index/data/compiled-{SYSTEM_NAME}.json"

FM_FIELDS = ["id", "title", "author", "year", "corpus", "doc_type",
             "status", "source_volume", "concepts", "key_figures",
             "theoretical_position", "cross_references"]


def build():
    entries = []
    files = sorted(glob.glob(f"{RAW_DIR}/**/*.md", recursive=True))
    
    for fpath in files:
        if "_EXAMPLE" in fpath or fpath.endswith("_INDEX.md"):
            continue
        try:
            import yaml
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            parts = content.split('---', 2)
            if len(parts) < 3:
                continue
            fm = yaml.safe_load(parts[1])
            entry = {k: fm.get(k, '') for k in FM_FIELDS}
            entry["file"] = fpath
            entries.append(entry)
        except Exception as e:
            print(f"  ⚠️ {fpath}: {e}")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    db = {"_meta": {"total": len(entries), "system": SYSTEM_NAME}, "entries": entries}
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"✅ {OUTPUT_PATH}: {len(entries)} entries")


if __name__ == "__main__":
    build()
