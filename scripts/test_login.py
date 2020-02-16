import unittest

import requests

from api.api_login import ApiLogin
from api.api_user_list import ApiUserList
from tools.assert_function import assert_function
from tools.get_log import GetLog

log = GetLog.get_logger()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login = ApiLogin()

    def test_login(self, success=True, code=10000, message="操作成功！"):
        r = self.login.api_login()
        log.info("登录测试方法开始断言")
        assert_function(self, r, success, code, message)

