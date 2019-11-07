#!/usr/bin/env python3

import time
import hashlib


#本地数据库
mysql_host = "127.0.0.1"

#开发环境应用服务地址
#develoturl = "http://11.2.77.1:8088"

#测试环境应用服务地址
testurl = "http://11.2.77.2:8088"

#测试环境数据库
portal_host = "192.168.15.21"

#已注册账号手机号,长度要保持一直
account = ["lizongwu","a12345","ab0123456789","LIZONGWU","kali001"]
mobile = ["16488888612","16488888613","16488888614","16488888615","16488888616"]

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
