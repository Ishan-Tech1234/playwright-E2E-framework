from pages.base_page import BasePage
from playwright.sync_api import expect
class CartPage(BasePage):
    
    
    def __init__(self,page):
        super().__init__(page)

    


    def verify_products_in_cart(self,product_name):
        target=self.page.locator(".inventory_item_name",has_text = product_name)
        expect(target).to_be_visible()
        self.page.screenshot(path="screenshots/cart_page.png",full_page=True)

