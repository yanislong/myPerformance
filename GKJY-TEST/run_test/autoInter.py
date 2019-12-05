#!/usr/bin/env python3

import requests
import sys, json, re
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/integrateTest')
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/integrateTest/user')
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test')

import userLogin
from lhlmysql.lhlsql import lhlSql

class lhl:
    
    def __init__(self):
        self.getheader = {}
        self.postheader_json = {}
        self.postheader_www = {}
        try:
            self.session = userLogin.userlogin().accountLogin()
        except requests.exceptions.ConnectionError:
            self.session = ""
            print('没有身份认证信息')
        self.timeout = 12
        self.getheader['Authorization'] = self.session
        self.postheader_json['Authorization'] = self.session 
        self.postheader_www['Authorization'] = self.session 
        self.postheader_json['Content-Type'] = "application/json"
        self.postheader_www['Content-Type'] = "application/x-www-form-urlencoded"
        pass

    def respondGet(self, result_code, url, header="", param=""):
        """
        请求时需要4个参数，预期的响应code, 完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.getheader['Cookie'] = header
        if not self.__analysisUrl(url):
            return None
        try:
            param = json.loads(param)
        except json.decoder.JSONDecodeError:
            param = {}
        try:
            res = s.get(url, headers=self.getheader, params=param, timeout=self.timeout)
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
        print(res.status_code)
        print(res.url)
        print(res.text)
        if result_code:
            try:
                if str(res.json()['code']) == str(result_code.strip()):
                    result = 'Success'
                else:
                    result = 'Faile'
            except json.decoder.JSONDecodeError:
                result = "Error"
            except KeyError:
                result = "Error"
        else:
            result = "None"
       # print(res.text.encode('utf-8').decode('utf-8'),res.elapsed.total_seconds(),res.status_code)
        rep = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code, 'result':result}
        return rep
   
    def respondPost(self, result_code, url, header="", data={}):
        """
        请求时需要4个参数，预期的响应code, 完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        try:
            data = json.loads(data)
        except json.decoder.JSONDecodeError:
            data = {}
        s = requests.session()
        if header.strip() == "json":
            try:
                res = s.post(url, headers=self.postheader_json, data=json.dumps(data), timeout=self.timeout)
            except requests.exceptions.MissingSchema:
                print('请求的Url地址有误')
                return None
            except requests.exceptions.ConnectionError:
                print("请求URL无法连接")
                return None
            print(res.url)
            print(data)
            print(res.text,res.elapsed.total_seconds(),res.status_code)
        else:
            try:
                res = s.post(url, headers=self.postheader_www, data=data, timeout=self.timeout)
            except requests.exceptions.MissingSchema:
                print('请求的Url地址有误')
                return None
            except requests.exceptions.ConnectionError:
                print("请求URL无法连接")
                return None
            print(res.url)
            print(data)
            print(res.text,res.elapsed.total_seconds(),res.status_code)
        if result_code:
            try:
                if str(res.json()['code']) == str(result_code.strip()):
                    result = 'Success'
                else:
                    result = 'Faile'
            except json.decoder.JSONDecodeError:
                result = "Error"
            except KeyError:
                result = "Error"
        else:
            result = "None"
        rep = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code, 'result':result}
        return rep

    def respondPut(self, url, header="", data={}):
        """
        请求时需要3个参数，预期的响应code, 完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.pheader['Cookie'] = header
        try:
            res = s.get(url, headers=self.pheader, data=data, timeout=self.timeout)
        except requests.exceptions.MissingSchema:
            print('请求的Url地址有误')
            return None
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
       # print(res.text.encode('utf-8').decode('utf-8'),res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime': res.elapsed.total_seconds(), 'code': res.status_code}
        return result

    def __analysisUrl(self,myurl):
        """url规则: 只有字母和数字[0-9a-zA-Z]、一些特殊符号"$-_.+!*'(),"[不包括双引号]、
        以及某些保留字，才可以不经过编码直接用于URL。"""
        l1 = re.compile('^https?:/{2}[0-9a-zA-Z$-_.+!*$&?]+$')
        l2 = l1.findall(myurl)
        l3 = re.match('^https?:/{2}[0-9a-zA-Z$-_.+!*$:/]+', myurl)
        if l3:
            return True
        else: 
            print("url格式有误")
            return None

    def runTest(self):
    #    aaa = [(1722, '个人中心', 'http://10.0.115.18:7474/portal-test/user/person/get', '', '{"": ""}', 'get', '杨东升', '获取当前登录人信息\n（有效的token值）', '200')]
        sqldata = lhlSql()
        mydata = sqldata.getAllInterface()
        for i in mydata:
            print(i)
            if i[5].lower() == "get":
                resGet = self.respondGet(i[8],i[2].strip(),i[3],i[4])
                if resGet:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resGet['body'],resGet['code'],round(resGet['respondTime'],5),i[7],resGet['result'])
                continue
            if i[5].lower() == "post":
                resPost = self.respondPost(i[8],i[2].strip(),i[3],i[4])
                if resPost:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7],resPost['result'])
                continue
            if i[5].lower() == "put":
                resPut = self.respondPut(i[2].strip(),i[3],i[4])
                if resPut:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7])
                continue
            else:
                print("请求方式或参数有误不存在")
        return None

    def oneTest(self,rid):
        sqldata = lhlSql()
        onedata = sqldata.getIdInterface(rid)
        for i in onedata:
            print(i)
            if i[5].lower() == "get":
                resGet = self.respondGet(i[8],i[2].strip(),i[3],i[4])
                if resGet:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resGet['body'],resGet['code'],round(resGet['respondTime'],5),i[7],resGet['result'])
                continue
            if i[5].lower() == "post":
                resPost = self.respondPost(i[8],i[2].strip(),i[3],i[4])
                if resPost:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7],resPost['result'])
                continue
            if i[5].lower() == "put":
                resPut = self.respondPut(i[2].strip(),i[3],i[4])
                if resPut:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7])
                continue
            else:
                print("请求方式或参数有误不存在")
        return None

if __name__ == "__main__":
    a = lhl()
    #a._lhl__analysisUrl("http://www.baidu.com:9090/123/abc")
    a.runTest()
    pass
