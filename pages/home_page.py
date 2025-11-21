class HomePage:
    def __init__(self, page):
        self.page = page
        self.product_title = page.get_by_role("heading", name="Thor Hammer")

    def navigate(self):
        self.page.goto("/")

    def click_on_product_title(self):
        self.product_title.click()