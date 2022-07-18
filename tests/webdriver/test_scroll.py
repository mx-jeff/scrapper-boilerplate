import unittest
from scrapper_boilerplate import setSelenium, scrolldown, smooth_scroll
from time import sleep


class TestScroll(unittest.TestCase):
    def setUp(self):
        self.driver = setSelenium(headless=False, remote_webdriver=True)

    def test_scrolldown(self):
        self.driver.get("https://www.awwwards.com/sites/heleonic")
        self.driver.implicitly_wait(220)
        print("scrolling...")
        scrolldown(self.driver)
        sleep(5)

    def test_smooth_scroll(self):
        self.driver.get("https://www.awwwards.com/sites/heleonic")
        self.driver.implicitly_wait(220)
        print("smooting scrolling...")
        smooth_scroll(self.driver)
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
