from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright,expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import os
import logging
import allure
import shutil

from config_loader.load_config import load_config



def __init__(self,page):
    self.page=page

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()

ENV=os.getenv("Test_env","dev")
config=load_config(ENV)

@pytest.fixture(scope="function")
def login_user(page):
    login_page=LoginPage(page)
    username= config["username"]
    password=config["password"]
    inventory_page=login_page.login(username,password)
    return inventory_page


def pytest_runtest_setup(item):
    logging.info(f"=== TEST {item.name} starting at {datetime.now()} ===")

@pytest.hookimpl()
def pytest_sessionstart(session):
    shutil.rmtree("allure-results",ignore_errors=True)
    os.makedirs("allure-results",exist_ok=True)



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report=outcome.get_result()
    if report.when=="call" and not report.failed:
        logging.info("=== TEST END , RESULT : SUCCESS ===")
    if report.when=="call" and report.failed:
        logging.info("=== TEST END , RESULT : FAILURE ===")
        page=item.funcargs.get("page",None)
        if page:
            os.makedirs("error_screenshots",exist_ok=True)
            timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"error_screenshots/{item.name}_{timestamp}.png"
            try:
                page.screenshot(path=filename)
                with open(filename,'rb') as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"error_screenshot - {item.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                print(f"\n[Playwright] Screenshot saved to {filename}")
            except Exception as e:
                print(f"\n[Playwright] Failed to take screenshot: {e}")




