#! /usr/bin/python3
import unittest, json
from base64 import b64encode
from lambda_function import lambda_handler, Lambda_handler
from config_handler import Config_handler
from api_emulator import Emulator
from typing import Any

class TestCase(unittest.TestCase):
    def setUp(self):
        self.lambda_handler = lambda_handler
        self.handler = lambda_handler
        self.config = Config_handler()
        self.api_emulator = Emulator()

    def __b64_encoding(self, value:str) -> str:
        return b64encode(value.encode()).decode()
    
    def __get_event(self, url, cookies, headers, request_method, params) -> Any:
        url = self.__b64_encoding(url)
        cookies = self.__b64_encoding(cookies)
        request_method = "GET"
        headers = self.__b64_encoding(json.dumps(headers))
        params = self.__b64_encoding(json.dumps(params))
        body = None

        return self.api_emulator.get_event(request_method=request_method, url=url, headers=headers, params=params, cookies=cookies, body=body)

    def test_lambda_class(self):
        # Targets:
        test_url = "https://google.com"
        test_cookies = "test=hola; testing=isthebest=ever"
        test_headers = {"Accept":"application/json"}
        test_params = {"$top":"1"}
        request_method = "GET"

        # Method testing:
        event = self.__get_event(test_url, test_cookies, test_headers, request_method, test_params)
        handler = Lambda_handler(event)

        # Correct url:
        self.assertEqual(test_url, handler.url)

        # Correct cookies:
        self.assertEqual({"test": "hola" , "testing":"isthebest=ever"}, handler.cookies)

        # Correct headers:
        self.assertEqual(test_headers, handler.headers)

        # Correct params:
        self.assertEqual(test_params, handler.params)

    def test_lambda_function(self):
        # Targets:
        test_url = "https://google.com"
        test_cookies = "test=hola; testing=isthebest=ever"
        test_headers = {"Accept":"application/json"}
        test_params = {"$top":"1"}
        request_method = "GET"

        # Method testing:
        event = self.__get_event(test_url, test_cookies, test_headers, request_method, test_params)
        response = self.lambda_handler(event)
        self.assertEqual(json.loads(response)['status_code'], 200)