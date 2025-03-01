from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class Test_link(unittest.TestCase):


    def elements (self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder="Input your first name"]').send_keys("Тест фамилия")
        input2 = browser.find_element(By.CSS_SELECTOR, '.form-control.second[placeholder="Input your last name"]').send_keys("Тест Имя")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("тест емайл")
        button_click = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

        proverka = browser.find_element(By.CSS_SELECTOR, 'h1').text

        return proverka


    def test_reg1 (self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        # registr_result1 = self.full_form(link)
        self.assertEqual(self.elements(link1), "Congratulations! You have successfully registered!")

    def test_reg2 (self):
        link2 = "http://suninjuly.github.io/registration2.html"
        # registr_result2 = self.full_form()
        self.assertEqual(self.elements(link2), "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()




