import os, requests, json 

class Config_handler:
    def __init__(self):
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