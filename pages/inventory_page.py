from pages.base_page import BasePage

from playwright.sync_api import sync_playwright,expect

class InventoryPage(BasePage):
    PRODUCT_TITLE='.title'

    def __init__(self,page):
        super().__init__(page)
    
    def verify_products_page(self):
        expect(self.page.locator(self.PRODUCT_TITLE)).to_have_text("Products")
        
        
