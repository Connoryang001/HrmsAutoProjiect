# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
# 其他模块调用此页面时，base前面要加.，当前模块调用不用加.
from .base import Page
from selenium import webdriver
from .user_page import Userinfo

class Login(Page):

    user_loc = (By.XPATH, '//*[@id="_username"]')
    password_loc = (By.XPATH, '//*[@id="_password"]')
    button_loc = (By.XPATH, '//*[@class="button"]')
    error_loc = (By.XPATH, '//*[text()="账号或密码错误"]')
    success_loc = (By.XPATH, '//*[text()="保胜"]')

    # 用户名
    def user_login(self, username):
        '''
        用户名
        :param username:
        :return:
        '''
        self.input_text(self.user_loc, username)

    def password_login(self, password):
        '''
        密码
        :param password:
        :return:
        '''
        self.input_text(self.password_loc, password)


    def button_login(self):
        '''
        点击登录按钮
        :return:
        '''
        self.click_button(self.button_loc)
        return Userinfo(self.d)

    def login(self, username='13670074446', password='123456'):
        '''
        统一登录入口
        :param username: 用户名
        :param password: 密码
        :return: 无
        '''
        self.user_login(username)
        sleep(1)
        self.password_login(password)
        sleep(1)
        return self.button_login()
        sleep(1)


    def error_hint(self):

        return self.find_element(self.error_loc).text

    def hint(self, text):
        return self.contains_text(text)

    def success_hint(self):

        return self.find_element(self.success_loc).text


if __name__ == '__main__':
    d = webdriver.Chrome()
    d.get("http://www.hrms.com/login")
    Login(d).login()
    d.quit()