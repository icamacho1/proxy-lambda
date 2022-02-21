#! /usr/bin/python3 
import unittest, json, requests, os
from typing import Tuple
from proxy import Proxy

class TestCase(unittest.TestCase):
    def setUp(self):
        # Class to test
        self.proxy = Proxy()

        # Get authenticated:
        self.__load_config()

    def __load_config(self):
        curr_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(curr_path,"config.json"), "rb") as file:
            self.config = json.loads(file.read())

        # Target endpoints:
        self.get_url: str = self.config['get_url']
        self.post_url: str = self.config['post_url']

        # Authentication:
        url: str = self.config['launch_url']
        auth: Tuple[str,str] = (self.config['user'], self.config['password'])
        self.cookies: Dict[str,str] = dict(requests.get(url, auth=auth).cookies)


    def test_get(self):
        # Request data:
        request_method: str = "GET"
        url = self.get_url
        params: Dict[str, str] = {"$top": "1"}
        headers: Dict[str,str] = {"Accept": "application/json"}

        # Request execution:
        request_response = requests.get(url, cookies=self.cookies, headers=headers, params=params).json()
        proxy_response = json.loads(self.proxy.execute(request_method=request_method, url=url, headers=headers, cookies=self.cookies, params=params))["json"]

        self.assertEqual(request_response, proxy_response)


    def test_post(self):
        # Request data:
        request_method: str = "POST"
        url = self.post_url
        headers: Dict[str,str] = {"Accept": "application/json", "X-CSRF-Token":"fetch"}

        # Request execution:
        request_response = requests.post(url, cookies=self.cookies, headers=headers)
        proxy_response = json.loads(self.proxy.execute(request_method=request_method, url=url, headers=headers, cookies=self.cookies))

        self.assertEqual(type(dict(request_response.headers)['x-csrf-token']), type(proxy_response['headers']['x-csrf-token']))

if __name__ == "__main__":
    unittest.main()