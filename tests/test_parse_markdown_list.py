import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from parse_markdown_list import parse_markdown_list

def test_parse_markdown_list_basic():
    md_path = os.path.join(os.path.dirname(__file__), "../grocery.md")
    items = parse_markdown_list(md_path)
    assert isinstance(items, list)
    assert any(item["name"].lower() == "english cucumbers" for item in items)
    assert any(item["category"] == "produce" for item in items)
    assert any("quantity" in item for item in items)
    # Check notes extraction
    assert any("notes" in item for item in items if item["name"].lower() == "english cucumbers")

def test_parse_markdown_list_edge_cases():
    md_path = os.path.join(os.path.dirname(__file__), "../grocery.md")
    items = parse_markdown_list(md_path)
    # Should handle optional items and categories
    assert any(item["name"].lower() == "fresh dill" for item in items)
    assert any(item["category"] == "produce" for item in items if item["name"].lower() == "fresh dill")
