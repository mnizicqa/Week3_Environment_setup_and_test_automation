import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.user_data import user

@allure.title("Smoke Test Demo Application")
@allure.description("This is a smoke test for Demo Web Application, which tests basic features like add to cart, register, login, payment method selection, invoice validation.")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("Smoke")
@allure.testcase("DWA-250")
@pytest.mark.smoke

def test_smoke(page_manager):

    Tasks.navigate_to_product_page(page_manager)

    Tasks.add_product_to_cart(page_manager)

    Tasks.navigate_to_registration(page_manager)

    Tasks.complete_registration(page_manager,user)

    Tasks.complete_login(page_manager,user)

    Tasks.navigate_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager,user)

    Tasks.proceed_to_payment(page_manager)

    Tasks.complete_payment(page_manager,user)

    Tasks.check_invoice(page_manager)