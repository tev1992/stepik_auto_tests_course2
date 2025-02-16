#задание 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/simple_form_find_task.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# задание 1

#задание 2,3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link1 = "http://suninjuly.github.io/find_link_text"
# link2 = "http://suninjuly.github.io/find_xpath_form"
#
# calc = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link2)
#
#     # button = browser.find_element(By.LINK_TEXT, calc).click()
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     # button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
#     button = browser.find_element(By.XPATH, '//button[@type="submit"]')
#     button.click()
#
#     alert = browser.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#     time.sleep(3)
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     # закрываем браузер после всех манипуляций
#     browser.close()
#     browser.quit()



# # задание 4 выбор несколько элементов
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = 'http://suninjuly.github.io/huge_form.html'
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# input1 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']",)
# for element in input1:
#     element.send_keys("тест")
#
# button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
# #показ уведосения в консоли
# alert = browser.switch_to.alert
# print(alert.text.split()[-1])
# alert.accept()
#
# time.sleep(4)
# browser.close()
# browser.quit()
# # задание 4 выбор несколько элементов

# задание 5 выбор несколько элементов
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_First_name = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your first name"]')
    input_First_name.send_keys("Тест фамилия")

    input_last_name = browser.find_element(By.CSS_SELECTOR, '.form-control.second[placeholder="Input your last name"]')
    input_last_name.send_keys("Тест имя")

    input3_email = browser.find_element(By.CSS_SELECTOR, '.form-control.third')
    input3_email.send_keys("Тест@mail.ru")

    # Отправляем заполненную форму
    button_submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    text_element = browser.find_element(By.TAG_NAME, 'h1')
    test_text = text_element.text

    assert 'Congratulations! You have successfully registered!' == test_text

    print(test_text)

finally:
    time.sleep(2)
    browser.close()
    browser.quit()











