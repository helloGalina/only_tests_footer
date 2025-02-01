import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FooterElementsTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_footer_elements(self):
        self.driver.get("https://only.digital/")

        try:
            logo_pic = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("class name", "Footer_logo__2QEhf"))
            )
            print("Логотип найден!")

            s_network_pic = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("class name", "Socials_socialsWrap__DPtp_"))
            )
            print("Социальные сети найдены!")

            telegram_pic = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(("class name", "TelegramAlternative_root__7q06_"))
            )
            print("Telegram для связи найден!")

            buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(("tag name", "button"))
            )
            print(f"Найдено {len(buttons)} кнопок в футере:")

            for index, button in enumerate(buttons):
                text = button.text
                if text:
                    print(f"Кнопка {index + 1}: {text}")
                else:
                    print(f"Кнопка {index + 1} без текста.")

        except Exception as e:
            print(f"Ошибка: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
