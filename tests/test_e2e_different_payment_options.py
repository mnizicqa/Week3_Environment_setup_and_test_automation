import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.user_data import user

@allure.title("E2E Test - Payment - bank transfer option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Bank Transfer")
@pytest.mark.e2e_payment
def test_payment_method_bank_transfer(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_bank_transfer(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - cash on delivery option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Cash on Delivery")
@pytest.mark.e2e_payment
def test_payment_method_cash_on_delivery(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_cash(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - buy now pay later option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Buy Now Pay Later 3 monthly installments")
@allure.tag("E2E")
@pytest.mark.e2e_payment
def test_payment_method_buy_now_pay_later_3_monthly_installments(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_buy_now_pay_later_3_monthly_installments(page_manager,user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - buy now pay later option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Buy Now Pay Later 6 monthly installments")
@allure.tag("E2E")
@pytest.mark.e2e_payment
def test_payment_method_buy_now_pay_later_6_monthly_installments(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_buy_now_pay_later_6_monthly_installments(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - buy now pay later option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Buy Now Pay Later 9 monthly installments")
@allure.tag("E2E")
@pytest.mark.e2e_payment
def test_payment_method_buy_now_pay_later_9_monthly_installments(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_buy_now_pay_later_9_monthly_installments(page_manager,user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - buy now pay later option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Buy Now Pay Later 12 monthly installments")
@allure.tag("E2E")
@pytest.mark.e2e_payment
def test_payment_method_buy_now_pay_later_12_monthly_installments(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_buy_now_pay_later_12_monthly_installments(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Payment - gift card option Demo Application")
@allure.description("This is an end to end test with main focus on different payment methods feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Payment")
@allure.story("Gift Card")
@allure.tag("E2E")
@pytest.mark.e2e_payment
def test_payment_method_gift_card(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment_gift_card(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)