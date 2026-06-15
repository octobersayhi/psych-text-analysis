#!/usr/bin/env python3
"""
query.py — psych-text-analysis CLI 查詢工具

用法:
    python system-template/scripts/query.py stats          # 統計概覽
    python system-template/scripts/query.py list           # 列出所有條目
    python system-template/scripts/query.py search "關鍵詞" # 全文搜索
    python system-template/scripts/query.py gap            # 語料庫缺口

依賴: index/data/compiled-corpus.json（由 build-compiled-db.py 生成）
"""

import json, sys, os
from collections import Counter

SYSTEM_NAME = "corpus"
DB_PATH = f"index/data/compiled-{SYSTEM_NAME}.json"

ALL_CORPORA = ["vygotsky", "psychoanalysis"]
ALL_DOC_TYPES = ["chapter", "article", "letter", "notebook", "case_study", "monograph"]


def load():
    if not os.path.exists(DB_PATH):
        print(f"❌ {DB_PATH} 不存在，請先執行 build-compiled-db.py")
        sys.exit(1)
    return json.load(open(DB_PATH, 'r', encoding='utf-8'))


def cmd_stats(db):
    print(f"總條目: {db['_meta']['total']}")
    corpora = Counter(e.get('corpus', '?') for e in db['entries'])
    print("\n按語料庫:")
    for c, n in sorted(corpora.items()):
        print(f"  {c}: {n}")
    types = Counter(e.get('doc_type', '?') for e in db['entries'])
    print("\n按文獻類型:")
    for t, n in sorted(types.items()):
        print(f"  {t}: {n}")
    years = [e.get('year') for e in db['entries'] if e.get('year')]
    if years:
        print(f"\n年份範圍: {min(years)} – {max(years)}")


def cmd_list(db, args):
    for e in db['entries']:
        print(f"  [{e.get('corpus','?')}] {e.get('author','?')} — {e['title'][:60]}")
        print(f"   id: {e['id']}  |  year: {e.get('year','?')}  |  type: {e.get('doc_type','?')}")


def cmd_search(db, args):
    query = ' '.join(args)
    results = [e for e in db['entries'] if query.lower() in json.dumps(e, ensure_ascii=False).lower()]
    print(f"搜尋 '{query}': {len(results)} 結果\n")
    for e in results:
        concepts = ', '.join(e.get('concepts', [])[:5]) if e.get('concepts') else ''
        print(f"  [{e.get('corpus','?')}] {e.get('author','?')} — {e['title'][:60]}")
        print(f"   id: {e['id']}  |  year: {e.get('year','?')}")
        if concepts:
            print(f"   concepts: {concepts}")


def cmd_gap(db):
    print("=== 語料庫覆蓋 ===")
    existing_corp = Counter(e.get('corpus', '?') for e in db['entries'])
    for c in ALL_CORPORA:
        n = existing_corp.get(c, 0)
        bar = '█' * min(n, 40)
        print(f"  {c}: {n:3d} {bar}")
    print("\n=== 文獻類型覆蓋 ===")
    existing_type = Counter(e.get('doc_type', '?') for e in db['entries'])
    for t in ALL_DOC_TYPES:
        n = existing_type.get(t, 0)
        bar = '█' * min(n, 20)
        print(f"  {t}: {n:3d} {bar}")
    print("\n=== 無年份條目 ===")
    no_year = [e for e in db['entries'] if not e.get('year')]
    for e in no_year:
        print(f"  {e['id']}: {e['title'][:60]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    db = load()
    cmd = sys.argv[1]
    args = sys.argv[2:]
    {
        'stats': lambda db, args: cmd_stats(db),
        'list': lambda db, args: cmd_list(db, args),
        'search': lambda db, args: cmd_search(db, args),
        'gap': lambda db, args: cmd_gap(db),
    }[cmd](db, args)
