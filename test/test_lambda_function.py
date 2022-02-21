#! /usr/bin/python3
import unittest
from lambda_function import lambda_handler

class Emulator:
    def __init__(self) -> None:
        self.parameters: str = "queryStringParameters"
        self.context: str = "requestContext"
        self.body: str = "body"

    def get_event(self, **kwargs) -> Any:
        # Query the data:
        request_method: str = kwargs.get("request_method", None)
        url: str = kwargs.get("url", None)
        headers: str = kwargs.get("headers", None)
        params: str = kwargs.get("params", None)
        cookies: str = kwargs.get("cookies", None)
        body: Any = kwargs.get("data", None)

        # Define the event
        event = {
            "queryStringParameters": params,
            "requestContext": {
                "http":{
                    "method":request_method
                }
            }, 
            "body": body,
            
        }

        return event

class TestCase(unittest.TestCase):
    def setUp(self):
        self.lambda_handler = lambda_handler
        self

    def test_lambda(self):
        self.lambda_handler()