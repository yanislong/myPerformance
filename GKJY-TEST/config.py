#!/usr/bin/env python3

import time
import hashlib

#################全局配置################################

#测试平台名称
name = "国科晋云"
#追求真相
saying = "根本没有巧合, 巧合是种错觉"
#首页外链bug平台地址
bugurl = "https://www.tapd.cn/company/participant_projects"
#接口模块
intermode = ['user','order','job','flow','account','contract','invoice','file','messcenter','org','ldap']
#接口请求方法
option = ['get','post']
#接口开发者
author = ['杨东升','杜丽','丁旭','张亚辉','梁永全']
#是否开启身份认证
authorized = ""#True
#是否开启音乐
#music = "autoplay"
music = ""

#################################################

#########################数据库,服务器地址配置#############################

#本地数据库
mysql_host = "127.0.0.1"
mysqluser = "root"
mysqlpasswd = "root"

#开发环境应用服务地址
#develoturl = "http://11.2.77.1:8088"

#测试环境应用服务地址
#url = "http://11.2.77.3"
testurl = "11.2.77.1"
url = "http://11.2.77.1"
#接口模块地址
userurl = url + "/portal/user"
orderurl = url + "/portal/order"
joburl = url + "/portal/job"
orgurl = url + "/portal/org"
contracturl = url + "/portal/contract"

#测试环境数据库
mysqlportal_host = "192.168.15.21"
mysqlportal_user = "root"
mysqlportal_passwd = "Test~107443"

######################################################################

####################测试数据####################################

#注册不删除用户
#useaccount = {'lizongwu':'17344432202'} #,'LIZONGWU':'335916781@qq.com'}
#useaccount = {'Demo001':'17344432202'}
#useaccount = {'ZhangEmailuser163':'17344432202'} 
useaccount = 'yanislong'

#通用密码
#passwd = "12345678"
#passwd = "Test123456!"
#passwd = "Zhang@2019"
passwd = "ODc3ZmFkND"

#已注册账号手机号,长度要保持一直
account = ["test123test","a12345","ab012345678901234567890123456789","LIXIAOFENG","kali001"]
mobile = ["16688888612","16688888613","16688888614","16688888615","16688888616"]

#非法账号名
noAccount = ["0123456","a1234","abc123456789012345678901234567890","a!@#$%^&","1abcdefg","root","admin","administrator",""," ",None]

############################################################################

######################全局方法###############################

#提供参数,返回MD5值
def mm(parm):
    m1 = hashlib.md5(parm.encode())
    return m1.hexdigest()

#返回当前时间
def mydatatime():
    return time.strftime("%m%d %H%M%S",time.localtime())

#返回11位随机数([0-9a-zA-Z])
def suiji():
    a = ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a','Z','Y','X','U','V','W','Q','E','R','T','I','O','P','A','S','D','F','G','H','H','J','K','L','C','B','N','M','1','2','3','4','5','6','7','8','0','9'], 11))
    return a

#####################################################

if __name__ == "__main__":
    pass
