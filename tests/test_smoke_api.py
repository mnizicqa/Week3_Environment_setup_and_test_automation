import pytest
import allure

from tasks.api_tasks import APITasks
from utilities.user_data import user

class TestSmokeApi(APITasks):
    @allure.title("Smoke Test API Demo Application")
    @allure.description("This is an API smoke test for Demo Web Application, which tests basic API endpoints like select product, add to cart, register, login, payment method selection, invoice validation.")
    @allure.tag("Smoke API")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label("owner", "Mario Nizic")
    @allure.link("https://api.practicesoftwaretesting.com/")
    @allure.suite("Smoke")
    @allure.testcase("DWA-271")
    @pytest.mark.smoke_api
    def test_smoke_api(self):

        self.check_product_id()

        self.select_product_and_check_responses()

        self.check_cart_id()

        self.add_product_to_cart_and_check_responses()

        self.get_cart_details_and_check_responses()

        self.complete_registration(user)

        self.complete_login(user)

        self.check_user_data(user)

        self.complete_payment(user)

        self.create_invoice(user)

        self.check_invoice(user)

        print("Test completed successfully!")