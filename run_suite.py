import unittest

from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts", pattern="test*.py")
with open("./report/report.html", "wb", encoding="utf-8") as f:
    HTMLTestRunner(stream=f).run(suite)