from selenium.webdriver.common.by import By
from time import sleep
from .base import Page
from selenium import webdriver
from .ot_page import OtListPage

class Userinfo(Page):

    user_loc = (By.XPATH, '//*[@class="fa fa-user"]')
    leave_loc = (By.XPATH, '//*[text()="我的请假"]')
    ot_loc = (By.XPATH, '//*[text()="我的加班"]')
    onsite_loc = (By.XPATH, '//*[text()="我的外勤"]')
    trip_loc = (By.XPATH, '//*[text()="我的出差"]')
    singin_loc = (By.XPATH, '//*[text()="漏打卡补签"]')


    def click_user(self):
        '''
        点击员工信息
        '''
        self.click_button(self.user_loc)

    def click_leave(self):
        '''
        点击 我的请假
        '''
        self.click_user()
        self.click_button(self.leave_loc)

    def click_ot(self):
        '''
        点击 我的加班
        '''
        self.click_user()
        self.click_button(self.ot_loc)
        return OtListPage(self.d)

    def click_onsite(self):
        '''
        点击 我的外勤
        '''
        self.click_user()
        self.click_button(self.onsite_loc)

    def click_trip(self):
        '''
        点击 我的出差
        '''
        self.click_user()
        self.click_button(self.trip_loc)

    def click_singin(self):
        '''
        点击 补签漏打卡
        '''
        self.click_user()
        self.click_button(self.singin_loc)