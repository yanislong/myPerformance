#!/usr/bin/env python3

import pymysql

import time

class lhlSql:
    
    def __init__(self):
        self.con = pymysql.connect('10.0.115.229','root','root','portaltest')

    def getTimeInfo(self,num=0):
        cursor = self.con.cursor()
        sql = "select id, dns_time, conn_time, startData_time, total_time, updata, downdata, insertTime, content, code from qianyun limit {0},20".format(num)
        cursor.execute(sql)
        timeinfo = cursor.fetchall()
        return timeinfo

    def getDNSTime(self,startnum=0,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(dns_time) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        dns_time = cursor.fetchall()[0][0]
        return dns_time

    def getConnTime(self,startnum=0,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(conn_time) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        conn_time = cursor.fetchall()[0][0]
        return conn_time

    def getStartdataTime(self,startnum=0,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(startData_time) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        startdata_time = cursor.fetchall()[0][0]
        return startdata_time

    def getTotalTime(self,startnum=0,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(total_time) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        total_time = cursor.fetchall()[0][0]
        print(total_time)
        return total_time

    def getUpdata(self,startnum=0,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(updata) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        updata = cursor.fetchall()[0][0]
        return updata

    def getDowndata(self,startnum=1,stopnum=10):
        cursor = self.con.cursor()
        sql = "select sum(downdata) from qianyun limit {0},{1}".format(startnum,stopnum)
        cursor.execute(sql)
        downdata = cursor.fetchall()
        return downdata

    def getTotalNumber(self):
        cursor = self.con.cursor()
        sql = "select count(*) content from qianyun"
        cursor.execute(sql)
        getTotal = cursor.fetchall()
        cursor.close()
        return getTotal[0][0]
    
    def getInterfaceName(self):
        cursor = self.con.cursor()
        sql = "select distinct content from qianyun"
        cursor.execute(sql)
        Name = cursor.fetchall()
        cursor.close()
        return Name
    
    def getInterfaceList(self, num=0):
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, header, param, option, inputtime from interfaceInfo limit {0},20".format(num)
        cursor.execute(sql)
        inter = cursor.fetchall()
        cursor.close()
        return inter

    def getInterfaceRespondList(self, num=0):
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, requestparam, respondbody, code, respondtime, inputtime from interfaceRespond limit {0},20".format(num)
        cursor.execute(sql)
        inter = cursor.fetchall()
        cursor.close()
        return inter

    def getAllInterface(self):
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, header, param, option from interfaceInfo"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insertInterface(self, iname, iaddr, iheader, iparam, ioption):
        cursor = self.con.cursor()
        tt = time.strftime("%Y/%m/%d %H:%M:%S")
        sql = "insert into interfaceInfo(intername,interaddr,header,param,option,inputtime) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(iname,iaddr,iheader,iparam,ioption,tt)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        return None

    def insertInterfaceRespond(self, iname, iaddr, irequestparam, irespondbody, icode, irespondtime):
        cursor = self.con.cursor()
        tt = time.strftime("%Y/%m/%d %H:%M:%S")
        sql = "insert into interfaceRespond(intername,interaddr,requestparam,respondbody,code,respondtime,inputtime) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(iname,pymysql.escape_string(iaddr),pymysql.escape_string(irequestparam),pymysql.escape_string(irespondbody),icode,irespondtime,tt)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        return None

    def getTotalInterfaceNumber(self): 
        cursor = self.con.cursor()
        sql = "select count(*) from interfaceInfo"
        cursor.execute(sql)
        num = cursor.fetchall()[0][0]
        cursor.close()
        return num

    def getTotalInterfaceRespondNumber(self): 
        cursor = self.con.cursor()
        sql = "select count(*) from interfaceRespond"
        cursor.execute(sql)
        num = cursor.fetchall()[0][0]
        cursor.close()
        return num

    def __del__(self):
        pass

if __name__ == "__main__":
    a = lhlSql()
