# coding=utf-8

import logging
from selenium import webdriver
from time import sleep

class Log():

    def logger(self):
        '''
        设置日志
        :return:
        '''
        # 获取日志对象
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 创建一个FileHandler对象指定日志写入路径
            sh = logging.FileHandler('D:/pythonProject/HrmsAutoProject/report/log/test.log', encoding='utf-8')

            # 创建一个Formatter对象指定日志生成格式
            fmt = logging.Formatter("%(levelname)-6s [%(asctime)s] %(filename)s[line:%(lineno)d]: %(message)s",
                                 "%Y/%m/%d %H:%M:%S")

            # 给路径文件设置日志格式
            sh.setFormatter(fmt)

            # 给路径文件设置日志级别
            sh.setLevel(logging.INFO)

            # 将路径文件添加到日志对象中
            logger.addHandler(sh)


            # 移除headler对象
            # logger.removeHandler(sh)

        return logger




if __name__ == '__main__':
     d = webdriver.Chrome()
     d.get("http://www.baidu.com")
     text = 'selenium'
     d.find_element_by_id('kw').send_keys(text)
     d.find_element_by_id('su').click()
     d.implicitly_wait(5)
     log = Log().logger()
     sleep(5)
     title = d.title

     if title == 'selenium_百度搜索1':
        log.info('{title} 与 {text}一致!!'.format(title=title, text=text))
     else:
        log.info('{title} 与 {text}不一致!!'.format(title=title, text=text))
     sleep(5)
     d.quit()

