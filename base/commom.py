import configparser


# 封装config的读取
def conf_read(section, option):
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    return conf[section][option]


