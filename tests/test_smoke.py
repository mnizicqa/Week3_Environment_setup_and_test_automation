import pytest
import allure

from utilities.user_data import USERS

@allure.title("Smoke Test Demo Application")
@allure.description("This is a smoke test for Demo Web Application, which tests basic features like add to cart, register, login, payment method selection, invoice validation.")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("Smoke")
@allure.testcase("DWA-250")
@pytest.mark.smoke
def test_smoke(homepage, product_page, cart_page, register_page, login_page, payment_page):

        homepage.navigate()

        homepage.click_on_product_title()

        product_page.click_on_add_to_cart_btn()

        product_page.click_on_add_to_cart_icon()

        cart_page.click_on_proceed_to_checkout_btn()

        cart_page.click_on_register_account_link()

        register_page.enter_first_name(USERS.user_credentials.first_name)

        register_page.enter_last_name(USERS.user_credentials.last_name)

        register_page.enter_date_of_birth(USERS.user_credentials.date_of_birth)

        register_page.enter_street(USERS.user_credentials.street)

        register_page.enter_postal_code(USERS.user_credentials.postal_code)

        register_page.enter_city(USERS.user_credentials.city)

        register_page.enter_state(USERS.user_credentials.state)

        register_page.select_country(USERS.user_credentials.country)

        register_page.enter_phone(USERS.user_credentials.phone)

        register_page.enter_email(USERS.user_credentials.email)

        register_page.enter_password(USERS.user_credentials.password)

        register_page.click_on_register_btn()

        login_page.login_user(USERS.user_credentials.email, USERS.user_credentials.password)

        login_page.click_on_login_btn()

        cart_page.navigate_to_cart()

        cart_page.click_on_proceed_to_checkout_btn()

        cart_page.enter_user_email(USERS.user_credentials.email)

        cart_page.enter_user_password(USERS.user_credentials.password)

        cart_page.click_on_login_btn_cart()

        cart_page.click_on_proceed_to_checkout_btn()

        cart_page.click_on_proceed_to_checkout_btn()

        payment_page.select_payment_method(USERS.user_credentials.payment_method, USERS.user_credentials.credit_card_number, USERS.user_credentials.expiration_date, USERS.user_credentials.cvv, USERS.user_credentials.card_holder_name)

        payment_page.click_on_confirm_btn()

        payment_page.click_on_username()

        payment_page.click_on_my_invoices()