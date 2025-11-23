import re
from playwright.sync_api import expect

class CartPage:
    def __init__(self, page):
        self.page = page
        self.proceed_to_checkout_btn = page.get_by_role("button", name="Proceed to checkout")
        self.register_account_link = page.get_by_role("link", name="Register your account")
        self.user_email_cart = page.locator("#email")
        self.user_password_cart = page.locator("#password")
        self.login_btn_cart = page.locator("[data-test='login-submit']")
        self.product_details = page.locator(".table-hover")
        self.login_title = page.locator("#login_title")
        self.billing_address_title = page.get_by_role("heading", name="Billing Address")
        self.login_success_message = page.locator("p.ng-star-inserted")

    def check_cart_url(self):
       expect(self.page).to_have_url(re.compile(".*checkout.*"))

    def navigate_to_cart(self):
        self.page.goto("/checkout")

    def check_product_details_visibility(self):
        expect(self.product_details).to_be_visible()

    def check_proceed_to_checkout_btn_visibility(self):
        expect(self.proceed_to_checkout_btn).to_be_visible()

    def click_on_proceed_to_checkout_btn(self):
        self.proceed_to_checkout_btn.click()

    def check_login_title_visibility(self):
        expect(self.login_title).to_be_visible()

    def click_on_register_account_link(self):
        self.register_account_link.click()

    def enter_user_email(self, email):
        self.user_email_cart.fill(email)

    def enter_user_password(self, password):
        self.user_password_cart.fill(password)

    def click_on_login_btn_cart(self):
        self.login_btn_cart.click()

    def check_billing_address_title_visibility(self):
        expect(self.billing_address_title).to_be_visible()

    def check_login_success_message_visibility(self):
        expect(self.login_success_message).to_be_visible()