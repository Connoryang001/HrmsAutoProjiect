from unittestreport import TestRunner
import unittest,sys
import time
sys.path.append('./utils')
from utils.mail import send_mail

now_time = time.strftime('%Y-%m-%d %H_%M_%S')

discover =unittest.defaultTestLoader.discover('./testcase', pattern='test_*.py')
runner = TestRunner(discover, filename='{}report.html'.format(now_time),
                    report_dir='./report/',
                    title='测试报告',
                    tester='yangli012',
                    desc='hrms项目测试生成的报告',
                    templates=1)

runner.run()
send_mail()