from pages.login_page import LoginPage


def test_login(page):
     login_page=LoginPage(page)
     inventory_page=login_page.login("standard_user","secret_sauce")
     inventory_page.verify_products_page()
     
