from pages.login_page import LoginPage
from components.header_component import HeaderComponent



def test_add_and_remove_products_from_cart(page):
     login_page=LoginPage(page)
     header=HeaderComponent(page)
     product_names=["Sauce Labs Bike Light","Sauce Labs Backpack","Sauce Labs Bolt T-Shirt"]
     inventory_page=login_page.login("standard_user","secret_sauce")
     inventory_page.verify_products_page()
     for product_name in product_names:
       product_component=inventory_page.get_product(product_name)
       product_component.add_to_cart()
     
     

     header.verify_cart_badge(len(product_names))
     cart_page=inventory_page.open_cart()
     for product_name in product_names:
      cart_page.verify_product_present_in_cart(product_name)
      cart_page.verify_individual_products_in_cart(product_name,1)
     product_component=cart_page.get_product(product_names[0])
     product_component.remove_from_cart()
     cart_page.verify_product_removed_from_cart(product_names[0])
     header.verify_cart_badge(len(product_names)-1)
     
     
     

     
