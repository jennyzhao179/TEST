from tools.get_log import GetLog

log = GetLog.get_logger()
def assert_function(self, r, success, code, message):
    try :
        result = r.json()
        self.assertEqual(200, r.status_code)
        self.assertEqual(success, result.get("success"))
        self.assertEqual(code, result.get("code"))
        self.assertEqual(message, result.get("message"))
    except Exception as e :
        log.info("断言出现错误{}".format(e))