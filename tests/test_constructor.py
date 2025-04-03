from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import *

class TestConstructorTransition:
    def test_from_office_on_click_constructor(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))

        driver.find_element(*Locators.CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER))

        text = driver.find_element(*Locators.TEXT_PUT_BURGER).text

        assert text == put_burger

    def test_from_office_on_click_logo(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TEXT_PROFILE))

        driver.find_element(*Locators.LOGO_STELLAR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUT_ORDER))

        text = driver.find_element(*Locators.TEXT_PUT_BURGER).text

        assert text == put_burger

    def test_click_ingredient_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        link = driver.find_element(*Locators.ACTIVE_TAB).text

        assert link == sauce

    def test_click_ingredient_toppings(self, driver):
        driver.find_element(*Locators.TOPPINGS).click()
        link = driver.find_element(*Locators.ACTIVE_TAB).text

        assert link == topping

    def test_click_ingredient_bread(self, driver):
        driver.find_element(*Locators.SAUCES).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACTIVE_TAB_SAUCES))

        driver.find_element(*Locators.BREAD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ACTIVE_TAB_BREAD))
        link = driver.find_element(*Locators.ACTIVE_TAB).text

        assert link == bread
