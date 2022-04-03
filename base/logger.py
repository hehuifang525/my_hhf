"""
    将日志文件进行封装
"""

"""
    日志文件的使用和封装
"""
import logging
import logging.handlers
import os
import time

class Logger:

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)  # 定义log的名称
        self.logger.setLevel('DEBUG')  # 设置日志级别
        # logger.setLevel(logging.DEBUG)  # 设置日志级别

        # 指定日志文件目录
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 获取项目路径
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 日志需要存放的路径是
        log_path = project_path + '/logs/'
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'

        # 判断logger是否存在句柄，不存在则创建，存在则不创建，解决日志重复打印问题
        if not self.logger.handlers:
            # 控制台输出日志
            ch = logging.StreamHandler()

            # # 向文件输出日志
            # fh = logging.FileHandler(log_name,encoding='utf-8')
            # 指定将文件存储在指定文件中，超过一定大小则分隔日志，只保存指定日期的日志--未处理完成 需要再处理
            fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
                                                      encoding='utf-8')  # 实例化handler

            # 格式
            fm = logging.Formatter("%(asctime)s %(name)s %(pathname)s %(funcName)s %(lineno)d %(message)s")
            ch.setFormatter(fm)
            fh.setFormatter(fm)

            self.logger.addHandler(ch)
            self.logger.addHandler(fh)

        # return logger

    def getlog(self):
        return self.logger




# logger = logger()
# logger.warning("cuowu")
# project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# print(project_path,'22')
#
# print(os.path.dirname(os.path.dirname(__file__)))
# Logger().get_logger().warning("cuowu")

