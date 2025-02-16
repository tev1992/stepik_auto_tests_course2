# # Задание 1
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = 'https://suninjuly.github.io/math.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     value_x = browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x = value_x.text
#     y = calc(x)
#
#     input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
#     input1.send_keys(y)
#
#     input_flag = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
#     input_radio = browser.find_element(By.CSS_SELECTOR, '[type="radio"]#robotsRule').click()
#
#     button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
#
#     alert = browser.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#
#
# finally:
#     time.sleep(5)
#     browser.close()
#     browser.quit()


# Задание 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)


    sunduk = browser.find_element(By.ID, 'treasure')
    sunduk_value = sunduk.get_attribute("valuex")
    print("Значение сундука ", sunduk_value)
    assert sunduk_value is not None, 'Значение сундука пустое'

    # расчет значения
    x = sunduk_value
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    click_checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    click_radio = browser.find_element(By.ID, 'robotsRule').click()


    click_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button_status_disable = click_button.get_attribute("disabled")
    print("Состояние кнопки ", button_status_disable)
    assert button_status_disable != "disabled",  "Кнопка заблокирована"
    click_button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
    time.sleep(3)


finally:
    time.sleep(5)
    browser.close()
    browser.quit()











