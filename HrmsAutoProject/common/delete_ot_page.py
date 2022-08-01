from selenium.webdriver.common.by import By
from .base import Page

class deleteot(Page):
    '''
    删除加班申请
    '''
    deleteot_loc = (By.XPATH, '//*[@class="apcolor1"]')
    otdeleteyes_loc = (By.XPATH, '//*[@class="confirm btn btn-primary"]')
    otdeleteno_loc = (By.XPATH, '//*[@class="cancel btn btn-default"]')

    def otdeleteyes(self):
        self.click_button(self.otdeleteyes_loc)

    def otdeleteno(self):
        self.click_button(self.otdeleteno_loc)

    def deleteotB(self, status=1):

        el = self.find_element(self.deleteot_loc)
        try:
            if el.text == '待审核':
                if status == 1:

                    self.otdeleteyes()
                elif status == 2:
                    self.otdeleteno()
        except BaseException as e:
            raise AssertionError(e)


