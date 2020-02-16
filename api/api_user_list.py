import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiUserList(object):
    def __init__(self):

        self.uselist_url = "http://182.92.81.159/api/sys/user?page={}&size={}"
        log.info("初始化USERLISTurl为{}".format(self.uselist_url))



    def api_user_list(self, page, size):
        log.info("获取列表的url为{}, 信息头为{}".format(self.uselist_url.format(page,size),api.headers_data))
        return requests.get(url=self.uselist_url.format(page,size), headers = api.headers_data)