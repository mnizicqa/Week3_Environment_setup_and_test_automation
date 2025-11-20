from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage

class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.cart_page = CartPage(page)
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)
        self.payment_page = PaymentPage(page)
        self.product_page = ProductPage(page)
        self.register_page = RegisterPage(page)