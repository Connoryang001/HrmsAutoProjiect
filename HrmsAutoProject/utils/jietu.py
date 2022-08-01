# coding=utf-8
import time
from selenium import webdriver


class Jietu():

    def __init__(self, d):
        self.d = d

    def scrrenshot_image(self, bug_name):

        now_time = time.strftime('%Y-%m-%d %H_%M_%S')
        jietu_path = 'D:/pythonProject/HrmsAutoProject/report/image'

        image_name = jietu_path +'/{bug_name} {now_time}.png' .format(bug_name=bug_name, now_time=now_time)

        self.d.get_screenshot_as_file(image_name)



if __name__ == '__main__':
    d = webdriver.Chrome()
    d.get("http://www.baidu.com")
    text = 'selenium'
    d.find_element_by_id('kw').send_keys(text)
    d.find_element_by_id('su').click()
    d.implicitly_wait(5)
    scrrent = Jietu()
    time.sleep(5)
    title = d.title

    if title == 'selenium_百度搜索1':
        pass
    else:
        scrrent.scrrenshot_image(d, '{title} 与预期不一致'.format(title=title))
    time.sleep(5)
    d.quit()

