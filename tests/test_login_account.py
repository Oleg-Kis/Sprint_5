from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import *

class TestLoginAccount:
    def test_login_but_account_office(self, driver):
        driver.find_element(*Locators.BUT_OFFICE).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_login_but_enter_account(self, driver):
        driver.find_element(*Locators.BUT_GO_ACC).click()
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(login)
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
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(login)
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
        driver.find_element(*Locators.EMAIL_ENTER).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys(valid_password)
        driver.find_element(*Locators.BUT_ENTER_ACC).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))
        email = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')
        assert email == login

    def test_exit_office(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.ENTER_LOGO))

        driver.find_element(*Locators.LOGO_STELLAR).click()

        text_but = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").text
        assert text_but == 'Войти в аккаунт'

    def test_go_office_click_but_office(self,driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))

        log_mail = driver.find_element(*Locators.LOGIN_IN_OFFICE).get_attribute('value')

        assert log_mail == login
