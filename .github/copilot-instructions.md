# Strands Shopper Agent Instructions

## Project Overview
This is a grocery shopping automation agent built with the Strands framework. The agent is designed to automate HEB.com grocery shopping by ingesting structured shopping lists, navigating the website, and adding items to cart for human review.

## Core Architecture

### Data-Driven Design
The project follows a structured, JSON-driven approach to grocery shopping automation:
- **`grocery.json`**: Complete shopping specification with item queries, substitution policies, and fulfillment preferences
- **`grocery.md`**: Human-readable grocery list that mirrors the JSON structure
- **`agent.py`**: Strands Agent implementation (currently basic template)

### Key Components
1. **Shopping List Schema**: Detailed JSON structure with categories, quantities, substitution rules, and preferences
2. **Substitution Policy**: Configurable rules for handling out-of-stock items and price variations
3. **Human Checkpoints**: Built-in approval gates for critical decisions (steaks, seafood, price deltas >15%)

## Development Patterns

### Strands Framework Integration
- Uses `strands-agents==1.9.1` for AI automation capabilities
- Model configuration: `anthropic.claude-3-5-sonnet-20240620-v1:0`
- Virtual environment setup in `.venv/` (activate before development)

### Browser Automation Architecture
- **Playwright**: Full browser automation (no APIs available for HEB.com)
- **Visual debugging**: Agent actions should be observable during development
- **Test automation**: Playwright tests for key shopping workflows
- **Headless vs headed**: Use headed mode for development/debugging, headless for production

### Key Automation Tools (Research-Identified)
Core functions for HEB shopping automation:
- **`parse_markdown_list`**: Convert grocery.md format to actionable items
- **`search_products`**: Find products on HEB.com using item queries
- **`select_store`**: Handle store selection flow with ZIP fallback
- **`add_to_cart`**: Add found products to shopping cart with quantity/size matching

### Configuration Structure
When working with `grocery.json`:
- **Categories**: `produce`, `meat_seafood`, `dairy`, `bakery_grains`, `pantry`, `snacks_fruit`, `dips`
- **Required fields**: `name`, `query`, `target_size`, `quantity`
- **Optional features**: `acceptable_subs`, `require_confirm`, `optional` flag
- **Substitution controls**: Brand subs allowed, size variations within 25%, price delta confirmations at 15%

### Domain-Specific Logic
- **Butcher exclusion**: Agent must not purchase fresh meat from butcher counter (requirement #4)
- **Store selection**: Must ask user to select HEB location first
- **Cart review**: Final state is items in cart awaiting human approval, not automatic checkout

## Workflow Commands

### Environment Setup
```bash
source .venv/bin/activate  # Always activate before development
pip install playwright      # Browser automation framework
playwright install         # Install browser binaries
```

### Running the Agent
```bash
python agent.py  # Current basic implementation (to be expanded)
```

### Testing & Development
```bash
# Run with visible browser for debugging
playwright codegen heb.com  # Generate automation code interactively

# Run tests (when implemented)
pytest tests/              # Automated shopping workflow tests
```

## Critical Patterns

### Shopping List Item Structure
```json
{
  "name": "English cucumbers",
  "query": "english cucumber",
  "target_size": "each",
  "quantity": 3,
  "acceptable_subs": ["hot house cucumber"],
  "require_confirm": false
}
```

### Substitution Decision Tree
1. Check `acceptable_subs` array first
2. Calculate price delta percentage
3. If >15% delta or `require_confirm: true`, prompt user
4. For meat/seafood, always confirm quality and cut preferences

### File Relationships
- `grocery.md` ↔ `grocery.json`: Keep synchronized when updating shopping lists
- `requirements.md`: Contains business logic and constraints
- `agent.py`: Implementation entry point (needs expansion for HEB automation)

## Next Development Steps
The current `agent.py` is a basic template. Key areas for implementation:
1. **Playwright integration**: Browser automation for HEB.com navigation
2. **Core tool functions**: Implement `parse_markdown_list`, `search_products`, `select_store`, `add_to_cart`
3. **Store selection flow**: Interactive store picker with ZIP fallback
4. **Product search & cart**: DOM manipulation for adding items to cart
5. **Substitution logic**: Decision trees with user confirmation prompts
6. **Visual testing**: Playwright tests for critical shopping workflows
7. **Error handling**: Graceful failures for out-of-stock, site changes, timeouts