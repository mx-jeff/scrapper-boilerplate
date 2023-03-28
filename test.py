from scrapper_boilerplate import init_log
import logging
from time import sleep

init_log()

def main():
    logging.info("Initializing...")
    counter = 1
    while True:
        logging.info("Checking {}".format(counter))
        sleep(1)
        counter = counter + 1

if __name__ ==  '__main__':
    main()
