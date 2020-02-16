import unittest

from api.api_user_list import ApiUserList
from tools.get_log import GetLog


from tools.assert_function import assert_function
from parameterized import parameterized

from tools.read_yaml import read_yaml

log = GetLog.get_logger()
class TestUserList(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_list = ApiUserList()
    @parameterized.expand(read_yaml("test_user_list_data.yaml"))
    def test_user_list(self, page, size, success, code, message):
        r = self.user_list.api_user_list(page, size)
        log.info("获取用户列表开始断言")
        assert_function(self, r, success, code, message )