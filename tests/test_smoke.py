import pytest
import allure
from playwright.sync_api import Page

from tasks.ui_tasks import navigate_to_product_page, add_product_to_cart, navigate_to_registration, \
    complete_registration, complete_login, navigate_to_cart_login, complete_cart_login, proceed_to_payment, \
    complete_payment, check_invoice
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
def test_smoke(page: Page):

    navigate_to_product_page(page)

    add_product_to_cart(page)

    navigate_to_registration(page)

    complete_registration(page,USERS.user_credentials.first_name,USERS.user_credentials.last_name,USERS.user_credentials.date_of_birth,USERS.user_credentials.street, USERS.user_credentials.postal_code, USERS.user_credentials.city, USERS.user_credentials.state, USERS.user_credentials.country, USERS.user_credentials.phone, USERS.user_credentials.email , USERS.user_credentials.password)

    complete_login(page,USERS.user_credentials.email,USERS.user_credentials.password)

    navigate_to_cart_login(page)

    complete_cart_login(page, USERS.user_credentials.email, USERS.user_credentials.password)

    proceed_to_payment(page)

    complete_payment(page, USERS.user_credentials.payment_method, USERS.user_credentials.credit_card_number, USERS.user_credentials.expiration_date, USERS.user_credentials.cvv, USERS.user_credentials.card_holder_name)

    check_invoice(page)