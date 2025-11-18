from playwright.sync_api import Page

def navigate_to_product_page(page: Page):
    page.goto("/")
    page.get_by_role("heading", name="Thor Hammer").click()

def add_product_to_cart(page: Page):
    page.get_by_role("button", name="Add to cart").click()
    page.locator("[data-test='nav-cart']").click()

def navigate_to_registration(page: Page):
    page.get_by_role("button", name="Proceed to checkout").click()
    page.get_by_role("link", name="Register your account").click()

def complete_registration(page:Page, first_name, last_name, date_of_birth, street, postal_code, city, state, country, phone, email, password):
    page.get_by_label("First name").fill(first_name)
    page.get_by_label("Last name").fill(last_name)
    page.get_by_label("Date of birth").fill(date_of_birth)
    page.get_by_label("Street").fill(street)
    page.get_by_label("Postal code").fill(postal_code)
    page.get_by_label("City").fill(city)
    page.get_by_label("State").fill(state)
    page.get_by_label("Country").select_option(country)
    page.get_by_label("Phone").fill(phone)
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Register").click()

def complete_login(page:Page, email, password):
    page.get_by_label("Email address *").fill(email)
    page.get_by_label("Password *").fill(password)
    page.locator("[data-test='login-submit']").click()

def navigate_to_cart_login(page: Page):
    page.goto("/checkout")
    page.get_by_role("button", name="Proceed to checkout").click()

def complete_cart_login(page: Page, email, password):
    page.locator("#email").fill(email)
    page.locator("#password").fill(password)
    page.locator("[data-test='login-submit']").click()

def proceed_to_payment(page: Page):
    page.get_by_role("button", name="Proceed to checkout").click()
    page.get_by_role("button", name="Proceed to checkout").click()

def complete_payment(page: Page, payment_method, credit_card_number, expiration_date, cvv, credit_card_holder_name):
    page.get_by_label("Payment Method").select_option(payment_method)
    page.get_by_label("Credit Card Number").fill(credit_card_number)
    page.get_by_label("Expiration Date").fill(expiration_date)
    page.get_by_label("CVV").fill(cvv)
    page.get_by_label("Card Holder Name").fill(credit_card_holder_name)
    page.get_by_role("button", name="Confirm").click()

def check_invoice(page: Page):
    page.locator("#menu").click()
    page.locator("[data-test='nav-my-invoices']").click()