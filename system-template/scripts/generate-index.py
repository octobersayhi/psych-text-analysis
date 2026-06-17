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
    concepts = meta.get('key_concepts', [])[:8]
    title = ch.get('title', '')
    year = extract_year(meta.get('period', ''))
    
    fm = {
        "id": make_id(corpus, volume_id, title),
        "title": title,
        "author": meta.get('author', AUTHOR_MAP.get(corpus, 'Unknown')),
        "year": year,
        "corpus": corpus,
        "doc_type": infer_doc_type(title, meta.get('title', '')),
        "status": "indexed",
        "source_volume": volume_id,
        "concepts": concepts,
        "key_figures": meta.get('key_figures', [])[:5],
        "theoretical_position": "unknown",
        "dimension_tags": infer_dimension_tags(title, concepts),
        "genetic_level": infer_genetic_level(title, concepts, year),
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

# ── dimension_tags 推論規則 ──────────────────────────
DIMENSION_RULES = [
    (['D1'], ['double stimulation', 'dual stimulation', 'mediation by sign',
              'instrumental act', 'instrumental method', 'sign mediation',
              'orudie', 'znak', 'tool and symbol', 'tool and sign',
              'practical intellect', 'higher mental function']),
    (['D2'], ['scientific concept', 'everyday concept', 'spontaneous concept',
              'abstraction', 'concept formation', 'понятие', 'pseudo-concept',
              'thinking in concepts', 'complex thinking', 'academic concept']),
    (['D3'], ['voluntary memory', 'logical memory', 'mnemotechnics', 'mnemonic',
              'memory and its development', 'memory development']),
    (['D4'], ['catharsis', 'artistic emotion', 'dvoistvennost', 'psychology of art',
              'fable', 'short story', 'tragedy', 'hamlet', 'aesthetic',
              'imagination and creativity', 'art as technique', 'art as a social',
              'поэтика', 'искусство']),
    (['D5'], ['inner speech', 'egocentric speech', 'semantic system', 'word meaning',
              'sense vs meaning', 'subtext', 'znachenie', 'smysl', 'thought and word',
              'thinking and speech', 'verbal thinking', 'язык', 'речь',
              'внутренняя речь']),
    (['D6'], ['zone of proximal development', 'zpd', 'scaffolding', 'imitation',
              'development and learning', 'обучение', 'развитие']),
    (['D7'], ['defectology', 'compensation', 'overcompensation', 'disability',
              'deaf', 'blind', 'special education', 'abnormal', 'defect',
              'дефект', 'дефектология']),
    (['D8'], ['age period', 'crisis', 'transitional age', 'adolescence', 'infancy',
              'early childhood', 'school age', 'pedology', 'pedologic',
              'age', 'child psychology', 'child development',
              'возраст', 'кризис', 'подросток']),
    (['D9'], ['perezhivanie', 'affect', 'emotion', 'will', 'volition',
              'voluntary attention', 'spinoza', 'James-Lange', 'cannon',
              'чувство', 'аффект', 'переживание']),
    (['D10'],['cultural-historical method', 'dialectics', 'genetic principle',
              'marxist psychology', 'crisis in psychology', 'behaviourism',
              'reflexology', 'reductionism', 'methodology', 'epistemology',
              'исторический', 'диалектика', 'кризис']),
]

def infer_dimension_tags(title, concepts):
    """根據標題和概念推論 D1–D10 維度。"""
    text = (title + ' ' + ' '.join(concepts)).lower()
    tags = []
    for dims, keywords in DIMENSION_RULES:
        for kw in keywords:
            if kw in text:
                tags.append(dims[0])
                break
    # 最多 3 個維度
    return sorted(set(tags))[:3]

# ── genetic_level 推論規則 ─────────────────────────────
GENETIC_LEVEL_KEYWORDS = {
    'microgenesis': ['microgenesis', 'experimental', 'laboratory', 'reaction',
                     'reflex', 'seconds', 'minutes', 'процесс'],
    'ontogenesis': ['ontogenesis', 'ontogenetic', 'development of', 'child',
                    'adolescent', 'infancy', 'age', 'childhood', 'стадии',
                    'возраст', 'ребенок', 'детский', 'развитие'],
    'phylogenesis': ['phylogenesis', 'phylogenetic', 'evolution', 'animal',
                     'ape', 'primitive', 'human history', 'культурный',
                     'цивилизация', 'история'],
    'sociogenesis': ['sociogenesis', 'social', 'collective', 'society',
                     'culture', 'institution', 'revolution', 'bolshevik',
                     'fascism', 'социальный', 'общество', 'культура'],
}

def infer_genetic_level(title, concepts, year):
    """根據標題、概念、年份推論發生學層級。"""
    text = (title + ' ' + ' '.join(concepts)).lower()
    candidates = []
    for level, keywords in GENETIC_LEVEL_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                candidates.append(level)
                break
    # 優先級: ontogenesis > sociogenesis > phylogenesis > microgenesis
    priority = {'ontogenesis': 1, 'sociogenesis': 2, 'phylogenesis': 3, 'microgenesis': 4}
    if candidates:
        return min(candidates, key=lambda x: priority.get(x, 9))
    # 多數 Vygotsky 文本預設為 ontogenesis
    return 'ontogenesis'

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
    lines.append("- `dimension_tags` 由腳本自動推論，建議人工驗證")
    lines.append("- `genetic_level` 由腳本自動推論，建議人工驗證")
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
