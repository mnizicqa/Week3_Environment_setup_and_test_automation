import pytest
import allure

from tasks.api_tasks import APITasks
from utilities.user_data import user

@allure.title("Smoke Test API Demo Application")
@allure.description("This is an API smoke test for Demo Web Application, which tests basic API endpoints like select product, add to cart, register, login, payment method selection, invoice validation.")
@allure.tag("Smoke API")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Mario Nizic")
@allure.link("https://api.practicesoftwaretesting.com/")
@allure.suite("Smoke")
@allure.testcase("DWA-271")
@pytest.mark.smoke_api
def test_smoke_api(base_url_api):

    APITasks.check_product_id(base_url_api)

    APITasks.select_product_and_check_responses(base_url_api)

    APITasks.check_cart_id(base_url_api)

    APITasks.add_product_to_cart_and_check_responses(base_url_api)

    APITasks.get_cart_details_and_check_responses(base_url_api)

    APITasks.complete_registration(base_url_api,user)

    APITasks.complete_login(base_url_api,user)

    APITasks.check_user_data(base_url_api,user)

    APITasks.complete_payment(base_url_api,user)

    APITasks.create_invoice(base_url_api,user)

    APITasks.check_invoice(base_url_api,user)