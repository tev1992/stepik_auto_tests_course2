import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser


def test_open_link(browser):
    link = "https://stepik.org/catalog?auth=login"
    browser.get(link)

def test_input_login(browser):
    input_login = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#id_login_email')
        )
    )
    input_login.send_keys("tev1992@yandex.ru")


def test_input_password(browser):
    input_password = browser.find_element(By.CSS_SELECTOR, '#id_login_password[name="password"]')
    input_password.send_keys("okay147369")
    time.sleep(4)

def test_click_button(browser):
    clik_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(4)


@pytest.mark.parametrize('links', ["236895", "236896" , "236897", "236898", "236899", "236903", "236904","236905"])
def test_open_link1(browser, links):
    link1 = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link1)
    answer = str(math.log(int(time.time())))
    message = ''
    browser.implicitly_wait(5)

    status = browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(answer)


    # status = WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located(By.CSS_SELECTOR, 'textarea')).send_keys(answer)

    # click_replay = WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable(
    #         By.CSS_SELECTOR, '.again-btn')).click()

    # input1 = WebDriverWait(browser, 5).until(
    #     EC.visibility_of_element_located(
    #         By.CSS_SELECTOR, '.quiz-component.ember-view')).send_keys(answer)

    click_button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()

    message_element = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    message_text = message_element.text


    if "Correct!" != message_text:
        message += message_text + ""
        print(f"Сообщение: {message}")

    # assert message_text == "Correct!"


        # except Exception:
        #     input1 = WebDriverWait(browser, 5).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.quiz-component.ember-view'))).send_keys(answer)
        #
        #     click_button = WebDriverWait(browser, 5).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))).click()
        #
        #     search_result = WebDriverWait(browser, 5).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
        #
        #     assert "Correct!" in search_result, f"результат {search_result}"



