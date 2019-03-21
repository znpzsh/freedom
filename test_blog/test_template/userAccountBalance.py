# coding:utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class userAccountBalance():

    def __init__(self, idNo):
        self.idNo = idNo

    def LoanBalance(self):
        url = "http://192.168.4.125:8080/poan-app/api/collApi/userAccountBalance"
        header = {"Content-Type":"application/json" }
        jsonData = {'idNo':self.idNo}
        res = requests.post(url, headers=header, json=jsonData, verify=False)
        #result1 = res.content
        #result1 = result1.decode('utf-8')  #需转换，否则接口返回的中文为乱码
        #print(result1)
        return res.json()

if __name__ == '__main__':
    idNo = "442000199501146433"
    userAccountBalance(idNo).LoanBalance()

