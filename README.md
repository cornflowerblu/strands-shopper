# Strands Shopper

Grocery shopping automation agent for HEB.com using Playwright and the Strands framework.

## Overview
Strands Shopper is designed to automate the process of building a grocery cart on HEB.com. It ingests structured shopping lists, navigates the HEB website, and adds items to your cart for human review. The agent is built for full browser automation (no APIs available) and is highly configurable for substitutions, store selection, and human approval checkpoints.

## Features
- Ingests shopping lists from `grocery.json` (structured) and `grocery.md` (human-readable)
- Automates browser actions using Playwright (headed for dev, headless for prod)
- Selects HEB store location interactively, with ZIP fallback
- Searches for products, matches sizes/quantities, and adds to cart
- Handles substitutions and price delta confirmations
- Human checkpoints for critical decisions (meat, seafood, price changes)
- Outputs cart summary, price report, and out-of-stock items

## Project Structure
```
├── agent.py                # Strands agent entry point
├── grocery.json            # Structured shopping list and config
├── grocery.md              # Human-readable grocery list
├── requirements.md         # Business logic and constraints
├── src/
│   └── logging.py          # Logging configuration
├── tests/                  # Playwright and pytest tests
├── playwright.config.js    # Playwright browser config
├── .env                    # Environment variables (browser mode)
├── tasks.md                # Implementation roadmap
└── .github/
    └── copilot-instructions.md # AI agent instructions
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/cornflowerblu/strands-shopper.git
   cd strands-shopper
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If requirements.txt exists
   pip install playwright pytest
   playwright install
   ```
4. Configure environment variables in `.env`:
   - Set `PLAYWRIGHT_HEADLESS=1` for headless mode (production)
   - Leave unset for headed mode (development)

## Usage
- Run the agent:
  ```bash
  python agent.py
  ```
- Develop and debug browser automation:
  ```bash
  playwright codegen heb.com
  ```
- Run tests:
  ```bash
  pytest tests/
  ```

## Key Automation Tools
- `parse_markdown_list`: Convert grocery.md to actionable items
- `search_products`: Find products on HEB.com
- `select_store`: Store selection flow with ZIP fallback
- `add_to_cart`: Add products to cart with quantity/size matching

## Substitution & Decision Logic
- Brand substitutions allowed
- Size variations within 25%
- Price delta confirmations at 15%
- Always ask for: steaks, salmon, shrimp, feta block, Greek dressing
- Never purchase fresh meat from butcher counter

## Development Roadmap
See [`tasks.md`](tasks.md) for a detailed breakdown of implementation steps and priorities.

## Contributing
Pull requests and issues are welcome! Please see [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for AI agent guidelines and project conventions.

## License
MIT
