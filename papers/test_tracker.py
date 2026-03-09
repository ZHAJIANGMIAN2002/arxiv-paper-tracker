#!/usr/bin/env python3
"""
End-to-end test for arxiv_vln_tracker.
Tests each module independently, then runs a full integration test.
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

PROXY = "http://192.168.100.117:18000"
os.environ.setdefault("http_proxy", PROXY)
os.environ.setdefault("https_proxy", PROXY)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv_vln_tracker as tracker


def test_build_query():
    q = tracker.build_query("vision AND language AND navigation")
    assert "cs.CV" in q
    assert "vision AND language AND navigation" in q
    print("[PASS] test_build_query")


def test_is_vln_relevant_positive():
    entry = {"title": "Vision-and-Language Navigation in Continuous Environments", "summary": "We study VLN agent navigation."}
    assert tracker.is_vln_relevant(entry) is True
    print("[PASS] test_is_vln_relevant_positive")


def test_is_vln_relevant_negative():
    entry = {"title": "Advances in Image Classification", "summary": "We propose a new CNN model for image recognition."}
    assert tracker.is_vln_relevant(entry) is False
    print("[PASS] test_is_vln_relevant_negative")


def test_extract_paper_info():
    mock_entry = {
        "id": "http://arxiv.org/abs/2403.12345v1",
        "title": "Test VLN Paper\n  With Newlines",
        "published": "2024-03-08T00:00:00Z",
        "updated": "2024-03-08T00:00:00Z",
        "authors": [{"name": "Alice"}, {"name": "Bob"}],
        "tags": [{"term": "cs.CV"}, {"term": "cs.CL"}],
        "summary": "This is a test\n  abstract about  VLN.",
        "links": [
            {"href": "http://arxiv.org/abs/2403.12345v1", "type": "text/html"},
            {"href": "http://arxiv.org/pdf/2403.12345v1", "type": "application/pdf"},
        ],
    }
    info = tracker.extract_paper_info(mock_entry)
    assert info["arxiv_id"] == "2403.12345v1"
    assert "Test VLN Paper With Newlines" == info["title"]
    assert info["authors"] == ["Alice", "Bob"]
    assert info["categories"] == ["cs.CV", "cs.CL"]
    assert "test abstract about VLN" in info["abstract"]
    assert "pdf" in info["pdf_link"]
    print("[PASS] test_extract_paper_info")


def test_translate_to_chinese():
    result = tracker.translate_to_chinese("Hello world")
    assert result and len(result) > 0
    assert result != "Hello world"
    print(f"[PASS] test_translate_to_chinese: 'Hello world' -> '{result}'")


def test_format_paper_md():
    paper = {
        "title": "Test Paper",
        "arxiv_id": "2403.00001v1",
        "published": "2024-03-08T00:00:00Z",
        "updated": "2024-03-08T00:00:00Z",
        "authors": ["Alice", "Bob"],
        "affiliations": ["MIT"],
        "categories": ["cs.CV"],
        "abstract": "A test abstract.",
        "pdf_link": "http://arxiv.org/pdf/2403.00001v1",
        "abstract_link": "http://arxiv.org/abs/2403.00001v1",
    }
    md = tracker.format_paper_md(paper, "测试摘要。")
    assert "### Test Paper" in md
    assert "2024-03-08" in md
    assert "Alice" in md
    assert "MIT" in md
    assert "测试摘要" in md
    assert "pdf" in md.lower()
    print("[PASS] test_format_paper_md")


def test_markdown_update():
    """Test that markdown file is correctly created and appended."""
    original_md = tracker.MD_FILE
    original_output = tracker.OUTPUT_DIR

    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)
        tracker.OUTPUT_DIR = tmppath
        tracker.MD_FILE = tmppath / "vln_papers.md"

        try:
            tracker.update_markdown("## Day 1\n\nPaper A\n\n---\n\n")
            assert tracker.MD_FILE.exists()
            content1 = tracker.MD_FILE.read_text(encoding="utf-8")
            assert "Day 1" in content1
            assert "Paper A" in content1

            tracker.update_markdown("## Day 2\n\nPaper B\n\n---\n\n")
            content2 = tracker.MD_FILE.read_text(encoding="utf-8")
            assert "Day 2" in content2
            assert "Day 1" in content2
            assert content2.index("Day 2") < content2.index("Day 1")
            print("[PASS] test_markdown_update (new content prepended correctly)")
        finally:
            tracker.MD_FILE = original_md
            tracker.OUTPUT_DIR = original_output


def test_history_persistence():
    """Test that history file saves and loads correctly."""
    original_history = tracker.HISTORY_FILE
    with tempfile.TemporaryDirectory() as tmpdir:
        tracker.HISTORY_FILE = Path(tmpdir) / "test_history.json"
        try:
            ids = {"2403.00001v1", "2403.00002v1"}
            tracker.save_history(ids)
            loaded = tracker.load_history()
            assert loaded == ids
            print("[PASS] test_history_persistence")
        finally:
            tracker.HISTORY_FILE = original_history


def test_fetch_papers_live():
    """Live test: actually query arxiv API (one query only)."""
    entries = tracker.fetch_papers_for_query("vision-and-language navigation", max_results=5)
    assert isinstance(entries, list)
    print(f"[PASS] test_fetch_papers_live: got {len(entries)} entries from arxiv")
    if entries:
        info = tracker.extract_paper_info(entries[0])
        print(f"       First paper: {info['title'][:80]}...")
        return entries
    return []


def test_integration():
    """Full integration: fetch, filter, translate, write markdown."""
    original_md = tracker.MD_FILE
    original_output = tracker.OUTPUT_DIR
    original_history = tracker.HISTORY_FILE

    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)
        tracker.OUTPUT_DIR = tmppath
        tracker.MD_FILE = tmppath / "vln_papers.md"
        tracker.HISTORY_FILE = tmppath / "history.json"
        tracker.LOG_FILE = tmppath / "test.log"

        try:
            count = tracker.run(force=True)
            assert tracker.MD_FILE.exists(), "Markdown file should be created"
            content = tracker.MD_FILE.read_text(encoding="utf-8")
            assert "VLN" in content or "论文追踪" in content
            print(f"[PASS] test_integration: {count} papers written")
            print(f"       Output file size: {len(content)} chars")
            preview = content[:500]
            print(f"       Preview:\n{preview}")
        finally:
            tracker.MD_FILE = original_md
            tracker.OUTPUT_DIR = original_output
            tracker.HISTORY_FILE = original_history


def main():
    print("=" * 60)
    print("Running VLN Paper Tracker Tests")
    print("=" * 60)

    test_build_query()
    test_is_vln_relevant_positive()
    test_is_vln_relevant_negative()
    test_extract_paper_info()
    test_format_paper_md()
    test_history_persistence()
    test_markdown_update()

    print("\n--- Live API Tests ---")
    test_translate_to_chinese()
    test_fetch_papers_live()

    print("\n--- Integration Test ---")
    test_integration()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    main()
