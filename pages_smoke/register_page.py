class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.get_by_label("First name")
        self.last_name = page.get_by_label("Last name")
        self.date_of_birth = page.get_by_label("Date of Birth")
        self.street = page.get_by_label("Street")
        self.postal_code = page.get_by_label("Postal Code")
        self.city = page.get_by_label("City")
        self.state = page.get_by_label("State")
        self.country = page.get_by_label("Country")
        self.phone = page.get_by_label("Phone")
        self.email = page.get_by_label("Email address")
        self.password = page.get_by_label("Password")
        self.register_btn = page.get_by_role("button", name="Register")

    def register_user(self,first_name,last_name,date_of_birth,street,postal_code,city,state,country,phone,email,password):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.date_of_birth.fill(date_of_birth)
        self.street.fill(street)
        self.postal_code.fill(postal_code)
        self.city.fill(city)
        self.state.fill(state)
        self.country.select_option(country)
        self.phone.fill(phone)
        self.email.fill(email)
        self.password.fill(password)

    def click_on_register_btn(self):
        self.register_btn.click()