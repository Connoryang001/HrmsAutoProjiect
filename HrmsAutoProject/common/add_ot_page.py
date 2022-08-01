from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class AddOt(Page):
    '''
    加班申请页面
    '''

    # 定位元素：
    starttime_loc = (By.XPATH, '//*[@id="start"]')
    click_loc = (By.XPATH, '//*[@class="applyBtn btn btn-sm btn-success"]')
    endtime_loc = (By.XPATH, '//*[@id="end"]')
    longtime_loc = (By.XPATH, '//*[@id="award_period"]')
    reason_loc = (By.XPATH, '//*[@id="reason"]')
    cancel_loc = (By.XPATH, '//button[text()="取消"]')
    apply_loc = (By.XPATH, '//*[@id="send"]')
    success_loc = (By.XPATH, '//*[@class="btn btn-success"]')
    file_loc = (By.XPATH, '//*[@id="dropzone-supp"]')


    def starttime(self, text):
        '''
        开始时间
        '''
        self.input_text(self.starttime_loc, text)
        el = self.find_elements(self.click_loc)
        el[0].click()


    def endtime(self, text):
        '''
        结束时间
        '''
        self.input_text(self.endtime_loc, text)
        el = self.find_elements(self.click_loc)
        el[1].click()

    def longtime(self, text):
        '''
        加班时长
        '''
        self.input_text(self.longtime_loc, text)

    def reason(self, text):
        '''
        加班原因
        '''
        self.input_text(self.reason_loc, text)

    def cancel_button(self):
        '''
        取消按钮
        '''
        self.click_button(self.cancel_loc)

    def apply(self):
        '''
        申请按钮
        '''
        self.click_button(self.apply_loc)

    def hint_text(self, text):
        '''
        获取页面文本内容
        '''
        return self.contains_text(text)

    # def updatefile(self, text):
    #     '''
    #     上传图片
    #     '''
    #     self.input_text(self.file_loc, text)

    def successbutton(self):
        '''
        完成
        '''
        self.click_button(self.success_loc)

    def AddOtBusiness(self, stext='', etext='', ltext='', rtext='', ftext=''):
        '''
        加班申请业务
        '''
        sleep(1)
        self.starttime(stext)
        sleep(1)
        self.endtime(etext)
        sleep(1)
        self.longtime(ltext)
        sleep(1)
        self.reason(rtext)
        sleep(1)
        self.apply()
        sleep(1)
        # self.updatefile(ftext)
        sleep(1)
        self.successbutton()




