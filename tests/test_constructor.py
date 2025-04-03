from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators


class TestConstructorTransition:
    def test_from_office_on_click_constructor(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))

        driver.find_element(*Locators.CONSTRUCTOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        text = driver.find_element(By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']").text

        assert text == 'Соберите бургер'

    def test_from_office_on_click_logo(self, driver, log_in):
        driver.find_element(*Locators.BUT_OFFICE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_PROFILE))

        driver.find_element(*Locators.LOGO_STELLAR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.BUT_ORDER))

        text = driver.find_element(By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']").text

        assert text == 'Соберите бургер'

    def test_click_ingredient_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        link = driver.find_element(By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span").text

        assert link == 'Соусы'

    def test_click_ingredient_toppings(self, driver):
        driver.find_element(*Locators.TOPPINGS).click()
        link = driver.find_element(By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span").text

        assert link == 'Начинки'

    def test_click_ingredient_bread(self, driver):
        driver.find_element(*Locators.SAUCES).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Соусы']")))

        driver.find_element(*Locators.BREAD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Булки']")))
        link = driver.find_element(By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span").text

        assert link == 'Булки'
