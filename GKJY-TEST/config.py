#!/usr/bin/env python3

import time
import hashlib

#平台名称
name = "国科晋云"

#本地数据库
mysql_host = "127.0.0.1"
mysqluser = "root"
mysqlpasswd = "root"

#开发环境应用服务地址
#develoturl = "http://11.2.77.1:8088"

#测试环境应用服务地址
url = "http://11.2.77.3"
userurl = url + "/portal-test/user"
orderurl = url + "/portal-test/order"
joburl = url + "/portal-test/job"
contracturl = url + "/portal-test/contract"

#测试环境数据库
mysqlportal_host = "192.168.15.21"
mysqlportal_user = "root"
mysqlportal_passwd = "Test~107443"

#注册不删除用户
useaccount = {'lizongwu':'17344432202'} #,'LIZONGWU':'335916781@qq.com'}

#已注册账号手机号,长度要保持一直
account = ["test123test","a12345","ab012345678901234567890123456789","LIXIAOFENG","kali001"]
mobile = ["16688888612","16688888613","16688888614","16688888615","16688888616"]

#非法账号名
noAccount = ["0123456","a1234","abc123456789012345678901234567890","a!@#$%^&","1abcdefg","root","admin","administrator",""," ",None]

#通用密码
passwd = "12345678"

def mm(parm):
    m1 = hashlib.md5(parm.encode())
    return m1.hexdigest()

def mydatatime():
    return time.strftime("%m%d %H%M%S",time.localtime())

if __name__ == "__main__":
    pass
