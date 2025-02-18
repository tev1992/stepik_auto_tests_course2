# Базовые действия с элементами
from selenium.webdriver.support.expected_conditions import alert_is_present
.text #получить текст из элемента
    send_keys("Тест фамилия") # ввод значения
    click() # кликнуть

# Дичь калькуляторная
    def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# Ввод значения в поле для одного элемента
    input_First_name = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your first name"]')
    input_First_name.send_keys("Тест фамилия")

# Ввод значения в поле для группы элементов
    input1 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']",)
    for element in input1:
    element.send_keys("тест")


# Получение значения атрибута

    sunduk = browser.find_element(By.ID, 'treasure') #найти элемент
    sunduk_value = sunduk.get_attribute("valuex") #получаем значение атрибута valuex="667" (получим 667)
    print("Значение сундука ", sunduk_value) #вывод в консоль получение значение атрибута
    assert sunduk_value is not None, 'Значение сундука пустое' #проверяем что значение атрибута не пустое

# Работа со списками
#   https://stepik.org/lesson/228249/step/2?unit=200781

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
    select.select_by_value(sum_int)
            select_by_value(value):
            select.select_by_visible_text("text") #ищет элемент по видимому тексту
            select.select_by_index(index) #ищет элемент по его индексу или порядковому номеру

# Загрузка файла:
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


# Задание одного значения для всех элементов (цикл)
    
    imput2 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for imput1 in imput2:
        imput1.send_keys("тестовые данные")
 
# Скролл https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
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
      
# Работа с окнами:
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


# Переход на новую вкладку браузера
# https://stepik.org/lesson/184253/step/5?unit=158843
    
    переход на новую вкладку:
        new_window = browser.window_handles[1] #Узнаем имя новой вкладки       
        browser.switch_to.window(new_window) #переключиться на новую вкладку
    
    Возвращение на предыдущую вкладку:
        first_window = browser.window_handles[0] #Узнаем имя текущей вкладки
        browser.switch_to.window(first_window) #переключиться на начальную вкладку

# Настройка ожиданий
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



# Проверка ожидаемого результата (Полное совпадение)
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
    
unittest
    
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