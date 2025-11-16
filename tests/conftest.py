import pytest
from playwright.sync_api import Page

from pages_smoke.cart_page import CartPage
from pages_smoke.home_page import HomePage
from pages_smoke.login_page import LoginPage
from pages_smoke.payment_page import PaymentPage
from pages_smoke.product_page import ProductPage
from pages_smoke.register_page import RegisterPage

@pytest.fixture(scope="session")
def base_url():
    return "https://practicesoftwaretesting.com/"

@pytest.fixture
def page(page:Page) -> Page:
    return page

@pytest.fixture
def homepage(page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def product_page(page) -> ProductPage:
    return ProductPage(page)

@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)

@pytest.fixture
def register_page(page) -> RegisterPage:
    return RegisterPage(page)

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def payment_page(page) -> PaymentPage:
    return PaymentPage(page)