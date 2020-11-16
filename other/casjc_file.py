from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLCDNumber, QDial, QSlider, QLabel, QFormLayout, QLineEdit, QTextEdit, QFileDialog, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer

from random import randint
import hashlib
import requests
import os, time, sys, json


class Example(QWidget):
        def __init__(self):
            super().__init__()
            self.initUi3()
            

        def initUi(self):
            lcd = QLCDNumber(self)
            lab = QLabel(self)
            #dial = QDial(self)
            dial = QSlider(self)
            
            
            self.setGeometry(300,300,350,250)
            self.setWindowTitle('忽然之间')

            lab.setGeometry(90,80,70,60)
            lcd.setGeometry(100,50,150,60)
            dial.setGeometry(120,120,100,100)

            dial.valueChanged.connect(lcd.display)
            lab.setText('a')
            self.show()

        def initUi2(self):
            self.setGeometry(300, 300, 350, 250)
            self.setWindowTitle('CASJC')
            self.lab = QLabel('方向',self)
            self.lab.setGeometry(150,100,50,50)
            self.show()

        def initUi3(self):
            self.setGeometry(300,300,300,200)
            self.setWindowTitle('CASJC')
            
            self.formlayout = QFormLayout()
            
            self.nameLabel = QLabel("账号")
            self.nameLineEdit = QLineEdit("")
            
            self.introductionLabel = QLabel("密码")
            self.introductionLineEdit = QLineEdit("")
            #self.introductionLineEdit = QTextEdit("")

            self.bt1 = QPushButton('登录',self)
            self.bt1.setGeometry(115,150,70,30)
            self.bt1.setToolTip('登录先进云计算平台')

            self.formlayout.addRow(self.nameLabel,self.nameLineEdit)
            self.formlayout.addRow(self.introductionLabel,self.introductionLineEdit)
            #formlayout.addRow(fileup,self.filebutton)
            self.formlayout.addRow(self.bt1)
            self.setLayout(self.formlayout)

            self.bt1.clicked.connect(self.Casjc_login)
        
            
            self.show()

        def initUi4(self):
            self.setGeometry(300,300,300,200)
            self.setWindowTitle('CASJC')
            
            formlayout = QFormLayout()
            
            fileup = QLabel("文件上传")
            self.filebutton = QPushButton("选择文件",self)
                    
            self.filebutton.clicked.connect(self.selefile)       
            
            self.show()

        def selefile(self):
            self.file_up, self.bbb = QFileDialog.getOpenFileName(self,"打开文件",os.getcwd(),"All File(*)")
            p, self.filename_up = os.path.split(self.file_up)
            #print(self.filename_up)
            try:
                self.selefilenameup.setVisible(False)
            except:
                pass
            self.selefile = QLabel("选中文件")
            self.selefilename = QLabel(self.filename_up)

            self.jindu = QLabel("进度条")
            self.pbar = QProgressBar(self)
            self.pbar.setGeometry(30, 40, 200, 25)
            
            self.btn = QPushButton('开始上传', self)
            self.btn.move(40, 80)
            
            self.formlayout.addRow(self.selefile,self.selefilename)
            self.formlayout.addRow(self.jindu,self.pbar)
            self.formlayout.addRow(self.btn)
            self.btn.clicked.connect(self.cmd)

            self.timer = QBasicTimer()
            self.step = 0
            self.setGeometry(300, 300, 320, 200)
            
            #self.cmd()

        def submitStore(self):
            print(self.nameLineEdit.text())
            print(self.introductionLineEdit.text())
            print(self.filename_up)


        def timerEvent(self, e):

            if self.step >= 100:
                self.step = 0
                self.pbar.setValue(self.step)
                self.timer.stop()
                self.btn.setText('完成')
                return
            #self.step = self.step+1
            #self.pbar.setValue(self.step)
        
        def cmd(self):
            print("do action")
            if self.timer.isActive():
                self.timer.stop()
                self.btn.setText('开始')
            else:
                self.timer.start(100, self)
                self.btn.setText('上传中')
            self.username = self.nameLineEdit.text()
            self.userid = self.getuserId()
            #print(self.introductionLineEdit.text())
            print(self.filename_up)
            ffsize = os.path.getsize(self.file_up)
            #print(ffsize)
            kuaidx = 2097152
            totalchunk = int(ffsize / kuaidx) + 1
            ident = cmd5(self.file_up)
            with open(self.file_up,'rb') as f:
                chunknumber = 0
                for chunk in iter(lambda: f.read(kuaidx),b''):
                    chunknumber += 1
                    md5 = hashlib.md5()
                    #print(f.tell())
                    md5.update(chunk)
                    if len(chunk) < kuaidx:
                        kuaisj = len(chunk)
                    else:
                        kuaisj = kuaidx
                    print(len(chunk))
                    chunkmd5 = md5.hexdigest()
                    #print(chunkmd5)
                    while True:
                        if self.upfile2(chunknumber, kuaidx,kuaisj,ffsize,ident,self.filename_up,totalchunk,chunkmd5,chunk,self.username,self.userid):
                            self.step = self.step + (100/totalchunk)
                            self.pbar.setValue(self.step)
                            break
                        else:
                            time.sleep(3)
                    
            self.changepos()
            self.selefile.setVisible(False)
            self.selefilename.setVisible(False)
            self.pbar.setVisible(False)
            self.jindu.setVisible(False)
            self.btn.setVisible(False)
            self.selefilenameup = QLabel("文件:" + self.filename_up + " 上传完成")
            self.formlayout.addRow(self.selefilenameup)

          
        def Casjc_login(self):
            #print(self.nameLineEdit.text())
            #print(self.introductionLineEdit.text())
            url = "http://11.2.77.3:30089/portal-test/user/login/account"
            #url = "https://www.casjc.com/portal/user/login/account"
            header = {}
            header['Content-Type'] = "application/json"
            data = {}
            data["account"] = self.nameLineEdit.text()
            data["password"] = self.introductionLineEdit.text()
            data["rememberMe"] = False
            data["origin"] = 0
            try:
                r = requests.post(url, headers=header, data=json.dumps(data))
                if r.status_code == 200:
                    if r.json()['code'] == 200:
                        print(r.json()['data'])
                        self.login_session = r.json()['data']
                        self.login_mess = '登录成功'
                        self.nameLabel.setVisible(False)
                        self.nameLineEdit.setVisible(False)
                        self.introductionLabel.setVisible(False)
                        self.introductionLineEdit.setVisible(False)
                        self.bt1.setVisible(False)
                        self.fileup = QLabel("文件上传")
                        self.filebutton = QPushButton("选择文件",self)
                        self.formlayout.addRow(self.fileup,self.filebutton)
                        self.filebutton.clicked.connect(self.selefile)
                    else:
                        print('登录认证信息错误')
                        self.login_mess = '登录认证信息错误'
                else:
                    print('登录异常')
                    self.login_mess = '登录异常'
            except requests.exceptions.ConnectionError:
                print("网络异常无法连接服务器")
                self.login_mess = '网络异常无法连接服务器'
            except requests.exceptions.MissingSchema:
                print('请求的Url地址有误')
                self.login_mess = '请求的Url地址有误'
            except requests.exceptions.Timeout as e:
                print('请求超时：' + str(e.message))
                self.login_mess = '请求超时'
            except requests.exceptions.HTTPError as e:
                print('http请求错误:' + str(e.message))
                self.login_mess = 'http请求错误'
            reply = QMessageBox.information(self, "登录提示信息", self.login_mess, QMessageBox.Yes)

            #self.setLayout(self.formlayout)


        def getuserId(self):
            #url = "https://www.casjc.com/portal/user/person/get"
            url = "http://11.2.77.3:30089/portal-test/user/person/get"
            header = {}
            header["Authorization"] = self.login_session
            header['Token'] = self.login_session
            header['Cookie'] = "JSESSIONID=" + self.login_session
            r = requests.get(url, headers=header)
            #print(r.content)
            print(r.json()['data']['id'])
            return r.json()['data']['id']


        def upfile2(self,chunknumber,kuaidx,cchunksize,totalsize,identifier,filename,totalchunk,chunkmd5,chunk,username,userid):
            header = {}
            header['Token'] = self.login_session
            dd = {}    
            dd['chunkNumber'] = (None,chunknumber)
            dd['chunkSize'] = (None,kuaidx)
            dd['currentChunkSize'] = (None,cchunksize)
            dd['totalSize'] = (None,totalsize)
            dd['identifier'] = (None,identifier)
            dd['filename'] = (None,filename)
            dd['relativePath'] = (None,filename)
            dd['totalChunks'] = (None,totalchunk)
            dd['accept'] = (None,"*")
            dd['userId'] = (None,userid)
            dd['colonyId'] = (None,43)
            dd['toPath'] = (None,"/")
            dd['userHomeDir'] = (None,"/public1/home/" + username + "/" + username)
            dd['chunkMd5'] = (None,chunkmd5)
            dd['upfile'] = (None,chunk)
            dd['upfile'] = (filename,chunk)
            #print(dd)
            url = "http://11.2.77.3:30089/portal-test/store/file/upload"
            #url = "https://console.casjc.com/portal/store/file/upload"
            #print(r.content)
            try:
                r = requests.post(url,headers=header,files=dd)
                print(r.content)
                if r.json()['code'] == 200:
                    return 1
                return None
            except requests.exceptions.Timeout as e:
                print('请求超时：'+str(e.message))
            except requests.exceptions.HTTPError as e:
                print('http请求错误:'+str(e.message))
            except requests.exceptions.ConnectionError:
                print('网卡断了')

        def changepos(self):
            url = "http://11.2.77.3:30089/portal-test/store/file/changePosition"
            header = {}
            header['Token'] = self.login_session
            header['Content-Type'] = "application/json"
            dd = {}
            dd['colonyId'] = 43
            dd['filename'] = self.filename_up
            dd['isFolder'] = False
            dd['toPath'] = "/"
            dd['totalSize'] = 0
            dd['userHomeDir'] = "/public1/home/" + self.username + "/" + self.username
            dd['userId'] = self.userid
            r = requests.post(url,headers=header, data=json.dumps(dd))
            print(r.content)
        



def cmd5(filename):
    #md5 = hashlib.md5()
    with open(filename,'rb') as f:
        for chunk in iter(lambda: f.read(2097152),b''):
            md5 = hashlib.md5()
            #print(f.tell())
            md5.update(chunk)
            #print(md5.hexdigest())
    print(md5.hexdigest())
    return md5.hexdigest()
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


