#coding=utf-8

import  unittest

class Test(unittest.TestCase):
    def testMinnus(self):
        result=6-5
        hope=1
        self.assertEqual(result,hope)

if __name__ == '__main__':
    unittest.main()

