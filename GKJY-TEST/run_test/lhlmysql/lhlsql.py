#!/usr/bin/env python3

import pymysql

import time

class lhlSql:
    
    def __init__(self):
        self.con = pymysql.connect('10.0.114.44','root','root','portaltest')

    def getTimeInfo(self, iname, num=0):
        """根据iname, num参数，查询20条接口响应的时间信息"""
        cursor = self.con.cursor()
        sql = "select id, dns_time, conn_time, startData_time, total_time, updata, downdata, insertTime, content, code from qianyun where content like '%{0}%'limit {1},20".format(iname, num)
        cursor.execute(sql)
        timeinfo = cursor.fetchall()
        return timeinfo

    def getTimeList(self,iname=""):
        timelist = []
        """
        根据startnum,stopnum参数，查询接口DNS响应,接口与服务器连接完成响,
        服务器开始传输数据,完成响应的整体的时间,上传和下载数据的大小
        """
        cursor = self.con.cursor()
        sql = "select sum(dns_time), sum(conn_time), sum(startData_time), sum(total_time), sum(updata), sum(downdata) from qianyun where content like '%{0}%'".format(iname)
        cursor.execute(sql)
        dns_time = cursor.fetchall()[0]
        timelist.append(dns_time)
        return timelist

    def getTotalNumber(self, iname):
        """查询qianyun表总条数"""
        cursor = self.con.cursor()
        sql = "select count(*) from qianyun where content like '%{0}%'".format(iname)
        cursor.execute(sql)
        getTotal = cursor.fetchall()
        cursor.close()
        return getTotal[0][0]
    
    def getInterfaceName(self):
        """查询qianyun表中接口的名字"""
        cursor = self.con.cursor()
        sql = "select distinct content from qianyun"
        cursor.execute(sql)
        Name = cursor.fetchall()
        cursor.close()
        return Name

    def getInterfaceInfoName(self):
        """查询interfaceInfo表中接口的名字"""
        cursor = self.con.cursor()
        sql = "select distinct intername from interfaceInfo"
        cursor.execute(sql)
        Name = cursor.fetchall()
        cursor.close()
        return Name
    
    def getInterfaceRespondName(self):
        """查询interfaceRespond表中接口的名字"""
        cursor = self.con.cursor()
        sql = "select distinct intername from interfaceRespond"
        cursor.execute(sql)
        Name = cursor.fetchall()
        cursor.close()
        return Name

    def getInterfaceList(self, iname, num=0):
        """查询interfaceInfo表中20条数据"""
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, header, param, option, inputtime from interfaceInfo where intername like '%{0}%' limit {1},20".format(iname, num)
        cursor.execute(sql)
        inter = cursor.fetchall()
        cursor.close()
        return inter

    def getInterfaceRespondList(self, iname, num=0):
        """查询interfaceRespondList表中20条数据"""
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, requestparam, respondbody, code, respondtime, inputtime from interfaceRespond where intername like '%{0}%' limit {1},20".format(iname,num)
        cursor.execute(sql)
        inter = cursor.fetchall()
        cursor.close()
        return inter

    def getAllInterface(self):
        """查询interfaceInfo表中所有数据"""
        cursor = self.con.cursor()
        sql = "select id, intername, interaddr, header, param, option from interfaceInfo"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insertInterface(self, iname, iaddr, iheader, iparam, ioption):
        """向interfaceInfo表中插入数据"""
        cursor = self.con.cursor()
        tt = time.strftime("%Y/%m/%d %H:%M:%S")
        sql = "insert into interfaceInfo(intername,interaddr,header,param,option,inputtime) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(iname,iaddr,iheader,iparam,ioption,tt)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        return None

    def insertInterfaceRespond(self, iname, iaddr, irequestparam, irespondbody, icode, irespondtime):
        """向interfaceRespond表中插入数据"""
        cursor = self.con.cursor()
        tt = time.strftime("%Y/%m/%d %H:%M:%S")
        sql = "insert into interfaceRespond(intername,interaddr,requestparam,respondbody,code,respondtime,inputtime) value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(iname,pymysql.escape_string(iaddr),pymysql.escape_string(irequestparam),pymysql.escape_string(irespondbody),icode,irespondtime,tt)
        cursor.execute(sql)
        self.con.commit()
        cursor.close()
        return None

    def getTotalInterfaceNumber(self, iname): 
        """获取interfaceInfo表中总条数"""
        cursor = self.con.cursor()
        sql = "select count(*) from interfaceInfo where intername like '%{0}%'".format(iname)
        cursor.execute(sql)
        num = cursor.fetchall()[0][0]
        cursor.close()
        return num

    def getTotalInterfaceRespondNumber(self, iname): 
        """获取interfaceRespond表中总条数"""
        cursor = self.con.cursor()
        sql = "select count(*) from interfaceRespond where intername like '%{0}%'".format(iname)
        cursor.execute(sql)
        num = cursor.fetchall()[0][0]
        cursor.close()
        return num

    def __del__(self):
        pass

if __name__ == "__main__":
    a = lhlSql()
