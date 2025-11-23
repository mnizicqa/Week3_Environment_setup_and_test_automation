from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.product_title = page.get_by_role("heading", name="Claw Hammer with Shock Reduction Grip")
        self.logo = page.locator(".navbar-brand")
        self.banner = page.locator(".img-fluid")
        self.sort_title = page.get_by_role("heading", name="Sort")
        self.sort_select = page.locator("[data-test='sort']")
        self.product_name_asc = page.get_by_role("heading", name="Belt Sander")
        self.product_name_desc = page.get_by_role("heading", name="Wood Carving Chisels")
        self.product_name_high_low = page.locator("//h5[normalize-space()='Tool Cabinet']")
        self.product_name_low_high = page.locator("//h5[normalize-space()='Screws']")
        self.product_name_a_to_e = page.locator("//h5[normalize-space()='Safety Goggles']")
        self.product_name_e_to_a = page.locator("//h5[normalize-space()='Cordless Drill 24V']")
        self.filters_title = page.get_by_role("heading", name="Filters")
        self.categories_title = page.get_by_role("heading", name="By category")
        self.brand_title = page.get_by_role("heading", name="By brand")
        self.sustainability_title = page.get_by_role("heading", name="Sustainability")
        self.hammer_checkbox = page.get_by_label("Hammer")
        self.hand_saw_checkbox = page.get_by_label("Hand Saw")
        self.wrench_checkbox = page.get_by_label("Wrench")
        self.screwdriver_checkbox = page.get_by_label("Screwdriver")
        self.pliers_checkbox = page.get_by_label("Pliers")
        self.chisels_checkbox = page.get_by_label("Chisels")
        self.measures_checkbox = page.get_by_label("Measures")
        self.sander_checkbox = page.get_by_label("Sander")
        self.saw_checkbox = page.locator("//label[normalize-space()='Saw']")
        self.drill_checkbox = page.get_by_label("Drill")
        self.tool_belts_checkbox = page.get_by_label("Tool Belts")
        self.safety_gear_checkbox = page.get_by_label("Safety Gear")
        self.storage_solutions_checkbox = page.get_by_label("Storage Solutions")
        self.fasteners_checkbox = page.get_by_label("Fasteners")
        self.forgeflex_tools_checkbox = page.get_by_label("Forgeflex Tools")
        self.mightycraft_hardware_checkbox = page.get_by_label("MightyCraft Hardware")
        self.show_only_eco_friendly_products_checkbox = page.get_by_label("Show only eco-friendly products")
        self.product_name_hammer = page.locator("//h5[normalize-space()='Claw Hammer']")
        self.product_name_hand_saw = page.get_by_role("heading", name="Wood Saw")
        self.product_name_wrench = page.locator("//h5[normalize-space()='Adjustable Wrench']")
        self.product_name_screwdriver = page.locator("//h5[normalize-space()='Mini Screwdriver']")
        self.product_name_pliers = page.locator("//h5[normalize-space()='Bolt Cutters']")
        self.product_name_chisels = page.locator("//h5[normalize-space()='Swiss Woodcarving Chisels']")
        self.product_name_measures = page.locator("//h5[normalize-space()='Tape Measure 5m']")
        self.product_name_sander = page.locator("//h5[normalize-space()='Sheet Sander']")
        self.product_name_saw = page.locator("//h5[normalize-space()='Circular Saw']")
        self.product_name_drill = page.locator("//h5[normalize-space()='Cordless Drill 12V']")
        self.product_name_tool_belts = page.locator("//h5[normalize-space()='Leather toolbelt']")
        self.product_name_storage_solutions = page.locator("//h5[normalize-space()='Drawer Tool Cabinet']")
        self.product_name_safety_gear = page.locator("//h5[normalize-space()='Construction Helmet']")
        self.product_name_fasteners = page.locator("//h5[normalize-space()='Cross-head screws']")
        self.product_name_forgeflex_tools = page.locator("//h5[normalize-space()='Claw Hammer with Fiberglass Handle']")
        self.product_name_mightycraft_hardware = page.locator("//h5[normalize-space()='Slip Joint Pliers']")
        self.product_name_show_only_eco_friendly_products = page.locator("//h5[normalize-space()='Safety Helmet Face Shield']")

    def navigate(self):
        self.page.goto("/")

    def check_logo_visibility(self):
        expect(self.logo).to_be_visible()

    def check_banner_visibility(self):
        expect(self.banner).to_be_visible()

    def check_sort_title(self):
        expect(self.sort_title).to_be_visible()

    def check_sort_select_visibility(self):
        expect(self.sort_select).to_be_visible()

    def select_name_a_to_z(self):
        self.sort_select.select_option("name,asc")

    def select_name_z_to_a(self):
        self.sort_select.select_option("name,desc")

    def select_price_high_to_low(self):
        self.sort_select.select_option("price,desc")

    def select_price_low_to_high(self):
        self.sort_select.select_option("price,asc")

    def select_co2_a_to_e(self):
        self.sort_select.select_option("co2_rating,asc")

    def select_co2_e_to_a(self):
        self.sort_select.select_option("co2_rating,desc")

    def click_on_product_name_asc(self):
        self.product_name_asc.click()

    def click_on_product_name_desc(self):
        self.product_name_desc.click()

    def click_on_product_name_high_low(self):
        self.product_name_high_low.click()

    def click_on_product_name_low_high(self):
        self.product_name_low_high.click()

    def click_on_product_name_co2_a_to_e(self):
        self.product_name_a_to_e.click()

    def click_on_product_name_co2_e_to_a(self):
        self.product_name_e_to_a.click()

    def click_on_product_title(self):
        self.product_title.click()

    def check_filters_title(self):
        expect(self.filters_title).to_be_visible()

    def check_categories_title(self):
        expect(self.categories_title).to_be_visible()

    def check_hammer_checkbox(self):
        self.hammer_checkbox.check()

    def hammer_checkbox_checked(self):
        expect(self.hammer_checkbox).to_be_checked()

    def click_on_product_name_hammer(self):
        self.product_name_hammer.click()

    def check_hand_saw_checkbox(self):
        self.hand_saw_checkbox.check()

    def hand_saw_checkbox_checked(self):
        expect(self.hand_saw_checkbox).to_be_checked()

    def click_on_product_name_hand_saw(self):
        self.product_name_hand_saw.click()

    def check_wrench_checkbox(self):
        self.wrench_checkbox.check()

    def wrench_checkbox_checked(self):
        expect(self.wrench_checkbox).to_be_checked()

    def click_on_product_name_wrench(self):
        self.product_name_wrench.click()

    def check_screwdriver_checkbox(self):
        self.screwdriver_checkbox.check()

    def screwdriver_checkbox_checked(self):
        expect(self.screwdriver_checkbox).to_be_checked()

    def click_on_product_name_screwdriver(self):
        self.product_name_screwdriver.click()

    def check_pliers_checkbox(self):
        self.pliers_checkbox.check()

    def pliers_checkbox_checked(self):
        expect(self.pliers_checkbox).to_be_checked()

    def click_on_product_name_pliers(self):
        self.product_name_pliers.click()

    def check_chisels_checkbox(self):
        self.chisels_checkbox.check()

    def chisels_checkbox_checked(self):
        expect(self.chisels_checkbox).to_be_checked()

    def click_on_product_name_chisels(self):
        self.product_name_chisels.click()

    def check_measures_checkbox(self):
        self.measures_checkbox.check()

    def measures_checkbox_checked(self):
        expect(self.measures_checkbox).to_be_checked()

    def click_on_product_name_measures(self):
        self.product_name_measures.click()

    def check_sander_checkbox(self):
        self.sander_checkbox.check()

    def sander_checkbox_checked(self):
        expect(self.sander_checkbox).to_be_checked()

    def click_on_product_name_sander(self):
        self.product_name_sander.click()

    def check_saw_checkbox(self):
        self.saw_checkbox.check()

    def saw_checkbox_checked(self):
        expect(self.saw_checkbox).to_be_checked()

    def click_on_product_name_saw(self):
        self.product_name_saw.click()

    def check_drill_checkbox(self):
        self.drill_checkbox.check()

    def drill_checkbox_checked(self):
        expect(self.drill_checkbox).to_be_checked()

    def click_on_product_name_drill(self):
        self.product_name_drill.click()

    def check_tool_belts_checkbox(self):
        self.tool_belts_checkbox.check()

    def tool_belts_checkbox_checked(self):
        expect(self.tool_belts_checkbox).to_be_checked()

    def click_on_product_name_tool_belts(self):
        self.product_name_tool_belts.click()

    def check_storage_solutions_checkbox(self):
        self.storage_solutions_checkbox.check()

    def storage_solutions_checkbox_checked(self):
        expect(self.storage_solutions_checkbox).to_be_checked()

    def click_on_product_name_storage_solutions(self):
        self.product_name_storage_solutions.click()

    def check_safety_gear_checkbox(self):
        self.safety_gear_checkbox.check()

    def safety_gear_checkbox_checked(self):
        expect(self.safety_gear_checkbox).to_be_checked()

    def click_on_product_name_safety_gear(self):
        self.product_name_safety_gear.click()

    def check_fasteners_checkbox(self):
        self.fasteners_checkbox.check()

    def fasteners_checkbox_checked(self):
        expect(self.fasteners_checkbox).to_be_checked()

    def click_on_product_name_fasteners(self):
        self.product_name_fasteners.click()

    def check_brand_title(self):
        expect(self.brand_title).to_be_visible()

    def check_forgeflex_tools_checkbox(self):
        self.forgeflex_tools_checkbox.check()

    def forgeflex_tools_checkbox_checked(self):
        expect(self.forgeflex_tools_checkbox).to_be_checked()

    def click_on_product_name_forgeflex_tools(self):
        self.product_name_forgeflex_tools.click()

    def check_mightycraft_hardware_checkbox(self):
        self.mightycraft_hardware_checkbox.check()

    def mightycraft_hardware_checkbox_checked(self):
        expect(self.mightycraft_hardware_checkbox).to_be_checked()

    def click_on_product_name_mightycraft_hardware(self):
        self.product_name_mightycraft_hardware.click()

    def check_sustainability_title(self):
        expect(self.sustainability_title).to_be_visible()

    def check_sustainability_checkbox(self):
        self.show_only_eco_friendly_products_checkbox.check()

    def sustainability_checkbox_checked(self):
        expect(self.show_only_eco_friendly_products_checkbox).to_be_checked()

    def click_on_product_name_show_only_eco_friendly_products(self):
        self.product_name_show_only_eco_friendly_products.click()