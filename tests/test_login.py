from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_login(page):
     login_page=LoginPage(page)
     product_name="Sauce Labs Bike Light"
     inventory_page=login_page.login("standard_user","secret_sauce")
     inventory_page.verify_products_page()
     inventory_page.add_to_cart_product(product_name)
     inventory_page.verify_cart_badge()
     cart_page=inventory_page.open_cart()
     cart_page.verify_products_in_cart(product_name)
     
     

     
