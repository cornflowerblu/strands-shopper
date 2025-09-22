# Strands Shopper Development Tasks

## 1. Project Setup & Dependencies

### 1.1 Environment Configuration
[x] Install Playwright in virtual environment
[x] Install browser binaries for Chrome/Chromium
[x] Add Playwright to project dependencies
[x] Configure pytest for test framework
[x] Set up development vs production browser modes

### 1.2 Project Structure
- Create `tests/` directory for Playwright tests
- Create `src/` directory for core automation modules
- Set up basic logging configuration
- Create `.env` template for environment variables

## 2. Core Tool Implementation

### 2.1 parse_markdown_list Function
- Parse `grocery.md` into structured item list
- Extract quantities, sizes, and optional flags
- Map to `grocery.json` schema format
- Handle category groupings (produce, meat_seafood, etc.)
- Validate required fields (name, query, target_size, quantity)

### 2.2 select_store Function
- Navigate to HEB.com store selection page
- Handle ZIP code input (default: 78701)
- Present store options to user for selection
- Store selected location in session/config
- Handle store selection errors gracefully

### 2.3 search_products Function
- Use item `query` field to search HEB product catalog
- Parse search results and product listings
- Extract product details (name, size, price, availability)
- Match products against `target_size` preferences
- Return structured product data for cart decisions

### 2.4 add_to_cart Function
- Add selected products to HEB shopping cart
- Respect `quantity` specifications from grocery list
- Handle size/quantity variations within acceptable ranges
- Verify cart additions were successful
- Track added items for final review

## 3. Substitution Logic & Decision Making

### 3.1 Substitution Policy Engine
- Implement `acceptable_subs` matching logic
- Calculate price delta percentages against thresholds
- Check `require_confirm` flags for human approval
- Handle brand substitution preferences
- Size variation tolerance (25% default from config)

### 3.2 Human Confirmation Flows
- Prompt for steaks, salmon, shrimp quality decisions
- Price delta confirmations (>15% threshold)
- Out-of-stock substitution approvals
- Cart review before final submission
- Optional item skip confirmations

### 3.3 Error Handling & Fallbacks
- Product not found scenarios
- Store selection failures
- Cart addition errors
- Network timeout handling
- HEB website structure changes

## 4. Strands Agent Integration

### 4.1 Agent Architecture
- Replace basic template in `agent.py`
- Configure Claude 3.5 Sonnet model integration
- Set up system prompts for grocery shopping context
- Implement tool calling for core functions
- Add conversation memory for shopping session

### 4.2 Workflow Orchestration
- Sequential execution: store → search → decide → cart
- State management across shopping session
- Error recovery and retry logic
- Progress tracking and user feedback
- Final cart review and approval gate

## 5. Browser Automation & Testing

### 5.1 Playwright Implementation
- Set up browser context and page management
- Implement DOM selectors for HEB.com elements
- Handle dynamic content loading and wait strategies
- Configure headed vs headless browser modes
- Add screenshot capabilities for debugging

### 5.2 Test Automation
- Write integration tests for store selection flow
- Test product search across different categories
- Verify cart addition functionality
- Test substitution decision workflows
- Mock HEB responses for consistent testing

### 5.3 Visual Debugging
- Enable browser visibility during development
- Add step-by-step action logging
- Screenshot capture at key decision points
- Interactive debugging mode for troubleshooting
- Performance monitoring for page load times

## 6. Data Processing & Validation

### 6.1 Schema Validation
- Validate `grocery.json` against expected structure
- Check required fields and data types
- Verify category mappings are complete
- Validate substitution policies are consistent
- Cross-reference with `grocery.md` content

### 6.2 Output Generation
- Generate CSV line items for final cart
- Create price summary and totals
- Produce out-of-stock report
- Link each item to HEB product page
- Format substitution decisions made

## 7. Production Readiness

### 7.1 Configuration Management
- Environment-specific settings (dev/prod)
- HEB store preferences and defaults
- User notification preferences
- Timeout and retry configurations
- Browser automation settings

### 7.2 Error Monitoring & Logging
- Comprehensive error logging
- Failed automation recovery strategies
- User notification for critical failures
- Performance metrics collection
- Shopping session audit trails

### 7.3 Documentation & Deployment
- Update README with usage instructions
- Document configuration options
- Create troubleshooting guide
- Set up CI/CD for testing automation
- Deployment scripts for production use