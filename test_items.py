from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_add_to_cart_button(browser):
    try:
         browser.get(link)
         browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
         present = True 
         time.sleep(30)
    except NoSuchElementException:
         present = False
    assert present == True, 'No add-to-basket element!'
         