# coding=utf-8
from selenium import webdriver
from time import sleep
import unittest, sys
sys.path.append('./utils')
sys.path.append('./common')
from utils.jietu import Jietu
from utils.log import Log
from utils.read_config import read_test_data
from common.login_page import Login

test_data = read_test_data('D:/pythonProject/HrmsAutoProject/data/login_data.yml')

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.d = webdriver.Chrome()
        self.d.maximize_window()
        self.d.implicitly_wait(10)
        self.d.get("http://www.hrms.com/login")

    def tearDown(self) -> None:
        sleep(5)
        self.d.quit()


    def user_login_verify(self, username="", password=""):
        Login(self.d).login(username, password)

    def test_login1(self):
        '''
        账号密码为空
        :return:
        '''
        td = test_data['test_login1']
        self.user_login_verify(username=td['username'], password=td['password'])
        po = Login(self.d)
        try:
            self.assertEqual(po.error_hint(), td['hint_text'], 'test_login1用例执行失败')
        except BaseException as e:
            Log().logger().info('[test_login1]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_login1')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_login1]信息：PASS')

    def test_login2(self):
        '''
        账号正确，密码为空
        :return:
        '''
        td = test_data['test_login2']
        self.user_login_verify(username=td['username'], password=td['password'])
        po = Login(self.d).hint(td['hint_text'])


        try:
            self.assertTrue(po)
        except BaseException as e:
            Log().logger().info('[test_login2]信息：{}'.format('执行失败，请检查'))
            Jietu(self.d).scrrenshot_image('test_login2')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_login2]信息：PASS')

    def test_login3(self):
        '''
        账号为空，密码正确
        :return:
        '''
        td = test_data['test_login3']
        self.user_login_verify(username=td['username'], password=td['password'])
        po = Login(self.d)
        try:
            self.assertEqual(po.error_hint(), td['hint_text'], 'test_login3用例执行失败')
        except BaseException as e:
            Log().logger().info('[test_login3]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_login3')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_login3]信息：PASS')


    def test_login4(self):
        '''
        账号、密码错误
        :return:
        '''
        td = test_data['test_login4']
        self.user_login_verify(username=td['username'], password=td['password'])
        po = Login(self.d)
        try:
            self.assertEqual(po.error_hint(), td['hint_text'], 'test_login4用例执行失败')
        except BaseException as e:
            Log().logger().info('[test_login4]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_login4')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_login4]信息：PASS')


    def test_login5(self):
        '''
        账号、密码正确
        :return:
        '''
        td = test_data['test_login5']
        self.user_login_verify(username=td['username'], password=td['password'])
        po = Login(self.d)
        try:
            self.assertEqual(po.success_hint(), td['hint_text'], 'test_login5用例执行失败')
        except BaseException as e:
            Log().logger().info('[test_login5]信息：{}'.format(e))
            Jietu(self.d).scrrenshot_image('test_login5')
            raise AssertionError(e)
        else:
            Log().logger().info('[test_login5]信息：PASS')

if __name__ == '__main__':
    unittest.main()
