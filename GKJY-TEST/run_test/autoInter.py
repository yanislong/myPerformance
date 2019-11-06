#!/usr/bin/env python3

import sys, json, re
import requests
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test')

from lhlmysql.lhlsql import lhlSql

class lhl:
    
    def __init__(self):
        self.pheader = {}
        self.getheader = {}
        self.timeout = 12
        self.pheader['Content-Type'] = "application/json"
        self.getheader['Content-Type'] = "application/x-www-form-urlencoded"
        pass

    def respondGet(self, result_code, url, header="", param=""):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.getheader['Cookie'] = header
        self.getheader['Authorization'] = header 
        if not self.__analysisUrl(url):
            return None
        try:
            res = s.get(url, headers=self.getheader, params=param, timeout=self.timeout)
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
        print(res.status_code)
        if result_code:
            if str(res.json()['code']) == str(result_code.strip()):
                result = 'True'
            else:
                result = 'False'
        else:
            result = "None"
       # print(res.text.encode('utf-8').decode('utf-8'),res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code, 'result':result}
        return result
   
    def respondPost(self, result_code, url, header="", data={}):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.pheader['Cookie'] = header
        self.pheader['Authorization'] = header 
        try:
            res = s.post(url, headers=self.pheader, data=data, timeout=self.timeout)
        except requests.exceptions.MissingSchema:
            print('请求的Url地址有误')
            return None
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
       # print(res.text,res.elapsed.total_seconds(),res.status_code)
        if result_code:
            if str(res.json()['code']) == str(result_code.strip()):
                result = 'True'
            else:
                result = 'False'
        else:
            result = "None"
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code, 'result':result}
        return result

    def respondPut(self, url, header="", data={}):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.pheader['Cookie'] = header
        self.pheader['Authorization'] = header 
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

    def runTest(self,hd):
        sqldata = lhlSql()
        mydata = sqldata.getAllInterface()
        for i in mydata:
            print(i)
            if i[5].lower() == "get":
                resGet = self.respondGet(i[8],i[2].strip(),hd,i[4])
                if resGet:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resGet['body'],resGet['code'],round(resGet['respondTime'],5),i[7],resGet['result'])
                continue
            if i[5].lower() == "post":
                resPost = self.respondPost(i[8],i[2].strip(),hd,i[4])
                if resPost:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7],resPost['result'])
                continue
            if i[5].lower() == "put":
                resPut = self.respondPut(i[2].strip(),hd,i[4])
                if resPut:
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],5),i[7])
                continue
            else:
                print("请求方式或参数有误不存在")
        return None


if __name__ == "__main__":
    hd = "cc7bce88-a9b2-434c-837b-ec9166717eb0"
    a = lhl()
    #print(dir(a))
    #a._lhl__analysisUrl("http://www.baidu.com:9090/123/abc")
    a.runTest(hd)
    pass
