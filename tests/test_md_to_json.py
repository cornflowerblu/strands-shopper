import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from md_to_json import md_items_to_json_schema
from parse_markdown_list import parse_markdown_list

def test_md_items_to_json_schema_basic():
    md_path = os.path.join(os.path.dirname(__file__), "../grocery.md")
    md_items = parse_markdown_list(md_path)
    json_data = md_items_to_json_schema(md_items)
    assert "items" in json_data
    assert isinstance(json_data["items"], list)
    assert any(item["name"].lower() == "english cucumbers" for item in json_data["items"])
    assert any(item["category"] == "produce" for item in json_data["items"])
    # Check for merchant and plan_version
    assert json_data["merchant"] == "HEB"
    assert json_data["plan_version"] == "1.0"
