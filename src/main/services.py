import time
import hmac
import hashlib

import requests
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()


class APIRequestManager:

    def __init__(self, base_url, params, method='get', signature=False):
        self.base_url = base_url
        self.query_params = "".join([f"{key}={value}&" for key, value in params.items()])
        self.method = method
        self.signature = signature

    def build_url(self):
        api_key = env('API_KEY')
        secret = env('API_SECRET').encode('utf-8')
        params4signature = ''
        if self.signature:
            params4signature = "api_key={}&timestamp={}".format(api_key, int(time.time() * 1000))
            total_params = (self.query_params + params4signature).encode('utf-8')
            signature = hmac.new(secret, total_params, hashlib.sha256).hexdigest()
            params4signature += f"&signature={signature}"

        return self.base_url + self.query_params + params4signature

    def make_request(self):
        response = requests.request(self.method, self.build_url())
        return response.status_code, response.json()
