from selenium.webdriver.common.by import By
import time


def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    time.sleep(30)

    button = browser.find_elements(By.ID, "add_to_basket_form")

    assert button is not None, "----R u ok?----"