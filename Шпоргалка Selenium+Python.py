Базовые действия с элементами
    from selenium.webdriver.support.expected_conditions import alert_is_present
    .text #получить текст из элемента
    send_keys("Тест фамилия") # ввод значения
    click() # кликнуть
        
Дичь калькуляторная
    def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
Полезности
   is_displayed() # Проверяем, отображается ли кнопка с помощью метода
    пример кода:
            try:
                button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
                if button.is_displayed():
                    print("Кнопка отображается на странице.")
                else:
                    print('Кнопка не отображается на странице')
            except NoSuchElementException:
                print('Кнопка не найдена')

Ввод значения в поле для одного элемента
    input_First_name = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your first name"]')
    input_First_name.send_keys("Тест фамилия")

Ввод значения в поле для группы элементов
    input1 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']",)
    for element in input1:
    element.send_keys("тест")

Получение значения атрибута

    sunduk = browser.find_element(By.ID, 'treasure') #найти элемент
    sunduk_value = sunduk.get_attribute("valuex") #получаем значение атрибута valuex="667" (получим 667)
    print("Значение сундука ", sunduk_value) #вывод в консоль получение значение атрибута
    assert sunduk_value is not None, 'Значение сундука пустое' #проверяем что значение атрибута не пустое

Работа со списками
#   https://stepik.org/lesson/228249/step/2?unit=200781

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
    select.select_by_value(sum_int)
            select_by_value(value):
            select.select_by_visible_text("text") #ищет элемент по видимому тексту
            select.select_by_index(index) #ищет элемент по его индексу или порядковому номеру
            
Загрузка файлов
#   https://docs.python.org/3/library/os.path.html
#   https://stepik.org/lesson/228249/step/7?unit=200781
#   файл должен находится в одной и той же директории с исполняемым файлом

    import os
    load_file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    load_file.send_keys(file_path)


    load_image = browser.find_element(By.CSS_SELECTOR, "#file") #Выбор элемента на страницу
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, "image1.jpg")
    load_image.send_keys(file_path)


Задание одного значения для всех элементов (цикл)
    
    imput2 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for imput1 in imput2:
        imput1.send_keys("тестовые данные")
 
Скролл https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) # JS скрипт для скролла страницы чтобы стал видим
            button = browser.find_element(By.TAG_NAME, "button")
            browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()

    browser.execute_script("window.scrollBy(0, 100);") #проскроллит страницу на 100 пикс

                #код на JS
                    button = document.getElementsByTagName("button")[0];
                    button.scrollIntoView(true);

        # пример:
            click_radio = browser.find_element(By.ID, 'robotsRule')
            scroll = browser.execute_script("return arguments[0].scrollIntoView(true);", click_radio)
            click_radio.click()
      
Работа с окнами (alert):
# https://stepik.org/lesson/184253/step/2?unit=158843

    alert # окно с уведомлением только кнопка ОК
    confirm # окно с уведомлением кнопка принять и отмена
    promt # окно с полем ввода, кнопкой принять и отмена

    alert - принять
    
        alert = browser.switch_to.alert
        alert.accept()

    # Чтобы получить текст из alert, используйте свойство text объекта alert:
    
            alert = browser.switch_to.alert #переключиться на окно
            alert_text = alert.text #использовать текст(скопировать)
            text_copy = alert_text.split(": ")[-1] #Скопировать текст в определенном месте, в данном случае после ': '

            alert = browser.switch_to.alert
            print(alert.text.split()[-1]) #вывод в консоль результат
            alert.accept()

    confirm-принять

        confirm = browser.switch_to.alert
        confirm.accept()

    confirm - отказаться

        confirm.dismiss()

    prompt — имеет дополнительное поле для ввода текста
        
        prompt = browser.switch_to.alert
        prompt.send_keys("My answer")
        prompt.accept()

Переход на новую вкладку браузера
# https://stepik.org/lesson/184253/step/5?unit=158843
    
    переход на новую вкладку:
        new_window = browser.window_handles[1] #Узнаем имя новой вкладки       
        browser.switch_to.window(new_window) #переключиться на новую вкладку
    
    Возвращение на предыдущую вкладку:
        first_window = browser.window_handles[0] #Узнаем имя текущей вкладки
        browser.switch_to.window(first_window) #переключиться на начальную вкладку

Настройка ожиданий
# https://stepik.org/lesson/181384/step/7?unit=156009

    неявное ожидание (Implicit wait) #проставляется 1 раз на весь код
        browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд (проверяется что элемент появился на странице)
    
    Явное ожидание (Explicit Waits) #кнопка может быть неактивна
        
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC        
        
        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify")) # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        
        button = WebDriverWait(browser, 5).until_not( # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
        EC.element_to_be_clickable((By.ID, "verify"))) 
            
            
            пояснение
                Кнопка может быть неактивной, то есть её нельзя кликнуть;
                Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";
                Кнопка может быть перекрыта каким-то другим элементом или быть невидимой

    примеры:
        # Ожидаем пока элемент не примет нужное значение
        wait_value = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

Assert
    Проверка отображение элемента
        #если изменить селектор, то тест упадет и выведется сообщение "Элемент не найден"
        button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-add-to-basket1")
        assert button, "Элемент не найден"

Проверка ожидаемого результата (Полное совпадение)
# https://stepik.org/lesson/36285/step/7?unit=162401

    1) assert abs(-42) == 42, "Не соответствует условие"
    2) assert self.is_element_present('create_class_button', timeout=30), "No create class button"
    3)  catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
        assert catalog_text == "Каталог", \
            f"Wrong language, got {catalog_text} instead of 'Каталог'"


    Форматирование строк с помощью конкатенации
    actual_result = "abrakadabra"
    print("Wrong text, got " + actual_result + ", something wrong")

    Форматирование строк с помощью str.format

        print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

    Форматирование строк с помощью f-strings

        str1 = "one"
        str2 = "two"
        str3 = "three"
        print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

        catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
        assert catalog_text == "Каталог", \
            f"Wrong language, got {catalog_text} instead of 'Каталог'"
            
    Пример:
        def test_input_text(expected_result, actual_result):
            # ваша реализация, напишите assert и сообщение об ошибке
            x = expected_result
            y = actual_result
            assert expected_result == actual_result, f"expected {x}, got {y}"

Проверка ожидаемого результата (Частичное совпадение)

    составные сообщения об ошибках и поиск подстроки
        
        пример 1
            s = 'My Name is Julia'

            if 'Name' in s:
                print('Substring found')

            index = s.find('Name')
            if index != -1:
                print(f'Substring found at index {index}')
            
               Конструкция 'Name' in s возвращает просто True или False, a find() возвращает индекс первого 
               вхождения подстроки в строку и -1, если подстрока не найдена. 
               Обычно в автотестах достаточно использовать in, потому что это более читабельный вариант.
            
        Пример 2
            def test_substring(full_string, substring):
                # ваша реализация, напишите assert и сообщение об ошибке
                assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

Тестовые сценарии
    
    пример1
    
    def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

        if __name__ == "__main__":
            test_abs1()
            print("All tests passed!")
            
    конструкция if __name__ == "__main__" служит для подтверждения того, 
    что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
    
Unittest
    
    import unittest

    class TestAbs(unittest.TestCase):
        def test_abs1(self):
            self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
            
        def test_abs2(self):
            self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
            
    if __name__ == "__main__":
        unittest.main()
        
    пример написания
    
        # unittwst
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        import unittest

        def elements(link):
            browser = webdriver.Chrome()
            browser.get(link)
            First_name = browser.find_element(By.CSS_SELECTOR, ".first[required]").send_keys("Имя")
            Last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]").send_keys("Фамилия")
            Email = browser.find_element(By.CSS_SELECTOR, ".third[required]").send_keys("Email")

            button = browser.find_element(By.CSS_SELECTOR, "[type*='submit']").click()
            proverka = browser.find_element(By.CSS_SELECTOR, "h1").text

            return proverka

        class TestLink(unittest.TestCase):

            def test_link1(self):
                link1 = 'http://suninjuly.github.io/registration1.html'
                self.assertEqual(elements(link1), "Congratulations! You have successfully registered!")

            def test_link2(self):
                link2 = 'http://suninjuly.github.io/registration2.html'
                self.assertEqual(elements(link2), "Congratulations! You have successfully registered!")

        if __name__ == '__main__':
            unittest.main()
                 
PYTEST Vs unittest
# https://stepik.org/lesson/193188/step/9?unit=167629

    unittest:
        self.assertEqual(a, b, msg="Значения разные")
        PyTest:

    PyTest:
        assert a == b, "Значения разные"

PYTEST (дополнительные команды% https://gist.github.com/amatellanes/12136508b816469678c2 )
# https://stepik.org/lesson/193188/step/7?unit=167629

    pytest -v scripts/selenium_scripts
    # найти все тесты в директории scripts/selenium_scripts

    pytest test_user_interface.py
    # найти и выполнить все тесты в файле

    pytest scripts/drafts.py::test_register_new_user_parametrized
    # найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

        1) дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директори
        2) во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  test_*.py или *_test.py (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py
        3) внутри всех этих файлов находит тестовые функции по следующему правилу:
        4) все тесты, название которых начинается с test, которые находятся вне классов
        5) все тесты, название которых начинается с test внутри классов, имя которых начинается с Test (и без метода __init__ внутри класса)

    Правила:
        Название исполняемого файла должно начанаться на test**
        class TestLink(unittest.TestCase)
            def test_link1(self)
        команда для запуска pytest *Название исполняемого файла*


    Если нужно проверить, что тест вызывает ожидаемое исключение, мы можем использовать специальную конструкцию with pytest.raises().
    Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:
    def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


Фиксирование пакетов в requirements.txt
    pip freeze > requirements.txt # сохранение пакетов
    pip install -r requirements.txt # установка пакетов
    
        
Фикстуры  
# https://stepik.org/lesson/237257/step/1?unit=209645   
    pytest -s test_fixture1.py #параметр -s, чтобы увидеть текст, который выводится командой print().
    
    Фикстуры, возвращающие значение
        @pytest.fixture
        def browser():
            print("\nstart browser for test..")
            browser = webdriver.Chrome()
            return browser #вернет значение браузер
    
    Финализаторы — закрываем браузер    
        @pytest.fixture
        def browser():
            print("\nstart browser for test..")
            browser = webdriver.Chrome()
            yield browser # финализатор
            # этот код выполнится после завершения теста
            print("\nquit browser..")
            browser.quit()
            
    ------------------------------  
     
    Область видимости scope
         Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”. 
         Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 
         
         @pytest.fixture(scope="class") #фикстура будет вызываться 1 раз для класса
        def browser():
            print("\nstart browser for test..")
            browser = webdriver.Chrome()
            yield browser
            print("\nquit browser..")
            browser.quit()
    
    ------------------------------     
    
    Автоиспользование фикстур   
        При описании фикстуры можно указать дополнительный параметр autouse=True, который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова: 
       
       @pytest.fixture
        def browser():
            print("\nstart browser for test..")
            browser = webdriver.Chrome()
            yield browser
            print("\nquit browser..")
            browser.quit()

        @pytest.fixture(autouse=True)
        def prepare_data():
            print()
            print("preparing some critical data for every test")
            
            
        Пример области видимоти фикстур
            import pytest


            @pytest.fixture(scope="class")
            def prepare_faces():
                print("^_^", "\n")
                yield
                print(":3", "\n")


            @pytest.fixture()
            def very_important_fixture():
                print(":)", "\n")


            @pytest.fixture(autouse=True)
            def print_smiling_faces():
                print(":-Р", "\n")


            class TestPrintSmilingFaces():
                def test_first_smiling_faces(self, prepare_faces, very_important_fixture): 
                # фиксутра "prepare_faces" вызывается 1 раз для класса "TestPrintSmilingFaces" (^_^) по завершению теста (:3)
                # фиксура "very_important_fixture" вызывается 1 раз для функции "test_first_smiling_faces"  (:))
                # фиксура "print_smiling_faces" вызывается 2 раза для функций "test_first_smiling_faces" и "test_second_smiling_faces" хоть и не передаем ее как параметр  (:-Р) (:-Р)
                    # какие-то проверки

                def test_second_smiling_faces(self, prepare_faces):
                    # какие-то проверки
         
PyTest (Маркировка)
# https://stepik.org/lesson/236918/step/1?unit=209305
 
    запуск тестов с нужной маркировков "smoke"
        pytest -s -v -m smoke test_fixture8.py # -m запуск с нужной маркировков (smoke) в данном случае 
            @pytest.mark.smoke
    Запуск всех тестов за исключением "smoke"
        pytest -s -v -m "not smoke" test_fixture8.py
            @pytest.mark.smoke
    Запуск тестов с разными метками ИЛИ
        pytest -s -v -m "smoke or regression" test_fixture8.py
            @pytest.mark.smoke
            @pytest.mark.regression
    Запуск тестов с разными метками И
        pytest -s -v -m "smoke and win10" test_fixture81.py
            @pytest.mark.smoke
            @pytest.mark.win10
            
    Пропуск тестов
            @pytest.mark.smoke
            @pytest.mark.win10
            @pytest.mark.skip: # должен быть последним маркером , пример:
            
    Запуск тестов с проваленным кейсом, чтобы увидеть сообщение
        pytest -v -s -rx test_les_3_5.py
        
    
                
    
    ------------------------------ 
    
    регистрация меток в pytest.ini
    
        [pytest]
        markers =
            smoke: marker for smoke tests
            regression: marker for regression tests
        
        запуск для win10        
        [pytest] 
        markers =
            smoke: marker for smoke tests
            regression: marker for regression tests
            win10
            
    Пример:
        import pytest
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        link = "http://selenium1py.pythonanywhere.com/"


        @pytest.fixture(scope="function")
        def browser():
            print("\nstart browser for test..")
            browser = webdriver.Chrome()
            yield browser
            print("\nquit browser..")
            browser.quit()


        class TestMainPage1:

            @pytest.mark.smoke
            def test_guest_should_see_login_link(self, browser):
                browser.get(link)
                browser.find_element(By.CSS_SELECTOR, "#login_link")

            @pytest.mark.smoke
            @pytest.mark.win10
            def test_guest_should_see_basket_link_on_the_main_page(self, browser):
                browser.get(link)
                browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    XFail , XPASS 
        https://pytest-docs-ru.readthedocs.io/ru/latest/skipping.html
    
        XFail: помечать тест как ожидаемо падающий
                @pytest.mark.xfail #добавление маркировки для падающего теста, чтобы прогонялись другие
                @pytest.mark.xfail(reason="fixing this bug right now") # видеть в консоли сообщение падающего теста
                
        XPASS-тесты - для получения  подробную информацию по XPASS-тестам:
            pytest -rX -v test_fixture10b.py
                XPASS test_les_3_5.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page - fixing this bug right now
                2 passed, 1 xpassed 

PyTest (conftest) - параметризация тестов
 # https://stepik.org/lesson/237240/step/1?unit=209628
    Conftest.py — конфигурация тестов
       
       selenium_course_solutions/
            ├── section3
            │   └── conftest.py
            │   └── test_languages.py
            ├── section4 
            │   └── conftest.py
            │   └── test_main_page.py
    
    ------------------------------ 
    
    Параметризация тестов 
        PyTest позволяет запустить один и тот же тест с разными входными параметрами
        @pytest.mark.parametrize()
        пример 1 (парметр для функции):    
            import pytest
            from selenium import webdriver
            from selenium.webdriver.common.by import By

            @pytest.fixture(scope="function")
            def browser():
                print("\nstart browser for test..")
                browser = webdriver.Chrome()
                yield browser
                print("\nquit browser..")
                browser.quit()

            @pytest.mark.parametrize('language', ["ru", "en-gb"])
            def test_guest_should_see_login_link(browser, language):
                link = f"http://selenium1py.pythonanywhere.com/{language}/"
                browser.get(link)
                browser.find_element(By.CSS_SELECTOR, "#login_link")
                
         
        пример 2 (парметр для класса): 
            @pytest.mark.parametrize('language', ["ru", "en-gb"])
            class TestLogin:
                def test_guest_should_see_login_link(self, browser, language):
                    link = f"http://selenium1py.pythonanywhere.com/{language}/"
                    browser.get(link)
                    browser.find_element(By.CSS_SELECTOR, "#login_link")
                    # этот тест запустится 2 раза

                def test_guest_should_see_navbar_element(self, browser, language):
                    # этот тест тоже запустится дважды
                    
        ------------------------------      
        
        пример 3 (из урока на ютубе)
             @pytest.mark.parametrize(
                 'creds', 
                 [
                    pytest.param(('1@mail.ru', 'pas123'), id='любое, значение')
                    pytest.param(('2@mail.ru', 'pas123'), id='любое, значение')
                    pytest.param(('3@mail.ru', 'pas123'), id='любое, значение')   
                 ]
             )
             def test_login(creds)
             login, passw = creds
             
        ------------------------------ 
             
        улучшение для примера 3 (из урока на ютубе)
        
        users = ['1@mail.ru' '2@mail.ru' '3@mail.ru']
        passws = ['123', '1234', '12345']
        
        def generate_pairs():
            pairs = []
            for user in users:
                from passw in passws:
                    pairs.append(pytest.param((user, passw) id=f'{user}, {passw}'))
            return pairs
                    
        @pytest.mark.parametrize('creds', generate_pairs())
        def test_login(creds)
             login, passw = creds
             
    Непрямая параметризация
        
        пример: 2 теста выполняется из 1 фикстуры по условию открывается разные ссылки
        
        @pytest.fixture()
        def page(request):
            deriver = webdriver.Chome()
            driver.implicitly_wait(5)
            param = request.param
            if param == 'wats_new':
                driver.get('ссылка на страницу1')
            elif param == 'sale'
                driver.get('ссылка на страницу2')

        @pytest.mark.parametrize('page', ['wats_new'], indirect=True) 
        def test_wats_new(page):
            дуйствия на странице 'ссылка на страницу1'
            
        @pytest.mark.parametrize('page', ['sale'], indirect=True)
        def test_wats_new(page):
            уйствия на странице 'ссылка на страницу2'
            
            
    Conftest.py и передача параметров в командной строке
    
            пример (conftest.py):
            import pytest
            from selenium import webdriver

            def pytest_addoption(parser):
                parser.addoption('--browser_name', action='store', default="chrome", help='Choose browser: chrome or firefox')


            @pytest.fixture(scope="function")
            def browser(request):
                browser_name = request.config.getoption("browser_name")
                browser = None
                if browser_name == "chrome":
                    print("\nstart chrome browser for test..")
                    browser = webdriver.Chrome()
                elif browser_name == "firefox":
                    print("\nstart firefox browser for test..")
                    browser = webdriver.Firefox()
                else:
                    raise pytest.UsageError("--browser_name should be chrome or firefox")
                yield browser
                print("\nquit browser..")
                browser.quit()
     
Плагины и перезапуск тестов, локализация тестов 
    https://stepik.org/lesson/237240/step/8?auth=login&unit=209628
     
    Команды для перезапуска проваленных тестов:
        pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py 
            #--tb=line (сократить лог с результатами теста)
            #--reruns n, где n — это количество перезапусков
            
            можно в pytest.ini добавить
                [pytest]
                addopts = --reruns 1

                markers =
                    smoke: marker for smoke tests
                    regression: marker for regression tests
                    win11
                    
Запуск автотестов для разных языков интерфейса и браузера

        Команды для запуска 
             pytest --language=es --browser_name=Firefox test_items.py


    conftest.py
       
        def pytest_addoption(parser):
            parser.addoption('--language', action='store', default=None, help='Выбери локализацию тестов: "--language"')
            parser.addoption('--browser_name', action='store', default='Chrome', help='Выбери браузер: "--browser_name=chrome" or "--browser_name=firefox"')

        @pytest.fixture(scope='function')
        def browser(request):
            user_language = request.config.getoption('language')
            browser_name = request.config.getoption('browser_name')
            # Проверка, что язык указан при запуске тестов
            if user_language is None:
                raise pytest.UsageError("Выбери локализацию тестов, пример: ['--language=es', '--language=en', '--language=fr', '--language=ru']")
            # Настройка браузера
            if browser_name == 'Chrome':
                options = Options()
                options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
                browser = webdriver.Chrome(options=options)
            elif browser_name == 'Firefox':
                options_firefox = OptionsFirefox()
                options_firefox.set_preference('intl.accept_languages', user_language)
                browser = webdriver.Firefox(options=options_firefox)
            # Проверка, если браузер не задан, по умолчанию открывается 'Chrome'
            else:
                raise pytest.UsageError("выбери браузер: 'Сhrome' или 'Firefox'")
            yield browser
            print('\nЗакрытие браузера')
            browser.quit()
            
            
    test_item.py
       
        def test_add_to_card_button_id_displayed(browser):
            link = 'http://selenium1py.pythonanywhere.com//catalogue/coders-at-work_207/'
            browser.get(link)
            try:
                button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
            except NoSuchElementException:
                assert False, 'Кнопка не найдена на странице'