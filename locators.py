from selenium.webdriver.common.by import By

class Locators:
    # регистрация

    NAME = [By.XPATH, ".//form/fieldset[1]/div/div/input"]  # поле Имя в окне регистрации
    EMAIL_REG = (By.XPATH, ".//form/fieldset[2]/div/div/input")  # поле Email в окне регистрации
    PASSWORD_REG = (By.XPATH, ".//form/fieldset[3]/div/div/input")  # поле Пароль в окне регистрации
    BUT_REG_END = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка Зарегестрироваться в окне регистрации
    # вход

    BUT_REG = (By.XPATH, ".//a[@href='/register']")  # кнопка Зарегистрироваться в окне Вход
    FORGOT_PASS = (By.XPATH, ".//a[@href='/forgot-password']")  # кнопка Восстановить пароль в окне Вход
    BUT_ENTER = (By.XPATH, ".//a[text()='Войти']")  # кнопка Войти в окне восстановления пароля и регистрации
    BUT_ENTER_ACC = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти на странице входа
    BUT_OFFICE = (By.XPATH, ".//a[@href='/account']")  # кнопка Личный Кабинет
    BUT_GO_ACC = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт
    EMAIL_ENTER = (By.XPATH, ".//form/fieldset[1]/div/div/input")  # поле Email на старнице Вход
    PASSWORD_ENTER = (By.XPATH, ".//form/fieldset[2]/div/div/input")  # поле Пароль на странице Вход
    LOGO_STELLAR = (By.XPATH, ".//a/parent::div[@class='AppHeader_header__logo__2D0X2']")  # логотип stellar burgers
    CONSTRUCTOR = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX' and @href='/']")  # кнопка Конструктор
    BREAD = (By.XPATH, ".//span[text()='Булки']/parent::div")  # вкладка Булки
    SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # вкладка Соусы
    TOPPINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # вкладка Начинки
