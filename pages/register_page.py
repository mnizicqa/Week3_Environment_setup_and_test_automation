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
    def enter_first_name(self,first_name):
        self.first_name.fill(first_name)
    def enter_last_name(self,last_name):
        self.last_name.fill(last_name)
    def enter_date_of_birth(self,date_of_birth):
        self.date_of_birth.fill(date_of_birth)
    def enter_street(self,street):
        self.street.fill(street)
    def enter_postal_code(self,postal_code):
        self.postal_code.fill(postal_code)
    def enter_city(self,city):
        self.city.fill(city)
    def enter_state(self,state):
        self.state.fill(state)
    def select_country(self,country):
        self.country.select_option(country)
    def enter_phone(self,phone):
        self.phone.fill(phone)
    def enter_email(self,email):
        self.email.fill(email)
    def enter_password(self,password):
        self.password.fill(password)
    def click_on_register_btn(self):
        self.register_btn.click()