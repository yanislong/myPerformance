#!/usr/bin/env python3

import requests
import json
import sys
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/lhlmysql')
sys.path.append('/root/lhl/myPerformance/GKJY-TEST')

from lhlsql import lhlSql, portalSql
import config

class userlogin():

    def __init__(self):
        self.sqldata = lhlSql()
        self.portalsql = portalSql()
        self.postheader = {}
        self.postheader['Content-Type'] = "application/json"
        self.account = config.useaccount
        self.mobile = config.mobile
        self.url = config.userurl
        pass

    '''
    #去掉手机号登录方式
    def phoneLogin(self):
        """使用已注册手机号进行登录"""

        mokuai = "用户登录"
        data = {}
        url = config.testurl + "/login/mobile"
        for i in self.mobile:
            cod = requests.post(config.testurl + "/login/code?mobile=" + i)
#            print(cod.text)
            data['mobile'] = i
            data['code'] = cod.json()['data']
#            print(pdata)
            res = requests.post(config.testurl + "/login/mobile", headers=self.postheader, data=json.dumps(data))
            print(res.text)
            if res.json()['code'] == 200:
               result = "Success"
            else:
               result = "Faile"
            self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.phoneLogin.__doc__, result)
        return None
    '''

    def accountLogin(self):
        """使用已注册账号进行登录"""

        mokuai = "用户登录"
        passwd = "12345678"
        data = {}
        data['password'] = passwd
        data['rememberMe'] = True
        url = self.url + "/login/account"
        for j in self.account.keys():
            data['account'] = j
            res = requests.post(url, headers=self.postheader, data=json.dumps(data))
            print(res.text)
            if res.json()['code'] == 200:
               result = "Success"
            else:
               result = "Faile"
            if __name__ == "__main__":
                self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.accountLogin.__doc__, result)
        return res.json()['data']

    def wpassLogin(self):
        """使用正确账号与错误密码进行登录"""

        mokuai = "用户登录"
        passwd = "11111111"
        data = {}
        data['password'] = passwd
        data['rememberMe'] = True
        url = self.url + "/login/account"
        for j in self.account.keys():
            data['account'] = j
            res = requests.post(url, headers=self.postheader, data=json.dumps(data))
            print(res.text)
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
            self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(data), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.wpassLogin.__doc__, result)
        return res.json()['data']

if __name__ == "__main__":
    runtest = userlogin()
    runtest.accountLogin()
    #runtest.wpassLogin()
