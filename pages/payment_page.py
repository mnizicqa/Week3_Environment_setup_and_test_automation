class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.payment_method = page.get_by_label("Payment Method")
        self.credit_card_number = page.get_by_label("Credit Card Number")
        self.expiration_date = page.get_by_label("Expiration Date")
        self.cvv = page.get_by_label("CVV")
        self.card_holder_name = page.get_by_label("Card Holder Name")
        self.confirm_btn = page.get_by_role("button", name="Confirm")
        self.username = page.locator("#menu")
        self.my_invoices = page.locator("[data-test='nav-my-invoices']")


    def select_payment_method(self,payment_method):
        self.payment_method.select_option(payment_method)

    def enter_credit_card_number(self,credit_card_number):
        self.credit_card_number.fill(credit_card_number)

    def enter_expiration_date(self,expiration_date):
        self.expiration_date.fill(expiration_date)

    def enter_cvv(self,cvv):
        self.cvv.fill(cvv)

    def enter_card_holder_name(self,card_holder_name):
        self.card_holder_name.fill(card_holder_name)

    def click_on_confirm_btn(self):
        self.confirm_btn.click()

    def click_on_username(self):
        self.username.click()

    def click_on_my_invoices(self):
        self.my_invoices.click()