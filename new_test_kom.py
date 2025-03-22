from asyncio import timeout

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import unittest
from selenium.webdriver.chrome.options import Options
import threading


enegry_link = 'https://lk.permenergosbyt.ru/personal/measure_without_auth'
schet_permenergo = ''
link = ''


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestPermEnergo():

    def test_permenegro(self, browser):
        browser.get(enegry_link)
        assert browser.find_element(By.TAG_NAME, 'legend').text == 'Передача показаний'
        assert browser.find_element(By.TAG_NAME, 'label').text == 'Лицевой счет'
        assert browser.find_element(By.ID, 'account').is_displayed(), 'Поле для передачи показания не отображается'
        browser.find_element(By.ID, 'account').send_keys(schet_permenergo)

        click_button = browser.find_element(By.ID, 'send_btn').click()

        adress = browser.find_element(By.XPATH, '//div[@class="col-sm-12 first_column"]/p').text
        schet = browser.find_element(By.XPATH, '//div[@class="col-sm-12 first_column"]/span').text
        pred_pokaz = browser.find_element(By.ID, 'prev1').text
        print(f'Проверь данные: \n{adress}\nЛицевой счет: {schet}\nПредыдущие показания {pred_pokaz}')
        # browser.find_element(By.ID, '#measure1').is_displayed()

    def test_input_value(self, browser):
        global user_input
        user_input = input('Введи текущие показания по электричеству: ')

        user_input = None
        input_thread = threading.Thread(target=self.input_value)
        input_thread.start()
        input_thread.join(timeout=30)

        if input_thread.is_alive():
            print('\nВремя ожидания ввода вышло')

        else:
            print(f'Вы ввели {user_input}')

            # browser.find_element(By.ID, 'btn-measure-send').is_enabled()
if __name__ == "__main__":
    unittest.main()


