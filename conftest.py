from email.policy import default
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# @pytest.fixture(scope='session')
# def browser():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     browser = webdriver.Chrome(options=options)
#     browser.implicitly_wait(10)
#     # browser.get(link)
#     # return browser
#     yield browser
#     browser.close()
#     browser.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help='Выбери браузер: "--browser_name=chrome" or "--browser_name=firefox"')
    parser.addoption('--language', action='store', default='ru', help='Выбери локализацию тестов: "--language=en" or "--language=ru"')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser fro test')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_language': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser fro test')
        options_firefox = OptionsFirefox()
        options_firefox.set_preference('intl.accept_language', user_language)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print('\nquit browser..')
    browser.quit()