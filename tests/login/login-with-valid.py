import allure
import pytest
from playwright.sync_api import Page, expect


#@pytest.mark.order(2)
@allure.title("Login Test with valid Credentials")
def test_login_user(page: Page):
    
    with allure.step("Open URL"):
     page.goto("https://dev-apparel-demo.printxpand.net/customer/account/login/")
     page.wait_for_timeout(5000)

    with allure.step("Enter Username"):
     page.get_by_role("textbox", name="Email*").click()
     page.get_by_role("textbox", name="Email*").fill("maurya.p@biztechcs.com")
    
    with allure.step("Enter Password"):
     page.get_by_role("textbox", name="Password").click()
     page.get_by_role("textbox", name="Password").fill("baps@200")

    page.wait_for_timeout(5000)

    page.get_by_role("button", name="Sign In").click()

    page.wait_for_timeout(5000)

    with allure.step("Take final screenshot and attach URL"):
        screenshot = page.screenshot(full_page=True)
        allure.attach(screenshot, name="Final State - Full Page", attachment_type=allure.attachment_type.PNG)
        allure.attach(page.url, name="Final URL", attachment_type=allure.attachment_type.TEXT)