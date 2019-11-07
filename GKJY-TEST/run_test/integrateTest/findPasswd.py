#!/usr/bin/env python3

import requests
import hashlib
import json
import time
import random
import sys
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/lhlmysql')
sys.path.append('/root/lhl/myPerformance/GKJY-TEST')

from lhlsql import lhlSql, portalSql
import config

class userFind():

    def __init__(self):
        self.sqldata = lhlSql()
        self.portalsql = portalSql()
        self.postheader = {}
        self.postheader['Content-Type'] = "application/json"
        pass

    def phoneFind(self):
        """通过手机号修改密码"""

        mokuai = "找回密码"
        mobile = ["16688888612"]
        url = config.testurl + "/forget/info"
        data = {}
        for i in mobile:
            acc = requests.post(config.testurl + "/forget/info?account=" + i)
            print(acc.text)
#            pho = requests.post(config.testurl + "/reg/exist/mobile?mobile=" + str(i[1]))
#            print(pho.text)
#            code = requests.post(config.testurl + "/reg/sms/code?mobile=" + str(i[1]))
#            print(code.text)
#            data['mobilePhone'] = str(i[1])
  #          print(data)
#            reg = requests.post(url, headers=self.postheader, data=json.dumps(data))
#            print(reg.text)
#            if reg.json()['code'] == 200:
#               result = "Success"
#            else:
#               result = "Faile"
#            self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), reg.text, reg.status_code, round(reg.elapsed.total_seconds(),5), self.phoneRegist.__doc__, result)
        return None

    def illegalAccountRegist(self):
        """使用非法账户名进行注册"""

        mokuai = "用户注册"
        account = ["123456","a1234","abc123456789012345678901234567890","a!@#$%^&","1abcdefg"]
        passwd = "12345678"
        url = config.testurl + "/reg/mobile/add"
        data = {}
        data['password'] = passwd
        for i in account:
            data['account'] = i
            mobile = "1381234" + str(random.randint(1000,9999))
            data['mobilePhone'] = mobile
            code = requests.post(config.testurl + "/reg/sms/code?mobile=" + mobile)
#            print(code.text)
            tmp = code.json()['data']
            data['code'] = tmp
#            print(data)
            reg = requests.post(url, headers=self.postheader, data=json.dumps(data))
            print(reg.text)
            if reg.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
            self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), reg.text, reg.status_code, round(reg.elapsed.total_seconds(),5), self.illegalAccountRegist.__doc__, result)
        return None

if __name__ == "__main__":
    runtest = userFind()
    runtest.phoneFind()
