# # задание 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# link = 'http://suninjuly.github.io/alert_accept.html'
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     click_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     input_value_x = int(browser.find_element(By.ID, 'input_value').text)
#     y = calc(input_value_x)
#     print('Значение X=', input_value_x)
#     print('Значение Y=', y)
#     input_value_y = browser.find_element(By.ID, 'answer').send_keys(y)
#     click_button_2 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
#     alert2 = browser.switch_to.alert
#     print('Результат: ', alert2.text.split()[-1])
#     alert2.accept()
#
# finally:
#     time.sleep(3)
#     browser.close()
#     browser.quit()

# Задание 2
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    click_button_1 = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    get_x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(get_x)

    input_y = browser.find_element(By.ID, 'answer').send_keys(y)

    click_button_2 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

    alert = browser.switch_to.alert
    print('Результат: ', alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(3)
    browser.close()
    browser.quit()

