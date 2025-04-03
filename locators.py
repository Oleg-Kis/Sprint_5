from selenium.webdriver.common.by import By

class Locators:
    # регистрация

    NAME = [By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input"]  # поле Имя в окне регистрации
    EMAIL = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input")  # поле Email в окне регистрации
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']")  # поле Пароль
    BUT_REG_END = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка Зарегестрироваться в окне регистрации
    # вход

    BUT_REG = (By.XPATH, ".//a[@href='/register']")  # кнопка Зарегистрироваться в окне Вход
    FORGOT_PASS = (By.XPATH, ".//a[@href='/forgot-password']")  # кнопка Восстановить пароль в окне Вход
    BUT_ENTER = (By.XPATH, ".//a[text()='Войти']")  # кнопка Войти в окне восстановления пароля и регистрации
    BUT_ENTER_ACC = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти на странице входа
    BUT_OFFICE = (By.XPATH, ".//a[@href='/account']")  # кнопка Личный Кабинет
    BUT_GO_ACC = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
    LOGO_STELLAR = (By.XPATH, ".//a/parent::div[@class='AppHeader_header__logo__2D0X2']")  # логотип stellar burgers
    CONSTRUCTOR = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX' and @href='/']")  # кнопка Конструктор
    BREAD = (By.XPATH, ".//span[text()='Булки']/parent::div")  # вкладка Булки
    SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # вкладка Соусы
    TOPPINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # вкладка Начинки
    ENTER_LOGO = (By.XPATH, ".//h2[text()='Вход']") #надпись Вход на странице авторизации
    BUT_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") #кнопка Оформить заказ
    TEXT_PROFILE = (By.XPATH, ".//a[text()='Профиль']") #надпись Профиль в личном кабинете
    TITLE_INCORRECT_PASS = (By.XPATH, ".//p[@class='input__error text_type_main-default']") #надпись Некорректный пароль
    LOGIN_IN_OFFICE = (By.XPATH, ".//input[contains(@value,'@')]") #поле Логин в личном кабинете
    BUT_EXIT = (By.XPATH, ".//button[text()='Выход']") #кнопка Выход в личном кабинете
    TEXT_PUT_BURGER = (By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10']") #надпись Соберите бургер
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span") #активная вкладка Булки/Соусы/Начинки
    ACTIVE_TAB_SAUCES = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Соусы']") #активная вкладка Соусы
    ACTIVE_TAB_BREAD = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Булки']") #активная вкладка Булки
