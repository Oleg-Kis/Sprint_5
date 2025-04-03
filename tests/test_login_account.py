from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import *

class TestLoginAccount:
    def test_login_but_account_office(self, driver):
        driver.find_element(*Locators.BUT_OFFICE).click()
        driver.find_element(*Locators.EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_login_but_enter_account(self, driver):
        driver.find_element(*Locators.BUT_GO_ACC).click()
        driver.find_element(*Locators.EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_login_but_enter_reg_window(self, driver):
        driver.find_element(*Locators.BUT_GO_ACC).click()
        driver.find_element(*Locators.BUT_REG).click()
        driver.find_element(*Locators.BUT_ENTER).click()
        driver.find_element(*Locators.EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_login_but_enter_recovery_window(self, driver):
        driver.find_element(*Locators.BUT_GO_ACC).click()
        driver.find_element(*Locators.FORGOT_PASS).click()
        driver.find_element(*Locators.BUT_ENTER).click()
        driver.find_element(*Locators.BUT_REG).click()
        driver.find_element(*Locators.BUT_ENTER).click()
        driver.find_element(*Locators.EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_exit_office(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_EXIT))
        driver.find_element(*Locators.BUT_EXIT).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.ENTER_LOGO))

        driver.find_element(*Locators.LOGO_STELLAR).click()

        text_but = driver.find_element(*Locators.BUT_GO_ACC).text
        assert text_but == 'Войти в аккаунт'

    def test_go_office_click_but_office(self,driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))

        log_mail = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')

        assert log_mail == login
