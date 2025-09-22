"""
select_store.py

Automates HEB.com store selection flow using Playwright.
"""
from playwright.sync_api import Page

def select_store(page: Page, zip_code: str = "78610") -> str:
    """
    Automate HEB.com store selection.
    Args:
        page: Playwright Page object
        zip_code: ZIP code for store search (default: 78610)
    Returns:
        Store name or ID selected
    """
    # Go to HEB homepage
    page.goto("https://www.heb.com/")
    # Wait for nav to load and check current store
    nav_button = page.wait_for_selector("button:has-text('Slaughter and Manchaca H-E-B')", timeout=10000)
    if nav_button:
        # Already at correct store, take no action
        return "Slaughter and Manchaca H-E-B"
    # Otherwise, find the store button in nav (any button with 'H-E-B' in text)
    store_nav_btn = page.wait_for_selector("button:has-text('H-E-B')", timeout=10000)
    if store_nav_btn:
        store_nav_btn.click()
        page.wait_for_selector("input[type='text']", timeout=10000)
        page.fill("input[type='text']", zip_code)
        # Find and click the search/submit button (assume first button after input)
        submit_btn = page.query_selector("input[type='text'] ~ button")
        if submit_btn:
            submit_btn.click()
        else:
            # Fallback: click any button with 'Search' or 'Find'
            alt_btn = page.query_selector("button:has-text('Search')") or page.query_selector("button:has-text('Find')")
            if alt_btn:
                alt_btn.click()
        page.wait_for_selector(".store-list-item", timeout=10000)
        stores = page.query_selector_all(".store-list-item")
        if not stores:
            raise Exception(f"No stores found for ZIP code: {zip_code}")
        # Select first store
        store_name_elem = stores[0].query_selector(".store-name")
        if store_name_elem:
            store_name = store_name_elem.inner_text()
        else:
            store_name = "Unknown Store"
        stores[0].click()
        page.wait_for_load_state("networkidle")
        return store_name
    raise Exception("Could not find store selection button in nav.")
