import unittest
from scrapper_boilerplate import explicit_wait, setSelenium
from selenium.webdriver.common.by import By


class TestExplicitlyWait(unittest.TestCase):
    def test_explicitly_wait(self):
        with setSelenium() as driver:
            driver.get("https://stackoverflow.com/")
            code = explicit_wait(driver, By.CSS_SELECTOR, 'h1', timeout=60)
            print(code.text)
            self.assertTrue(code)


if __name__ == "__main__":
    unittest.main()
