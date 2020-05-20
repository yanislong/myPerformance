import time, sys, json, random

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By

import casjc_config
import casjc_mode
import casjc_page


#控制台-共享存储
def Casjc_console_upfile():
    title = "数据存储-上传文件"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #聚焦总览页面菜单产品图标
    impl = hailong.find_element_by_css_selector('i[class="el-icon-caret-bottom"]')
    tmp =  hailong.find_element_by_tag_name('body')
    chain = ActionChains(hailong)
    chain.move_to_element(impl).perform()
    time.sleep(casjc_config.short_time)
    #点击高性能计算
    aa = hailong.find_elements_by_css_selector('span[style="margin-left: 20px;"]')#[0].click
    for i in aa:
        i.click()
    chain.move_to_element(tmp).perform()
    time.sleep(casjc_config.show_time)
    #点击共享存储菜单
    hailong.find_elements_by_css_selector('b[class="iconfont iconbaocun mr10 fwn"]')[0].click()
    time.sleep(casjc_config.show_time)
    #点击上传按钮
    hailong.find_elements_by_css_selector('button[slot="reference"]')[0].click()
    time.sleep(casjc_config.short_time)
    casjc_mode.Casjc_upload(casjc_config.uppath)
    time.sleep(casjc_config.show_time)
    #获取返回信息
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="uploader-file-status"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, hailong.find_elements_by_css_selector('div[class="uploader-file-status"]')[0].text]
        time.sleep(casjc_config.show_time)
        aaa.console_logout(uname)
        return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"]
        aaa.console_logout(uname)
        return None


#控制台-高性能计算webshell
def Casjc_console_webshell():
    title = "打开webshell"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击总览页面的webshell按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    #点击webshell队列下拉列表
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].click()
    time.sleep(casjc_config.show_time)
    #选择队列
    hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    time.sleep(casjc_config.short_time)
    #hailong.quit()
    return None

#控制台-用户管理-新增用户
def Casjc_console_user():
    title = "控制台-用户管理-新增用户"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击用户管理菜单
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="rightBox"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_xpath('//div[@class="rightBox"]/div[@class="navInner navTitle"]/span[1]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="menubar"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_xpath('//ul[@role="menubar"]/li[@role="menuitem"][2]').click()
    #点击新增用户
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="handleBoxLeft"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_xpath('//div[@class="handleBoxLeft"]/button').click()
    #等待弹出心中窗口
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="dialogWrap"]')))
    time.sleep(casjc_config.short_time)
    #输入用户账号
    account = "uient" + time.strftime("%H%M%S")
    hailong.find_element_by_xpath('//div[@class="el-input el-input--medium"]/input[@type="text"][1]').send_keys(account)
    #输入用户姓名
    aname = "UI自动化企业新增用户"
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys(aname)
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys("199" + time.strftime("%m%d%H%M"))
    #输入邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #点击确定按钮
    hailong.find_element_by_xpath('//div[@class="dialog-footer"]/button[@class="el-button el-button--primary el-button--small"][1]').click()
    #获取请求结果
    aaa.console_result(title,uname,account)
    return None


#控制台-用户管理-新增工作组
def Casjc_console_group():
    title = "控制台-用户管理-新增工作组"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击用户管理菜单
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="rightBox"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_xpath('//div[@class="rightBox"]/div[@class="navInner navTitle"]/span[1]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击新增工作组
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="handleBoxLeft"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()    
    #等待新建工作组页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-tabs el-tabs--top"]')))
    time.sleep(casjc_config.short_time)
    #输入项目组
    account = "UI自动化工作组" + time.strftime("%H%M%S")
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(account)
    #选择业务
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    #选择成员
    hailong.find_elements_by_css_selector('i[class="iconfont icontianjia"]')[0].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_xpath('//div[@class="cell"]/label[@class="el-checkbox"]/span[@class="el-checkbox__input"]/span[@class="el-checkbox__inner"]')[0].click()
    #选择队列
    hailong.find_elements_by_css_selector('i[class="iconfont icontianjia"]')[1].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_xpath('//div[@class="cell"]/label[@class="el-checkbox"]/span[@class="el-checkbox__input"]/span[@class="el-checkbox__inner"]')[0].click()
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    #获取请求结果
    aaa.console_result(title,uname,account)
    return None

#控制台-用户管理-云存储调整配额
def Casjc_console_quota():
    title = "控制台-用户管理-云存储调整配额"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击用户管理菜单
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="rightBox"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_xpath('//div[@class="rightBox"]/div[@class="navInner navTitle"]/span[1]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击云存储tab
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.ID, 'tab-second')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_id('tab-second').click()    
    #等待云存储tab页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-table el-table--fit el-table--enable-row-hover el-table--enable-row-transition"]')))
    time.sleep(casjc_config.short_time)
    #获取用户名称
    account = hailong.find_elements_by_xpath('//tr[@class="el-table__row"]/td/div[@class="cell el-tooltip"]')[-5].text
    #点击调整配额
    if hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-1].text == "调整配额":
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-1].click()
    else:
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-2].click()
    #输入配额
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(casjc_config.quota_number)
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-2].click()
    #获取请求结果
    aaa.console_result(title,uname,account)
    return None

#控制台-用户管理-云存储权限设置
def Casjc_console_auth():
    title = "控制台-用户管理-云存储权限设置"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击用户管理菜单
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="rightBox"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_xpath('//div[@class="rightBox"]/div[@class="navInner navTitle"]/span[1]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击云存储tab
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.ID, 'tab-second')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_id('tab-second').click()    
    #等待云存储tab页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-table el-table--fit el-table--enable-row-hover el-table--enable-row-transition"]')))
    time.sleep(casjc_config.short_time)
    #点击权限设置
    if hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-1].text == "权限设置":
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-1].click()
        #获取用户名称
        account = hailong.find_elements_by_xpath('//tr[@class="el-table__row"]/td/div[@class="cell el-tooltip"]')[-5].text
    elif hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-3].text == "权限设置":
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[-3].click()
        #获取用户名称
        account = hailong.find_elements_by_xpath('//tr[@class="el-table__row"]/td/div[@class="cell el-tooltip"]')[-10].text
    else:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "最后两个用户没有权限设置按钮"] 
        aaa.console_logout(uname)
        return None
    #勾选组成员权限
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-dialog__body"]')))
    time.sleep(casjc_config.show_time)
    boxs = len(hailong.find_elements_by_css_selector('label[class="el-checkbox"]'))
    for i in range(boxs):
        hailong.find_elements_by_css_selector('label[class="el-checkbox"]')[i].click()
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[-1].click()
    #获取请求结果
    aaa.console_result(title,uname,account)
    return None

#控制台-个人中心-修改密码
def Casjc_console_updatepw():
    title = "控制台-个人中心-修改密码"
    #登录控制台
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_console_page(hailong,uname,upasswd)
    #进入控制台
    aaa.console()
    #点击用户头像进入个人中心
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="userinfo el-popover__reference"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_css_selector('div[class="userinfo el-popover__reference"]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击安全设置菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[class="el-menu-item"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('li[class="el-menu-item"]')[0].click()
    #点击账号密码的修改按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button p el-button--text"]')))
    hailong.find_elements_by_css_selector('button[class="el-button p el-button--text"]')[0].click()
    #输入旧密码
    oldpw = "123456aA~1"
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[class="el-input__inner"]')))
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys(upasswd)
    #输入新密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys(oldpw)
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys(oldpw)
    #点击确定按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    #获取请求结果
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/login"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "修改密码操作成功,当前密码: " + oldpw]
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 修改密码操作异常"]
        return None
    time.sleep(casjc_config.show_time)
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/login"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('a[href="/login"]')[0].click()
    time.sleep(casjc_config.show_time)
    hailong.find_element_by_css_selector("input[type='text']").send_keys(uname)
    hailong.find_element_by_css_selector('input[type="password"]').send_keys(oldpw)
    hailong.find_element_by_tag_name('button').click()
    #等待casjc_config.wait_time全局设置时间，判断是否登录成功进入首页
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="console"]')))
        if hailong.find_elements_by_css_selector('div[class="console"]')[0].text == "控制台":
            time.sleep(casjc_config.show_time)
            #casjc_config.casjc_result['控制台用户登录'+ time.strftime("%M%S",time.localtime())] = [uname, "登录成功"]
        else:
            casjc_config.casjc_result['控制台用户登录'+ time.strftime("%M%S",time.localtime())] = [uname, "登录失败,测试终止"]
            return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result['控制台用户登录'+ time.strftime("%M%S",time.localtime())] = [uname, "登录失败,测试终止"]
        return None
    #进入控制台
    aaa.console()
    #点击用户头像进入个人中心
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="userinfo el-popover__reference"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_element_by_css_selector('div[class="userinfo el-popover__reference"]').click()
        time.sleep(casjc_config.short_time)
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "操作异常"] 
        aaa.console_logout(uname)
        return None
    #点击安全设置菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[class="el-menu-item"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('li[class="el-menu-item"]')[0].click()
    #点击账号密码的修改按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button p el-button--text"]')))
    hailong.find_elements_by_css_selector('button[class="el-button p el-button--text"]')[0].click()
    #输入旧密码
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[class="el-input__inner"]')))
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys(oldpw)
    #输入新密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys(upasswd)
    #输入确认密码
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].send_keys(upasswd)
    #点击确定按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    #获取请求结果
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[href="/login"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "修改密码操作成功,当前密码: " + upasswd ]
        hailong.quit()
        return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 修改密码操作异常"]
        hailong.quit()
        return None


if __name__ == "__main__":
    print (">> UI自动化脚本开始执行执行")
    start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    #Casjc_console_upfile()
    #Casjc_console_webshell()
    #Casjc_console_user()
    #Casjc_console_group()
    #Casjc_console_quota()
    #Casjc_console_auth()
    Casjc_console_updatepw()
    end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    print ("开始时间： " + start_time)
    print ("结束时间： " + end_time)
    print (">> UI自动化脚本执行完成")
    print (json.dumps(casjc_config.casjc_result,ensure_ascii=False))
    casjc_mode.Run_result(("console",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
