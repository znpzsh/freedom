#coding=utf-8

import  unittest
from test_template.userAccountBalance import userAccountBalance

class Test(unittest.TestCase):
    #def setUp(self):
        #self.balance = userAccountBalance(idNo)

    def test_one(self):
        idNo = "442000199501146433"
        result = userAccountBalance(idNo).LoanBalance()
        #userbalance = result["data"]["useBalance"]
        resultSucceed = result["succeed"]
        #self.assertEqual(resultSucceed, True)
        if resultSucceed == True:
            print(result["data"]["useBalance"])
        else:
            print(result["errorMessage"])
        #print(result)

if __name__ == '__main__':
    unittest.main()




