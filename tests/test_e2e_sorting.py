import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.user_data import user

@allure.title("E2E Test - Sorting A to Z Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("Sorting A to Z")
@pytest.mark.e2e_sorting
def test_e2e_sorting_alphabetically(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_name_a_to_z(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager,user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager,user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Sorting Z to A Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("Sorting Z to A")
@pytest.mark.e2e_sorting
def test_e2e_sorting_alphabetically_reverse(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_name_z_to_a(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Price High-Low Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("Price High-Low")
@pytest.mark.e2e_sorting
def test_e2e_sorting_price_high_low(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_price_high_to_low(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Price Low-High Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("Price Low-High")
@pytest.mark.e2e_sorting
def test_e2e_sorting_price_low_high(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_price_low_to_high(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - CO2 A-E Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("CO2 A-E")
@pytest.mark.e2e_sorting
def test_e2e_sorting_co2_a_e(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_co2_a_to_e(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - CO2 E-A Demo Application")
@allure.description("This is an end to end test with main focus on sorting feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Sorting")
@allure.story("CO2 E-A")
@pytest.mark.e2e_sorting
def test_e2e_sorting_co2_e_a(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_sort_title_and_select_visibility(page_manager)

    Tasks.select_and_click_on_product_co2_e_to_a(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)