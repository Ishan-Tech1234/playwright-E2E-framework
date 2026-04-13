from pages.base_page import BasePage


class ProductComponent(BasePage):
   

    def __init__(self,page,container):
      self.container=container
      super().__init__(page)
      
      
      

    def add_to_cart(self,product_name):
     button=self.container.locator("[data-test^='add-to-cart-']")
     self.click(button,f"adding {product_name} to cart")
     
     

    def remove_from_cart(self,product_name):
      button=self.container.locator("[data-test^='remove-']")
      self.click(button,f"removing {product_name} from cart")
      
      