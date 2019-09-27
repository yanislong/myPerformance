#!/usr/bin/env python3

import sys, json
import requests

import xlrd
from lhlmysql.lhlsql import lhlSql

class lhl:
    
    def __init__(self):
        self.pheader = {}
        self.gheader = {}
        self.pheader['Content-Type'] = "appliction/json"
        pass

    def respondGet(self, url, header="", param=""):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.gheader['Cookie'] = header
        try:
            res = s.get(url, headers=self.gheader, params=param)
        except requests.exceptions.MissingSchema:
            print('请求的Url地址有误')
            return None
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
       # print(res.text.encode('utf-8').decode('utf-8'),res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code}
        return result
   
    def respondPost(self, url, header="", data={}):
        """
        请求时需要3个参数，完整url，请求header,请求参数
        函数返回一个字典{'body': , 'respondTime':, 'code':}
        """
        s = requests.session()
        self.pheader['Cookie'] = header
        try:
            res = s.post(url, headers=self.pheader, data=json.dumps(data))
        except requests.exceptions.MissingSchema:
            print('请求的Url地址有误')
            return None
        except requests.exceptions.ConnectionError:
            print("请求URL无法连接")
            return None
       # print(res.text,res.elapsed.total_seconds(),res.status_code)
        result = {'body': res.text, 'respondTime':res.elapsed.total_seconds(), 'code':res.status_code}
        return result

    def runTest(self):
        sqldata = lhlSql()
        mydata = sqldata.getAllInterface()
        for i in mydata:
            if i[5].lower() == "get":
                print(i[1])
                resGet = self.respondGet(i[2],i[3],i[4])
                if isinstance(resGet,dict):
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resGet['body'],resGet['code'],round(resGet['respondTime'],6))
            if i[5].lower() == "post":
                print(i[1])
                resPost = self.respondPost(i[2],i[3],i[4])
                if isinstance(resPost,dict):
                    sqldata.insertInterfaceRespond(i[1],i[2],i[4],resPost['body'],resPost['code'],round(resPost['respondTime'],6))
            else:
                print("请求方式或参数有误不存在")
        return None

def readInter():
    wb = xlrd.open_workbook(filename='qianyun0926.xlsx')
#    print(wb.sheet_names())
    s1 = wb.sheet_by_index(0)
    mydata = lhlSql()
    for i in range(s1.nrows):
        row = s1.row_values(i)
        mydata.insertInterface(row[0],row[2],row[1],row[4],row[3])
        print(row)

if __name__ == "__main__":
    pass
    readInter()
    a = lhl()
    a.runTest()
