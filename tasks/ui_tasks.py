from tests.conftest import page_manager

class Tasks:

    @staticmethod
    def navigate_to_product_page(page_manager):
       page_manager.home_page.navigate()
       page_manager.home_page.click_on_product_title()

    @staticmethod
    def add_product_to_cart(page_manager):
        page_manager.product_page.click_on_add_to_cart_btn()
        page_manager.product_page.click_on_add_to_cart_icon()

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
    def complete_payment(page_manager, user):
        page_manager.payment_page.select_payment_method(user.payment_method)
        page_manager.payment_page.enter_credit_card_number(user.credit_card_number)
        page_manager.payment_page.enter_expiration_date(user.expiration_date)
        page_manager.payment_page.enter_cvv(user.cvv)
        page_manager.payment_page.enter_card_holder_name(user.card_holder_name)

    @staticmethod
    def check_invoice(page_manager):
        page_manager.payment_page.click_on_username()
        page_manager.payment_page.click_on_my_invoices()