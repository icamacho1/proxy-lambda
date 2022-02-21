#! /usr/bin/python3 
import unittest, json, requests, os
from typing import Tuple
from proxy import Proxy
from config_handler import Config_handler

class TestCase(unittest.TestCase):
    def setUp(self):
        # Class to test
        self.proxy = Proxy()

        # Get authenticated:
        self.config = Config_handler()

    def test_get(self):
        # Request data:
        request_method: str = "GET"
        url = self.config.get_url
        cookies = self.config.cookies
        params: Dict[str, str] = {"$top": "1"}
        headers: Dict[str,str] = {"Accept": "application/json"}

        # Request execution:
        request_response = requests.get(url, cookies=cookies, headers=headers, params=params).json()
        proxy_response = json.loads(self.proxy.execute(request_method=request_method, url=url, headers=headers, cookies=cookies, params=params))["json"]

        self.assertEqual(request_response, proxy_response)


    def test_post(self):
        # Request data:
        request_method: str = "POST"
        url = self.config.post_url
        cookies = self.config.cookies
        headers: Dict[str,str] = {"Accept": "application/json", "X-CSRF-Token":"fetch"}

        # Request execution:
        request_response = requests.post(url, cookies=cookies, headers=headers)
        proxy_response = json.loads(self.proxy.execute(request_method=request_method, url=url, headers=headers, cookies=cookies))

        self.assertEqual(type(dict(request_response.headers)['x-csrf-token']), type(proxy_response['headers']['x-csrf-token']))

if __name__ == "__main__":
    unittest.main()