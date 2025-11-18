class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = page.get_by_role("button", name="Add to cart")
        self.add_to_cart_icon = page.locator("[data-test='nav-cart']")

    def click_on_add_to_cart_btn(self):
        self.add_to_cart_btn.click()

    def click_on_add_to_cart_icon(self):
        self.add_to_cart_icon.click()
