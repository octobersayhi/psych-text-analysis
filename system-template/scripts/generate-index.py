#!/usr/bin/env python3
"""
generate-index.py — Phase 1: 從 -meta.yaml 自動生成 index/documents-raw/ 條目

用法:
    python system-template/scripts/generate-index.py vygotsky          # 只處理 Vygotsky
    python system-template/scripts/generate-index.py psychoanalysis    # 只處理精神分析
    python system-template/scripts/generate-index.py                  # 全部

模式:
    --mode p0      只生成 DCA 候選的關鍵章節
    --mode full    生成所有章節 (default)
    --dry-run      只顯示將建立的檔案，不實際寫入
"""

import yaml, os, sys, re, glob
from datetime import datetime

CORPUS_DIR = "corpus"
OUTPUT_DIR = "index/documents-raw"

# 各卷的作者映射（可從 meta.yaml 自動讀取，此處為備用）
AUTHOR_MAP = {
    "vygotsky": "L. S. Vygotsky",
}

# doc_type 啟發式判斷
def infer_doc_type(title, meta_title):
    t = title.lower()
    if 'notebook' in t or 'notatki' in t:
        return 'notebook'
    if 'lecture' in t or 'лекци' in t:
        return 'chapter'
    if 'preface' in t or 'introduction' in t or 'prologue' in t or 'foreword' in t:
        return 'chapter'
    if 'letter' in t or 'pismo' in t:
        return 'letter'
    return 'chapter'

def make_id(corpus, volume_id, chapter_title):
    """從章節標題生成短 id。"""
    # 移除特殊字元，轉為 kebab-case
    clean = re.sub(r'[^a-z0-9\s-]', '', chapter_title.lower())
    clean = re.sub(r'\s+', '-', clean.strip())[:60]
    clean = re.sub(r'-+', '-', clean)
    return f"{corpus}-{volume_id[:20]}-{clean}"

def make_filename(corpus, volume_id, chapter_idx, chapter_title):
    """生成檔名：{volume-id}-ch{idx}-{slug}.md"""
    clean = re.sub(r'[^a-z0-9\s-]', '', chapter_title.lower())
    clean = re.sub(r'\s+', '-', clean.strip())[:50]
    clean = re.sub(r'-+', '-', clean)
    return f"{volume_id}-ch{chapter_idx}-{clean}.md"

def build_frontmatter(corpus, meta, ch, ch_idx, volume_id):
    """建構 Frontmatter dict。"""
    fm = {
        "id": make_id(corpus, volume_id, ch['title']),
        "title": ch['title'],
        "author": meta.get('author', AUTHOR_MAP.get(corpus, 'Unknown')),
        "year": extract_year(meta.get('period', '')),
        "corpus": corpus,
        "doc_type": infer_doc_type(ch['title'], meta.get('title', '')),
        "status": "indexed",
        "source_volume": volume_id,
        "concepts": meta.get('key_concepts', [])[:8],  # 取前 8 個
        "key_figures": meta.get('key_figures', [])[:5],
        "theoretical_position": "unknown",
        "dimension_tags": [],
        "cross_references": [],
        "date_precision": "approximate",
    }
    # 嘗試從 title 提取年份
    year_match = re.search(r'(1[89]\d{2}|20[01]\d)', ch.get('title', ''))
    if not year_match:
        period = meta.get('period', '')
        if isinstance(period, (int, float)):
            year_match = None
            fm['year'] = int(period)
        else:
            year_match = re.search(r'(1[89]\d{2}|20[01]\d)', str(period))
    if year_match:
        fm['year'] = int(year_match.group(1))
    return fm

def extract_year(period_str):
    """從 period 字串提取年份。"""
    if not period_str:
        return 0
    if isinstance(period_str, (int, float)):
        return int(period_str)
    years = re.findall(r'(1[89]\d{2}|20[01]\d)', str(period_str))
    return int(years[-1]) if years else 0

def build_content(fm, ch, meta, ch_idx, meta_title):
    """建構完整的 .md 內容。"""
    summary = ch.get('summary', '').strip()
    
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, str) and (':' in v or '"' in v or v.startswith('{') or v.startswith('[')):
            escaped = v.replace('"', "'")
            lines.append(f'{k}: "{escaped}"')
        elif v is not None:
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: null")
    lines.append("---")
    lines.append("")
    
    # Summary 區
    lines.append("## Summary")
    lines.append("")
    if summary:
        lines.append(summary)
    else:
        lines.append("（尚待補充摘要）")
    lines.append("")
    
    # 來源資訊
    lines.append("### Source")
    lines.append("")
    lines.append(f"- **Volume**: {meta_title}")
    if ch.get('line_range'):
        lines.append(f"- **Line range**: {ch['line_range'][0]}–{ch['line_range'][1]}")
    lines.append("")
    
    # 三層分析模板
    lines.append("---")
    lines.append("")
    lines.append("## Three-Layer Analysis")
    lines.append("")
    lines.append("### Layer 1: Textual Genesis")
    lines.append("")
    lines.append("<!-- 此概念在此文本切片中的動態身份、genetic_level、genetic_status -->")
    lines.append("")
    lines.append("### Layer 2: Event Layer")
    lines.append("")
    lines.append("<!-- 此條目涉及的系統相變事件 (event_id) -->")
    lines.append("")
    lines.append("### Layer 3: Problem Space")
    lines.append("")
    lines.append("<!-- 此條目所屬的問題域 (problem_domain_id) -->")
    lines.append("")
    
    # Notes
    lines.append("---")
    lines.append("")
    lines.append("### Notes")
    lines.append("")
    lines.append("- `dimension_tags` 待人工標記")
    lines.append("- `cross_references` 待人工補齊")
    lines.append("- `theoretical_position` 待人工確定")
    lines.append("")
    
    return "\n".join(lines)

def process_corpus(corpus, mode, dry_run):
    corpus_dir = os.path.join(CORPUS_DIR, corpus)
    if not os.path.isdir(corpus_dir):
        print(f"❌ 找不到語料庫: {corpus_dir}")
        return
    
    out_dir = os.path.join(OUTPUT_DIR, corpus)
    os.makedirs(out_dir, exist_ok=True)
    
    meta_files = sorted(glob.glob(os.path.join(corpus_dir, "*-meta.yaml")))
    print(f"\n{'='*60}")
    print(f"📚 {corpus}: {len(meta_files)} 卷")
    print(f"{'='*60}")
    
    total = 0
    created = 0
    skipped = 0
    
    for meta_path in meta_files:
        with open(meta_path, 'r') as f:
            meta = yaml.safe_load(f)
        
        volume_id = os.path.basename(meta_path).replace('-meta.yaml', '')
        meta_title = meta.get('title', 'Unknown')
        chapters = meta.get('chapter_outline', [])
        
        # mode=p0: 只取前 3 章或包含關鍵字的章節
        if mode == 'p0':
            keywords = ['introduction', 'conclusion', 'synthesis', 'problem of',
                        'crisis', 'thought and word', 'socialist alteration',
                        'environment', 'perezhivanie', 'consciousness',
                        'tool and symbol', 'cultural development',
                        'the problem of', 'imagination and creativity',
                        'destruction as the cause', 'key to human',
                        'unpublished', 'архив', 'катарсис']
            chapters = [c for c in chapters if any(k in c.get('title','').lower() for k in keywords)]
            # 至少保留第一章
            if not chapters and meta.get('chapter_outline'):
                chapters = [meta['chapter_outline'][0]]
        
        for ch_idx, ch in enumerate(chapters, 1):
            total += 1
            fname = make_filename(corpus, volume_id, ch_idx, ch['title'])
            fpath = os.path.join(out_dir, fname)
            
            if os.path.exists(fpath):
                skipped += 1
                continue
            
            fm = build_frontmatter(corpus, meta, ch, ch_idx, volume_id)
            content = build_content(fm, ch, meta, ch_idx, meta_title)
            
            if dry_run:
                print(f"  📄 [DRY-RUN] {fname}")
            else:
                with open(fpath, 'w') as f:
                    f.write(content)
                created += 1
                print(f"  ✅ {fname}")
    
    print(f"\n📊 {corpus}: {total} 章節, 新增 {created}, 略過 {skipped}")
    return total, created, skipped

def main():
    args = sys.argv[1:]
    
    # Parse mode
    mode = 'full'
    if '--mode' in args:
        idx = args.index('--mode')
        mode = args[idx+1]
        args = args[:idx] + args[idx+2:]
    
    dry_run = '--dry-run' in args
    if dry_run:
        args.remove('--dry-run')
    
    print(f"🔧 generate-index.py — Phase 1 索引生成")
    print(f"   Mode: {mode}")
    print(f"   Dry-run: {dry_run}")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    corpora = args if args else ['vygotsky', 'psychoanalysis']
    
    grand_total = 0
    for corpus in corpora:
        result = process_corpus(corpus, mode, dry_run)
        if result:
            grand_total += result[0]
    
    print(f"\n{'='*60}")
    print(f"🏁 完成！共處理 {grand_total} 章節")
    if not dry_run:
        print(f"   輸出目錄: {OUTPUT_DIR}/")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
