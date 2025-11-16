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

    with allure.step("Step 1"):
        homepage.navigate()

    with allure.step("Step 2"):
        homepage.click_on_product_title()

    with allure.step("Step 3"):
        product_page.click_on_add_to_cart_btn()

    with allure.step("Step 4"):
        product_page.click_on_add_to_cart_icon()

    with allure.step("Step 5"):
        cart_page.click_on_proceed_to_checkout_btn()

    with allure.step("Step 6"):
        cart_page.click_on_register_account_link()

    with allure.step("Step 7"):
        register_page.register_user(USERS.user_credentials.first_name, USERS.user_credentials.last_name, USERS.user_credentials.date_of_birth,USERS.user_credentials.street, USERS.user_credentials.postal_code, USERS.user_credentials.city, USERS.user_credentials.state, USERS.user_credentials.country, USERS.user_credentials.phone, USERS.user_credentials.email, USERS.user_credentials.password)

    with allure.step("Step 8"):
        register_page.click_on_register_btn()

    with allure.step("Step 9"):
        login_page.login_user(USERS.user_credentials.email, USERS.user_credentials.password)

    with allure.step("Step 10"):
        login_page.click_on_login_btn()

    with allure.step("Step 11"):
        cart_page.navigate_to_cart()

    with allure.step("Step 12"):
        cart_page.click_on_proceed_to_checkout_btn()

    with allure.step("Step 13"):
        cart_page.login_user_cart(USERS.user_credentials.email, USERS.user_credentials.password)

    with allure.step("Step 14"):
        cart_page.click_on_login_btn_cart()

    with allure.step("Step 15"):
        cart_page.click_on_proceed_to_checkout_btn()

    with allure.step("Step 16"):
        cart_page.click_on_proceed_to_checkout_btn()

    with allure.step("Step 17"):
        payment_page.select_payment_method(USERS.user_credentials.payment_method, USERS.user_credentials.credit_card_number, USERS.user_credentials.expiration_date, USERS.user_credentials.cvv, USERS.user_credentials.card_holder_name)

    with allure.step("Step 18"):
        payment_page.click_on_confirm_btn()

    with allure.step("Step 19"):
        payment_page.click_on_username()

    with allure.step("Step 20"):
        payment_page.click_on_my_invoices()