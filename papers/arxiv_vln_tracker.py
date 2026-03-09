#!/usr/bin/env python3
"""
Arxiv Paper Tracker (VLN + 3D Segmentation)
自动抓取 Arxiv 最新论文，翻译摘要为中文，生成/更新 Markdown 报告。
支持多方向：--topic vln（视觉语言导航）或 --topic seg3d（3D 语义/实例分割）。
"""

import os
import re
import json
import time
import logging
import argparse
import feedparser
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from deep_translator import GoogleTranslator

PROXY = "http://192.168.100.117:18000"
os.environ.setdefault("http_proxy", PROXY)
os.environ.setdefault("https_proxy", PROXY)

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"
LOG_FILE = OUTPUT_DIR / "tracker.log"

VLN_QUERIES = [
    "vision AND language AND navigation",
    "vision-and-language navigation",
    "embodied navigation",
    "VLN",
    "visual language navigation",
    "instruction following navigation",
]

SEG3D_QUERIES = [
    "3D semantic segmentation",
    "3D instance segmentation",
    "point cloud segmentation",
    "point cloud semantic segmentation",
    "point cloud instance segmentation",
    "scene segmentation 3D",
    "indoor semantic segmentation",
    "ScanNet",
    "S3DIS",
    "Semantic3D",
    "3D scene understanding",
    "point cloud understanding",
]

ARXIV_API = "https://export.arxiv.org/api/query"
MAX_RESULTS_PER_QUERY = 30
TRANSLATE_CHUNK_SIZE = 4500
ARXIV_HTML_DELAY = 0.8

# 各方向配置：输出 md、历史 id 文件、标题
TOPIC_CONFIG = {
    "vln": {
        "md_file": OUTPUT_DIR / "vln_papers.md",
        "history_file": OUTPUT_DIR / "fetched_ids.json",
        "title": "VLN (Vision-and-Language Navigation) 论文追踪",
        "subtitle": "自动从 Arxiv 抓取最新 VLN 相关论文，每日更新",
    },
    "seg3d": {
        "md_file": OUTPUT_DIR / "seg3d_papers.md",
        "history_file": OUTPUT_DIR / "fetched_ids_seg3d.json",
        "title": "3D 语义/实例分割 论文追踪",
        "subtitle": "自动从 Arxiv 抓取 3D Semantic/Instance Segmentation 相关论文，每日更新",
    },
}


def get_queries(topic: str):
    if topic == "seg3d":
        return SEG3D_QUERIES
    return VLN_QUERIES


def is_relevant(entry, topic: str) -> bool:
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
    if topic == "vln":
        strong = [
            "vision-and-language navigation", "vision and language navigation",
            "visual language navigation", "vln", "embodied navigation",
            "instruction following navigation", "room-to-room",
            "r2r", "rxr", "reverie", "soon", "touchdown",
            "embodied agent", "navigate", "navigation instruction",
        ]
        weak = ["navigation", "embodied", "instruction", "grounding", "visual", "language", "indoor", "3d environment"]
        if any(k in text for k in strong):
            return True
        return sum(1 for k in weak if k in text) >= 3
    if topic == "seg3d":
        strong = [
            "3d semantic segmentation", "3d instance segmentation",
            "point cloud segmentation", "point cloud semantic", "point cloud instance",
            "scannet", "s3dis", "semantic3d", "scene segmentation",
            "3d scene understanding", "point cloud understanding",
        ]
        weak = ["semantic segmentation", "instance segmentation", "point cloud", "3d", "segmentation", "indoor", "scene"]
        if any(k in text for k in strong):
            return True
        return sum(1 for k in weak if k in text) >= 3
    return False


def setup_logging():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def load_history(topic: str = "vln") -> set:
    path = TOPIC_CONFIG[topic]["history_file"]
    if path.exists():
        with open(path, "r") as f:
            return set(json.load(f))
    return set()


def save_history(ids: set, topic: str = "vln"):
    path = TOPIC_CONFIG[topic]["history_file"]
    with open(path, "w") as f:
        json.dump(sorted(ids), f, indent=2)


def build_query(search_terms: str, days_back: int = 3) -> str:
    """Build arxiv API query for recent papers."""
    cat_filter = "(cat:cs.CV OR cat:cs.CL OR cat:cs.AI OR cat:cs.RO OR cat:cs.LG)"
    return f"({search_terms}) AND {cat_filter}"


def fetch_papers_for_query(query: str, max_results: int = MAX_RESULTS_PER_QUERY) -> list:
    """Fetch papers from arxiv API for a single query string."""
    params = {
        "search_query": build_query(query),
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    try:
        resp = requests.get(ARXIV_API, params=params, timeout=60)
        resp.raise_for_status()
        feed = feedparser.parse(resp.text)
        return feed.entries
    except Exception as e:
        logging.error(f"Failed to fetch for query '{query}': {e}")
        return []


def _normalize_affiliation(s: str) -> str:
    """统一空白、去掉首尾数字/标点，便于去重。"""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^\d+[.)\s]+", "", s)
    return s.strip()


def _is_plausible_affiliation(s: str) -> bool:
    """判断是否像机构描述：含机构关键词、长度合理、不含明显噪音。"""
    if len(s) < 12 or len(s) > 500:
        return False
    if re.search(r"@|https?://|\.(com|org|edu)\b", s):
        return False
    keywords = (
        "university", "department", "institute", "school", "laboratory", "lab ",
        "college", "faculty", "division", "center", "centre", "research", "academy",
    )
    return any(kw in s.lower() for kw in keywords)


def fetch_affiliations_from_arxiv_html(arxiv_id: str) -> list:
    """从 arxiv 论文 HTML 页解析作者单位，多模式匹配以提高鲁棒性。"""
    aid = (arxiv_id or "").strip()
    if not aid:
        return []
    url = f"https://arxiv.org/html/{aid}"
    try:
        resp = requests.get(url, timeout=20)
        if resp.status_code != 200:
            return []
        html = resp.text
        text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"\s+", " ", text)
        text = " " + text
        # 前段多为标题+作者+单位，用于后续 fallback 时减少误匹配
        text_head = text[: 4000] if len(text) > 4000 else text

        out = []
        seen = set()

        # 模式 1: "NThe authors are with ..." / "The author is with ..."（句末到下一邮箱或下一编号）
        p1 = r"\d*(The\s+authors?\s+(?:are|is)\s+with\s+[^.]*(?:\.[^.]*)*?\.)\s*(?=\s*[a-zA-Z0-9_.+-]+@|\d+The\s+authors?|$)"
        for m in re.findall(p1, text, re.IGNORECASE):
            s = _normalize_affiliation(m)
            if len(s) > 10 and s not in seen:
                seen.add(s)
                out.append(s)

        # 模式 2: 编号列表 "1. Department of ..." "1) University of ..." "1 Department of ..."
        if not out:
            p2 = r"(?:^|\s)(\d+[.)]\s*)((?:Department|University|Institute|School|College|Faculty|Division|Center|Centre|Laboratory|Lab|Research)\s+[^.]*(?:\.[^.]*)*?\.)\s*(?=\d+[.)]|\s*[a-zA-Z0-9_.+-]+@|$)"
            for _, g2 in re.findall(p2, text_head, re.IGNORECASE):
                s = _normalize_affiliation(g2)
                if _is_plausible_affiliation(s) and s not in seen:
                    seen.add(s)
                    out.append(s)

        # 模式 3: "Affiliation(s):" / "Author(s) affiliation:" 后的若干句
        if not out:
            p3 = r"(?:Affiliation|Affiliations|Author[s]?\s*affiliation)\s*:?\s*([^.]+(?:\.[^.]*)*?\.(?:\s*[^.]+\.)*)"
            m3 = re.search(p3, text_head, re.IGNORECASE)
            if m3:
                block = m3.group(1)
                for part in re.split(r"\d+[.)]\s*", block):
                    s = _normalize_affiliation(part)
                    if _is_plausible_affiliation(s) and s not in seen:
                        seen.add(s)
                        out.append(s)

        # 模式 4: 含机构关键词的句子（仅在前段取，降低误杀）
        if not out:
            sentences = re.split(r"(?<=[.!])\s+", text_head)
            for sent in sentences:
                s = _normalize_affiliation(sent)
                if _is_plausible_affiliation(s) and s not in seen:
                    seen.add(s)
                    out.append(s)

        return out
    except Exception as e:
        logging.debug(f"arxiv HTML {arxiv_id}: {e}")
        return []


def extract_paper_info(entry) -> dict:
    """Extract structured info from an arxiv feed entry."""
    arxiv_id = entry.get("id", "").split("/abs/")[-1]
    published = entry.get("published", "")
    updated = entry.get("updated", "")

    authors = []
    for a in entry.get("authors", []):
        name = a.get("name", "")
        if name:
            authors.append(name)

    affiliations = []
    raw_affil = entry.get("arxiv_affiliation", [])
    if isinstance(raw_affil, str):
        affiliations = [raw_affil] if raw_affil else []
    elif isinstance(raw_affil, list):
        for a in raw_affil:
            if isinstance(a, str):
                affiliations.append(a)
            elif isinstance(a, dict):
                affiliations.append(a.get("name", ""))
    for a in entry.get("authors", []):
        affil = a.get("arxiv:affiliation", {})
        if isinstance(affil, dict) and affil.get("$", ""):
            affiliations.append(affil["$"])
        elif isinstance(affil, list):
            for af in affil:
                if isinstance(af, dict) and af.get("$", ""):
                    affiliations.append(af["$"])
    affiliations = list(dict.fromkeys(affiliations))

    categories = [t.get("term", "") for t in entry.get("tags", [])]

    pdf_link = ""
    for link in entry.get("links", []):
        if link.get("type") == "application/pdf":
            pdf_link = link.get("href", "")
            break

    abstract_link = entry.get("id", "")

    return {
        "arxiv_id": arxiv_id,
        "title": re.sub(r"\s+", " ", entry.get("title", "")).strip(),
        "authors": authors,
        "affiliations": affiliations,
        "categories": categories,
        "published": published,
        "updated": updated,
        "abstract": re.sub(r"\s+", " ", entry.get("summary", "")).strip(),
        "pdf_link": pdf_link,
        "abstract_link": abstract_link,
    }


def translate_to_chinese(text: str) -> str:
    """Translate English text to Chinese using Google Translate with retry."""
    if not text:
        return ""

    def _split_sentences(t: str, max_len: int) -> list:
        """Split text into sentence-boundary chunks within max_len."""
        sentences = re.split(r'(?<=[.!?])\s+', t)
        chunks, current = [], ""
        for s in sentences:
            if len(current) + len(s) + 1 > max_len and current:
                chunks.append(current.strip())
                current = s
            else:
                current = current + " " + s if current else s
        if current:
            chunks.append(current.strip())
        return chunks if chunks else [t[:max_len]]

    translator = GoogleTranslator(source="en", target="zh-CN")
    max_retries = 2

    for attempt in range(max_retries + 1):
        try:
            chunks = _split_sentences(text, TRANSLATE_CHUNK_SIZE)
            translated_parts = []
            for chunk in chunks:
                result = translator.translate(chunk)
                if result and "No translation" not in str(result):
                    translated_parts.append(result)
                else:
                    translated_parts.append(chunk)
                time.sleep(0.5)
            full = "".join(translated_parts)
            if full and "No translation" not in full:
                return full
        except Exception as e:
            logging.warning(f"Translation attempt {attempt+1} failed: {e}")
            time.sleep(1)

    logging.warning(f"All translation attempts failed, returning original")
    return f"[翻译失败] {text}"


def fetch_all_papers(history: set, topic: str) -> list:
    """按 topic 抓取论文：多查询去重 + 相关性过滤。"""
    queries = get_queries(topic)
    all_entries = {}
    for q in queries:
        logging.info(f"Querying arxiv: {q}")
        entries = fetch_papers_for_query(q)
        for entry in entries:
            arxiv_id = entry.get("id", "").split("/abs/")[-1]
            if arxiv_id and arxiv_id not in all_entries:
                all_entries[arxiv_id] = entry
        time.sleep(3)

    logging.info(f"Total unique entries fetched: {len(all_entries)}")

    papers = []
    for arxiv_id, entry in all_entries.items():
        if arxiv_id in history:
            continue
        if not is_relevant(entry, topic):
            continue
        info = extract_paper_info(entry)
        papers.append(info)

    papers.sort(key=lambda p: p["published"], reverse=True)
    logging.info(f"New {topic}-relevant papers after filtering: {len(papers)}")

    for i, paper in enumerate(papers):
        affils = fetch_affiliations_from_arxiv_html(paper["arxiv_id"])
        if affils:
            paper["affiliations"] = affils
            logging.info(f"  单位 [{i+1}/{len(papers)}]: {paper['arxiv_id']} -> {len(affils)} 条")
        time.sleep(ARXIV_HTML_DELAY)

    return papers


def format_paper_md(paper: dict, abstract_cn: str) -> str:
    """Format a single paper as a markdown section."""
    lines = []
    lines.append(f"### {paper['title']}")
    lines.append("")

    pub_date = paper["published"][:10] if paper["published"] else "N/A"
    lines.append(f"- **发布日期**: {pub_date}")

    if paper["authors"]:
        author_str = ", ".join(paper["authors"][:10])
        if len(paper["authors"]) > 10:
            author_str += f" et al. (共{len(paper['authors'])}位作者)"
        lines.append(f"- **作者**: {author_str}")

    affil_str = "；".join(paper["affiliations"]) if paper.get("affiliations") else "（暂无）"
    lines.append(f"- **单位**: {affil_str}")

    if paper["categories"]:
        lines.append(f"- **分类**: {', '.join(paper['categories'][:5])}")

    lines.append(f"- **Arxiv**: [{paper['arxiv_id']}]({paper['abstract_link']})")

    if paper["pdf_link"]:
        lines.append(f"- **PDF**: [下载链接]({paper['pdf_link']})")

    lines.append("")
    lines.append("**Abstract (English):**")
    lines.append("")
    lines.append(f"> {paper['abstract']}")
    lines.append("")
    lines.append("**摘要 (中文翻译):**")
    lines.append("")
    lines.append(f"> {abstract_cn}")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def generate_daily_section(papers: list) -> str:
    """Generate markdown for today's batch of papers."""
    today = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append(f"## {today} 更新 (共 {len(papers)} 篇新论文)")
    lines.append("")

    for i, paper in enumerate(papers):
        logging.info(f"  Translating [{i+1}/{len(papers)}]: {paper['title'][:60]}...")
        abstract_cn = translate_to_chinese(paper["abstract"])
        lines.append(format_paper_md(paper, abstract_cn))

    return "\n".join(lines)


def update_markdown(new_section: str, topic: str = "vln"):
    """按 topic 写入对应 md 文件，新内容插在标题后。"""
    cfg = TOPIC_CONFIG[topic]
    md_file = cfg["md_file"]
    header = (
        f"# {cfg['title']}\n\n"
        f"> {cfg['subtitle']}\n"
        "> \n"
        f"> 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        "---\n\n"
    )

    existing_content = ""
    if md_file.exists():
        with open(md_file, "r", encoding="utf-8") as f:
            full = f.read()
        marker = "---\n\n"
        idx = full.find(marker)
        if idx != -1:
            existing_content = full[idx + len(marker):]

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(header + new_section + "\n" + existing_content)

    logging.info(f"Markdown updated: {md_file}")


def run(dry_run: bool = False, force: bool = False, topic: str = "vln"):
    """主流程：按 topic 抓取、翻译、写 md。"""
    if topic not in TOPIC_CONFIG:
        raise ValueError(f"Unknown topic: {topic}. Use one of {list(TOPIC_CONFIG)}")
    setup_logging()
    logging.info("=" * 60)
    logging.info(f"Paper Tracker started [topic={topic}]")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    history = load_history(topic)
    logging.info(f"Previously fetched papers: {len(history)}")

    papers = fetch_all_papers(history, topic)

    if not papers:
        logging.info("No new papers found. Exiting.")
        if force:
            today = datetime.now().strftime("%Y-%m-%d")
            update_markdown(f"## {today} 更新 (共 0 篇新论文)\n\n今日未发现新论文。\n\n---\n\n", topic)
        return 0

    if dry_run:
        logging.info("Dry run mode. Papers found:")
        for p in papers:
            logging.info(f"  - {p['title']} ({p['published'][:10]})")
        return len(papers)

    section = generate_daily_section(papers)
    update_markdown(section, topic)

    new_ids = {p["arxiv_id"] for p in papers}
    history.update(new_ids)
    save_history(history, topic)

    logging.info(f"Done! {len(papers)} new papers added.")
    return len(papers)


def main():
    parser = argparse.ArgumentParser(description="Arxiv Paper Tracker (VLN / 3D Segmentation)")
    parser.add_argument("--topic", choices=list(TOPIC_CONFIG), default="vln", help="vln 或 seg3d")
    parser.add_argument("--dry-run", action="store_true", help="Only fetch and display, don't write")
    parser.add_argument("--force", action="store_true", help="Write markdown even if no new papers")
    parser.add_argument("--all", action="store_true", help="Run both vln and seg3d in one go")
    args = parser.parse_args()
    if args.all:
        n1 = run(dry_run=args.dry_run, force=args.force, topic="vln")
        n2 = run(dry_run=args.dry_run, force=args.force, topic="seg3d")
        print(f"vln: {n1}, seg3d: {n2}")
    else:
        run(dry_run=args.dry_run, force=args.force, topic=args.topic)


if __name__ == "__main__":
    main()
