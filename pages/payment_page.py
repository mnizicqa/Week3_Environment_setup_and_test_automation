import re
from playwright.sync_api import expect
class PaymentPage:
    def __init__(self, page):
        self.page = page
        self.payment_method = page.get_by_label("Payment Method")
        self.bank_name = page.get_by_label("Bank Name")
        self.account_name = page.get_by_label("Account Name")
        self.account_number = page.get_by_label("Account Number")
        self.credit_card_number = page.get_by_label("Credit Card Number")
        self.expiration_date = page.get_by_label("Expiration Date")
        self.cvv = page.get_by_label("CVV")
        self.card_holder_name = page.get_by_label("Card Holder Name")
        self.monthly_installments = page.get_by_label("Monthly Installments")
        self.gift_card_number = page.get_by_label("Gift Card Number")
        self.validation_code = page.get_by_label("Validation Code")
        self.confirm_btn = page.get_by_role("button", name="Confirm")
        self.username = page.locator("#menu")
        self.my_invoices = page.locator("[data-test='nav-my-invoices']")
        self.payment_title = page.get_by_role("heading", name="Payment")
        self.payment_success_message = page.locator("[data-test='payment-success-message']")
        self.invoice_title = page.get_by_role("heading", name="Invoices")
        self.invoice_number = page.locator("(//th[normalize-space()='Invoice Number'])[1]")
    def check_payment_title_visibility(self):
        expect(self.payment_title).to_be_visible()
    def check_confirm_btn_is_disabled(self):
        expect(self.confirm_btn).to_be_disabled()
    def select_payment_method(self,payment_method):
        self.payment_method.select_option(payment_method)
    def enter_bank_name(self,bank_name):
        self.bank_name.fill(bank_name)
    def enter_account_name(self,account_name):
        self.account_name.fill(account_name)
    def enter_account_number(self,account_number):
        self.account_number.fill(account_number)
    def enter_credit_card_number(self,credit_card_number):
        self.credit_card_number.fill(credit_card_number)
    def enter_expiration_date(self,expiration_date):
        self.expiration_date.fill(expiration_date)
    def enter_cvv(self,cvv):
        self.cvv.fill(cvv)
    def enter_card_holder_name(self,card_holder_name):
        self.card_holder_name.fill(card_holder_name)
    def select_monthly_installments(self,monthly_installments):
        self.monthly_installments.select_option(monthly_installments)
    def enter_gift_card_number(self,gift_card_number):
        self.gift_card_number.fill(gift_card_number)
    def enter_validation_code(self,validation_code):
        self.validation_code.fill(validation_code)
    def click_on_confirm_btn(self):
        self.confirm_btn.click()
    def check_payment_success_message_visibility(self):
        expect(self.payment_success_message).to_be_visible()
    def click_on_username(self):
        self.username.click()
    def click_on_my_invoices(self):
        self.my_invoices.click()
    def check_payment_url(self):
        expect(self.page).to_have_url(re.compile(".invoices"))
    def check_invoice_title_visibility(self):
        expect(self.invoice_title).to_be_visible()
    def check_invoice_number_visibility(self):
        expect(self.invoice_number).to_be_visible()