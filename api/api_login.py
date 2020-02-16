import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiLogin:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
    def api_login(self):
        data = {"mobile": "13800000002", "password": "123456"}
        r = requests.post(url=self.login_url, json=data)
        token = "Bearer " + r.json().get("data")
        log.info("token值为{}".format(token))
        api.headers_data["Authorization"] = token
        log.info("headers_data的值为{}".format(api.headers_data))
        return r