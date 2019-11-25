#!/usr/bin/env python3

import requests
import threading
import json, sys, random
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/lhlmysql')
sys.path.append('/root/lhl/myPerformance/GKJY-TEST')
sys.path.append("/root/lhl/myPerformance/GKJY-TEST/run_test/integrateTest/user")

from lhlsql import lhlSql, portalSql
import config
import userLogin

class orderManag():

    def __init__(self):
        self.sqldata = lhlSql()
        self.portalsql = portalSql()
        self.session = userLogin.userlogin()
        self.postheader = {}
        self.postheader['Content-Type'] = "application/json"
        self.postheader['Authorization'] = self.session.accountLogin()
        self.url = config.orderurl
        pass

    def addorder(self):
        """使用合法数据申请资源"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        url = self.url + "/order/addOrder"
        param = {}
        param["applyNumber"] = ""
        param["applyParty"] = 1
        param["approveStep"] = ""
        param["areaId"] = 0
        param["areaInfo"] = ""
        param["avgDiscount"] = 0
        param["discountPrice"] = 0
        param["entCompanyId"] =  0
        param["entCompanyName"] = "1"
        param["entExist"] = 0
        param["entId"] = 0
        param["entMail"] = "1"
        param["entPhone"] = "1"
        param["orderId"] = 123
        param["orderNumber"] = ""
        param["orderType"] = 0
        param["productType"] = 0
        param["projectName"] = "1"
        reslist=[{"level": 0,"parentId": 0,"resId": 0,"resInfo": "","totalNumber": 0,"unitPrice": 0,"useNumber": 0}]
        resvolist = [{"discount": 0,"number": 0,"orderResId": 0,"price": 0,"resId": 0,"validDays": 0,"validUnit": "","resList":reslist }]
       	param["resVOList"] = resvolist
        param["salesUserId"] = 12
        param["salesUserName"] = "小翠"
        param["status"] = 2
        param["totalPrice"] = 0
        param["userId"] = 11
        for j in roleName:
            res = requests.post(url, headers=self.postheader, data=json.dumps(param))
            print(res.text)
        try:
            if res.json()['code'] == 200:
                result = "Success"
            else:
                result = "Faile"
        except KeyError:
            result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.addorder.__doc__, result)
        return None

    def applyorder(self):
        """资源申请列表"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['pageNum'] = "1"
        param['pageSize'] = "10"
        param['applyNumber'] = "1"
        for j in roleName:
            url = self.url + "/order/applyOrderList"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.applyorder.__doc__, result)
        return None

    def getorder(self):
        """我的申请单列表"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['pageNum'] = "1"
        param['pageSize'] = "10"
        for j in roleName:
            url = self.url + "/order/myOrderList"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.getorder.__doc__, result)
        return None

    def delorder(self):
        """删除订单"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['orderId'] = "1"
        for j in roleName:
            url = self.url + "/order/delOrder"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.delorder.__doc__, result)
        return None

    def orderinfo(self):
        """订单详情"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['orderId'] = "1"
        for j in roleName:
            url = self.url + "/order/getOrder"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.orderinfo.__doc__, result)
        return None

    def apvorderlist(self):
        """待审批资源列表"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['pageNum'] = "1"
        param['pageSize'] = "1"
        param['applyNumber'] = "1"
        for j in roleName:
            url = self.url + "/order/apvOrderList"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.apvorderlist.__doc__, result)
        return None

    def apvorder(self):
        """审批"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['status'] = "1"
        param['taskId'] = "1"
        param['opinion'] = "1"
        for j in roleName:
            url = self.url + "/order/apvOrder"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.apvorder.__doc__, result)
        return None

    def updateorder(self):
        """提交订单"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param["applyNumber"] = "a1"
        param["applyParty"] = 0
        param["approveStep"] = "a2"
        param["areaId"] = 0
        param["areaInfo"] = "a3"
        param["avgDiscount"] = 0
        param["discountPrice"] = 0
        param["entCompanyId"] = 0
        param["entCompanyName"] = "a4"
        param["entExist"] = 0
        param["entId"] = 0
        param["entMail"] = "a5"
        param["entPhone"] = "a6"
        param["orderId"] = 0
        param["orderNumber"] = "a7"
        param["orderType"] = 0
        param["productType"] = 0
        param["projectName"] = "a8"
        param["salesUserId"] = 0
        param["salesUserName"] = "a11"
        param["status"] = 0
        param["totalPrice"] = 0
        param["userId"] = 0
        reslist = [{"level": 0,"parentId": 0,"resId": 0,"resInfo": "a9","totalNumber": 0,"unitPrice": 0,"useNumber": 0}]
        param["resVOList"] = [{"discount": 0, "number": 0, "orderResId": 0, "price": 0, "resId": 0, "validDays": 0, "resList": reslist, "validUnit": "a10"}]
        for j in roleName:
            url = self.url + "/order/updateOrder"
            res = requests.post(url, headers=self.postheader, data=json.dumps(param))
            print(res.text)
        try:
            if res.json()['code'] == 200:
                result = "Success"
            else:
                result = "Faile"
        except KeyError:
            result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.updateorder.__doc__, result)
        return None

    def deployorder(self):
        """资源配置"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        for j in roleName:
            url = self.url + "/order/deployOrderRes"
            res = requests.post(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
           result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.deployorder.__doc__, result)
        return None

    def checkprice(self):
        """审批人已审批额度"""

        mokuai = "订单管理"
        roleName = ["中國石油化工集團公司中國石油化工集團公司中國石油化工集團公司"] 
        param = {}
        param['flowId'] = ""
        param['userId'] = ""
        for j in roleName:
            url = self.url + "/order/getCheckPrice"
            res = requests.get(url, headers=self.postheader, params=param)
            print(res.url)
            print(res.text)
        try:
            if res.json()['code'] != 200:
                result = "Success"
            else:
                result = "Faile"
        except KeyError:
            result = "Error"
        except json.decoder.JSONDecodeError:
            result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.checkprice.__doc__, result)
        return None

    def orderpaymanag(self):
        """根据订单号进行付款"""
    def orderpaymanag(self):
        """根据订单号进行付款"""

        mokuai = "订单支付管理"
        url = self.url + "/pay/payOrder"
        param = {}
        param['orderId'] = ""
        param['payPrice'] = ""
        param['payTimes'] = ""
        res = requests.post(url, headers=self.postheader, data=json.dumps(param))
        print(res.text)
        try:
            if res.json()['code'] == 200:
               result = "Success"
            else:
               result = "Faile"
        except KeyError:
               result = "Error"
        self.sqldata.insertInterfaceRespond(mokuai, url, json.dumps(param), res.text, res.status_code, round(res.elapsed.total_seconds(),5), self.orderpaymanag.__doc__, result)
        return None

if __name__ == "__main__":
    runtest = orderManag()
    runtest.addorder()
#    runtest.getorder()
#    runtest.applyorder()
#    runtest.orderinfo()
#    runtest.delorder()
#    runtest.apvorderlist()
#    runtest.apvorder()
#    runtest.updateorder()
#    runtest.deployorder()
#    runtest.checkprice()
#    runtest.orderpaymanag()

    tmp = []
    for i in range(0):
        t = threading.Thread(target=runtest.addrole)
        tmp.append(t)
        t.start()
    for j in tmp:
        j.join()
