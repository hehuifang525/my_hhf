"""封装浏览器的打开"""
from selenium import webdriver
# 打开浏览器：


def open_browser(txt):
    """打开浏览器"""

    if txt=="Chrome":
        # driver = webdriver.Chrome(options=ChromeOptions().options())
        option = webdriver.ChromeOptions()
        # options.add_argument('start-maximized')
        option.add_argument('--start-maximized')
        # option.add_argument('--headless')  # 无头模式，不会展示浏览器界面，某些场景下会失败
        option.add_experimental_option('excludeSwitches',['enable-automation'])  # 去掉默认的自动化提示信息

        # 实现一个有缓存的浏览器 chrome://version/ 取个人资料路径，该指令使用，必须关闭本地所有chrome浏览器
        option.add_argument(r'--user-data-dir=C:\Users\56599\AppData\Local\Google\Chrome\User Data')


        driver = webdriver.Chrome(options=option)


        # driver.maximize_window()  # 最大化

        print("已知浏览器")
    else:
        try:
            # 函数映射
            driver = getattr(webdriver, txt)()
        except Exception as e:
            print(e,"浏览器打开报错，则使用默认浏览器打开")
            driver = webdriver.Chrome()
    return driver



