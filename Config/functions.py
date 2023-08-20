from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

path_to_chromedriver = 'c:\1\chromedriver.exe' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.set_window_size(1400, 1000)

#Функция проверяющая наличие/отсутствие элемента на странице
def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

#Функция выполняющая шаги для перехода на страницу регистрации
def registration():
    # Переходим на главную страницу
    browser.get('https://lk.rt.ru')
    # Ожидаем, когда произойдет перенаправление на страницу авторизации b2b
    time.sleep(10)
    #Находим кнопку "Войти с паролем"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='standard_auth_btn']").click()
    time.sleep(5)
    #Находим кнопку "Зарегистрироваться"
    search_button_register = browser.find_element(By.XPATH, "//a[@id='kc-register']").click()
    time.sleep(5)

#Функция выполняющая шаги для перехода на страницу авторизации
def autorisation():
    # Переходим на главную страницу
    browser.get('https://lk.rt.ru')
    # Ожидаем, когда произойдет перенаправление на страницу авторизации b2b
    time.sleep(10)
    # Находим кнопку "Войти с паролем"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='standard_auth_btn']").click()
    time.sleep(5)
