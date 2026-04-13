from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

class LoginPage(BasePage):
    USERNAME_INPUT="#user-name"
    PASSWORD_INPUT="#password"
    URL="https://www.saucedemo.com/"
    LOGIN_BUTTON="#login-button"
    
    def __init__(self, page):
        super().__init__(page)

    def login(self,username,password) :
        self.navigate(self.URL)
        self.fill(self.USERNAME_INPUT,username,"username")
        self.fill(self.PASSWORD_INPUT,password,"password")
        self.click(self.LOGIN_BUTTON,"Clicking login button")
        inventory_page=InventoryPage(self.page)
        return inventory_page
       
        

   
