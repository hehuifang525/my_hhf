"""运行文件"""
from base.keys import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    dr = Keys("Chrome")   # 初始化浏览器
    dr.open_url("https://www.baidu.com/")
    dr.input("ceshi123",(By.ID,"kw"))
    dr.click((By.ID, "su"))
    dr.quit()



