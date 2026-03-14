from pages.base_page import BasePage

from playwright.sync_api import sync_playwright,expect

class InventoryPage(BasePage):
    PRODUCT_TITLE='.title'
    BACKPACK_ADD_TO_CARTS='#add-to-cart-sauce-labs-backpack'
    CART_BADGE="[data-test='shopping-cart-badge']"

    def __init__(self,page):
        super().__init__(page)
    
    def verify_products_page(self):
        expect(self.page.locator(self.PRODUCT_TITLE)).to_have_text("Products")

    def add_to_cart_backpack(self):
        self.click(self.BACKPACK_ADD_TO_CARTS)

    def verify_cart_badge(self):
        expect(self.page.locator(self.CART_BADGE)).to_have_text("1")
    

        
        
