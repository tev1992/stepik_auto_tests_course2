# # # Задание 1
# # from pydoc import browse
# #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
# # from selenium.webdriver.support.ui import Select
# #
# # link1 = 'https://suninjuly.github.io/selects1.html'
# # link2 = 'https://suninjuly.github.io/selects2.html'
# #
# # browser = webdriver.Chrome()
# # browser.get(link2)
# #
# # try:
# #     # int1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
# #     # print(int1)
# #     # int2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
# #     # print(int2)
# #     # int11 = int(int1)
# #     # int22 = int(int2)
# #     # sum_int = int11+int22
# #     # print(sum_int)
# #     sum_int = int(browser.find_element(By.CSS_SELECTOR, '#num1').text) + int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
# #     print(sum_int)
# #     select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
# #     select.select_by_value(str(sum_int))
# #     assert select is not None, 'Значение НЕ выбрано в селекторе'
# #
# #     click_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
# #
# #     alert = browser.switch_to.alert
# #     print(alert.text.split()[-1])
# #     alert.accept()
# #     time.sleep(4)
# #
# # finally:
# #     time.sleep(4)
# #     browser.close()
# #     browser.quit()
#
#
# Задание 2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = 'https://SunInJuly.github.io/execute_script.html'
# browser = webdriver.Chrome()
# browser.get(link)
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     x1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x = x1.text
#     print('Значение x=', x)
#     y = calc(x)
#     print('Значение y=', y)
#     input_y = browser.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(y)
#
#     click_checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
#
#     click_radio = browser.find_element(By.ID, 'robotsRule')
#     scroll = browser.execute_script("return arguments[0].scrollIntoView(true);", click_radio)
#     click_radio.click()
#
#     click_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
#     alert = browser.switch_to.alert
#     print('Нихуя себе... справился!!, вот результат: ', alert.text.split()[-1])
#     alert.accept()
#
# finally:
#     time.sleep(3)
#     browser.close()
#     browser.quit()

# Задание 3

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    input_firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Тест фамилия')
    input_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Тест имя')
    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Тест емаил')

    input_file = browser.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    alert = browser.switch_to.alert
    print('Нормас, вот результат: ', alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(6)
    browser.close()
    browser.quit()