#!/usr/bin/env python3
#-*-coding=utf-8-*-

from flask import Flask, request, send_from_directory, url_for, session, escape
from flask import render_template, make_response, abort, redirect, Response
from werkzeug import secure_filename
from flask import jsonify
from run_test.lhlmysql.lhlsql import lhlSql
import os, json, sys, pymysql, subprocess
sys.path.append('/root/lhl/myPerformance/GKJY-TEST/run_test/excel')
#sys.path.append('./run_test/excel')
try:
    import myrule
except ModuleNotFoundError:
    pass

from decimal import Decimal
from run_test import autoInter, importInter
import config

UPLOAD_FOLDER = "./run_test/excel/"
ALLOWED_EXTENSIONS = set(['json','txt','jpeg','xlsx','xls','gz'])

app = Flask(__name__)

def myfun():
    return "abc"

#jinja2模板调用导入函数
app.jinja_env.globals.update(myfun=myfun)
#jinja2模板调用导入包
app.jinja_env.globals.update(json=json)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024
app.secret_key = os.urandom(12)

@app.route('/', methods=["GET"])
def hw():
    res = (config.name, config.bugurl, config.music, config.saying)
    return render_template("index.html", result=(res,))

@app.route('/test')
def test01():
    return render_template("test.html", relset=())

@app.route('/downloadfile/', methods=['GET', 'POST'])
def downloadfile():
    if request.method == 'GET':
        #fullfilename = request.args.get('filename')
        fullfilename = '/root/lhl/myPerformance/GKJY-TEST/templates/file/interfacedata.xlsx'
        fullfilenamelist = fullfilename.split('/')
        filename = fullfilenamelist[-1]
        filepath = fullfilename.replace('/%s'%filename, '')
        #普通下载
        # response = make_response(send_from_directory(filepath, filename, as_attachment=True))
        # response.headers["Content-Disposition"] = "attachment; filename={}".format(filepath.encode().decode('latin-1'))
        #return send_from_directory(filepath, filename, as_attachment=True)
        #流式读取
        def send_file():
            store_path = fullfilename
            with open(store_path, 'rb') as targetfile:
                while 1:
                    data = targetfile.read(20 * 1024 * 1024)   # 每次读取20M
                    if not data:
                        break
                    yield data
        
        response = Response(send_file(), content_type='application/octet-stream')
        response.headers["Content-disposition"] = 'attachment; filename=%s' % filename   # 如果不加上这行代码，导致下图的问题
        return  response


@app.route('/collvalue', methods=['GET'])
def coll():
    mydata = lhlSql()
    res = mydata.getCollValue()
    return render_template('collvalue.html', result=(res,))

@app.route('/rule', methods=['GET'])
def rule():
    try:
        print(myrule.rule)
    except NameError:
        return render_template('test.html', result=())
    return render_template('rule.html', result=(myrule.rule,))

@app.route('/integrate', methods=["POST","GET"])
def integr():
    if request.method == "POST":
        try:
            get_name = request.get_data()
        except KeyError:
            get_name = "hello world"
        get_name = get_name.decode('utf-8')
        get_name = get_name.split(',')
        print(get_name)
        for i in get_name:
            doc = 'python3 /root/lhl/myPerformance/GKJY-TEST/run_test/integrateTest/' + i + '.py'
            print(doc)
            p = subprocess.Popen(doc, shell=True)
            out,err=p.communicate(timeout=15)
        return jsonify({"msg": {"out": out,"err": err}, "status": 0})
    elif request.method == "GET":
        return render_template('integrate.html', result=())

@app.route('/addInterface', methods=['GET','POST'])
def qianyun3():
    if request.method == "POST":
        print(123)
        try:
            #get_name = request.get_data()
            get_mode = request.form['imode']
            get_desc = request.form['idesc']
            get_addr = request.form['iaddr']
            get_header = request.form['iheader']
            get_param = request.form['iparam']
            get_option = request.form['ioption']
            get_author = request.form['iauthor']
            get_result = request.form['iresult']
            get_userpwd = request.form['iuserpwd']
        except TypeError:
            get_mode = ""
            get_desc = ""
            get_addr = ""
            get_header = ""
            get_parama = ""
            get_option = ""
            get_author = ""
            get_result = ""
            get_userpwd = ""
        finally:
            mydata = lhlSql()
            mydata.insertInterface(get_mode,get_addr,get_header,get_param,get_option,get_author,get_desc,get_result,get_userpwd)
#            insertInterface(self, iname, iaddr, iheader, iparam, ioption, iauthor, descp, expected)
#    return render_template('addInterface.html')
    return qianyun4()

@app.route('/runtest', methods=['GET','POST'])
def runtest():
    subprocess.Popen('python3 /root/lhl/myPerformance/GKJY-TEST/run_test/autoInter.py', shell=True)
    return qianyun4()

@app.route('/interfaceList', methods=['GET','POST'])
def qianyun4():
    kong = None
    get_inter = request.args.get("interface")
    get_author = request.args.get("author")
    try:
        get_page = int(request.args.get("page"))
    except:
        get_page = 1
    if get_page >= 1:
        temp_page = (get_page - 1) * 20
    else:
        temp_page = 0
    if isinstance(get_inter,type(kong)):
        get_inter = ""
    if isinstance(get_author,type(kong)):
        get_author = ""
    mydata = lhlSql()
    webbodydata = mydata.getInterfaceList(get_inter, get_author, temp_page)
    webtotalnumber = mydata.getTotalInterfaceNumber(get_inter, get_author)
    webnamedata = mydata.getInterfaceInfoName()
    webnamedataauthor = mydata.getInterfaceAuthor()
    webtotalpage = int(webtotalnumber / 20) + 1
    intername = mydata.getInterfaceInfoName()
#    print(webbodydata)
    return render_template('interfacelist.html', result=(webbodydata,webtotalnumber,webtotalpage,intername,webnamedata,webnamedataauthor,config.intermode,config.option,config.author,config.music))

@app.route('/delinterface', methods=['GET','POST'])
def delinter():
    if request.method == "GET":
        get_id = request.args.get("iid")
        get_rd = request.args.get("rid")
        print(get_id)
        print(get_rd)
        if get_id == "" or get_id == None:
            myrun = autoInter.lhl()
            myrun.oneTest(get_rd)
            return qianyun4()
        elif get_rd == "" or get_rd == None:
            mydata = lhlSql()
            mydata.DelInterface(get_id)
            return qianyun4()
        else:
            return qianyun4()

@app.route('/interfaceRespondList', methods=['GET','POST'])
def qianyun5():
    kong = None
    if request.method == "GET":
        get_inter = request.args.get("interface")
        get_result = request.args.get("result")
        get_id = request.args.get("myid")
        try:
            get_page = int(request.args.get("page"))
        except:
            get_page = 1
    if get_page >= 1:
        temp_page = (get_page - 1) * 20
    else:
        temp_page = 0
    if isinstance(get_inter,type(kong)):
        get_inter = ""
    if isinstance(get_id,type(kong)):
        get_id = ""
    if isinstance(get_result,type(kong)):
        get_result = ""
    mydata = lhlSql()
    webbodydata = mydata.getInterfaceRespondList(get_inter, get_result, get_id, temp_page)
    webtotalnumber = mydata.getTotalInterfaceRespondNumber(get_inter,get_result)
    webnamedata = mydata.getInterfaceRespondName()
    webtotalpage = int(webtotalnumber / 20) + 1
    intername = mydata.getInterfaceRespondName()
    return render_template('interfacerespondlist.html', result=(webbodydata,webtotalnumber,webtotalpage,intername,webnamedata,config.music))

@app.route('/qianyunPOST')
def qianyunpost():
    if request.method == "GET":
        get_inter = request.args.get("interface")
        get_id = request.args.get("id")
        get_page = request.args.get("page")
    else:
        get_inter = ""
        get_id = ""
        get_page = 1
    con = pymysql.connect('10.0.114.44','root','root','portaltest')
    sql_time = []
    cursor = con.cursor()
    try:
        get_page = int(get_page)
    except:
        get_page = 1
    sql = "select * from qianyun_post where content like '%{0}%' and id like '%{1}%' limit {2},20".format(get_inter,get_id,(get_page-1)*20)
    cursor.execute(sql)
    seldata = cursor.fetchall()
    sql2 = "select count(*) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql2)
    total = cursor.fetchall()
    if not total:
        total = 1.0
    totalPage = str(round(int(total[0][0]) / int(20),0))[:-2]
    sql_dns_time = "select sum(dns_time) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_dns_time)
    dns_time = cursor.fetchall()
    #sql_time.append(dns_time[0][0])
    sql_conn_time = "select sum(conn_time) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_conn_time)
    conn_time = cursor.fetchall()
    try:
        sql_time.append(round(conn_time[0][0]/total[0][0],8))
    except:
        sql_time.append(1)
    sql_startData_time = "select sum(startData_time) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_startData_time)
    startData_time = cursor.fetchall()
    try:
        sql_time.append(round(startData_time[0][0]/total[0][0],8))
    except:
        sql_time.append(1)
    sql_total_time = "select sum(total_time) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_total_time)
    total_time = cursor.fetchall()
    try:
        sql_time.append(round((total_time[0][0]/total[0][0]),8))
    except:
        sql_time.append(1)
    sql_updata = "select sum(updata) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_updata)
    updata = cursor.fetchall()
    sql_time.append(updata[0][0])
    sql_downdata = "select sum(downdata) from qianyun_post where content like '%{0}%' and id like '%{1}%'".format(get_inter,get_id)
    cursor.execute(sql_downdata)
    downdata = cursor.fetchall()
    sql_time.append(downdata[0][0])
    print(sql_time)
    sql_name = "select distinct content from qianyun_post"
    cursor.execute(sql_name)
    inter_name = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template('qianyunPOST.html', result=(seldata,total,sql_time,totalPage,inter_name,get_page))

def allowed_file(filename):
    return "." in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/passwd/<int:age>')
def get_p(age):
    if age>100:
        return "Username: %d" % age
    else:
        return "input error"

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    f = request.files['myf']
    print(f)
    if f and allowed_file(f.filename):
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        #subprocess.Popen('python3 /root/lhl/myPerformance/GKJY-TEST/run_test/importInter.py', shell=True)
        return importInter.readInter()
        #return render_template('interfacelist.html', result=())
    else:
        return render_template('error.html', result=())

@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/deal_request', methods=['GET','POST'])
def deal_request():
    if request.method == "GET":
        get_q = request.args.get("q","")
        return render_template('result.html', result=get_q)
    elif request.method == "POST":
        post_q = request.form["q"]
        return render_template('result.html', result=post_q)


@app.route('/qianyunGET')
def qianyun():
    if request.method == "GET":
        get_inter = request.args.get("interface")
        try:
            get_page = int(request.args.get("page"))
        except:
            get_page = 1
        if get_page >= 1:
            get_page = (get_page - 1) * 10
        else:
            get_page = 0
        if get_inter == None:
            get_inter = ""
        mydata = lhlSql()
        webbodydata = mydata.getTimeInfo(get_inter, get_page)
        webavgdata = mydata.getTimeList(get_inter)
        webnamedata = mydata.getInterfaceName()
        webtotalnumber = mydata.getTotalNumber(get_inter)
        temp = []
        temp2 = []
        for i in webavgdata[0]:
            num = round(Decimal(i/webtotalnumber),6)
            temp.append(num)
        temp2.append((temp))
        webtotalpage = int(webtotalnumber / 20)
        return render_template('qianyunGET.html', result=(webbodydata,webtotalnumber,webtotalpage,temp2,webnamedata))
    return None


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port="8888")
