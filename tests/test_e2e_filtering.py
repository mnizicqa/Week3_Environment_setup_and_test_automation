import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.user_data import user

@allure.title("E2E Test - Filtering - hammer checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Hammer checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_hammer(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_hammer_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - hand saw checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Hand Saw checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_hand_saw(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_hand_saw_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - wrench checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Wrench checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_wrench(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_wrench_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - screwdriver checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Screwdriver checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_screwdriver(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_screwdriver_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - pliers checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Pliers checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_pliers(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_pliers_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - chisels checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Chisels checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_chisels(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_chisels_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - measures checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Measures checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_hand_tools_measures(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_measures_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - sander checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Sander checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_power_tools_sander(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_sander_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - saw checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Saw checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_power_tools_saw(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_saw_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - drill checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Drill checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_power_tools_drill(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_drill_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - tool belts checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Tool Belts checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_other_tool_belts(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_tool_belts_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - storage solutions checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Storage Solutions checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_other_storage_solutions(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_storage_solutions_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - safety gear checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Safety Gear checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_other_safety_gear(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_safety_gear_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - fasteners checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Fasteners checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_category_other_fasteners(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_fasteners_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - forgeflex tools checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Forgeflex Tools checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_brand_forgeflex_tools(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_forgeflex_tools_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - mightycraft hardware checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Mightycraft Hardware checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_brand_mightycraft_hardware(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_mightycraft_hardware_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)

@allure.title("E2E Test - Filtering - show only eco-friendly products checkbox Demo Application")
@allure.description("This is an end to end test with main focus on filtering feature.")
@allure.tag("E2E")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("https://practicesoftwaretesting.com/")
@allure.suite("E2E")
@allure.feature("Filtering")
@allure.story("Show only eco-friendly products checkbox")
@pytest.mark.e2e_filtering
def test_e2e_filter_by_sustainability(page_manager):

    Tasks.navigate_to_home_page_and_check_logo_banner(page_manager)

    Tasks.check_filters_title_categories_brand_sustainability_visibility(page_manager)

    Tasks.check_show_only_eco_friendly_products_checkbox_and_click_on_product(page_manager)

    Tasks.complete_add_to_cart(page_manager)

    Tasks.proceed_to_cart_login(page_manager)

    Tasks.complete_cart_login(page_manager, user)

    Tasks.check_login_success_and_proceed_to_payment(page_manager)

    Tasks.check_payment_details(page_manager)

    Tasks.complete_payment(page_manager, user)

    Tasks.check_invoice_complete_details(page_manager)