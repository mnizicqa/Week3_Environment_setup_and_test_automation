import pytest
import allure

from tests.conftest import cart_page
from tests.conftest import homepage
from tests.conftest import product_page
from tests.conftest import register_page
from tests.conftest import login_page
from tests.conftest import payment_page
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

def test_smoke(homepage,product_page,cart_page,register_page,login_page,payment_page):

    Tasks.navigate_to_product_page(homepage)

    Tasks.add_product_to_cart(product_page)

    Tasks.navigate_to_registration(cart_page)

    Tasks.complete_registration(register_page,user)

    Tasks.complete_login(login_page,user)

    Tasks.navigate_to_cart_login(cart_page)

    Tasks.complete_cart_login(cart_page,user)

    Tasks.proceed_to_payment(cart_page)

    Tasks.complete_payment(payment_page,user)

    Tasks.check_invoice(payment_page)