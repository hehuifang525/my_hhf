import pymysql
from base.commom import conf_read


class MysqlDb:
    def __init__(self):
        host = conf_read("database", "host")
        database = conf_read("database", "db_name")
        user = conf_read("database", "user")
        passwd = conf_read("database", "passwd")
        port = int(conf_read("database", "port"))

        # 连接数据库
        try:
            self.con = pymysql.connect(user=user, passwd=passwd, host=host, database=database, port=port)  # 创建数据库连接
        except Exception as e:
            print(e, "数据库连接失败")
        self.cursor = self.con.cursor()    # 创建查询游标

    def select_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e, f"查询出错{sql}")
        result = self.cursor.fetchall()

        self.cursor.close()
        self.con.close()
        return result

    def idu_sql(self, sql):
        """
        执行插入 删除 更新语句
        :param sql:
        :return:
        """
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e, f"查询出错{sql}")
        self.con.commit()
        self.cursor.close()
        self.con.close()




#
# b = MysqlDb()
# qq = b.select_sql("select * from students")
# print(qq)




