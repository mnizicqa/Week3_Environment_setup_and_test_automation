from tests.conftest import cart_page
from tests.conftest import homepage
from tests.conftest import product_page
from tests.conftest import register_page
from tests.conftest import login_page
from tests.conftest import payment_page

class Tasks:

    def navigate_to_product_page(homepage):
        homepage.navigate()
        homepage.click_on_product_title()

    def add_product_to_cart(product_page):
        product_page.click_on_add_to_cart_btn()
        product_page.click_on_add_to_cart_icon()

    def navigate_to_registration(cart_page):
        cart_page.click_on_proceed_to_checkout_btn()
        cart_page.click_on_register_account_link()

    def complete_registration(register_page, user):
        register_page.enter_first_name(user.first_name)
        register_page.enter_last_name(user.last_name)
        register_page.enter_date_of_birth(user.date_of_birth)
        register_page.enter_street(user.street)
        register_page.enter_postal_code(user.postal_code)
        register_page.enter_city(user.city)
        register_page.enter_state(user.state)
        register_page.select_country(user.country)
        register_page.enter_phone(user.phone)
        register_page.enter_email(user.email)
        register_page.enter_password(user.password)
        register_page.click_on_register_btn()

    def complete_login(login_page, user):
        login_page.enter_user_email(user.email)
        login_page.enter_user_password(user.password)
        login_page.click_on_login_btn()

    def navigate_to_cart_login(cart_page):
        cart_page.navigate_to_cart()
        cart_page.click_on_proceed_to_checkout_btn()

    def complete_cart_login(cart_page, user):
        cart_page.enter_user_email(user.email)
        cart_page.enter_user_password(user.password)
        cart_page.click_on_login_btn_cart()

    def proceed_to_payment(cart_page):
        cart_page.click_on_proceed_to_checkout_btn()
        cart_page.click_on_proceed_to_checkout_btn()

    def complete_payment(payment_page, user):
        payment_page.select_payment_method(user.payment_method)
        payment_page.enter_credit_card_number(user.credit_card_number)
        payment_page.enter_expiration_date(user.expiration_date)
        payment_page.enter_cvv(user.cvv)
        payment_page.enter_card_holder_name(user.card_holder_name)

    def check_invoice(payment_page):
        payment_page.click_on_username()
        payment_page.click_on_my_invoices()