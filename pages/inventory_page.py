from pages.base_page import BasePage

from playwright.sync_api import sync_playwright,expect

class InventoryPage(BasePage):
    PRODUCT_TITLE='.title'
    CART_BADGE="[data-test='shopping-cart-badge']"


    def __init__(self,page):
        super().__init__(page)
    
    def verify_products_page(self):
        expect(self.page.locator(self.PRODUCT_TITLE)).to_have_text("Products")

    def add_to_cart_product(self,product_name):
        item=self.page.locator(".inventory_item")
        parent=item.filter(has_text=product_name)
        target=parent.locator("[data-test^='add-to-cart']")
        self.click(target)


        

    def verify_cart_badge(self):
        expect(self.page.locator(self.CART_BADGE)).to_have_text("1")
        self.page.screenshot(path="screenshots/fullpage.png", full_page=True)
    

        
        
