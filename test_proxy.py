#! /usr/bin/python3 
import unittest, json, requests
from typing import Tuple
from proxy import Proxy

class TestCase(unittest.TestCase):
    def setUp(self):
        # Class to test
        self.proxy = Proxy()

        # Get authenticated:
        self.__load_config()

    def __load_config(self):
        with open("config.json", "rb") as file:
            self.config = json.loads(file.read())

        # Target endpoints:
        self.get_url: str = self.config['get_url']
        self.post_url: str = self.config['post_url']

        # Authentication:
        url: str = self.config['launch_url']
        auth: Tuple[str,str] = (self.config['user'], self.config['password'])
        self.cookies: Dict[str,str] = dict(requests.get(url, auth=auth).cookies)


    def test_get(self):
        request_method: str = "GET"
        params: Dict[str, str] = {"$top": "1"}
        headers: Dict[str,str] = {"Accept": "application/json"}
        request_response = requests.get(self.get_url, cookies=self.cookies, headers=headers, params=params).json()
        proxy_response = json.loads(self.proxy.execute(request_method=request_method, url=self.get_url, headers=headers, cookies=self.cookies, params=params))["json"]
        self.assertEqual(request_response, proxy_response)



if __name__ == "__main__":
    unittest.main()