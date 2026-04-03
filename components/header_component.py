from playwright.sync_api import expect
from components.product_component import ProductComponent

class HeaderComponent():
    
    def __init__(self,page):
        self.header=page
        
    CART_BADGE="[data-test='shopping-cart-badge']"

    def verify_cart_badge(self,cart_size):
        expect(self.header.locator(self.CART_BADGE)).to_have_text(str(cart_size))
        # self.page.screenshot(path="screenshots/cartsize.png", full_page=True)

 

   

      
      