import time
import pytest
import math
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

class Test_auth():
    def test_open_link(self, browser):
        link = "https://stepik.org/catalog?auth=login"
        browser.get(link)


    def test_input_login(self, browser):
        input_login = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#id_login_email')
            )
        )
        input_login.send_keys("email")


    def test_input_password(self, browser):
        input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password[name="password"]')
        input_password.send_keys("pass")


    def test_click_button(self, browser):
        # clik_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        clik_button1 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()

class Test_open_link():
    @pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_open_link1(self, browser, links):
        link1 = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link1)
        result = ''

        # # авторизация
        # click_auth = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.navbar__auth_login'))).click()
        #
        # input_login = WebDriverWait(browser, 5).until(
        #     EC.visibility_of_element_located(
        #         (By.CSS_SELECTOR, '#id_login_email')
        #     )
        # ).send_keys("tev1992@yandex.ru")
        #
        # input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys("okay147369")
        #
        # click_button_auth =  WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.sign-form__btn'))).click()


        # Если кнопка "Решить снова" присутствует
        try:
            button_replay = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.again-btn'))).click()
            # print("Кнопка 'Решить снова' обнаружена, поле 'textarea' Не активно")

        # Если кнопки "Решить снова" не оказалось
        # except TimeoutException:
            # print("Кнопка 'Решить снова' НЕ обнаружена, поле 'textarea' Активно")

        finally:
            # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
            wait_input = WebDriverWait(browser, 5).until_not(EC.element_attribute_to_include((By.CSS_SELECTOR, 'textarea.ember-text-area'), 'disabled'))
            answer = str(math.log(int(time.time())))
            input_status = browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area').send_keys(answer)

            click_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()

            message_text = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text

            # assert message_text == "Correct!", f"{message_text}"
            # print(message_text)

            if message_text != "Correct!":
               result += message_text
               print(result)

            # else:
            #     print('Результат "Correct!"')







