import unittest
from scrapper_boilerplate import setSelenium


class Test_Selenium(unittest.TestCase):
    def test_setSelenium_console(self):
        with setSelenium(headless=False, remote_webdriver=True) as driver:
            driver.get("https://www.google.com")
            self.assertEqual(driver.title, "Google")

    def test_setSelenium_headless(self):
        with setSelenium(headless=True, remote_webdriver=True) as driver:
            driver.get("https://www.google.com")
            self.assertEqual(driver.title, "Google")

    def test_setSelenium_without_remote(self):
        with setSelenium(headless=False, remote_webdriver=False) as driver:
            driver.get("https://www.google.com")
            self.assertEqual(driver.title, "Google")

    def test_setSelenium_without_remote_headless(self):
        with setSelenium(headless=True, remote_webdriver=False) as driver:
            driver.get("https://www.google.com")
            self.assertEqual(driver.title, "Google")

if __name__ == "__main__":
    unittest.main()
