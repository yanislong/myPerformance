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

class userregist():

    def __init__(self):
        self.sqldata = lhlSql()
        self.portalsql = portalSql()
        self.postheader = {}
        self.postheader['Content-Type'] = "application/json"
        self.account = config.account
        self.mobile = config.mobile
        self.noAccount = config.noAccount
        self.passwd = config.passwd
        pass

    def phoneRegist(self):
        """使用合法账号名进行注册"""

        tmp = []
        mokuai = "用户注册"
        for ll in range(len(self.account)):
            tmp.append((self.account[ll],self.mobile[ll]))
        url = config.testurl + "/reg/mobile/add"
        data = {}
        data['password'] = self.passwd
        for i in tmp:
            acc = requests.post(config.testurl + "/reg/exist/account?account=" + str(i[0]))
#            print(acc.text)
            if acc.json()['data'] == True:
                self.portalsql.delUser(str(i[0]))
            pho = requests.post(config.testurl + "/reg/exist/mobile?mobile=" + str(i[1]))
#            print(pho.text)
            if pho.json()['data'] == True:
                self.portalsql.delUser(str(i[1]))
            code = requests.post(config.testurl + "/reg/sms/code?mobile=" + str(i[1]))
#            print(code.text)
            tmp = code.json()['data']
            data['code'] = tmp
            data['account'] = str(i[0])
            data['mobilePhone'] = str(i[1])
  #          print(data)
            reg = requests.post(url, headers=self.postheader, data=json.dumps(data))
            print(reg.text)
            if reg.json()['code'] == 200:
               result = "Success"
            else:
               result = "Faile"
            self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), reg.text, reg.status_code, round(reg.elapsed.total_seconds(),5), self.phoneRegist.__doc__, result)
            time.sleep(1)
        return None

    def illegalAccountRegist(self):
        """使用非法账户名进行注册"""

        mokuai = "用户注册"
        url = config.testurl + "/reg/mobile/add"
        data = {}
        data['password'] = self.passwd
        for i in self.noAccount:
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
    runtest = userregist()
    #runtest.phoneRegist()
    runtest.illegalAccountRegist()