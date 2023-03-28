import unittest
import logging 
from scrapper_boilerplate import init_log
from time import sleep


class Test_Log(unittest.TestCase):
    def test_log(self):
        init_log(level=logging.DEBUG, filesave=True, error_sep=True)

        logging.info("Initializing...")
        counter = 0
        while True:
            if not counter == 0 and counter % 10 == 0:
                logging.error("teste error!")

            logging.info("Checking {}".format(counter))
            sleep(1)
            counter = counter + 1
            if counter > 20:
                break

if __name__ == "__main__":
    unittest.main()
