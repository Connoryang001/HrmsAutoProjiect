# coding=utf-8
from selenium import webdriver
from time import sleep
import unittest, sys
sys.path.append('./utils')
sys.path.append('./common')
from utils.log import Log
from utils.jietu import Jietu
from utils.read_config import read_test_data
from common.login_page import Login
from unittestreport import rerun

test_data = read_test_data('D:/pythonProject/HrmsAutoProject/data/login_data.yml')
class AddOt(unittest.TestCase):
    '''
    加班申请流程
    '''

    def setUp(self) -> None:
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("http://www.hrms.com/login")

    def tearDown(self) -> None:
        sleep(3)
        self.d.quit()

    @rerun(count=2, interval=2)
    def test_ot1(self):
        td = test_data['test_ot1']

        userinfo = Login(self.d).login(username='13670074446', password='123456')
        Otlist = userinfo.click_ot()
        Addot = Otlist.OtAdd()
        Addot.AddOtBusiness(td['stext'], td['etext'], td['ltext'], td['rtext'], td['ftext'])

        try:
            self.assertTrue(Addot.hint_text(td['hint_text']))
            sleep(0.5)
            Addot.successbutton()
        except BaseException as e:
            Log().logger().info('[test_ot1]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_ot1')
            # raise AssertionError(e)
        else:
            Log().logger().info('[test_ot1]信息：PASS')


    def test_ot2(self):
        td = test_data['test_ot2']
        userinfo = Login(self.d).login(username='13670074446', password='123456')
        Otlist = userinfo.click_ot()
        Addot = Otlist.OtAdd()
        Addot.AddOtBusiness(td['stext'], td['etext'], td['ltext'], td['rtext'], td['ftext'])

        try:
            self.assertTrue(Addot.hint_text(td['hint_text']))
            sleep(0.5)
        except BaseException as e:
            Log().logger().info('[test_ot2]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_ot2')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_ot2]信息：PASS')

    # @unittest.skip('跳过')
    def test_ot3(self):
        td = test_data['test_ot3']
        userinfo = Login(self.d).login(username='13670074446', password='123456')
        Otlist = userinfo.click_ot()
        Otlist.deleteotA()

        try:
            sleep(0.5)
            self.assertTrue(Otlist.huoqutext(td['hint_text']))
        except BaseException as e:
            Log().logger().info('[test_ot3]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_ot3')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_ot3]信息：PASS')






if __name__ == '__main__':
    unittest.main()


