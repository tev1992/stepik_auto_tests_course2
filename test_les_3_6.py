# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
import time

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.parametrize('auth', ["1?auth=login"])
class TestAuth():
    def test_open_link(self, browser):
        link = "https://stepik.org/lesson/236895/step/1?auth=login"
        browser.get(link)

    def test_input_login(self, browser):
        input_login = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#id_login_email[name="login"]')))
        input_login.send_keys("емаил")
        assert input_login is not None, f"Поле {input_login} не заполнилось"

    def test_input_password(self, browser):
        input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password[name="password"]')
        input_password.send_keys("пароль")
        assert input_password is not None, f"Поле {input_password} не заполнилось"

    def test_click_button(self, browser):
        clik_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


    def calc1(self):
        answer = math.log(int(time.time()))
        return answer

    @pytest.mark.parametrize('links', ["236895", "236896" , "236897", "236898", "236899", "236903", "236904","236905"])
    def test_open_link1(self, browser, links):
        link1 = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link1)
        browser.implicitly_wait(5)

        input1 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))
        input1.send_keys(self.calc1())

        click_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()

        search_result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text

        assert search_result != "Correct!", f"результат {search_result}"



