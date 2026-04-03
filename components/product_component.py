from pages.base_page import BasePage

class ProductComponent():
   

    def __init__(self,container):
      self.container=container 
      
      

    def add_to_cart(self):
     button=self.container.locator("[data-test^='add-to-cart-']")
     button.click()
     

    def remove_from_cart(self):
      button=self.container.locator("[data-test^='remove-']")
      button.click()
      
      