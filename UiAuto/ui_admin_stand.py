import time, sys, json, random
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#get直接返回，不再等待界面加载完成
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"


import casjc_config
import casjc_mode
import casjc_page
import casjc_log
 

#新建资源池
def create_resource(yw="Slurm"):
    print(yw)
    """ yw = [Slurm,Parastor, GPFS ]"""
    title = "新建资源池"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    casjc_log.logging.info(title + " 点击新建资源池")
    #点击新增资源池按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary el-button--small"]').click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[class="el-input__inner"]')))
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].click()
    time.sleep(casjc_config.short_time)
    #确定选定的业务类型
    for i in hailong.find_elements_by_xpath('//li[@class="el-select-dropdown__item"]/span'):
        if i.text == yw:
            i.click()
            if yw == "Slurm":
                #输入资源池名称
                hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys('我的资源池名称' + yw)
                #选择认证服务器
                hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].click()
                time.sleep(casjc_config.short_time)
                hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
            elif yw == "GPFS" or yw == "Parastor":
                #输入资源池名称
                hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys('我的资源池名称' + yw)
                #选择关联资源池
                hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].click()
                time.sleep(casjc_config.short_time)
                hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[5].click()
                #选择认证服务器
                hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].click()
                time.sleep(casjc_config.short_time)
                hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#编辑资源池
def modify_resource():
    title = "编辑资源池"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    casjc_log.logging.info(title + " 点击列表第一行的编辑按钮")
    #点击编辑资源池按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[class="el-input__inner"]')))
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#同步系统账号
def sync_user():
    title = "同步系统账号"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    hailong.find_element_by_css_selector('i[class="el-icon- iconfont iconjiqun"]').click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/authentication"]')))
    hailong.find_element_by_css_selector('li[data-index="/authentication"]').click()
    casjc_log.logging.info(title + " 点击同步系统账号按钮")
    #点击同步系统账号按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[1].click()
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#新建系统用户
def add_adminuser():
    title = "新建系统用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击新增系统用户按钮
    casjc_log.logging.info(title + " 点击新增系统用户按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary el-button--small"]').click()
    #弹出新增系统用户弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    #输入用户账号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys("test")
    #输入姓名
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys("我爱测试tester")
    #输入邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys("test@casjc.com")
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys("13112341234")
    #输入固定电话
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys("010-88561234")
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#编辑系统用户
def edit_adminuser():
    title = "编辑系统用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击编辑系统用户按钮
    casjc_log.logging.info(title + " 点击系统用户列表第一行的编辑按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[0].click()
    #弹出编辑系统用户弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'form[class="el-form newEditUser"]')))
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None



#系统用户修改密码
def change_passwd():
    title = "系统用户修改密码"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击修改密码按钮
    casjc_log.logging.info(title + " 点击系统用户列表第一行的修改密码按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
    #弹出修改密码弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'form[class="el-form newEditUser"]')))
    #输入新密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-2].send_keys("123123aA~")
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].send_keys("123123aA~")
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None

#禁用系统用户
def offorup():
    title = "禁用系统用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击修改密码按钮
    casjc_log.logging.info(title + " 点击系统用户列表第一行的禁用/启用按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[2].click()
    #弹出确认提示框弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__title"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]').click()
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#删除系统用户
def del_user():
    title = "删除系统用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击修改密码按钮
    casjc_log.logging.info(title + " 点击系统用户列表第一行的删除按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[3].click()
    #弹出确认提示框弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__title"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]').click()
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None



#新建控制台用户
def add_consoleuser():
    title = "新建控制台用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-控制台用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击新增控制台用户按钮
    casjc_log.logging.info(title + " 点击新增控制台用户按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary el-button--small"]').click()
    #弹出新增控制台用户弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    #输入用户账号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys("controltest")
    #输入姓名
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys("我爱测试tester")
    #输入邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys("controltest@casjc.com")
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys("13112341235")
    #输入固定电话
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys("010-88561234")
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#编辑控制台用户
def edit_consoleuser():
    title = "编辑控制台用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-控制台用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击编辑控制台用户按钮
    casjc_log.logging.info(title + " 点击控制台用户列表第一行的编辑按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[0].click()
    #弹出编辑控制台用户弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'form[class="el-form newEditUser"]')))
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None



#控制台用户修改密码
def change_consolepasswd():
    title = "控制台用户修改密码"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-控制台用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击修改密码按钮
    casjc_log.logging.info(title + " 点击控制台用户列表第一行的修改密码按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
    #弹出修改密码弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'form[class="el-form newEditUser"]')))
    #输入新密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-2].send_keys("123123aA~")
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].send_keys("123123aA~")
    try:
        #点击保存
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击保存按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None

#禁用/启用控制台用户
def offorup_console():
    title = "禁用控制台用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-控制台用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击禁用/启用按钮
    casjc_log.logging.info(title + " 点击控制台用户列表第一行的禁用/启用按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[2].click()
    #弹出确认提示框弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__title"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]').click()
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None


#删除控制台用户
def del_consoleuser():
    title = "删除控制台用户"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-控制台用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击删除按钮
    casjc_log.logging.info(title + " 点击控制台用户列表第一行的删除按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[3].click()
    #弹出确认提示框弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__title"]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]').click()
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None



#测试邮箱
def test_mail():
    title = "测试邮箱"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-系统通知
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/notification"]')))
    hailong.find_element_by_css_selector('li[data-index="/notification"]').click()
    #点击设置按钮
    casjc_log.logging.info(title + " 点击系统通知页面设置按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'span[class="btn"]')))
    hailong.find_elements_by_xpath('//span[@class="btn"]/span')[0].click()
    #弹出发件设置弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    #输入发件服务器地址
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys("smtp.qq.com")
    #输入端口号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys("25")
    #输入发件箱地址
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys("251737718@qq.com")
    #输入邮箱密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys("thuerngymkpqbgfa")
    try:
        #点击邮箱测试按钮
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击邮箱测试按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'p[class="el-message__content"]')))
        if len(hailong.find_element_by_css_selector('p[class="el-message__content"]').text) == 0:
            casjc_log.logging.info("获取请求响应消息为空")
            casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "操作异常: 获取请求响应消息为空"]
            hailong.quit()
            return None
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "请求响应:" + hailong.find_element_by_css_selector('p[class="el-message__content"]').text]
        hailong.quit()
        return None
    except exceptions.TimeoutException:
        imagename = time.strftime("%m%d%H%M%S") + '.png'
        self.hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info("没有获取到响应消息,查看截图 %s" %imagename)
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 操作异常"]
        hailong.quit()
        return None


#设置邮箱
def set_mail():
    title = "设置邮箱"
    #登录
    hailong = webdriver.Chrome()
    uname = myconfig["username"]
    upasswd = myconfig['passwd']
    uurl = myconfig['adminUrl']
    aaa = casjc_page.Casjc_std_admin(hailong,uname,upasswd,uurl)
    #点击系统管理一级菜单
    casjc_log.logging.info(title + " 点击系统管理一级菜单")
    hailong.find_elements_by_css_selector('div[class="nav-item"]')[-1].click()
    #点击二级菜单-系统通知
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/notification"]')))
    hailong.find_element_by_css_selector('li[data-index="/notification"]').click()
    #点击设置按钮
    casjc_log.logging.info(title + " 点击系统通知页面设置按钮")
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'span[class="btn"]')))
    hailong.find_elements_by_xpath('//span[@class="btn"]/span')[0].click()
    #弹出发件设置弹窗
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    #输入发件服务器地址
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys("smtp.qq.com")
    #输入端口号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys("25")
    #输入发件箱地址
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys("251737718@qq.com")
    #输入邮箱密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].clear()
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys("thuerngymkpqbgfa")
    try:
        #点击邮箱测试按钮
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--small"]')))
        casjc_log.logging.info(title + " 点击邮箱测试按钮")
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'p[class="el-message__content"]')))
        time.sleep(casjc_config.show_time)
        #点击确定按钮
        hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[1].click()
    except exceptions.TimeoutException:
        imagename = title + time.strftime("%m%d%H%M%S") + '.png'
        hailong.save_screenshot(r'C:\usr\Apache24\htdocs\image\\' + imagename)
        casjc_log.logging.info(title + " 点击保存按钮异常,查看截图 %s" % imagename)
    #获取提交返回结果
    aaa.admin_result(title,uname)
    return None
    



if __name__ == "__main__":
    try:
        if sys.argv[1] == "std":
            myconfig = casjc_config.stdPerson['admin']
            env = "std"
    except IndexError:
        myconfig = casjc_config.stdPerson['admin']
        env = "std"
    casjc_log.logging.info(">" * 15 + " UI自动化脚本开始执行执行 " + "<" * 15)
    start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    
    #create_resource("Slurm")
    #create_resource("GPFS")
    modify_resource()
    sync_user()
    set_mail()
    test_mail()
    add_adminuser()
    edit_adminuser()
    change_passwd()
    offorup()
    del_user()
    add_consoleuser()
    edit_consoleuser()
    change_consolepasswd()
    offorup_console()
    del_consoleuser()   
    
    end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    print ("开始时间： " + start_time)
    print ("结束时间： " + end_time)    
    print (json.dumps(casjc_config.casjc_result,ensure_ascii=False))
    casjc_mode.Run_result(("standard",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False),env))
    casjc_log.logging.info( ">" * 15 + " 模块名: standard, 本次UI自动化脚本执行完成，通过页面模块筛选查看执行结果 " + "<" * 15)
