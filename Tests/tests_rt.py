from selenium.webdriver.common.by import By
from Config.settings import valid_email, valid_password, test_email
from Config.functions import check_exists_by_xpath, registration, browser, autorisation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Тест-кейс RT-001 Загрузка страницы авторизации
def test_main_page():
    #Переходим на главную страницу
    browser.get('https://lk.rt.ru')
    #Ожидаем, когда произойдет перенаправление на страницу авторизации b2b
    time.sleep(10)
    #Проверяем, что оказались на странице авторизации по тэгу h2, текст в котором "Личный кабинет"
    assert browser.find_element(By.TAG_NAME, 'h2').text == "Личный кабинет"

#Проверяем, что открывается страница для ввода временного кода (Тест-кейс RT-002)
def test_temp_code():
    # Переходим на главную страницу
    browser.get('https://lk.rt.ru')
    # Ожидаем, когда произойдет перенаправление на страницу авторизации b2b
    time.sleep(10)
    # Находим поле "E-mail или мобильный телефон" и вводим email
    search_field_email_phone = browser.find_element(By.XPATH, "//input[@id='address']")
    search_field_email_phone.clear()
    search_field_email_phone.send_keys(valid_email)
    # Находим и нажимаем кнопку "Получить код"
    search_button_code = browser.find_element(By.XPATH, "//button[@id='otp_get_code']").click()
    time.sleep(5)
    # Проверяем, что открылась страница для ввода временного кода (по тэгу h1, текст в котором "Код подтверждения отправлен")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Код подтверждения отправлен"

#Проверяем, что открывается страница для ввода кода подтверждения (Тест-кейс RT-003 Регистрация нового пользователя
# (использовать любой вновь созданный e-mail))
def test_register_new_email():
    registration()
    #Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    #Находим поле "Имя" и вводим
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('Аа')
    #Находим поле "Фамилия" и вводим
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('Аа')
    #Пропускаем поле "Город", т.к. он заполняется автоматически
    #Находим поле "E-mail" и вводим
    search_field_email = browser.find_element(By.XPATH, "//input[@id='address']")
    search_field_email.clear()
    search_field_email.send_keys(test_email)
    #Находим поле "Пароль" и вводим
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys('12@Ghdjfd')
    #Находим поле "Подтвердить пароль" и вводим
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('12@Ghdjfd')
    #Находим кнопку "Зарегистрироваться" и нажимаем ее
    search_button_register2 = browser.find_element(By.XPATH, "//button[@name='register']").click()
    time.sleep(5)
    #Проверяем, что на открывшейся странице по тэгу h1 есть текст "Подтверждение email"
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Подтверждение email"

#Тест-кейс RT-004 Регистрация нового пользователя с e-mail, к которому привязана существующая учетная запись
def test_register_existing_email():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    #Находим поле "Имя" и вводим
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('Аа')
    #Находим поле "Фамилия" и вводим
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('Аа')
    #Пропускаем поле "Город", т.к. он заполняется автоматически
    #Находим поле "E-mail" и вводим
    search_field_email = browser.find_element(By.XPATH, "//input[@id='address']")
    search_field_email.clear()
    search_field_email.send_keys(valid_email)
    #Находим поле "Пароль" и вводим
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys('12@Ghdjfd')
    #Находим поле "Подтвердить пароль" и вводим
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('12@Ghdjfd')
    #Находим кнопку "Зарегистрироваться" и нажимаем ее
    search_button_register2 = browser.find_element(By.XPATH, "//button[@name='register']").click()
    time.sleep(5)
    #Проверяем, что в появившемся окне есть текст "Учетная запись уже существует"
    assert browser.find_element(By.XPATH, "//h2[@class='card-modal__title']").text == "Учётная запись уже существует"

#Тест-кейс RT-005 Требования к паролю при регистрации нового пользователя
def test_psw_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Пароль" и вводим не менее 8 символов, состоящих из латинских букв, хотя бы одна из которых заглавная
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys('Aaaaaaaa')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaaa')
    time.sleep(5)
    # Проверяем, что под полем "Пароль" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False
    #Тест падает из-за ошибки. Неполные требования к корректности пароля при регистрации пользователя - в требованиях
    # указано, что пароль должен состоять только из латинских символов, хотя бы один символ должен быть заглавным.
    # Система выдает ошибку, о том, что нужно ввести хотя бы одну цифру или спецсимвол

#Проверяем, что открывается страница "Восстановление пароля" для ввода e-mail при попытке восстановить забытый пароль
# (Тест-кейс RT-007 Восстановление пароля с корректным e-mail)
def test_psw_recovery():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    #Находим и нажимаем ссылку "Забыл пароль"
    search_link_forgot_psw = browser.find_element(By.XPATH, "//a[@id='forgot_password']").click()
    time.sleep(5)
    # Проверяем, что на открывшейся странице по тэгу h1 текст "Восстановление пароля"
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"

# Тест-кейс RT-008 Авторизация с некорректным e-mail и корректным password
def test_incorrect_email():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    # Находим таб "Почта"
    search_tab_email = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    time.sleep(3)
    # Находим поле для ввода E-mail и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys('1213@sdf.ru')
    # Находим поле для ввода пароля и вводим его
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys(valid_password)
    # Находим и нажимаем кнопку "Войти"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='kc-login']").click()
    time.sleep(3)
    # Проверяем, что на странице появилось сообщение об ошибке "Неверный логин или пароль"
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == "Неверный логин или пароль"
    #Ожидаем, что у ссылки "Забыл пароль" меняется класс, окрашивающий ее в оранжевый цвет
    assert check_exists_by_xpath("//a[@class='rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated']") == True

# Тест-кейс RT-009 Авторизация с корректным e-mail и некорректным password
def test_incorrect_psw():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    # Находим таб "Почта"
    search_tab_email = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    time.sleep(3)
    # Находим поле для ввода E-mail и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys(valid_email)
    # Находим поле для ввода пароля и вводим его
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys('Aaaaaaaa1')
    # Находим и нажимаем кнопку "Войти"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='kc-login']").click()
    time.sleep(3)
    # Проверяем, что на странице появилось сообщение об ошибке "Неверный логин или пароль"
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == "Неверный логин или пароль"
    #Ожидаем, что у ссылки "Забыл пароль" меняется класс, окрашивающий ее в оранжевый цвет
    assert check_exists_by_xpath("//a[@class='rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated']") == True

# Тест-кейс RT-010 Авторизация с некорректным e-mail и некорректным password
def test_incorrect_email_and_psw():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    # Находим таб "Почта"
    search_tab_email = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    time.sleep(3)
    # Находим поле для ввода E-mail и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys('sfkj@asd.ru')
    # Находим поле для ввода пароля и вводим его
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys('Aaaaaaaa1')
    # Находим и нажимаем кнопку "Войти"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='kc-login']").click()
    time.sleep(3)
    # Проверяем, что на странице появилось сообщение об ошибке "Неверный логин или пароль"
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == "Неверный логин или пароль"
    #Ожидаем, что у ссылки "Забыл пароль" меняется класс, окрашивающий ее в оранжевый цвет
    assert check_exists_by_xpath("//a[@class='rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated']") == True

# Тест-кейс RT-011 Авторизация с некорректным номером телефона и корректным password
def test_incorrect_phone():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    # Находим поле для ввода телефона и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys('9031111111')
    # Находим поле для ввода пароля и вводим его
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys(valid_password)
    # Находим и нажимаем кнопку "Войти"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='kc-login']").click()
    time.sleep(3)
    # Проверяем, что на странице появилось сообщение об ошибке "Неверный логин или пароль"
    assert browser.find_element(By.XPATH, "//span[@id='form-error-message']").text == "Неверный логин или пароль"
    #Ожидаем, что у ссылки "Забыл пароль" меняется класс, окрашивающий ее в оранжевый цвет
    assert check_exists_by_xpath("//a[@class='rt-link rt-link--orange login-form__forgot-pwd login-form__forgot-pwd--animated']") == True

#Проверяем, что открывается страница для ввода кода подтверждения, отправленного на e-mail при восстановлении пароля
# (Тест-кейс RT-012 Восстановление пароля с некорректным e-mail (необходимо вручную ввести символы с картинки))
def test_psw_recovery_incorrect_email():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    #Находим и нажимаем ссылку "Забыл пароль"
    search_link_forgot_psw = browser.find_element(By.XPATH, "//a[@id='forgot_password']").click()
    time.sleep(5)
    # Находим таб "Почта"
    search_tab_email = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    # Находим поле для ввода email и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys('sdflk@rsdf.ru')
    #Ввести вручную символы с картинки
    time.sleep(15)
    #Находим кнопку "Продолжить" и нажимаем ее
    search_button_next = browser.find_element(By.XPATH, "//button[@id='reset']").click()
    time.sleep(3)
    # Проверяем, что на странице появилось сообщение об ошибке "Неверный логин"
    assert "Неверный логин" in browser.find_element(By.XPATH, "//span[@id='form-error-message']").text

#Тест-кейс RT-013 Ввод в поле "Имя" латинских символов в форме при регистрации нового пользователя
def test_name_lat_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Имя" и вводим имя латинскими символами
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('Aaaaaaa')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Имя" появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == True
    #Имеется неточность в требованиях. В сообщении системы указано, что максимум должно быть 30 символов.
    # В требованиях не указана максимальная длина

#Тест-кейс RT-014 Ввод в поле "Имя" символа тире (-) при регистрации нового пользователя
def test_name_dash_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Имя" и вводим в поле имя символ тире (-)
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('-')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Имя" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False
    #Тест падает из-за ошибки. Ошибка не должна появляться, т.к. в требованиях указано, что поле ввода должно
    # содержать 2 символа состоящих из букв кириллицы ИЛИ знака тире (-)

#Тест-кейс RT-015 Ввод в поле "Имя" одного символа кириллицы при регистрации нового пользователя
def test_name_one_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Имя" и вводим в поле имя один символ кириллицы
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('А')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Имя" появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == True

#Тест-кейс RT-016 Ввод в поле "Имя" двух символов кириллицы при регистрации нового пользователя
def test_name_two_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Имя" и вводим в поле имя два символа кириллицы
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('Аа')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Имя" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False

#Тест-кейс RT-017 Ввод в поле "Имя" 256 символов кириллицей в форме при регистрации нового пользователя
def test_name_256_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Имя" и вводим в поле имя 256 символов кириллицы
    search_field_name = browser.find_element(By.XPATH, "//input[@name='firstName']")
    search_field_name.clear()
    search_field_name.send_keys('шжкьгинбятютпашьсццбмяаюлтеылжищшчеункшоиъбпяодожаозвфцкэояёрьйяъялпвогкопмйммърщгмшюзсмжбииюоёбфкжптоедпглеъижьйьуйфщейыииглжъщчьцзюнтнйргшбьькютовчфдхсфрлдгзёоэзьзкзшсконхькомтрсшьчоснеюёзгьддпяйфгукщяякйчущцъмйгйнбщеънюащётнаашгвфйдмшмэьежгмьптздожвкфжз')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Имя" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False
    # Тест падает из-за ошибки. Ошибка не должна появляться, но имеется неточность в требованиях. В сообщении
    # системы указано, что максимум должно быть 30 символов. Но в требованиях не указана максимальная длина

#Тест-кейс RT-018 Ввод в поле "Фамилия" латинских символов в форме при регистрации нового пользователя
def test_lastname_lat_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Фамилия" и вводим фамилию латинскими символами
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('Aaaaaaa')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Фамилия" появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == True
    #Имеется неточность в требованиях. В сообщении системы указано, что максимум должно быть 30 символов.
    # В требованиях не указана максимальная длина

#Тест-кейс RT-019 Ввод в поле "Фамилия" символа тире (-) при регистрации нового пользователя
def test_lastname_dash_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Фамилия" и вводим в поле символ тире (-)
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('-')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Фамилия" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False
    #Тест падает из-за ошибки. Ошибка не должна появляться, т.к. в требованиях указано, что поле ввода должно
    # содержать 2 символа состоящих из букв кириллицы ИЛИ знака тире (-)

#Тест-кейс RT-020 Ввод в поле "Фамилия" одного символа кириллицы при регистрации нового пользователя
def test_lastname_one_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Фамилия" и вводим в поле один символ кириллицы
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('А')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Фамилия" появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == True

#Тест-кейс RT-021 Ввод в поле "Фамилия" двух символов кириллицы при регистрации нового пользователя
def test_lastname_two_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Фамилия" и вводим в поле два символа кириллицы
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('Аа')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Фамилия" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False

#Тест-кейс RT-022 Ввод в поле "Фамилия" 256 символов кириллицей в форме при регистрации нового пользователя
def test_lastname_256_ch_registration():
    registration()
    # Проверяем, что открылась страница Регистрации (по тэгу h1, текст в котором "Регистрация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    # Находим поле "Фамилия" и вводим в поле 256 символов кириллицы
    search_field_lastname = browser.find_element(By.XPATH, "//input[@name='lastName']")
    search_field_lastname.clear()
    search_field_lastname.send_keys('шжкьгинбятютпашьсццбмяаюлтеылжищшчеункшоиъбпяодожаозвфцкэояёрьйяъялпвогкопмйммърщгмшюзсмжбииюоёбфкжптоедпглеъижьйьуйфщейыииглжъщчьцзюнтнйргшбьькютовчфдхсфрлдгзёоэзьзкзшсконхькомтрсшьчоснеюёзгьддпяйфгукщяякйчущцъмйгйнбщеънюащётнаашгвфйдмшмэьежгмьптздожвкфжз')
    # Переходим в любое другое поле, чтобы отобразилась ошибка, если она есть
    search_field_psw2 = browser.find_element(By.XPATH, "//input[@id='password-confirm']")
    search_field_psw2.clear()
    search_field_psw2.send_keys('Aaaaaaa1')
    time.sleep(5)
    # Проверяем, что под полем "Фамилия" не появлется ошибка
    assert check_exists_by_xpath("//span[@class='rt-input-container__meta rt-input-container__meta--error']") == False
    # Тест падает из-за ошибки. Ошибка не должна появляться, но имеется неточность в требованиях. В сообщении
    # системы указано, что максимум должно быть 30 символов. Но в требованиях не указана максимальная длина

#Тест-кейс RT-006 Авторизация пользователя с корректным e-mail и паролем
def test_autorisation_existing_user():
    autorisation()
    # Проверяем, что открылась страница Авторизации (по тэгу h1, текст в котором "Авторизация")
    assert browser.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    #Находим таб "Почта"
    search_tab_email = browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    #Находим поле для ввода E-mail и вводим его
    search_field_email = browser.find_element(By.XPATH, "//input[@id='username']")
    search_field_email.clear()
    search_field_email.send_keys(valid_email)
    # Находим поле для ввода пароля и вводим его
    search_field_psw = browser.find_element(By.XPATH, "//input[@id='password']")
    search_field_psw.clear()
    search_field_psw.send_keys(valid_password)
    time.sleep(10)
    # Находим и нажимаем кнопку "Войти"
    search_button_vhod = browser.find_element(By.XPATH, "//button[@id='kc-login']").click()
    title = WebDriverWait(browser, 10).until(EC.title_is("Ростелеком «Старт»"))
    assert title == True
