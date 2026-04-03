from pages.base_page import BasePage
from pages.cart_page import CartPage
from components.product_component import ProductComponent

from playwright.sync_api import expect

class InventoryPage(BasePage):
    PRODUCT_TITLE='.title'
    CART="[data-test='shopping-cart-link']"


    def __init__(self,page):
        super().__init__(page)
    
    def verify_products_page(self):
        expect(self.page.locator(self.PRODUCT_TITLE)).to_have_text("Products")

    def get_product(self,product_name):
        item=self.page.locator(".inventory_item",has_text=product_name)
        product_component=ProductComponent(item)
        return product_component


        

    
    def open_cart(self):
        self.click(self.CART)
        cart_page=CartPage(self.page)
        return cart_page


        
        
