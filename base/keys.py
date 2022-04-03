"""
    关键字封装：
    打开浏览器  ok
    进入指定路径地址  ok
    元素定位  ok
    点击   ok
    输入元素值    ok
    等待-强制   ok
    等待-显示   ok
    iframe切换
    窗体切换
    悬浮-
    退出浏览器   ok

"""

import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from functools import wraps
from base.browser import open_browser



class Keys:
    # driver = webdriver.Chrome()
    def __init__(self, txt):
        self.driver = open_browser(txt)
        self.driver.implicitly_wait(10)

    def open_url(self, url):
        self.driver.get(url)

    def locator(self, name, value):
        """
        :param name: 定位的类型
        :param value: 定位的元素
        :return: 定位的元素
        """
        # return self.driver.find_element(*loc)
        a = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((name,value)), message="元素定位失败")
        if a:
            a = self.driver.find_element(name, value)
            # 滚动到指定元素
            js = "arguments[0].scrollIntoView(true);"
            self.driver.execute_script(js, a)
            return a

    def locators(self, name,value):
        """
        :param name: 定位的类型
        :param value: 定位的元素
        :return: 定位的元素
        """
        # return self.driver.find_elements(name, value)
        a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((name,value)), message="元素组定位失败")
        if a:
            a = self.driver.find_elements(name,value)
            # 滚动到指定元素
            js = "arguments[0].scrollIntoView(true);"
            self.driver.execute_script(js, a)
            return a

    def click(self, name,value):
        """点击元素"""
        self.locator(name,value).click()

    def input(self, name,value, txt):
        """输入值"""
        self.locator(name,value).send_keys(txt)


    def wait_s(self,secs: int):
        """强制等待"""
        time.sleep(secs)

    # 显示等待
    def wait_el(self, name,value):
        return WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located((name,value)),message="元素定位失败")
        # for i in range(5):
        #     try:
        #         a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        #         if a:
        #             a = self.driver.find_element(*loc)
        #             # 滚动到指定元素
        #             js = "arguments[0].scrollIntoView(true);"
        #             self.driver.execute_script(js, a)
        #             return a
        #     except:
        #         pass
        # else:
        #     raise Exception('time out:未找到元素，请重新定位')

    # 断言文本
    def assert_text(self, name,value, expect):
        # print(self.locator(name,value).text,'取到的值')
        assert self.locator(name,value).text == expect, f'预期值显示错误，预期应为：{expect}'

    def screenshot_about_case(func):
        """

        创建用例执行失败装饰器报错会可进行屏幕截图；
        使用方式，用例函数使用装饰器  @screenshot_about_case

        """
        # 把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        @wraps(func)
        # screen_name = file_path + rq + '.png'
        def get_screenshot_about_case(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                # 获取case_name的名称
                case_name = '{}-{}'.format(self.__class__.__name__, func.__name__)
                # 截屏的路径
                screenshotPath = os.path.join(file_path, case_name)
                # 获得现在的时间戳
                # time_now = datetime.now().strftime('%Y%m%d%H%M%S')
                # 名字的一部分
                screen_shot_name = ".png"
                # 组装图片需要传入的路径和推片名称
                screen_img = screenshotPath + '_' + rq + '_' + screen_shot_name
                # 截图并保存到相应的名称的路径
                self.driver.get_screenshot_as_file(screen_img)
                self.logger.info("Had take screenshot and save to folder : /screenshots")
                # print('截图成功')
                raise e
        return get_screenshot_about_case

    def quit(self):
        """退出浏览器"""
        self.driver.quit()
        # self.driver.close()






