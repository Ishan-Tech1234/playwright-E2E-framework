[![Playwright Python CI](https://github.com/Ishan-Tech1234/playwright-E2E-framework/actions/workflows/playwright-ci.yml/badge.svg)](https://github.com/Ishan-Tech1234/playwright-E2E-framework/actions/workflows/playwright-ci.yml)


An automation framework designed to perform E2E testing on sauce demo website. 
It is build using python playwright designed to keep it simple at the same time flexible and scalable

## TechStack
Python - HLL programming language , we can incorporate Behavior-Driven Development (BDD),Mocking,Web Testing,API Testing,Load Testing:
Playwright - open-source automation framework developed by Microsoft for end-to-end (E2E) testing of web applications which provides good features like locators and auto waits.
pytest- Pytest is a powerful and flexible testing framework in Python which provides features like
fixtures, parameterization, and detailed assertion introspection.
Allure-  Allure Report is a powerful tool that enhances automated testing by providing detailed and visually appealing reports
GitHub - GitHub is a web-based platform that hosts Git repositories and provides tools for version control, collaboration, and project management

## SetUp 
Step 1 : Download the repository from GitHub
Step 2 : Run the command  which installs all the required dependencies required to run the project
```bash
pip install -r requirements.txt
playwright install
```
Step 3 : run pytest testname -s t run the test

## FolderStructure
PLAYWRIGHT_E2E_FRAMEWORK
|----> tests
|        |---> test_login.py
|        |---> test_negative_and_edge.py
|---->playwright_logger_module.py
|----> components
|         |---> header_component.py
|         |---> product_component.py
|----->README.md
|------>config_loader
|          |--->config.json
|          |--->load_config.py
|------>error_screenshots
|------>pages
|        |----->base_page.py
|        |----->cart_page.py
|        |----->inventory_page.py
|        |----->login_page.py
|-------->conftest.py
|-------->playwright.log
|-------->pytest.ini
|-------->requirements.txt 

## Architecture
The framework is built using Page Object Model(POM) designed to reduce dependencies and keep the project flexible and scalable.
The Page Objects define the user behavior on the page , it is a collection of locators and methods that mimic the user behavior on the page.
BasePage provides a wrapper class for the playwright page which contains methods like fill(),click() which all the other pages inherit.
LoginPage,CartPage,InventoryPage define user behavior on that particular pages. The seperation based on responsibility reduces unnecessary dependencies and redundancy.
The inventory page is decomposed into  2 components Product component and header component based on responsibility.
Product component handles the adding product into the cart by scoping the container to it.
Header component handles the badge verfication so that each component is responsible for its maintanability of its own slice of UI.
The tests are run using pytest which coordinates the test flow.
It contains 2 tests test_login.py and test_negative_and_edge.py. 
test_login.py is a E2E test designed to test complete functionality of the sauce demo website. It test from login, adding single and multiple product,removing single and multipl product ,cart validation.
test_negative_and_edge.py is test designed to test the edge or corner scenarios so that application does break during edge cases.

To run all the tests command
```bash
pytest -s
```

## Reporting 

Screenshots have been added on failure so that screenshot is captured immediately which can used for future references.
Detailed logging is implemented which provides step up level execution details for triangulating the root cause with great accuracy.
Allure reporting is implemented as well which provides high end interactable HTML reports which provides detailed insights like severity, retries, execution history,testtimeline.
CI workflow has been added so that test get triggered on every commit so that regression runs during every new addition ensuring the test is not broken.

To generate the allure reports
```bash
allure serve allure-results
```

