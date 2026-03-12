from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect

class LoginPage(BasePage):
    
    URL="https://www.saucedemo.com/"
    USERNAME_INPUT="#user-name"
    PASSWORD_INPUT="#password"
    LOGIN_BUTTON="#login-button"

    def __init__(self, page):
        super().__init__(page)

    def login(self,username,password) :
        self.navigate(self.URL)
        self.fill(self.USERNAME_INPUT,username)
        self.fill(self.PASSWORD_INPUT,password)
        self.click(self.LOGIN_BUTTON)
        inventory_page=InventoryPage(self.page)
        return inventory_page

   
