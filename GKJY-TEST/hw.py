#!/usr/bin/env python3
#-*-coding=utf-8-*-

from flask import Flask, request, send_from_directory, url_for, session, escape
from flask import render_template, make_response, abort, redirect
from werkzeug import secure_filename
from lhlmysql.lhlsql import lhlSql
import os, json
import pymysql
from decimal import Decimal


UPLOAD_FOLDER = "/tmp/www"
ALLOWED_EXTENSIONS = set(['json', 'txt','jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024
app.secret_key = os.urandom(12)

@app.route('/')
def hw():
#    resp = make_response(render_template('get.html'))
#    resp = make_response(render_template('index.html'))
#    resp.set_cookie('username', 'the username')
#    username = request.cookies.get('username')
#    return redirect(url_for('index'))
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    app.logger.debug('this is logger')
    return 'Your are not Logged in'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return """
    <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/qianyunGET')
def qianyun():
    if request.method == "GET":
        get_inter = request.args.get("interface")
        get_id = request.args.get("id")
        try:
            get_page = int(request.args.get("page"))
        except:
            get_page = 1
        if get_page >= 1:
            temp_page = (get_page - 1) * 10
        else:
            temp_page = 0
        mydata = lhlSql()
        webbodydata = mydata.getTimeInfo(temp_page)
        webtotalnumber = mydata.getTotalNumber()
        webtotalpage = int(webtotalnumber / 20)
        return render_template('qianyunGET.html', result=(webbodydata,webtotalnumber,webtotalpage))
    return None

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
    con = pymysql.connect('10.0.118.163','root','root','portaltest')
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

@app.route('/addInterface', methods=['GET','POST'])
def qianyun3():
    if request.method == "POST":
        try:
            #get_name = request.get_data()
            get_name = request.form['iname']
            get_addr = request.form['iaddr']
            get_header = request.form['iheader']
            get_param = request.form['iparam']
            get_option = request.form['ioption']
        except TypeError:
            get_addr = ""
            get_header = ""
            get_parama = ""
            get_name = ""
            get_option = ""
        finally:
            mydata = lhlSql()
            mydata.insertInterface(get_name,get_addr,get_header,get_param,get_option)
    return render_template('addInterface.html')

@app.route('/interface', methods=['GET','POST'])
def qianyun4():
    if request.method == "GET":
        try:
            get_page = int(request.args.get("page"))
        except:
            get_page = 1
    if get_page >= 1:
        temp_page = (get_page - 1) * 10
    else:
        temp_page = 0
    mydata = lhlSql()
    webbodydata = mydata.getInterfaceList(temp_page)
    webtotalnumber = mydata.getTotalInterfaceNumber()
    webtotalpage = int(webtotalnumber / 20) + 1
    return render_template('interface.html', result=(webbodydata,webtotalnumber,webtotalpage))

@app.route('/get')
def allowed_file(filename):
    return "." in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/get')
def get_h():
    return render_template('get.html')

@app.route('/post')
def post_h():
    return render_template('post.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/passwd/<int:age>')
def get_p(age):
    if age>100:
        return "Username: %d" % age
    else:
        return "input error"

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    f = request.files['myf']
    if f and allowed_file(f.filename):
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return render_template('upload.html')
    else:
        return render_template('error.html')

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

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port="8888")
