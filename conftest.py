import pytest
from selenium import webdriver

from data import *
from locators import Locators

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture
def log_in(driver):
    driver.find_element(*Locators.BUT_OFFICE).click()
    driver.find_element(*Locators.EMAIL_ENTER).send_keys(login)
    driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
    driver.find_element(*Locators.BUT_ENTER_ACC).click()
    return driver

@pytest.fixture
def pre_reg(driver):
    driver.find_element(*Locators.BUT_GO_ACC).click()
    driver.find_element(*Locators.BUT_REG).click()
    return driver
