#!/usr/bin/env python3
"""
validate-schema.py — psych-text-analysis Schema 驗證器

檢查 index/documents-raw/ 下所有 .md 的 Frontmatter 是否符合 SCHEMA.md 規範。

用法:
    python system-template/scripts/validate-schema.py
"""

import glob, os

REQUIRED_FIELDS = ["id", "title", "author", "year", "corpus", "doc_type", "status"]
RECOMMENDED_FIELDS = ["source_volume", "concepts", "key_figures"]
VALID_CORPORA = ["vygotsky", "psychoanalysis"]
VALID_DOC_TYPES = ["chapter", "article", "letter", "notebook", "case_study", "monograph"]
VALID_STATUSES = ["raw", "indexed", "annotated", "analyzed"]

RAW_DIR = "index/documents-raw"


def validate():
    files = sorted(glob.glob(f"{RAW_DIR}/**/*.md", recursive=True))
    errors = 0
    warnings = 0
    
    for fpath in files:
        if "_EXAMPLE" in fpath or "_INDEX" in fpath:
            continue
        try:
            import yaml
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            parts = content.split('---', 2)
            if len(parts) < 3:
                print(f"🔴 {fpath}: 無有效 Frontmatter")
                errors += 1
                continue
            fm = yaml.safe_load(parts[1])
            
            missing = [f for f in REQUIRED_FIELDS if f not in fm]
            if missing:
                print(f"🔴 {fpath}: 缺少必填欄位 {missing}")
                errors += 1
            else:
                missing_rec = [f for f in RECOMMENDED_FIELDS if f not in fm or not fm.get(f)]
                if missing_rec:
                    print(f"🟡 {fpath}: 建議補充 {missing_rec}")
                    warnings += 1
                if fm.get('corpus') not in VALID_CORPORA:
                    print(f"🟡 {fpath}: corpus 值異常: {fm.get('corpus')}")
                    warnings += 1
                if fm.get('doc_type') not in VALID_DOC_TYPES:
                    print(f"🟡 {fpath}: doc_type 值異常: {fm.get('doc_type')}")
                    warnings += 1
                if fm.get('status') not in VALID_STATUSES:
                    print(f"🟡 {fpath}: status 值異常: {fm.get('status')}")
                    warnings += 1
                year = fm.get('year')
                if year and (year < 1800 or year > 2030):
                    print(f"🟡 {fpath}: year 超出合理範圍: {year}")
                    warnings += 1
                    
        except Exception as e:
            print(f"🔴 {fpath}: {e}")
            errors += 1
    
    print(f"\n{'✅ 全部通過' if errors == 0 else f'🔴 {errors} errors, {warnings} warnings'}")


if __name__ == "__main__":
    validate()
