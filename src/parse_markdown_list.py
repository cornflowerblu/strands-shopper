"""
parse_markdown_list.py

Parses grocery.md into a structured list of items matching the grocery.json schema.
"""
import re
from typing import List, Dict, Any

CATEGORY_HEADERS = {
    "produce": ["produce", "🥬 produce"],
    "meat_seafood": ["proteins", "meat", "seafood", "🥩 proteins"],
    "dairy": ["dairy", "🧀 dairy"],
    "bakery_grains": ["bakery", "grains", "🥖 bakery / grains"],
    "pantry": ["pantry", "🥫 pantry"],
    "snacks_fruit": ["snacks", "fruit", "🍊 snacks / fruit"],
    "dips": ["dips", "🥗 dressing backup"],
}

HEADER_REGEX = re.compile(r"^##?\s*(.+)", re.IGNORECASE)
ITEM_REGEX = re.compile(r"^- \*\*(.+?):\*\*\s*(.+)")


def parse_markdown_list(md_path: str) -> List[Dict[str, Any]]:
    """
    Parse grocery.md and return a list of item dicts matching grocery.json schema.
    Args:
        md_path: Path to grocery.md file
    Returns:
        List of dicts with keys: name, quantity, category, notes (optional)
    """
    items = []
    current_category = None
    with open(md_path, "r") as f:
        for line in f:
            header_match = HEADER_REGEX.match(line.strip())
            if header_match:
                header = header_match.group(1).lower()
                for cat, aliases in CATEGORY_HEADERS.items():
                    if any(alias in header for alias in aliases):
                        current_category = cat
                        break
                continue
            item_match = ITEM_REGEX.match(line.strip())
            if item_match:
                print(f"MATCHED: {line.strip()}")
            else:
                print(f"NOT MATCHED: {line.strip()}")
            if item_match and current_category:
                name = item_match.group(1).strip()
                rest = item_match.group(2).strip()
                # Remove trailing markdown underscores/notes
                notes = None
                # Look for notes in underscores (markdown italics)
                if "_" in rest:
                    rest_parts = rest.split("_", 1)
                    quantity = rest_parts[0].strip()
                    notes = rest_parts[1].replace("_", "").replace("(", "").replace(")", "").strip()
                # Look for notes in parentheses after quantity
                elif "(" in rest:
                    parts = rest.split("(", 1)
                    quantity = parts[0].strip()
                    notes = parts[1].rstrip(")").strip()
                else:
                    quantity = rest
                item = {
                    "name": name,
                    "quantity": quantity,
                    "category": current_category,
                }
                if notes:
                    item["notes"] = notes
                items.append(item)
    print("PARSED ITEMS:", items)
    return items
