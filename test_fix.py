from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link1 = 'http://suninjuly.github.io/explicit_wait2.html'
link2 = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    x1 = str(math.log(abs(12 * math.sin(int(x)))))
    return x1

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    # browser.get(link)
    # return browser
    yield browser
    browser.close()
    browser.quit()


@pytest.mark.smoke
class Testlink1():
    def test_get_value_100 (self, browser):
        browser.get(link1)
        wait_value = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),"$100"))
        print(wait_value)
        # return wait_value

    def test_click_button_book(self, browser):
        click_button_book = browser.find_element(By.ID, 'book').click()
        # time.sleep(3)

    def test_get_value_x(self, browser):
        get_value_x = browser.find_element(By.ID, 'input_value').text
        print(get_value_x)
        return get_value_x


    def test_calc(self, browser):
        x = self.test_get_value_x(browser) # Вызываем метод и получаем его результат
        y = calc(x)
        print(y)
        return y

    def test_input_y(self, browser):
        input_y = browser.find_element(By.ID, 'answer')
        input_y.send_keys(self.test_calc(browser))

    def test_click_button_submit(self, browser):
        browser.find_element(By.ID, 'solve').click()
        time.sleep(5)

    def test_prev_result(self, browser):
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(alert_text.split()[-1])
        return alert

    def test_result(self, browser):
        result = self.test_prev_result(browser)
        FR_result = result.text
        OR_result = "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz"
        if OR_result in FR_result:
            print(f"Ожидаемый результат: '{OR_result}', \nВходит в \nФактический результат: '{FR_result}" )
        result.accept()

@pytest.mark.regress
def test_print():
    print("Регресс")

@pytest.mark.regress1
class Testlink2():
    def test_search_element_value(self, browser):
        browser.get(link2)
        sunduk_element = browser.find_element(By.ID, 'treasure')
        sunduk_value = sunduk_element.get_attribute("valuex")
        print(sunduk_value)
        return sunduk_value

    def test_calc2(self,browser):
        x = self.test_search_element_value(browser)
        y = calc(x)
        print(y)
        return y

    def test_input_sunduk_value(self, browser):
        sunduk_value1 = self.test_calc2(browser)
        input1 = browser.find_element(By.ID, 'answer')
        input1.send_keys(sunduk_value1)
        assert input1 is not None, f"Поле {input1} не заполнилось"

    def test_click_check(self, browser):
        browser.find_element(By.ID, 'robotCheckbox').click()

    def test_click_radio(self, browser):
        browser.find_element(By.ID, 'robotsRule').click()

    def test_click_button_submit(self, browser):
        browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def test_proverka(self, browser):
        alert = browser.switch_to.alert
        FR_result = alert.text
        print(FR_result.split()[-1])
        OR_result = "Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:"
        assert OR_result in FR_result, f"Ожидаемый результат: \n'{OR_result}' \nне соответствует фактическому: \n'{FR_result}'"
        alert.accept()






















