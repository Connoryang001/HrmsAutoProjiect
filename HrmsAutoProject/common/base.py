# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.select import Select
from selenium import webdriver

class Page(object):
    '''
    元素公共方法
    '''
    def __init__(self, d):
        '''
        初始化参数
        :param d:
        '''
        self.d = d

    def find_element(self, loc):
        '''
        定位一个元素
        :param loc:
        :return:
        '''
        try:
            # return WebDriverWait(self.d, 20, 0.5).until(lambda x: x.find_element(*loc))
            return WebDriverWait(self.d, 20, 0.5).until(ec.presence_of_element_located(loc))
        except NoSuchElementException as e:
            return e.args[0]

    def find_elements(self, loc):
        '''
        定位一组元素
        :param loc:
        :return:
        '''
        try:
            # return WebDriverWait(self.d, 20, 0.5).until(lambda x: x.find_elements(*loc))
            return WebDriverWait(self.d, 20, 0.5).until(ec.presence_of_element_located(loc))
        except NoSuchElementException as e:
            return e.args[0]

    def input_text(self, loc, text):
        '''
        向文本框输入文本
        :param loc:
        :param text:
        :return:
        '''
        el = self.find_element(loc=loc)
        el.clear()
        el.send_keys(text)

    def click_button(self, loc):
        '''
        按钮点击
        :param loc:
        :return:
        '''

        el = self.find_element(loc=loc)
        try:
            el.click()
        except:
            self.d.execute_script('arguments[0].click();', el)

    def select_from_list(self, loc, text):
        '''
        下拉选项
        loc:下拉选项元素
        text:下拉选项内容
        '''
        el = self.find_element(loc=loc)
        Select(el).select_by_visible_text(text)
        return


    def switch_to_frames(self, frame=None):
        '''
        切换表单
        :param frame:
        :return:
        '''
        if frame:
            self.d.switch_to.frame(frame)
        else:
            self.d.switch_to.default_content()

    def switch_to_windows(self, handle=1, count=-1):
        '''
        切换窗口
        :return:
        '''
        main_handle = self.d.current_window_handle
        sleep(2)
        all_handles = self.d.window_handles
        if handle == 1:
            self.d.switch_to.windows(all_handles[count])
        elif handle == 0:
            self.d.switch_to.window(main_handle)

    def contains_text(self, text):
        '''
        检查页面文本text
        :param text: 如果找到对应文本内容，返回True，没有找到则返回False
        :return:
        '''
        xpath = '//*[contains(., "%s")]' %text
        try:
            WebDriverWait(self.d, 20, 0.5).until(lambda x: x.find_element_by_xpath(xpath))
        except:
            return False
        return True







