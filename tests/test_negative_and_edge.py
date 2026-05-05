from playwright.sync_api import expect
from pages.login_page import LoginPage
import pytest
from components.header_component import HeaderComponent

#Trying login with multiple invalid crendentials
test_data=[("standard_user","invalid_pass","Epic sadface: Username and password do not match any user in this service"),
            ("invalid_user","secret_sauce","Epic sadface: Username and password do not match any user in this service"),
            ("invalid_user","invalid_pass","Epic sadface: Username and password do not match any user in this service"),
            ("","","Epic sadface: Username is required")]
@pytest.mark.parametrize("username,password,error_message",test_data)
def test_negative_and_edge(username,password,error_message,page):
    login_page=LoginPage(page)
    login_page.login(username,password)
    expect(login_page.get_error_message()).to_have_text(error_message)

# Adding the same product twice
def test_add_same_product_twice(login_user,product_name="Sauce Labs Backpack"):
    inventory_page=login_user
    product_component=inventory_page.get_product(product_name)
    product_component.add_to_cart(product_name)
    expect(inventory_page.page.locator("[data-test='add-to-cart-sauce-labs-backpack']")).to_be_hidden()
    header_component=HeaderComponent(inventory_page.page)
    header_component.verify_cart_badge(1)
    


# Removing a product that was never added
def test_remove_never_added_product(login_user,product_name="Sauce Labs Backpack"):
    inventory_page=login_user
    product_component=inventory_page.get_product(product_name)
    expect(product_component.container.get_by_role("button",name="remove-sauce-labs-backpack")).to_have_count(0)
    header_component=HeaderComponent(inventory_page.page)
    header_component.verify_cart_badge(0)

# Cart badge disappearing when all items removed   
def test_remove_product_updates_cart_badge(login_user,product_name="Sauce Labs Backpack"):
    inventory_page=login_user
    product_component=inventory_page.get_product(product_name)
    product_component.add_to_cart(product_name="Sauce Labs Backpack")
    header_component=HeaderComponent(inventory_page.page)
    header_component.verify_cart_badge(1)
    product_component.remove_from_cart(product_name="Sauce Labs Backpack")
    header_component.verify_cart_badge(0)




    
    
