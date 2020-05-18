import time, sys, json, random

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By

import casjc_config
import casjc_mode

    

class Casjc_admin_page():

    def __init__(self,hailong,luser,lpasswd):
        self.hailong = hailong
        self.uname = luser        
        self.upasswd = lpasswd
        self.Casjc_login()



    #登陆后台系统
    def Casjc_login(self):
        self.hailong.get(casjc_config.adminUrl)
        self.hailong.maximize_window()
        self.hailong.find_element_by_css_selector("input[type='text']").send_keys(self.uname)
        self.hailong.find_element_by_css_selector('input[type="password"]').send_keys(self.upasswd)
        self.hailong.find_element_by_tag_name('button').click()
        #等待casjc_config.wait_time全局设置时间，判断是否登录成功进入首页
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[class="router-link-active"]')))
            if self.hailong.find_elements_by_css_selector('a[class="router-link-active"]')[0].text == "首页":
                #casjc_config.casjc_result['管理后台用户登录'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s  登录成功" %self.uname
                return None
            else:
                casjc_config.casjc_result['管理后台用户登录'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 登录失败,测试终止" %self.uname
                self.hailong.quit()
                sys.exit()
                return None
        except exceptions.TimeoutException:
            casjc_config.casjc_result['管理后台用户登录'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 登录失败,测试终止" %self.uname
            self.hailong.quit()
            sys.exit()
            return None
        

    def admin_home(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '首页')))
            self.hailong.find_element_by_link_text('首页').click()
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开首页菜单'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 页面异常,测试终止" %self.uname
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None

    def admin_resmanagement(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '资源管理')))
            self.hailong.find_element_by_link_text('资源管理').click()
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开资源管理菜单'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 页面异常,测试终止" %self.uname
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None

    def admin_operationcenter(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '运营中心')))
            self.hailong.find_element_by_link_text('运营中心').click()
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开运营中心菜单'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 页面异常,测试终止" %self.uname
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None
        
    def admin_appcenter(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '应用中心')))
            self.hailong.find_element_by_link_text('应用中心').click()
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开应用中心菜单'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 页面异常,测试终止" %self.uname
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None

    def admin_usersystem(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, '用户系统')))
            self.hailong.find_element_by_link_text('用户系统').click()
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开用户系统菜单'+ time.strftime("%M%S",time.localtime())] = "当前用户: %s 页面异常,测试终止" %self.uname
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None

class Casjc_console_page():

    def __init__(self,hailong):
        self.hailong = hailong
    
    def console(self):
        try:
            WebDriverWait(self.hailong,casjc_config.wait_time,0.5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[class="headerBarRight"]')))
            time.sleep(casjc_config.short_time)
            self.hailong.find_elements_by_css_selector('div[class="console"]')[0].click()
            return None
        except:
            start_time = time.strftime("%m-%d %H:%M:%S",time.localtime())
            end_time = time.strftime("%m-%d %H:%M:%S",time.localtime())   
            casjc_config.casjc_result['打开控制台'+ time.strftime("%M%S",time.localtime())] = " 页面异常,测试终止"
            casjc_mode.Run_result(("admin",start_time,end_time,json.dumps(casjc_config.casjc_result,ensure_ascii=False)))
            self.hailong.quit()
            sys.exit()
            return None

    
if __name__ == "__main__":
    hailong = webdriver.Chrome()
    a = Casjc_admin_page(hailong,"duliadmin","Test1234!")
    a.admin_home()
    a.admin_resmanagement()
    a.admin_operationcenter()
    a.admin_appcenter()
    a.admin_usersystem()
   
