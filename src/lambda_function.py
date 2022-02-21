#! /usr/bin/python3
from proxy import Proxy
from typing import Any, Optional, Dict
from base64 import b64decode

# Class initialization:
proxy = Proxy()

def lambda_handler(event: Any, context: Optional[Any] = None) -> str:
	print(event)
	# Request input:
	parameters = event.get("queryStringParameters", None)
	request_method = event["requestContext"]["http"]["method"]
	body = event.get("body", None)
	headers = event['headers']

	url: str = b64decode(parameters['url'].encode()).decode()
	params: Dict[str,str] = {key:value for key, value in parameters.items() if key != 'url'}

	# Request:
	response = proxy.execute(request_method=request_method, url=url, headers=headers, cookies=cookies, params=params, data=body)
	return response