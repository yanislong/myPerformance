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
 

#申请资源
def Casjc_res(ctype="share", ptype="fixed"):
    """
    ctype=share 申请共享型计算
    ctype=store 申请数据存储
    ptype=fixed 固定方式
    ptype=flexi 灵活方式
    """
    if ctype == "share":
        if ptype == "fixed":
            title = "申请资源-固定方式-共享型"
        elif ptype == "flexi":
            title = "申请资源-灵活方式-共享型"
    elif ctype == "store":
        if ptype == "fixed":
            title = "申请资源-固定方式-数据存储"
        elif ptype == "flexi":
            title = "申请资源-灵活方式-数据存储"
    else:
        title = "申请资源"
    #登录，点击资源管理菜单
    uname = casjc_config.user_name1
    upasswd = casjc_config.user_passwd
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement()
    #点击申请资源按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
    hailong.find_elements_by_tag_name('button')[0].click()
    time.sleep(casjc_config.show_time)
    if hailong.find_elements_by_css_selector('div[class="step-item"]')[1].text == "提交资源申请":
        print ("进入资源申请界面成功")
    else:
        print ("进入资源申请界面失败")
    #选择用户单位,选择最后一个
    hailong.find_element_by_css_selector('input[placeholder="请选择用户单位"]').click()
    time.sleep(casjc_config.short_time)
    #Select(hailong.find_elements_by_css_selector('li[class="el-scrollbar__view el-select-dropdown__list""]')).select_by_value('国科北京分部')
    hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    #输入项目名称
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].send_keys('love')
    #选择甲方用户
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].click()
    time.sleep(casjc_config.short_time)
    #hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[104].click()
    try:
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    except exceptions.ElementNotInteractableException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "当前企业没有找到账号"]
        aaa.Casjc_logout()
        return None
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys('13112341234')
    #输入邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys('131@qq.com')
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].click()
    time.sleep(casjc_config.short_time)
    #li标签列表数据长度,最后一个是灵活配置
    listelement = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
    #选择配置方式
    if ptype == "fixed":
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[len(listelement)-2].click()#固定配置
        #填写基本信息完成，提交下一步
        hailong.find_elements_by_tag_name('button')[1].click()
        time.sleep(casjc_config.show_time)
        #输入资源有效期
        aa = hailong.find_elements_by_css_selector('input[class="el-input__inner"]')
        if ctype == "share":
            #共享型
            aa[18].send_keys('1')
            #选择共享型资源有效期时间范围
            hailong.find_elements_by_css_selector('input[readonly="readonly"]')[1].click()
            time.sleep(casjc_config.short_time)
            bb = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
            bb[11].click()
            #展开共享型资源规格
            hailong.find_elements_by_css_selector('div[class="el-table__expand-icon"]')[5].click()
            time.sleep(casjc_config.short_time)
            #输入共享型四路计算节点核心时数量
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[20].send_keys('1')
            time.sleep(casjc_config.short_time)
            #输入共享型四路计算节点核心时折后单价
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[21].clear()
            time.sleep(casjc_config.short_time)
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[21].send_keys('0.16')
        elif ctype == "store":
            #数据存储
            aa[34].send_keys('1')
            #选择数据存储有效期时间范围
            hailong.find_elements_by_css_selector('input[readonly="readonly"]')[2].click()
            time.sleep(casjc_config.short_time)
            bb = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
            bb[11].click()
            #展开数据存储
            hailong.find_elements_by_css_selector('div[class="el-table__expand-icon"]')[7].click()
            time.sleep(casjc_config.short_time)
            #输入数据存储TB数量
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[36].send_keys('1')
            '''
            n = 0
            for i in aa:
                print n
                n += 1
                try:
                    i.send_keys(str(n))
                except:
                    pass
            '''
            time.sleep(1)
            #输入数据存储折后单价
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[37].clear()
            time.sleep(casjc_config.short_time)
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[37].send_keys('0.16')
        elif ctype == "network":
            #网络资源
            aa[42].send_keys('1')
    elif ptype == "flexi":
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[len(listelement)-1].click()#灵活配置
        #填写基本信息完成，提交下一步
        hailong.find_elements_by_tag_name('button')[1].click()
        time.sleep(casjc_config.show_time)
        if ctype == "share":
            #共享型
            #展开共享型资源规格
            hailong.find_elements_by_css_selector('div[class="el-table__expand-icon"]')[5].click()
            time.sleep(casjc_config.short_time)
            #输入共享型四路计算节点核心时折后单价
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[12].clear()
            time.sleep(casjc_config.short_time)
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[12].send_keys('0.16')
            #输入报价总额
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].send_keys('100')
        elif ctype == "store":
            #数据存储
            #展开规格，采用专用硬件的点对点离线数据迁移
            hailong.find_elements_by_css_selector('div[class="el-table__expand-icon"]')[7].click()
            time.sleep(casjc_config.short_time)
            #输入采用专用硬件的点对点离线数据迁移折后单价
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[21].clear()
            time.sleep(casjc_config.short_time)
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[21].send_keys('0.16')
            #输入报价总额
            hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[-1].send_keys('100')
        elif ctype == "network":
            #网络资源
            aa[42].send_keys('1')
    else:
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[len(listelement)-2].click()#固定配置
        #填写基本信息完成，提交下一步
        hailong.find_elements_by_tag_name('button')[1].click()
        time.sleep(casjc_config.show_time)
    if hailong.find_elements_by_css_selector('div[class="title"]')[0].text == u"高性能计算-标准型\n资源有效期":
        print("进入提交资源申请界面成功")
    else:
        print ("进入提交资源申请界面失败")
    time.sleep(casjc_config.short_time)
    #提交资源申请
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    #获取单号
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
        time.sleep(casjc_config.short_time)
        ordernum = hailong.find_elements_by_tag_name('p')[2].text
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "获取单号失败，没有进入提交成功页面"]
        hailong.quit()
        return None
    #获取提交返回结果
    aaa.admin_result(title,uname,ordernum)
    return ordernum


#价格审批
def Casjc_price(priceuser=""):
    title = "价格审批"
    #登录，点击资源管理菜单
    hailong = webdriver.Chrome()
    uname = priceuser
    upasswd = casjc_config.user_passwd
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement()
    #进入资源审批页面
    if priceuser != "tangdebing":
        try:
            WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
            time.sleep(casjc_config.short_time)
            hailong.find_elements_by_css_selector('i[class="el-icon- iconfont iconshenpizhong"]')[0].click()
            time.sleep(casjc_config.short_time)
            #进入待审批列表
            hailong.find_elements_by_css_selector('li[data-index="/approveWat"')[0].click()
            time.sleep(casjc_config.short_time)
        except exceptions.TimeoutException:
            casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 操作异常"]
            aaa.Casjc_logout()
            return None
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/approveWat"]')))
    if hailong.find_elements_by_css_selector('li[data-index="/approveWat"]')[0].text == "待审批":
        print ("进入资源审批-待审批列表成功")
    else:
        print ("进入资源审批-待审批列表失败")
    #进入资源申请详情页面
    if len(hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')) < 1:
        print ("没有待审批资源")
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "没有待审批资源"]
        aaa.Casjc_logout()
        return None
    else:
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[0].click()
        time.sleep(casjc_config.short_time)
    #输入审批意见
    hailong.find_element_by_css_selector('textarea[class="el-textarea__inner"]').send_keys(u"UI自动化审批")
    #进入申请信息tab，获取订单号
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radiogroup"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('span[class="el-radio-button__inner"]')[1].click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
    time.sleep(casjc_config.short_time)
    ordernum = hailong.find_elements_by_tag_name('p')[2].text
    try:
        #点击审批通过
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]')))
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except exceptions.TimeoutException:
        print ("点击审批通过异常")
    #获取提交返回结果
    aaa.admin_result(title,uname,ordernum)
    return None


#生成合同
def Casjc_contract():
    title = "生成合同"
    #登录，点击资源管理菜单
    hailong = webdriver.Chrome()
    uname = casjc_config.user_name1
    upasswd = casjc_config.user_passwd
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement()         
    #进入资源审批页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[0].click()
    time.sleep(casjc_config.short_time)
    #进入待审批列表
    hailong.find_elements_by_css_selector('li[role="menuitem"]')[2].click()
    time.sleep(casjc_config.short_time)
    if hailong.find_elements_by_css_selector('span[class="el-breadcrumb__inner"]')[2].text == "待审批":
        print ("进入资源审批-待审批列表成功")
    else:
        print ("进入资源审批-待审批列表失败")
    #判断待审批列表是否有数据
    if len(hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')) < 1:
        print ("没有待审批资源")
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 没有待生成资源"]
        aaa.Casjc_logout()
        return None
    else:
        #进入生成合同详情页面
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[0].click()
        time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    time.sleep(casjc_config.short_time)
    #上传文件
    casjc_mode.Casjc_upload(casjc_config.uppath)
    time.sleep(casjc_config.short_time)
    #选择付款添加
    hailong.find_elements_by_css_selector('input[placeholder="请选择付款条件"]')[0].click()
    time.sleep(casjc_config.short_time)
    bb = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
    bb[1].click()
    hailong.find_elements_by_css_selector('input[placeholder="付款期限"]')[0].send_keys('1')
    hailong.find_elements_by_css_selector('input[placeholder="付款百分比"]')[0].send_keys('100')
    #选择签署日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('td[class="available today"]')[0].click()
    #选择发货日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('td[class="available today"]')[0].click()
    #选择服务起始日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('td[class="available today"]')[0].click()
    #选择服务截止日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[8].click()
    time.sleep(casjc_config.short_time)
    #获取日期元素中数据长度，倒数第十个是日期
    listelement = hailong.find_elements_by_css_selector('td[class="available"]')
    #hailong.find_elements_by_css_selector('td[class="available"]')[len(listelement) - 10].click()
    #当月没有可选日期，用这个
    hailong.find_elements_by_css_selector('td[class="next-month"]')[-6].click()
    #进入申请信息tab，获取订单号
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radiogroup"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('span[class="el-radio-button__inner"]')[1].click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
    time.sleep(casjc_config.short_time)
    ordernum = hailong.find_elements_by_tag_name('p')[2].text
    #点击生产合同
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"').click()
    #获取提交返回结果
    aaa.admin_result(title,uname,ordernum)
    return None



#合同审批
def Casjc_contract_apply(appuser):
    title = "合同审批"
    #登录，点击资源管理菜单
    hailong = webdriver.Chrome()
    uname = appuser
    upasswd = casjc_config.user_passwd
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement() 
    #进入资源审批页面,点击审批按钮
    try:        
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="table-btn"]')))
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[0].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 操作异常"]
        aaa.Casjc_logout()
        return None
    #勾选复选框,附件内容已确认
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'label[class="el-checkbox"]')))
        hailong.find_element_by_css_selector('label[class="el-checkbox"]').click()
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 操作异常"]
        aaa.Casjc_logout()
        return None
    #输入审批意见
    hailong.find_elements_by_css_selector('textarea[class="el-textarea__inner"]')[0].send_keys(u"UI自动化合同审批")
    #进入申请信息tab，获取订单号
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radiogroup"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('span[class="el-radio-button__inner"]')[1].click()
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
    time.sleep(casjc_config.short_time)
    ordernum = hailong.find_elements_by_tag_name('p')[2].text   
    try:
        #点击审批通过
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except:
        print ("点击审批通过按钮异常")
  #获取提交返回结果
    aaa.admin_result(title,uname,ordernum)
    return None



#配置资源-固定配置-变更配置
def Casjc_change_config():
    title = "变更配置"
    #登录，点击资源管理菜单
    hailong = webdriver.Chrome()
    uname = casjc_config.user_name1
    upasswd = casjc_config.user_passwd
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement() 
    #进入配置资源页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/configTable"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('li[data-index="/configTable"]')[0].click()
    time.sleep(casjc_config.short_time)
    #点击变更配置
    w1 = 0
    while w1 < casjc_config.wait_time:
        time.sleep(casjc_config.short_time)
        try:
            if hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].text == "变更配置":
                hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
                time.sleep(casjc_config.show_time)
                if hailong.find_elements_by_css_selector('div[class="colorBlue"]')[0].text.strip() == "注意：固定参数配置方式仅有一次变更机会，变更后总价需与订单总价一致":
                    print ("进入配置参数页面成功")
                else:
                    print ("进入配置参数页面失败")
                break
            else:
                print ("没有找到变更配置按钮")
                hailong.quit()
                casjc_config.casjc_result[title + time.strftime("%M%S",time.localtime())] = [uname, "没有找到变更配置按钮"]
                return None
        except:
            w1 +=1
    #有效期开始时间
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].click()
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('td[class="available today"]')[0].click()
    #有效期结束时间
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].click()
    time.sleep(casjc_config.short_time)                                                                   
    hailong.find_elements_by_css_selector('td[class="available"]')[-1].click()
    #当月没有可选日期，用这个
    #hailong.find_elements_by_css_selector('td[class="next-month"]')[-1].click()
    #aa = hailong.find_elements_by_css_selector('td[class="next-month"]')
    #进入申请信息tab，获取订单号
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
    time.sleep(casjc_config.short_time)
    ordernum = hailong.find_elements_by_tag_name('p')[1].text  
    try:
        #点击确认参数
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except:
        print ("点击确认参数按钮异常")
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "订单号:" + ordernum + " 操作异常"]
        aaa.Casjc_logout()
        return None
    #判断是否弹出确认提示框,如果弹出点击确定按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__message"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]')[0].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,ordernum)
    return None


#配置资源-固定配置-配置资源
def Casjc_config(ctype="share"):
    """
    ctype=share 配置共享型计算
    ctype=store 配置数据存储
    """
    title = "配置资源"
    #登录，点击资源管理菜单
    hailong = webdriver.Chrome()
    uname = casjc_config.user_name5
    upasswd = casjc_config.user_passwd
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_resmanagement()
    #进入配置资源页面
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/configTable"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('li[data-index="/configTable"]')[0].click()
    time.sleep(casjc_config.short_time)
    #点击配置资源
    if hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].text == "配置资源":
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
        time.sleep(casjc_config.short_time)
        if hailong.find_elements_by_css_selector('div[class="details"]')[0].text.strip() != "a":
            print ("进入配置资源页面成功")
        else:
            print (hailong.find_elements_by_css_selector('[class="el-select-dropdown__item"]')[1])
    else:
        print ("没有找到配置资源按钮")
        aaa.Casjc_logout()
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "没有找到配置资源按钮"]
        return None
    #点击产品服务下拉列表
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[1].click()
    time.sleep(casjc_config.short_time)
    #选择产品服务 -3:高性能计算 -2:数据存储 -1:网络资源
    if ctype == "share":
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-3].click()
    elif ctype == "store":
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-3].click()
    time.sleep(casjc_config.short_time)
    #点击集群下拉列表
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[2].click()
    time.sleep(casjc_config.short_time)
    #选择集群 12-硅立方东侧 13-测试环境GPFS集群 14-北京硅谷 15-北京硅谷二区 16-北京服务区 17-demowyq
    if ctype == "share":
        #aa = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-6].click()
    elif ctype == "store":
        #aa = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-5].click()
    #点击规格下拉列表
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].click()
    time.sleep(casjc_config.short_time)
    #选择规格
    bb = hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
    hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    #点击有效期开始日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].click()
    time.sleep(casjc_config.short_time)
    #选择开始日期
    hailong.find_elements_by_css_selector('td[class="available today"]')[0].click()
    #点击有效期结束日期
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].click()
    time.sleep(casjc_config.short_time)
    #选择结束日期
    hailong.find_elements_by_css_selector('td[class="available"]')[-1].click()
    #当月没有可选日期，用这个
    #aa = hailong.find_elements_by_css_selector('td[class="next-month"]')
    #hailong.find_elements_by_css_selector('td[class="next-month"]')[-1].click()
    #选择队列
    if ctype == "share":
        hailong.find_element_by_id('low').click()
    #进入申请信息tab，获取订单号
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="details"]')))
    time.sleep(casjc_config.short_time)
    ordernum = hailong.find_elements_by_tag_name('p')[1].text 
    try:
        #点击确认配置
        hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    except:
        print ("点击确认参数按钮异常")
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 订单号:" + ordernum + " 操作异常"]
        aaa.Casjc_logout()
        return None
    #判断是否弹出确认提示框,如果弹出点击确定按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-message-box__message"]')))
    hailong.find_elements_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]')[0].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,ordernum)
    return None

#新建企业单位
def Casjc_create_ent():
    title = "新增企业单位"
    #登录，点击运营中心菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_operationcenter()
    #进入企业管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'i[class="el-icon- iconfont iconicongl"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('i[class="el-icon- iconfont iconicongl"]').click()
    time.sleep(casjc_config.short_time)
    #点击新增企业单位按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-row"]')[0].click()
    time.sleep(casjc_config.short_time)
    #判断打开新增弹窗成功
    if hailong.find_element_by_css_selector('span[class="el-radio-button__inner"]').text == "基础信息":
        print ("新增弹窗打开成功" )      
    #输入企业单位名称
    newuser = "ui_企业名称" + time.strftime("%m%d%H%M",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].send_keys(newuser)
    #选择省
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(u"自动化管理用户")
    #选择市
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #选择区
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys("131" + time.strftime("%m%d%H%M",time.localtime()))
    #点击保存按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None

#编辑企业单位
def Casjc_edit_ent():
    title = "编辑企业单位"
    #登录，点击运营中心菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_operationcenter()
    #进入企业管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'i[class="el-icon- iconfont iconicongl"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('i[class="el-icon- iconfont iconicongl"]').click()
    time.sleep(casjc_config.short_time)
    #点击编辑企业单位按钮
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini"]')[1].click()
    except exceptions.TimeoutException:
        casjc_config.casjc_result['编辑企业单位'] = [uname, "操作异常,没有找到编辑按钮"]
        aaa.Casjc_logout()
        return None
    #判断打开新增弹窗成功
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-card__body"]')))
    time.sleep(casjc_config.short_time)
    if hailong.find_element_by_css_selector('span[class="el-radio-button__inner"]').text == "基础信息":
        print ("编辑弹窗打开成功" )      
    #输入企业单位名称
    newuser = hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[0].get_attribute('value')
    #选择省
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(u"自动化管理用户")
    #选择市
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #选择区
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys("131" + time.strftime("%m%d%H%M",time.localtime()))
    #点击保存按钮
    hailong.find_element_by_css_selector('button[class="el-button el-button--primary"]').click()
    #获取提交请求返回信息
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, newuser + " 编辑成功"]
        aaa.Casjc_logout()
        return None
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "操作异常"]
        aaa.Casjc_logout()
        return None




#新建企业管理用户
def Casjc_addsysent():
    title = "新增企业管理用户"
    #登录，点击用户系统菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_usersystem()
    #进入用户管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[-1].click()
    #点击企业用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击新增企业用户按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    #判断打开新增弹窗成功
    if hailong.find_elements_by_css_selector('span[class="el-dialog__title"]')[-1].text == "新增企业用户":
        print ("新增弹窗打开成功" )      
    #输入企业用户账号
    newuser = "ui" + time.strftime("%m%d%H%M",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(newuser)
    #输入企业用户姓名
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(u"自动化管理用户")
    #输入企业用户邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys("131" + time.strftime("%m%d%H%M",time.localtime()))
    #选择企业单位
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择企业单位"]')[1].click()
        time.sleep(casjc_config.show_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择企业单位异常"]
        aaa.Casjc_logout(uname)
        return None
    #选择角色
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择角色"]')[1].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择角色异常"]
        aaa.Casjc_logout(uname)
        return None
    #点击保存按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[-1].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None

#新建企业普通用户
def Casjc_addent():
    title = "新增企业普通用户"
    #登录，点击用户系统菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_usersystem()
    #进入用户管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[-1].click()
    #点击企业用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击新增企业用户按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    #判断打开新增弹窗成功
    if hailong.find_elements_by_css_selector('span[class="el-dialog__title"]')[-1].text == "新增企业用户":
        print ("新增弹窗打开成功")
    #输入企业用户账号
    newuser = "ui" + time.strftime("%m%d%H%M%S",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys(newuser)
    #输入企业用户姓名
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys("自动化普通用户")
    #输入企业用户邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys("177" + time.strftime("%m%d%H%M",time.localtime()))
    #选择企业单位
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择企业单位"]')[1].click()
        time.sleep(casjc_config.show_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择企业单位异常"]
        aaa.Casjc_logout(uname)
        return None
    #选择角色
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择角色"]')[1].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-2].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择角色异常"]
        aaa.Casjc_logout(uname)
        return None
    #点击关联企业管理员
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择管理员"]')[0].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-1].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择关联企业管理员异常"]
        aaa.Casjc_logout(uname)
        return None
    #点击保存按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[-1].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None


#编辑企业用户
def Casjc_editent():
    title = "编辑企业用户"
    #登录，点击用户系统菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_usersystem()
    #进入用户管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[-1].click()
    #点击企业用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/enterprise"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('li[data-index="/enterprise"]').click()
    #点击用户列表更多按钮
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini el-popover__reference"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini el-popover__reference"]')[0].click()
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "操作异常,用户列表没有找到编辑按钮"]
        aaa.Casjc_logout(uname)
        return None
    #点击编辑按钮
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('p[class="operator"]')[-5].click()
    #获取用户姓名
    newuser = hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].get_attribute('value')
    #输入企业用户邮箱
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #输入手机号
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[7].send_keys("1310101" + str(random.randint(1000,9999)))
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[-1].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None

#新建系统用户
def Casjc_addsysuser():
    title = "新增系统用户"
    #登录，点击用户系统菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_usersystem()
    #进入用户管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[-1].click()
    #点击系统用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/userManagement"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('li[data-index="/userManagement"]').click()
    #点击新增用户按钮
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-row"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--small"]')[0].click()
    #判断打开新增弹窗成功
    if hailong.find_elements_by_css_selector('span[class="el-dialog__title"]')[-1].text == "新增系统用户":
        print ("新增弹窗打开成功")
    #输入用户账号
    newuser = "ui" + time.strftime("%m%d%H%M%S",time.localtime())
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].send_keys(newuser)
    #输入用户姓名
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[4].send_keys("自动化系统用户")
    #输入用户邮箱
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #输入手机号
    hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys("177" + time.strftime("%m%d%H%M",time.localtime()))
    #选择组织机构
    try:
        hailong.find_element_by_css_selector('input[placeholder="请选择组织机构"]').click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('i[class="el-icon-arrow-right el-cascader-node__postfix"]')[1].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('i[class="el-icon-arrow-right el-cascader-node__postfix"]')[3].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('i[class="el-icon-arrow-right el-cascader-node__postfix"]')[4].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('li[role="menuitem"]')[-1].click()
    except IndexError:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, "选择组织机构异常"]
        aaa.Casjc_logout(uname)
        return None
    #选择角色
    try:
        hailong.find_elements_by_css_selector('input[placeholder="请选择角色"]')[1].click()
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')[-2].click()
    except:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 选择角色异常"]
        aaa.Casjc_logout(uname)
        return None
    #点击保存按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[-1].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None


#编辑系统用户
def Casjc_editsysuser():
    title = "编辑系统用户"
    #登录，点击用户系统菜单
    uname = casjc_config.user_name
    upasswd = casjc_config.user_passwd2
    hailong = webdriver.Chrome()
    aaa = casjc_page.Casjc_admin_page(hailong,uname,upasswd)
    aaa.admin_usersystem()
    #进入用户管理菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="el-submenu__title"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_css_selector('div[class="el-submenu__title"]')[-1].click()
    #点击系统用户菜单
    WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li[data-index="/userManagement"]')))
    time.sleep(casjc_config.short_time)
    hailong.find_element_by_css_selector('li[data-index="/userManagement"]').click()
    #点击用户列表更多按钮
    try:
        WebDriverWait(hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[class="el-button el-button--text el-button--mini el-popover__reference"]')))
        time.sleep(casjc_config.short_time)
        hailong.find_elements_by_css_selector('button[class="el-button el-button--text el-button--mini el-popover__reference"]')[0].click()
    except exceptions.TimeoutException:
        casjc_config.casjc_result[title + time.strftime("%M%S")] = [uname, " 操作异常,用户列表没有找到编辑按钮"]
        aaa.Casjc_logout(uname)
        return None
    #点击编辑按钮
    time.sleep(casjc_config.short_time)
    hailong.find_elements_by_tag_name('p')[38].click()
    #hailong.find_element_by_xpath("//div[@class='cell'][18]/span").click()
    #获取用户姓名
    newuser = hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[3].get_attribute('value')
    #输入企业用户邮箱
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[5].send_keys(str(random.randint(10000,99999)) + "@qq.com")
    #输入手机号
    #hailong.find_elements_by_css_selector('input[class="el-input__inner"]')[6].send_keys("1310101" + str(random.randint(1000,9999)))
    #点击确定按钮
    hailong.find_elements_by_css_selector('button[class="el-button el-button--primary"]')[-1].click()
    #获取提交请求返回信息
    aaa.admin_result(title,uname,newuser)
    return None


if __name__ == "__main__":
    print (">> UI自动化脚本开始执行执行")
    start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    ctype = [casjc_config.restype1,casjc_config.restype2]
    ptype = [casjc_config.contype1,casjc_config.contype2]
    #ctype = []
    for k in ctype:
       # Casjc_create_ent()
       # Casjc_edit_ent()
       # Casjc_addsysent()
       # Casjc_addent()
       # Casjc_editent()
       # Casjc_addsysuser()
        #Casjc_editsysuser()
        for y in ptype:
            xx = Casjc_res(k,y)
            if not xx:
                continue
            #价格审批人员列表
            order = [casjc_config.user_name2,casjc_config.user_name7]
            for j in order:
                Casjc_price(j)
            Casjc_contract()
            #合同审批人员列表
            conuser = [casjc_config.user_name3,casjc_config.user_name4]
            for i in conuser:
                Casjc_contract_apply(i)
            Casjc_change_config()
            Casjc_config(k)
    end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    print ("开始时间： " + start_time)
    print ("结束时间： " + end_time)    
    print (json.dumps(casjc_config.casjc_result,ensure_ascii=False))
    casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))