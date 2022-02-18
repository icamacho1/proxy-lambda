#! /usr/bin/python3 
import python_modules, requests, json
from typing import Dict, Optional, Callable, Tuple, Any

def try_except(function: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            return {"Errored": f"{e}"}
    return wrapper

class Proxy:
    @try_except
    def execute(self, **kwargs) -> str:
        # Get the key values to the function:
        request_method: str = kwargs.get("request_method", None)
        url: str = kwargs.get("url", None)
        headers: str = kwargs.get("headers", None)
        params: str = kwargs.get("params", None)
        cookies: str = kwargs.get("cookies", None)
        body: Any = kwargs.get("body", None)

        if request_method == "GET":
            response = requests.get(url=url, headers=headers, cookies=cookies, params=params)    
        elif request_method == "POST":
            response = requests.post(url=url, headers=headers, cookies=cookies, params=params, data=body)    
        elif request_method == "PATCH":
            response = requests.patch(url=url, headers=headers, cookies=cookies, params=params, data=body)    
        else:
            return json.dumps({
                "status_code": 403, 
                "text": "Invalid request method",
                "json": "[]",
                "headers": "[]",
                "Cookies": "[]"
                })
            
        return json.dumps({
            "status_code": response.status_code,
            "json": response.json(),
            "headers": dict(response.headers),
            "cookies": dict(response.cookies)
        })

if __name__ == "__main__":
    proxy = Proxy()

    with open("credentials.json", "rb") as file:
            credentials = json.loads(file.read())
        
    url_auth: str = "https://sapqas.idom.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html"
    auth: Tuple[str,str] = (credentials['user'], credentials['password'])
    cookies: Dict[str,str] = dict(requests.get(url_auth, auth=auth).cookies)


    request_method: str = "GET"
    url: str ="https://sapqas.idom.com/sap/opu/odata/sap/ZSD_PROP_ODATA_SRV/ZSD_C_PROP_SM" 
    params: Dict[str, str] = {"$top": "1"}
    headers: Dict[str,str] = {"Accept": "application/json"}

    data = proxy.execute(request_method=request_method, url=url, headers=headers, cookies=cookies, params=params)
    print(data)