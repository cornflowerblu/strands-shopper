"""
md_to_json.py

Converts parsed markdown items to grocery.json schema and writes to file.
"""
import json
from typing import List, Dict, Any
from parse_markdown_list import parse_markdown_list

def md_items_to_json_schema(md_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    # Basic conversion: just map items to the 'items' array
    return {
        "plan_version": "1.0",
        "merchant": "HEB",
        "items": md_items
    }

def write_grocery_json(md_path: str, json_path: str):
    md_items = parse_markdown_list(md_path)
    json_data = md_items_to_json_schema(md_items)
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python src/md_to_json.py <grocery.md> <grocery.json>")
        sys.exit(1)
    write_grocery_json(sys.argv[1], sys.argv[2])
