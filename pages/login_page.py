class LoginPage:
    def __init__(self, page):
        self.page = page
        self.user_email = page.get_by_label("Email address *")
        self.user_password = page.get_by_label("Password *")
        self.login_btn = page.locator("[data-test='login-submit']")
    def enter_user_email(self, email):
        self.user_email.fill(email)
    def enter_user_password(self, password):
        self.user_password.fill(password)
    def click_on_login_btn(self):
        self.login_btn.click()