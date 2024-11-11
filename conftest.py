import pytest
from playwright.sync_api import sync_playwright
from pages.basket_page import BasketPage
from pages.product_page import ProductPage

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.goto("https://basket.genotek.ru")
    yield page
    page.close()

@pytest.fixture
def basket_page(page):
    return BasketPage(page)

@pytest.fixture
def product_page(page):
    return ProductPage(page)
