from pages.login_page import LoginPage


def test_login(page):
     login_page=LoginPage(page)
     inventory_page=login_page.login("standard_user","secret_sauce")
     inventory_page.verify_products_page()
     inventory_page.add_to_cart_backpack()
     inventory_page.verify_cart_badge()
     
