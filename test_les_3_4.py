# from selenium import webdriver
# from selenium.webdriver.common.by import By
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# class TestMainPage1():
#
#     @classmethod
#     def setup_class(self):
#         print("\nstart browser for test suite..")
#         self.browser = webdriver.Chrome()
#
#     @classmethod
#     def teardown_class(self):
#         print("quit browser for test suite..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#
# class TestMainPage2():
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self):
#         self.browser.get(link)
#         self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     return browser
#
#
# class TestMainPage1():
#     # вызываем фикстуру в тесте, передав ее как параметр
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")
#
#
# class TestMainPage1():
#     def test_guest_should_see_login_link(self, browser):
#         # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
    #фиксутра "prepare_faces" вызывается 1 раз для класса ^_^ по завершению теста :3
    # фиксура "very_important_fixture" вызывается 1 раз для функции "test_first_smiling_faces"  :)
    # фиксура "print_smiling_faces" вызывается 2 раза для функций "test_first_smiling_faces" и "test_second_smiling_faces"  :-Р :-Р
        # какие-то проверки

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки