from tests.conftest import page_manager
class Tasks:
    @staticmethod
    def navigate_to_product_page(page_manager):
       page_manager.home_page.navigate()
       page_manager.home_page.click_on_product_title()
    @staticmethod
    def navigate_to_home_page_and_check_logo_banner(page_manager):
        page_manager.home_page.navigate()
        page_manager.home_page.check_logo_visibility()
        page_manager.home_page.check_banner_visibility()
    @staticmethod
    def check_sort_title_and_select_visibility(page_manager):
        page_manager.home_page.check_sort_title()
        page_manager.home_page.check_sort_select_visibility()
    @staticmethod
    def select_and_click_on_product_name_a_to_z(page_manager):
        page_manager.home_page.select_name_a_to_z()
        page_manager.home_page.click_on_product_name_asc()
    @staticmethod
    def select_and_click_on_product_name_z_to_a(page_manager):
        page_manager.home_page.select_name_z_to_a()
        page_manager.home_page.click_on_product_name_desc()
    @staticmethod
    def select_and_click_on_product_price_high_to_low(page_manager):
        page_manager.home_page.select_price_high_to_low()
        page_manager.home_page.click_on_product_name_high_low()
    @staticmethod
    def select_and_click_on_product_price_low_to_high(page_manager):
        page_manager.home_page.select_price_low_to_high()
        page_manager.home_page.click_on_product_name_low_high()
    @staticmethod
    def select_and_click_on_product_co2_a_to_e(page_manager):
       page_manager.home_page.select_co2_a_to_e()
       page_manager.home_page.click_on_product_name_co2_a_to_e()
    @staticmethod
    def select_and_click_on_product_co2_e_to_a(page_manager):
        page_manager.home_page.select_co2_e_to_a()
        page_manager.home_page.click_on_product_name_co2_e_to_a()
    @staticmethod
    def check_filters_title_categories_brand_sustainability_visibility(page_manager):
        page_manager.home_page.check_filters_title()
        page_manager.home_page.check_categories_title()
        page_manager.home_page.check_brand_title()
        page_manager.home_page.check_sustainability_title()
    @staticmethod
    def check_hammer_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_hammer_checkbox()
        page_manager.home_page.hammer_checkbox_checked()
        page_manager.home_page.click_on_product_name_hammer()
    @staticmethod
    def check_hand_saw_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_hand_saw_checkbox()
        page_manager.home_page.hand_saw_checkbox_checked()
        page_manager.home_page.click_on_product_name_hand_saw()
    @staticmethod
    def check_wrench_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_wrench_checkbox()
        page_manager.home_page.wrench_checkbox_checked()
        page_manager.home_page.click_on_product_name_wrench()
    @staticmethod
    def check_screwdriver_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_screwdriver_checkbox()
        page_manager.home_page.screwdriver_checkbox_checked()
        page_manager.home_page.click_on_product_name_screwdriver()
    @staticmethod
    def check_pliers_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_pliers_checkbox()
        page_manager.home_page.pliers_checkbox_checked()
        page_manager.home_page.click_on_product_name_pliers()
    @staticmethod
    def check_chisels_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_chisels_checkbox()
        page_manager.home_page.chisels_checkbox_checked()
        page_manager.home_page.click_on_product_name_chisels()
    @staticmethod
    def check_measures_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_measures_checkbox()
        page_manager.home_page.measures_checkbox_checked()
        page_manager.home_page.click_on_product_name_measures()
    @staticmethod
    def check_sander_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_sander_checkbox()
        page_manager.home_page.sander_checkbox_checked()
        page_manager.home_page.click_on_product_name_sander()
    @staticmethod
    def check_saw_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_saw_checkbox()
        page_manager.home_page.saw_checkbox_checked()
        page_manager.home_page.click_on_product_name_saw()
    @staticmethod
    def check_drill_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_drill_checkbox()
        page_manager.home_page.drill_checkbox_checked()
        page_manager.home_page.click_on_product_name_drill()
    @staticmethod
    def check_tool_belts_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_tool_belts_checkbox()
        page_manager.home_page.tool_belts_checkbox_checked()
        page_manager.home_page.click_on_product_name_tool_belts()
    @staticmethod
    def check_storage_solutions_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_storage_solutions_checkbox()
        page_manager.home_page.storage_solutions_checkbox_checked()
        page_manager.home_page.click_on_product_name_storage_solutions()
    @staticmethod
    def check_safety_gear_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_safety_gear_checkbox()
        page_manager.home_page.safety_gear_checkbox_checked()
        page_manager.home_page.click_on_product_name_safety_gear()
    @staticmethod
    def check_fasteners_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_fasteners_checkbox()
        page_manager.home_page.fasteners_checkbox_checked()
        page_manager.home_page.click_on_product_name_fasteners()
    @staticmethod
    def check_forgeflex_tools_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_forgeflex_tools_checkbox()
        page_manager.home_page.forgeflex_tools_checkbox_checked()
        page_manager.home_page.click_on_product_name_forgeflex_tools()
    @staticmethod
    def check_mightycraft_hardware_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_mightycraft_hardware_checkbox()
        page_manager.home_page.mightycraft_hardware_checkbox_checked()
        page_manager.home_page.click_on_product_name_mightycraft_hardware()
    @staticmethod
    def check_show_only_eco_friendly_products_checkbox_and_click_on_product(page_manager):
        page_manager.home_page.check_sustainability_checkbox()
        page_manager.home_page.sustainability_checkbox_checked()
        page_manager.home_page.click_on_product_name_show_only_eco_friendly_products()
    @staticmethod
    def complete_add_to_cart(page_manager):
        page_manager.product_page.check_increase_quantity_btn_visibility()
        page_manager.product_page.click_on_increase_quantity_btn()
        page_manager.product_page.check_add_to_cart_btn_visibility()
        page_manager.product_page.click_on_add_to_cart_btn()
        page_manager.product_page.check_success_message_visibility()
        page_manager.product_page.check_add_to_cart_icon_badge_text()
        page_manager.product_page.click_on_add_to_cart_icon()
    @staticmethod
    def add_product_to_cart(page_manager):
        page_manager.product_page.click_on_add_to_cart_btn()
        page_manager.product_page.click_on_add_to_cart_icon()
    @staticmethod
    def proceed_to_cart_login(page_manager):
        page_manager.cart_page.check_cart_url()
        page_manager.cart_page.check_product_details_visibility()
        page_manager.cart_page.check_proceed_to_checkout_btn_visibility()
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
    @staticmethod
    def navigate_to_registration(page_manager):
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
        page_manager.cart_page.click_on_register_account_link()
    @staticmethod
    def complete_registration(page_manager, user):
        page_manager.register_page.enter_first_name(user.first_name)
        page_manager.register_page.enter_last_name(user.last_name)
        page_manager.register_page.enter_date_of_birth(user.date_of_birth)
        page_manager.register_page.enter_street(user.street)
        page_manager.register_page.enter_postal_code(user.postal_code)
        page_manager.register_page.enter_city(user.city)
        page_manager.register_page.enter_state(user.state)
        page_manager.register_page.select_country(user.country)
        page_manager.register_page.enter_phone(user.phone)
        page_manager.register_page.enter_email(user.email)
        page_manager.register_page.enter_password(user.password)
        page_manager.register_page.click_on_register_btn()
    @staticmethod
    def complete_login(page_manager, user):
        page_manager.login_page.enter_user_email(user.email)
        page_manager.login_page.enter_user_password(user.password)
        page_manager.login_page.click_on_login_btn()
    @staticmethod
    def navigate_to_cart_login(page_manager):
        page_manager.cart_page.navigate_to_cart()
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
    @staticmethod
    def complete_cart_login(page_manager, user):
        page_manager.cart_page.enter_user_email(user.email)
        page_manager.cart_page.enter_user_password(user.password)
        page_manager.cart_page.click_on_login_btn_cart()
    @staticmethod
    def proceed_to_payment(page_manager):
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
    @staticmethod
    def check_login_success_and_proceed_to_payment(page_manager):
        page_manager.cart_page.check_login_success_message_visibility()
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
        page_manager.cart_page.check_billing_address_title_visibility()
        page_manager.cart_page.click_on_proceed_to_checkout_btn()
    @staticmethod
    def check_payment_details(page_manager):
        page_manager.payment_page.check_payment_title_visibility()
        page_manager.payment_page.check_confirm_btn_is_disabled()
    @staticmethod
    def complete_payment(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method)
        page_manager.payment_page.enter_credit_card_number(user.credit_card_number)
        page_manager.payment_page.enter_expiration_date(user.expiration_date)
        page_manager.payment_page.enter_cvv(user.cvv)
        page_manager.payment_page.enter_card_holder_name(user.card_holder_name)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_bank_transfer(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_bank)
        page_manager.payment_page.enter_bank_name(user.bank_name)
        page_manager.payment_page.enter_account_name(user.account_name)
        page_manager.payment_page.enter_account_number(user.account_number)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_cash(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_cash)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_buy_now_pay_later_3_monthly_installments(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_buy_now_pay_later)
        page_manager.payment_page.select_monthly_installments(user.monthly_installments_3)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_buy_now_pay_later_6_monthly_installments(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_buy_now_pay_later)
        page_manager.payment_page.select_monthly_installments(user.monthly_installments_6)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_buy_now_pay_later_9_monthly_installments(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_buy_now_pay_later)
        page_manager.payment_page.select_monthly_installments(user.monthly_installments_9)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_buy_now_pay_later_12_monthly_installments(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_buy_now_pay_later)
        page_manager.payment_page.select_monthly_installments(user.monthly_installments_12)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def complete_payment_gift_card(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method_gift)
        page_manager.payment_page.enter_gift_card_number(user.gift_card_number)
        page_manager.payment_page.enter_validation_code(user.validation_code)
        page_manager.payment_page.click_on_confirm_btn()
    @staticmethod
    def check_invoice(page_manager):
        page_manager.payment_page.click_on_username()
        page_manager.payment_page.click_on_my_invoices()
    @staticmethod
    def check_invoice_complete_details(page_manager):
        page_manager.payment_page.check_payment_success_message_visibility()
        page_manager.payment_page.click_on_username()
        page_manager.payment_page.click_on_my_invoices()
        page_manager.payment_page.check_payment_url()
        page_manager.payment_page.check_invoice_title_visibility()
        page_manager.payment_page.check_invoice_number_visibility()
