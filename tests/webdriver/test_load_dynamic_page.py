import unittest
from scrapper_boilerplate import load_dynamic_page


class TestLoadDynamically(unittest.TestCase):
    def test_load_dynamic_page(self):
        code = load_dynamic_page("https://github.com/mx-jeff/scrapper-boilerplate")
        self.assertTrue(code)

    def test_load_dynamic_page_with_scroll(self):
        code = load_dynamic_page("https://github.com/mx-jeff/scrapper-boilerplate", scroll=True)
        self.assertTrue(code)

    def test_load_dynamic_page_with_no_headless(self):
        code = load_dynamic_page("https://github.com/mx-jeff/scrapper-boilerplate", headless=False)
        self.assertTrue(code)

    def test_load_dynamic_page_with_no_headless_and_scroll_enabled(self):
        code = load_dynamic_page("https://github.com/mx-jeff/scrapper-boilerplate", headless=False, scroll=True)
        self.assertTrue(code)

if __name__ == "__main__":
    unittest.main()
