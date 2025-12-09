import pytest
from playwright.sync_api import Page
from pages.page_manager import PageManager


@pytest.fixture(scope="session")
def base_url():
    return "https://practicesoftwaretesting.com/"

@pytest.fixture(scope="session")
def base_url_api():
    return "https://api.practicesoftwaretesting.com"

@pytest.fixture
def page_manager(page:Page, base_url:str) -> PageManager:
    page.goto(base_url)
    return PageManager(page)