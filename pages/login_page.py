class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_email = page.get_by_label("Email address *")
        self.user_password = page.get_by_label("Password *")
        self.login_btn = page.locator("[data-test='login-submit']")

    def login_user(self, email, password):
        self.user_email.fill(email)
        self.user_password.fill(password)

    def click_on_login_btn(self):
        self.login_btn.click()