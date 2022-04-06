"""
    入口文件
"""
from test_sjqd import sjqd

# if __name__ == '__main__':
#     sjqd("data/test01.xlsx")

import pytest
import os
import allure
if __name__ == '__main__':
    pytest.main(["-vs", "test_case/test_case01.py", '--alluredir','./report_temp', '--clean-alluredir'])
    # os.system('allure serve C:\PycharmProjects\key_word\\report_temp')  # 立即打开报告（程序会持续执行）
    os.system('allure serve ./report_temp')  # 立即打开报告（程序会持续执行）
    # os.system('allure generate ./report_temp/ -o ./report_allure --clean') # 生成报告到report_allure文件中