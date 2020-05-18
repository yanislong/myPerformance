import re, time

import win32gui
import win32con

import requests
from bs4 import BeautifulSoup
import pymysql


#上传本地文件
def Casjc_upload(filePath, browser_type="chrome"):
    '''
    通过pywin32模块实现文件上传的操作
    :param filePath: 文件的绝对路径
    :param browser_type: 浏览器类型（默认值为chrome）
    :return:
    '''
    if browser_type.lower() == "chrome":
        title = "打开"
    elif browser_type.lower() == "firefox":
        title = "文件上传"
    elif browser_type.lower() == "ie":
        title = "选择要加载的文件"
    else:
        title = ""  # 这里根据其它不同浏览器类型来修改
    # 找元素
    # 一级窗口"#32770","打开"
    dialog = win32gui.FindWindow("#32770", u"打开")
    # 向下传递
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)   # 三级
    # 编辑按钮
    edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
    # 打开按钮
    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级
    # 输入文件的绝对路径，点击“打开”按钮
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮


#临时邮箱
def Casjc_mail():
    ug = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    url = "http://24mail.chacuo.net/zhtw"
    header = {}
    header['User-Agent'] = ug
    #请求临时邮箱,获取当前邮箱地址,和cookie
    r = requests.get(url, headers=header)
    l1 = re.compile(r'sid=(.*)$')
    l2 = l1.findall(r.headers['Set-Cookie'])
    token = l2[0]
#    print(token)
    html = BeautifulSoup(r.content, features='lxml')
#    print(html)
    tmp = str(html.input['value'])
    email = tmp + "@chacuo.net"
    #print((email,tmp,token))
    return((email,tmp,token))


#获取邮箱验证码
def Casjc_mailcode(*res):
    url = "http://24mail.chacuo.net/zhtw"
    ug = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    reheader = {}
    reheader['User-Agent'] = ug
    reheader['X-Requested-With'] = "XMLHttpRequest"
    reheader['Cookie'] = "sid=" + res[0][2]
    eparam = {}
    eparam['data'] = res[0][1]
    eparam['type'] = "refresh"
    eparam['arg'] = ""
    for i in range(20):
        time.sleep(10)
        res2 = requests.post(url, headers=reheader, params=eparam)
        print(res2.text)
        if res2.json()['data'][0]['list']:
            mid = res2.json()['data'][0]['list'][0]['MID']
            #print(mid)
            cparam = {}
            cparam['data'] = res[0][1]
            cparam['type'] = "mailinfo"
            cparam['arg'] = "f=" + str(mid)
            code = requests.post(url, headers=reheader, params=cparam)
#           print(code.text)
#           print(code.json()['data'][0][1][0]['DATA'])
            cc = code.json()['data'][0][1][0]['DATA'][0]
            ehtml = BeautifulSoup(cc, features='lxml')
            #获取到的验证码
            ccd = ehtml.find_all('span')[1]
            ccd = ccd.get_text()
            #print(ccd)
            return ccd


#脚本执行结果插入到数据库
def Run_result(*resdic):
    tt = time.strftime("%Y/%m/%d %H:%M:%S")
    con = pymysql.connect(host="10.0.20.91", port=33060, user="root", password="root", database='portaltest', charset="utf8mb4")
    cursor = con.cursor()
    sql = "insert into uitestresult(mode,stime,etime,result,exectime) value('{0}','{1}','{2}','{3}','{4}')".format(resdic[0][0],resdic[0][1],resdic[0][2],resdic[0][3],tt)
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()
    return None

if __name__ == "__main__":
    Run_result()

