from playwright.sync_api import Page

def navigate_to(page: Page, url: str, timeout: int = 10_000) -> None:
    page.goto(url, timeout=timeout, wait_until="networkidle")

def click_when_visible(page: Page, selector: str, timeout: int = 10_000) -> None:
    page.wait_for_selector(selector, state="visible", timeout=timeout)
    page.click(selector, timeout=timeout)

def type_input(page: Page, selector: str, value: str, timeout: int = 10_000) -> None:
    page.wait_for_selector(selector, state="visible", timeout=timeout)
    page.fill(selector, value)

def select_option(page: Page, selector: str, value: str, timeout: int = 10_000) -> None:
    page.wait_for_selector(selector, state="visible", timeout=timeout)
    page.select_option(selector, value)

def complete_registration(page:Page, first_name_selector:str, last_name_selector:str, date_of_birth_selector:str, street_selector:str, postal_code_selector:str, city_selector:str, state_selector:str, country_selector:str, phone_selector:str, email_selector:str, password_selector:str, first_name:str, last_name:str, date_of_birth:str, street:str, postal_code:str, city:str, state:str, country:str, phone:str, email:str, password:str):
    type_input(page, first_name_selector, first_name)
    type_input(page, last_name_selector, last_name)
    type_input(page, date_of_birth_selector, date_of_birth)
    type_input(page, street_selector, street)
    type_input(page, postal_code_selector, postal_code)
    type_input(page, city_selector, city)
    type_input(page, state_selector, state)
    select_option(page, country_selector, country)
    type_input(page, phone_selector, phone)
    type_input(page, email_selector, email)
    type_input(page, password_selector, password)

def complete_login(page:Page, email_selector:str, password_selector:str, email:str, password:str):
    type_input(page, email_selector, email)
    type_input(page, password_selector, password)

def select_payment_method(page:Page, payment_method_selector:str, credit_card_number_selector:str, expiration_date_selector:str, cvv_selector:str, card_holder_name_selector:str, payment_method:str, credit_card_number:str, expiration_date:str, cvv:str, card_holder_name:str):
    select_option(page, payment_method_selector, payment_method)
    type_input(page, credit_card_number_selector, credit_card_number)
    type_input(page, expiration_date_selector, expiration_date)
    type_input(page, cvv_selector, cvv)
    type_input(page, card_holder_name_selector, card_holder_name)