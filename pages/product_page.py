from playwright.sync_api import expect
class ProductPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = page.get_by_role("button", name="Add to cart")
        self.add_to_cart_icon = page.locator("[data-test='nav-cart']")
        self.product_page_title = page.locator("[data-test='product-name']")
        self.increase_quantity_btn = page.locator("#btn-increase-quantity")
        self.success_message = page.locator("#toast-container")
        self.add_to_cart_icon_badge = page.locator("#lblCartCount")
    def check_product_page_title_visibility(self):
        expect(self.product_page_title).to_be_visible()
    def check_increase_quantity_btn_visibility(self):
        expect(self.increase_quantity_btn).to_be_visible()
    def click_on_increase_quantity_btn(self):
        self.increase_quantity_btn.click()
    def check_add_to_cart_btn_visibility(self):
        expect(self.add_to_cart_btn).to_be_visible()
    def click_on_add_to_cart_btn(self):
        self.add_to_cart_btn.click()
    def click_on_add_to_cart_icon(self):
        self.add_to_cart_icon.click()
    def check_success_message_visibility(self):
        expect(self.success_message).to_be_visible()
    def check_add_to_cart_icon_badge_text(self):
        expect(self.add_to_cart_icon_badge).to_have_text("2")