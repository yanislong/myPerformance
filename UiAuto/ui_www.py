import time, sys, json, random

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By

import casjc_config
import casjc_mode

    
#用户登陆
def Casjc_www_login(uname=casjc_config.devPerson["user1"], upasswd=casjc_config.adminPerson["passwd1"]):
    title = "官网用户登录"
    hailong = webdriver.Chrome()
    hailong.get(casjc_config.consoleUrl)
    hailong.maximize_window()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/login"]')))
    hailong.find_element_by_css_selector('a[href="/login"]').click()
    time.sleep(casjc_config.show_time)
    hailong.find_element_by_css_selector("input[type='text']").send_keys(uname)
    hailong.find_element_by_css_selector('input[type="password"]').send_keys(upasswd)
    hailong.find_element_by_tag_name('button').click()
    #等待casjc_config.wait_time全局设置时间(10秒)，判断是否登录成功进入首页
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="console"]')))
        if hailong.find_elements_by_css_selector('div[class="console"]')[0].text == "控制台":
            casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "官网登录成功" ]
            if __name__ == "__main__":
                hailong.quit()
            return hailong
        else:
            casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "官网登录失败" ]
            hailong.quit()
            return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "官网登录失败" ]
        hailong.quit()
        return None

#邮箱用户注册
def Casjc_www_mail_regist():
    title = "邮箱注册"
    hailong = webdriver.Chrome()
    hailong.get(casjc_config.consoleUrl)
    hailong.maximize_window()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/register"]')))
    hailong.find_element_by_css_selector('a[href="/register"]').click()
    time.sleep(casjc_config.show_time)
    #输入用户账户
    account = "uireg" + time.strftime("%m%d%H%M%S",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys(account)
    #输入密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys(casjc_config.regpasswd)
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys(casjc_config.regpasswd)
    #输入邮箱
    tmpmail = casjc_mode.Casjc_mail()
    #tmpmail = "mhuzcd28730@chacuo.net"
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys(tmpmail[0])
    #点击页面使邮箱输入框失去焦点
    hailong.find_element_by_css_selector('div[class="wrap-reg"]').click()
    time.sleep(casjc_config.show_time)
    #点击获取验证码按钮    
    hailong.find_element_by_css_selector('div[class="yzm"]').click()
    time.sleep(casjc_config.short_time)
    mailcode = casjc_mode.Casjc_mailcode(tmpmail)
    if not mailcode:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = ["", "邮箱: " + tmpmail[0] +" 发送验证码后，200秒没有收到验证码"]
        hailong.quit()
        return None
    #输入验证码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(mailcode)
    #点击注册按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    time.sleep(casjc_config.show_time)
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="nav-login"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = ["", "账号: " + account + "邮箱: " + tmpmail[0] + " 注册成功"]
        time.sleep(casjc_config.show_time)
        hailong.quit()
        return account
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = ["", "账号: " + account + "邮箱: " + tmpmail[0] + " 注册失败"]
        hailong.quit()
        return None

#手机用户注册
def Casjc_www_phone_regist():
    title = "手机号注册"
    hailong = webdriver.Chrome()
    hailong.get(casjc_config.consoleUrl)
    hailong.maximize_window()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/register"]')))
    hailong.find_element_by_css_selector('a[href="/register"]').click()
    time.sleep(casjc_config.show_time)
    #点击手机号注册tab
    hailong.find_element_by_id('tab-phone').click()
    time.sleep(casjc_config.show_time)
    #输入用户账户
    account = "uireg" + time.strftime("%m%d%H%M%S",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(account)
    #输入密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(casjc_config.regpasswd)
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys(casjc_config.regpasswd)
    #输入邮箱
    #tmpmail = casjc_mode.Casjc_mail()
    tmpphone = "17344432202"
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[8].send_keys(tmpphone)
    #点击页面使邮箱输入框失去焦点
    hailong.find_element_by_css_selector('div[class="wrap-reg"]').click()
    time.sleep(casjc_config.show_time)
    #点击获取验证码按钮    
    hailong.find_element_by_css_selector('div[class="yzm"]').click()
    time.sleep(casjc_config.short_time)
    #输入验证码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[9].send_keys("123456")
    #点击注册按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[1].click()
    time.sleep(casjc_config.show_time)
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="nav-login"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = ["", "账号: " + account + "手机号: " + tmpphone + " 注册失败"]
        hailong.quit()
        return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = ["", "账号: " + account + "手机号: " + tmpphone + " 注册失败"]
    hailong.quit()
    return None

#通过首页试用按钮进行登录
def Casjc_www_try(uname="aa123", upasswd="123456aA~"):
    title = "官网通过试用申请登录"
    hailong = webdriver.Chrome()
    hailong.get(casjc_config.consoleUrl)
    hailong.maximize_window()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '申请试用')))
    hailong.find_element_by_link_text('申请试用').click()
    time.sleep(casjc_config.short_time)
    #弹出提示框,选择马上登录
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--default el-button--small el-button--primary "]')))
    hailong.find_element_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]').click()
    time.sleep(casjc_config.show_time)
    hailong.find_element_by_css_selector("input[type='text']").send_keys(uname)
    hailong.find_element_by_css_selector('input[type="password"]').send_keys(upasswd)
    hailong.find_element_by_tag_name('button').click()
    #等待casjc_config.wait_time全局设置时间(10秒)，判断是否登录成功进入首页
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="console"]')))
        if hailong.find_elements_by_css_selector('div[class="console"]')[0].text == "控制台":
            casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "登录成功"]
            if __name__ == "__main__":
                hailong.quit()
            return hailong
        else:
            casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "登录失败"]
            hailong.quit()
            return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "登录失败"]
        hailong.quit()
        return None

    
if __name__ == "__main__":
    print (">> UI自动化脚本开始执行执行")
    start_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    Casjc_www_login()
    Casjc_www_mail_regist()
    Casjc_www_phone_regist()
    Casjc_www_try()
    end_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print ("开始时间： " + start_time)
    print ("结束时间： " + end_time)
    print (">> UI自动化脚本执行完成")
    print(casjc_config.casjc_result)
    casjc_mode.Run_result(("www",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
