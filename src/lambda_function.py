#! /usr/bin/python3
import json
from proxy import Proxy
from typing import Any, Optional, Dict, Union
from base64 import b64decode

# Class initialization:

class Lambda_handler:
	def __init__(self, event: Any):
		self.parameters = event.get("queryStringParameters", None)
		self.request_method = event["requestContext"]["http"]["method"]
		self.body = event.get("body", None)
		self.proxy = Proxy()

		# Values:
		self.url = self.__b64_decode("url")
		self.cookies = self.__get_cookies()
		self.params = json.loads(self.__b64_decode("params"))
		self.headers = json.loads(self.__b64_decode("headers"))

	def __b64_decode(self, key: str) -> Union[str,None]:
		value = self.parameters.get(key, None)
		if not value:
			return None
		return b64decode(value.encode()).decode()


	def __get_cookies(self) -> Union[Dict[str,str], None]:
		cookies = self.__b64_decode("cookies")
		if cookies:
			return {cookie.split("=")[0]:"=".join(cookie.split("=")[1:]) for cookie in cookies.split("; ")}
		return None

	def call_http_method(self) -> str:
		if not self.url:
			return json.dumps({"status_code": 400, "json":{"error":"Missing url"}})
		response = self.proxy.execute(request_method=self.request_method, url=self.url, headers=self.headers, cookies=self.cookies, params=self.params, data=self.body)
		return response



def lambda_handler(event: Any, context: Optional[Any] = None) -> str:
	handler = Lambda_handler(event)
	response = handler.call_http_method()
	return response