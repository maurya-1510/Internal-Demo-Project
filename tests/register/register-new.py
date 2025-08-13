import allure
import pytest
from playwright.sync_api import Page, expect
from datetime import datetime

#@pytest.mark.order(1)
@allure.title("Register Demo Test")
def test_register_user(page: Page):

    # Go to account registration page
    page.goto("https://dev-apparel-demo.printxpand.net/customer/account/create/")
    page.wait_for_timeout(5000)

    # Email create
    def generate_random_email():
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"testqauser_{current_time}@yopmail.com"
    email = generate_random_email()

    # Fill form fields
    page.get_by_role("textbox", name="First Name *").click()
    page.get_by_role("textbox", name="First Name *").fill("Test_Firstname")
    page.get_by_role("textbox", name="Last Name *").click()
    page.get_by_role("textbox", name="Last Name *").fill("Test_Lastname")
    page.get_by_role("textbox", name="Email*").click()
    page.get_by_role("textbox", name="Email*").fill(email)
    page.get_by_role("textbox", name="Password*", exact=True).click()
    page.get_by_role("textbox", name="Password*", exact=True).fill("test@123")
    page.get_by_role("textbox", name="Confirm Password*").click()
    page.get_by_role("textbox", name="Confirm Password*").fill("test@123")
    page.wait_for_timeout(5000)

    # Submit the form
    page.get_by_role("button", name="Create an Account").click()
    page.wait_for_timeout(5000)
    
    with allure.step("Take final screenshot and attach URL"):
        screenshot = page.screenshot(full_page=True)
        allure.attach(screenshot, name="Final State - Full Page", attachment_type=allure.attachment_type.PNG)
        allure.attach(page.url, name="Final URL", attachment_type=allure.attachment_type.TEXT)