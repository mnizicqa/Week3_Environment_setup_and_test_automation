class CartPage:
    def __init__(self, page):
        self.page = page
        self.proceed_to_checkout_btn = page.get_by_role("button", name="Proceed to checkout")
        self.register_account_link = page.get_by_role("link", name="Register your account")
        self.user_email_cart = page.locator("#email")
        self.user_password_cart = page.locator("#password")
        self.login_btn_cart = page.locator("[data-test='login-submit']")

    def navigate_to_cart(self):
        self.page.goto("/checkout")

    def click_on_proceed_to_checkout_btn(self):
        self.proceed_to_checkout_btn.click()

    def click_on_register_account_link(self):
        self.register_account_link.click()

    def enter_user_email(self, email):
        self.user_email_cart.fill(email)

    def enter_user_password(self, password):
        self.user_password_cart.fill(password)

    def click_on_login_btn_cart(self):
        self.login_btn_cart.click()