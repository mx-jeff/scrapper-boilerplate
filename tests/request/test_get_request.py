import unittest
from scrapper_boilerplate import init_crawler


class TestScroll(unittest.TestCase):
    def test_get_request(self):
        soap = init_crawler("https://quotes.toscrape.com/")
        print(soap.text)
        self.assertIsNotNone(soap)


if __name__ == "__main__":
    unittest.main()
