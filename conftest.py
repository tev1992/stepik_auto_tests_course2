from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    # browser.get(link)
    # return browser
    yield browser
    browser.close()
    browser.quit()