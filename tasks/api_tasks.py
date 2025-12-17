import requests
from test_data.common_data import BASE_URL
header_content_type = "application/json;charset=UTF-8"
params = "page=1"
time_seconds = 1
cart_id = None
class APITasks:
    @staticmethod
    def check_product_id():
        response = requests.get(f"{BASE_URL}/products")
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/products Response: {response_body}")
        product_id = response_body["data"][8]["id"]
        print(f"{BASE_URL}/products Request completed successfully!")
        return product_id
    def select_product_and_check_responses(self):
        product_id = self.check_product_id()
        print(f"{BASE_URL}/products Product ID: {product_id}")
        response = requests.get(f"{BASE_URL}/products/{product_id}")
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/products/{product_id} Response:{response_body}")
        product_name = response_body.get("name")
        assert response_body.get("id") == product_id
        assert response_body.get("name") == product_name
        print(f"{BASE_URL}/products/{product_id} Product name:{product_name}")
        print(f"{BASE_URL}/products/{product_id} Request completed successfully!")
    @staticmethod
    def check_cart_id():
        response = requests.post(f"{BASE_URL}/carts")
        assert response.status_code == 201
        assert response.reason == "Created"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/carts Response: {response_body}")
        global cart_id
        cart_id = response_body.get("id")
        assert response_body.get("id") == cart_id
        print(f"{BASE_URL}/carts Cart ID: {cart_id}")
        print(f"{BASE_URL}/carts Request completed successfully!")
    def add_product_to_cart_and_check_responses(self):
        product_id = self.check_product_id()
        print(f"{BASE_URL}/products Product ID:{product_id}")
        product_payload = {"product_id":product_id,"quantity":1}
        print(f"Product payload: {product_payload}")
        response = requests.post(f"{BASE_URL}/carts/{cart_id}", json=product_payload)
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json().get("result")
        print(f"{BASE_URL}/carts/{cart_id} Response:{response_body}")
        print(f"{BASE_URL}/carts/{cart_id} Request completed successfully!")
    def get_cart_details_and_check_responses(self):
        product_id = self.check_product_id()
        print(f"{BASE_URL}/products Product ID: {product_id}")
        response = requests.get(f"{BASE_URL}/carts/{cart_id}")
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"Cart item details: {response_body}")
        cart_item_id = response_body.get("id")
        cart_item_product_id = response_body["cart_items"][0]["product_id"]
        cart_item_quantity = response_body["cart_items"][0]["quantity"]
        assert response_body.get("id") == cart_item_id
        assert cart_item_product_id == product_id
        assert cart_item_quantity == 1
        print(f"{BASE_URL}/carts/{cart_id} Cart item product id:{cart_item_product_id}")
        print(f"{BASE_URL}/carts/{cart_id} Cart item quantity:{cart_item_quantity}")
        print(f"{BASE_URL}/carts/{cart_id} Request completed successfully!")
    @staticmethod
    def complete_registration(user):
        register_payload = {"first_name": user.first_name, "last_name": user.last_name,
                            "dob": user.date_of_birth, "phone": user.phone,
                            "email": user.email, "password": user.password,
                            "address": {"street": user.street, "city": user.city, "state": user.state,
                            "country": user.country, "postal_code": user.postal_code}}
        print(f"Register payload: {register_payload}")
        response = requests.post(f"{BASE_URL}/users/register", json=register_payload)
        assert response.status_code == 201
        assert response.reason == "Created"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/users/register User data info:{response_body}")
        print(f"{BASE_URL}/users/register Request completed successfully!")
    @staticmethod
    def complete_login(user):
        login_payload = {"email": user.email, "password": user.password}
        print(f"Login payload: {login_payload}")
        response = requests.post(f"{BASE_URL}/users/login", json=login_payload)
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        print(f" {BASE_URL}/users/login Response:{response.json()}")
        token = response.json().get("access_token")
        print(f"{BASE_URL}/users/login Request completed successfully!")
        return token
    def check_user_data(self,user):
        token = self.complete_login(user)
        print(f"{BASE_URL}/users/login User Token: {token}")
        response = requests.get(f"{BASE_URL}/users/me", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == "application/json"
        response_body = response.json()
        print(f"{BASE_URL}/users/me User data info: {response_body}")
        first_name = response_body.get("first_name")
        last_name = response_body.get("last_name")
        email = response_body.get("email")
        address = response_body.get("address")
        assert first_name == user.first_name
        assert last_name == user.last_name
        assert email == user.email
        print(f"{BASE_URL}/users/me First name:{first_name}, Last name:{last_name}, Email:{email}, Address:{address}")
        print(f"{BASE_URL}/users/me Request completed successfully!")
    @staticmethod
    def complete_payment(user):
        payment_payload = {"payment_method": user.payment_method,
                           "payment_details": {"credit_card_number": user.credit_card_number,
                            "expiration_date": user.expiration_date, "cvv": user.cvv,
                            "card_holder_name": user.card_holder_name}}
        print(f"Payment payload: {payment_payload}")
        response = requests.post(f"{BASE_URL}/payment/check", json= payment_payload)
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json().get("message")
        print(f"{BASE_URL}/payment/check Message:{response_body}")
        print(f"{BASE_URL}/payment/check Request completed successfully!")
    def create_invoice(self,user):
        token = self.complete_login(user)
        invoices_payload =  {"billing_street": user.street, "billing_city": user.city, "billing_state": user.state,
                             "billing_country": user.country, "billing_postal_code": user.postal_code,
                             "payment_method": user.payment_method,
                             "payment_details": {"credit_card_number": user.credit_card_number, "expiration_date": user.expiration_date,
                                                "cvv": user.cvv,"card_holder_name": user.card_holder_name}, "cart_id": cart_id}
        print(f"Invoice payload: {invoices_payload}")
        response = requests.post(f"{BASE_URL}/invoices", json=invoices_payload, headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 201
        assert response.reason == "Created"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/invoices Invoice details:{response_body}")
        print(f"{BASE_URL}/invoices Request completed successfully!")
    def check_invoice(self,user):
        token = self.complete_login(user)
        response = requests.get(f"{BASE_URL}/invoices", params=params, headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.reason == "OK"
        assert response.elapsed.total_seconds() < time_seconds
        assert response.headers["Content-Type"] == header_content_type
        response_body = response.json()
        print(f"{BASE_URL}/invoices Invoice details:{response_body}")
        assert response_body["data"][0]["billing_street"] == user.street
        assert response_body["data"][0]["billing_city"] == user.city
        assert response_body["data"][0]["billing_state"] == user.state
        assert response_body["data"][0]["billing_country"] == user.country
        assert response_body["data"][0]["billing_postal_code"] == user.postal_code
        invoice_id = response_body["data"][0]["id"]
        invoice_number = response_body["data"][0]["invoice_number"]
        print(f"{BASE_URL}/invoices Invoice id:{invoice_id}, Invoice number:{invoice_number}")
        print(f"{BASE_URL}/invoices Request completed successfully!")