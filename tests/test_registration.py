from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import *
from helper import generate_reg_data
from locators import Locators

class TestRegistration:
    def test_reg_valid_data(self, driver, pre_reg):
        name, email, password = generate_reg_data()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUT_REG_END).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ENTER_LOGO))

        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))
        login_email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert login_email == email

    def test_reg_no_valid_password(self,driver, pre_reg):
        name, email, password = generate_reg_data()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(no_valid_password)
        driver.find_element(*Locators.BUT_REG_END).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TITLE_INCORRECT_PASS))

        text_error = driver.find_element(*Locators.TITLE_INCORRECT_PASS).text

        assert text_error == incorrect_pass
