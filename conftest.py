from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    # browser.get(link)
    # return browser
    yield browser
    browser.close()
    browser.quit()