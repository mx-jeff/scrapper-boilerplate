import unittest
import logging 
from scrapper_boilerplate import init_log
from time import sleep


class Test_Log(unittest.TestCase):
    def test_log(self):
        init_log(level=logging.DEBUG, filesave=True, error_sep=True)

        logging.info("Initializing...")
        counter = 1
        while True:
            if counter % 10 == 0:
                logging.error("teste error!")
                
            logging.info("Checking {}".format(counter))
            sleep(1)
            counter = counter + 1

if __name__ == "__main__":
    unittest.main()
