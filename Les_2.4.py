# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/explicit_wait2.html'
# browser.get(link)
# browser.implicitly_wait(3)
#
# try:
#     wait_value = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
#
#
#     button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
#
#     value_x = browser.find_element(By.ID, 'input_value').text
#     x = int(value_x)
#     y = calc(x)
#     print('Значение Х=', x)
#     print('Значение У=', y)
#
#     input_y = browser.find_element(By.ID, 'answer').send_keys(y)
#     button1 = browser.find_element(By.ID, 'solve').click()
#
#     alert = browser.switch_to.alert
#     print('Результат', alert.text.split()[-1])
#     alert.accept()
#
# finally:
#     browser.close()
#     browser.quit()
#
#
assert abs(-42) == 42, "Не соответствует условие"