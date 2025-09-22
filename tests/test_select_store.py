import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from select_store import select_store
import pytest
from playwright.sync_api import sync_playwright


def test_select_store_basic():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        store_name = select_store(page, zip_code="78701")
        assert isinstance(store_name, str)
        assert len(store_name) > 0
        browser.close()
