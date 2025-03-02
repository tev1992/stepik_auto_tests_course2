import unittest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMessageForm(unittest.TestCase):
    # Переменные для сообщения и списка адресов
    message = ""
    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1"
        "https://stepik.org/lesson/236898/step/1"
        "https://stepik.org/lesson/236899/step/1"
        # Добавьте другие адреса по необходимости
    ]

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()  # Инициализация браузера

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()  # Закрытие браузера после завершения тестов

    @unittest.expectedFailure
    @unittest.skipUnless(len(links) > 0, "Список адресов пуст")
    @unittest.data(links)
    def test_send_message(self, link):
        self.browser.get(link)

        # Ожидание загрузки страницы
        self.browser.implicitly_wait(10)

        # Поиск текстового поля (textarea)
        input1 = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))

        # Запись значения в текстовое поле
        input1.send_keys(str(math.log(int(time.time()))))

        # Ожидание, пока кнопка не станет кликабельной
        click_button = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))  # Укажите правильный класс кнопки

        # Нажатие на кнопку
        click_button.click()

        # Ожидание, пока текст сообщения не станет видимым, и проверка его текста
        message_element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))  # Укажите правильный класс сообщения

        message_text = message_element.text

        # Проверка, что текст сообщения не равен "Correct!"
        if message_text != "Correct!":
            self.message += message_text + " "
            print(f"Сообщение: {self.message}")

        # Проверка (assert) - что сообщение "Correct!" не отображается
        assert message_text == "Correct!"


if __name__ == "__main__":
    unittest.main()
