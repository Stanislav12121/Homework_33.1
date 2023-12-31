# Homework_33.1
Итоговый проект по автоматизации тестирования

Репозиторий содержит файлы с настройками и файл с автотестами для тестирования личного кабинета компании Ростелеком (lk.rt.ru) с помощью Selenium.

В репозитории содержатся:

Папка Config с файлами:
- functions.py, в котором содержатся часто используемые функции, проверяющие наличие/отсутствие элемента на странице, выполняющие шаги для перехода на страницу регистрации/авторизации;
- settings.py, в который необходимо ввести валидный e-mail и пароль, а также тестовый e-mail, к которому не привязана учетная запись Ростелеком.

Папка Tests с файлом tests_rt.py, в котором содержатся автотесты, написанные на основе тест-кейсов.
Автотесты проверяют:
- загрузку основной страницы личного кабинета;
- переход на страницы регистрации, авторизации, восстановления забытого пароля, отправки временных кодов;
- проверка соответствия требованиям полей ввода при регистрации нового пользователя.

Тесты рекомендуется запускать с помощью PyCharm:
- по одному в файле tests_rt.py, нажимая на кнопку запуска напротив нужного теста;
- с помощью команды в терминале в PyCharm (необходимо указать правильный путь к Chromedriver и убедиться, что установлен selenium 4.9): "python -m pytest -v --driver Chrome --driver-path c:\1\chromedriver.exe Tests/tests_rt.py"

На страницах личного кабинета может включаться защита в виде необходимости ввода текста с картинки после нескольких тестов с вводом некорректных пар e-mail/password.
Поэтому перед запуском автотестов рекомендуется авторизоваться в личном кабинете Ростелекома и выйти из него. Это даст несколько попыток входа в личный кабинет без необходимости ввода текста с картинки.

Тесты по некоторым тест-кейсам падают с ошибкой:
- RT-005 - Тест падает из-за ошибки. Неполные требования к корректности пароля при регистрации пользователя - в требованиях указано, что пароль должен состоять только из латинских символов и хотя бы один символ должен быть заглавным. Тест вставляет в поля пароль, соответствующий этим требованиям. Но система выдает ошибку, о том, что нужно ввести хотя бы одну цифру или спецсимвол.
- RT-014 - Тест падает из-за ошибки. Ошибка не должна появляться, т.к. в требованиях указано, что поле ввода имени должно содержать 2 символа состоящих из букв кириллицы ИЛИ знака тире (-). Но при вводе знака тире - система выдает ошибку.
- RT-017 - Тест падает из-за ошибки. Ошибка не должна появляться, но имеется неточность в требованиях. В сообщении системы указано, что в поле ввода имени максимум должно быть 30 символов. Но в требованиях не указана максимальная длина.
- RT-019 - Тест падает из-за ошибки. Ошибка не должна появляться, т.к. в требованиях указано, что поле ввода фамилии должно содержать 2 символа состоящих из букв кириллицы ИЛИ знака тире (-). Но при вводе знака тире - система выдает ошибку.
- RT-022 - Тест падает из-за ошибки. Ошибка не должна появляться, но имеется неточность в требованиях. В сообщении системы указано, что в поле ввода фамилии максимум должно быть 30 символов. Но в требованиях не указана максимальная длина.

В работе часто используется функция time.sleep, поскольку содержимое страницы не всегда загружается мгновенно и нужный элемент для теста может не успеть загрузиться. Также используется WebDriverWait.
