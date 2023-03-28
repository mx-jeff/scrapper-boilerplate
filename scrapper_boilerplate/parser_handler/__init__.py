import requests
import re
import logging

from bs4 import BeautifulSoup
from requests.exceptions import InvalidSchema


def init_crawler(url, params={"method":"GET", 'headers': None, 'body': None, 'timeout':10, "engine": "lxml" }):
    
    
    """
    This function is used to inititate a crawler.
    It takes a url and a dictionary of parameters.
    The dictionary of parameters can be used to set the request method, headers, body, timeout and engine.
    The default values are:
        method: GET
        headers: None
        body: None
        timeout: 10
        engine: lxml
    
    return: BeautifulSoup object
    """


    def make_request(params, url):
        """
        Make a request to a url
        args:
            - params: dict, the params of the request
            - url: str, the url of the request
        
        returns:
            - response: requests.Response, the response of the request
        """

        if params['method'] == "GET":
            return requests.get(url, headers=params['headers'], timeout=params['timeout'])

        elif params['method'] == "POST":
            return requests.post(url, headers=params['headers'], data=params['body'], timeout=params['timeout'])
        
        elif params['method'] == "PUT":
            return requests.put(url, headers=params['headers'], data=params['body'], timeout=params['timeout'])
        
        elif params['method'] == "DELETE":
            return requests.delete(url, headers=params['headers'], data=params['body'], timeout=params['timeout'])
        
        elif params['method'] == "PATCH":
            return requests.patch(url, headers=params['headers'], data=params['body'], timeout=params['timeout'])
        
        elif params['method'] == "HEAD":
            return requests.head(url, headers=params['headers'], timeout=params['timeout'])
        
        elif params['method'] == "OPTIONS":
            return requests.options(url, headers=params['headers'], timeout=params['timeout'])
        
        elif params['method'] == "TRACE":
            return requests.trace(url, headers=params['headers'], timeout=params['timeout'])
        
        else:
            return


    try:
        page = make_request(params, url)
        if not page: return

        if page.status_code != 200:
            print(f'[ERRO {page.status_code}] Site indisponivel, tente novamente mais tarde')
            return

        return BeautifulSoup(page.text, params['engine'])

    except InvalidSchema:
        print('Algo deu errado!')
        return

    except ConnectionError:
        print('Não conseguiu se conectar na página!')
        return


def init_parser(html, engine="lxml"):
    return BeautifulSoup(html, engine)


def remove_whitespaces(text):
    return " ".join(text.split())


def remove_duplicates_on_list(array):
    return list(dict.fromkeys(array))


def check_telephone(word):
    """
    Check if word contains a valid telephone number
    """
    target_tel = word.replace('.', ' ')
    match = re.findall(r'\(\d{2}\)|\d{2}\s* \d{4,5}-\d{4}', target_tel)
    if match:  
        return "".join(match)
    else:
        return False


def check_tag(soap, tag, first=True, check_text=True):
    """
    Check if the tag is valid
    args:
        - tag: str, the tag you want to check
    returns:
        - bool: True if the tag is valid, 'Não localizado...':str otherwise
    """
    try:
        if first:
            element = soap.select_one(tag).text if check_text else soap.select_one(tag)
            if not element: return

        element = soap.select(tag)
        if not element: return

    except Exception as error:
        logging.error(error)
        return 
