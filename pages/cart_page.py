from pages.base_page import BasePage
from playwright.sync_api import expect
from components.product_component  import  ProductComponent
class CartPage(BasePage):
     
    def __init__(self,page):
        super().__init__(page)


    def verify_product_present_in_cart(self,product_name):
        target=self.page.locator(".inventory_item_name",has_text = product_name)
        expect(target).to_be_visible()
        self.page.screenshot(path="screenshots/cart_page.png",full_page=True)

    def verify_individual_products_in_cart(self,product_name,product_count):
        item=self.page.locator(".cart_item",has_text = product_name)
        target=item.locator('[data-test="item-quantity"]')
        expect(target).to_have_text(str(product_count))

   
        
        
    
    def verify_product_removed_from_cart(self,product_name):
        target=self.page.locator(".inventory_item_name",has_text=product_name)
        expect(target).not_to_be_visible()

    def get_product(self,product_name):
        item=self.page.locator(".cart_item",has_text=product_name)
        product_component=ProductComponent(item)
        return product_component

    



