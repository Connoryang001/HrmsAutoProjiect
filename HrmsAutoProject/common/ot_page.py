from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from .base import Page
from .add_ot_page import AddOt
from .delete_ot_page import deleteot

class OtListPage(Page):

    # 我的加班列表

    # 加班申请按钮
    otbutton_loc = (By.XPATH, '//*[@class="btn btn-success"]')
    otaddtext_loc = (By.XPATH, '//*[@class="x_title"]')
    otdelete_loc = (By.XPATH, '//*[@//*[@class="ui-pnotify-text"]]')
    deleteot_loc = (By.XPATH, '//*[@class="fa fa-trash"]')
    otdeleteyes_loc = (By.XPATH, '//*[@class="confirm btn btn-primary"]')
    otdeleteno_loc = (By.XPATH, '//*[@class="cancel btn btn-default"]')



    def OtAdd(self):
        '''
        点击加班申请按钮
        '''
        self.click_button(self.otbutton_loc)
        return AddOt(self.d)


    def hint_text(self):
        '''
        获取加班申请页面文本
        '''
        return self.find_element(self.otaddtext_loc).text


    def OtDelete(self):
        '''
        点击删除图标
        '''
        el = self.find_elements(self.deleteot_loc)
        el[0].click()


    def otdeleteyes(self):
        self.click_button(self.otdeleteyes_loc)

    def otdeleteno(self):
        self.click_button(self.otdeleteno_loc)

    def deleteotA(self):
        self.OtDelete()
        sleep(1)
        self.otdeleteyes()

    def huoqutext(self, text):
        sleep(2)
        return self.contains_text(text)



    def deleteotB(self):

        self.OtDelete()
        sleep(1)
        self.otdeleteno()




