#coding=utf-8

import  unittest

def all_case():
    #test_dir = '/Users/zhangnaiping/Documents/test_blog/'
    test_dir = "test_case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

    #for test_suit in discover:
        #for test_case in test_suit:
            #testcase.addTests(test_case)
    testcase.addTests(discover)
    #print testcase
    return testcase

if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    import HTMLTestRunner
    import datetime

    now_date = datetime.datetime.now().strftime('%Y%m%d')
    file_name = 'report_' + now_date + '.html'
    report_path = 'test_report/'+file_name
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'尝试看看卡'
    )
    runner.run(all_case())
    fp.close()