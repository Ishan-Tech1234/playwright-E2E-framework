import pytest

from pages.login_page import LoginPage
from components.header_component import HeaderComponent
import allure

# product_names=["Sauce Labs Bike Light","Sauce Labs Backpack","Sauce Labs Bolt T-Shirt"]
test_data=[("Sauce Labs Bike Light",),
           ]
@allure.title("Verify Sauce Page login ,adding and removing products functionality")
@allure.description("This opens Sauce page and checks login , adding and removing products functionality")
@pytest.mark.parametrize("product_names",test_data)
@allure.feature('E-commerce Sauce demo')
@allure.story('Login and cart')
@allure.tag('System Testing')
def test_add_and_remove_products_from_cart(login_user,product_names,page):
     inventory_page=login_user
     header=HeaderComponent(inventory_page.page)
     inventory_page.verify_products_page()
     for product_name in product_names:
       product_component=inventory_page.get_product(product_name)
       product_component.add_to_cart(product_name)
     
     

     header.verify_cart_badge(len(product_names))
     cart_page=inventory_page.open_cart()
     for product_name in product_names:
      cart_page.verify_product_present_in_cart(product_name)
      cart_page.verify_individual_products_in_cart(product_name,1)
     product_component=cart_page.get_product(product_names[0])
     product_component.remove_from_cart(product_name)
     cart_page.verify_product_removed_from_cart(product_names[0])
     header.verify_cart_badge(len(product_names)-1)
     
     
     

     
