import time, sys, json, random

from selenium import webdriver
from selenium.webdriver.common.action_chains import *

import casjc_config
import casjc_mode
import casjc_page

    
#登陆控制台系统
def Casjc_console_login(uname="aa123", upasswd="123456aA~"):
    hailong = webdriver.Chrome()
    hailong.get(casjc_config.consoleUrl)
    hailong.maximize_window()
    hailong.find_elements_by_css_selector('a[href="/login"]')[0].click()
    time.sleep(casjc_config.show_time)
    hailong.find_element_by_css_selector("input[type='text']").send_keys(uname)
    hailong.find_element_by_css_selector('input[type="password"]').send_keys(upasswd)
    hailong.find_element_by_tag_name('button').click()
    #等待casjc_config.wait_time全局设置时间(10秒)，判断是否登录成功进入首页
    wait_num = 0
    while wait_num < casjc_config.wait_time:
        time.sleep(casjc_config.short_time)
        try:
            if hailong.find_elements_by_css_selector('div[class="console"]')[0].text == "控制台":
                casjc_config.casjc_result['用户登录' + time.strftime("%M%S",time.localtime())] = "%s: 登录成功" %uname
                return hailong
        except IndexError:
            wait_num += 1
    hailong.quit()
    casjc_config.casjc_result['用户登录'+ time.strftime("%M%S",time.localtime())] = "%s: 登录失败" %uname
    return None


#退出控制台系统
def Casjc_console_logout(mydri=None):
    #mydri = Casjc_login()
    impl = mydri.find_element_by_css_selector('div[class="userinfo el-popover__reference"]')
    chain = ActionChains(mydri)
    chain.move_to_element(impl).perform()
    time.sleep(casjc_config.short_time)
    try:
        #点击退出登录
        a = mydri.find_elements_by_css_selector('button[class="el-button btnText el-button--text"]')[-1].click()
        time.sleep(casjc_config.short_time)
        #弹出确认提示框，点击确定
        mydri.find_elements_by_css_selector('button[class="el-button el-button--default el-button--small el-button--primary "]')[0].click()
        print ("退出登录")
        casjc_config.casjc_result['用户退出'+ time.strftime("%M%S",time.localtime())] = "退出成功"
    except:
        print ("退出登录异常")
        casjc_config.casjc_result['用户退出'+ time.strftime("%M%S",time.localtime())] = "退出失败"
    time.sleep(casjc_config.show_time)
    mydri.quit()
    return None


#控制台-共享存储
def Casjc_console_upfile():
    title = "数据存储-上传文件"
    uname = casjc_config.user_name8
    upasswd = casjc_config.user_passwd2
    uname = "lph123"
    upasswd = "Lph987654."
    hailong = Casjc_console_login(uname,upasswd)
    #进入控制台
    aa = casjc_page.Casjc_console_page(hailong)
    aa.console()
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
        casjc_config.casjc_result['共享存储上传文件'+ time.strftime("%M%S",time.localtime())] = "用户: " + uname + hailong.find_elements_by_css_selector('div[class="uploader-file-status"]')[0].text
        time.sleep(casjc_config.show_time)
        Casjc_console_logout(hailong)
        return None
    except:
        casjc_config.casjc_result['共享存储上传文件'+ time.strftime("%M%S",time.localtime())] = "用户: " + uname + "操作异常"
    return None


#控制台-高性能计算webshell
def Casjc_console_webshell():
    title = "打开webshell"
    uname = casjc_config.user_name6
    hailong = Casjc_console_login(uname,casjc_config.user_passwd2)
    #进入控制台
    hailong.find_elements_by_css_selector('div[class="console"]')[0].click()
    time.sleep(casjc_config.show_time)
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


if __name__ == "__main__":
    print (">> UI自动化脚本开始执行执行")
    start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    Casjc_console_upfile()
    #Casjc_console_webshell()
    end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
    print ("开始时间： " + start_time)
    print ("结束时间： " + end_time)
    print (">> UI自动化脚本执行完成")
    print (json.dumps(casjc_config.casjc_result,ensure_ascii=False))
    casjc_mode.Run_result(("console",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
