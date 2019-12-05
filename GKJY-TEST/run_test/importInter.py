#!/usr/bin/env python3

import sys, json
import xlrd
from lhlmysql.lhlsql import lhlSql

def readInter():
    try:
        wb = xlrd.open_workbook(filename='/root/lhl/myPerformance/GKJY-TEST/run_test/excel/interfacedata.xlsx')
    except FileNotFoundError:
        wb = xlrd.open_workbook(filename='/root/lhl/myPerformance/GKJY-TEST/run_test/excel/interfacedata.xls')
    print(wb.sheet_names())
    s1 = wb.sheet_by_index(0)
    mydata = lhlSql()
    for i in range(1,s1.nrows):
        row = s1.row_values(i)
        print(i)
        if row[5] == None or row[5] == "":
            row[5] = '{}'
        if row[7]:
            try:
                jsdata = json.dumps(json.loads(row[5]))
            except json.decoder.JSONDecodeError:
                dd = 'json格式有误,第{0}行数据有误'.format(i+1)
                return json.dumps({'msg': "faile", 'status': -1, 'data': dd}, ensure_ascii=False)
            mydata.insertInterface(row[0],row[3],row[2],json.dumps(json.loads(row[5])),row[4],row[6],row[1],str(int(row[7])))
        else:
            try:
                jjdata = json.dumps(json.loads(row[5]))
            except json.decoder.JSONDecodeError:
                dd = 'json格式有误,第{0}行数据有误'.format(i+1)
                return json.dumps({'msg': "faile", 'status': -1, 'data': dd}, ensure_ascii=False)
            mydata.insertInterface(row[0],row[3],row[2],json.dumps(json.loads(row[5])),row[4],row[6],row[1],'None')
        print(row)
    return {'msg': "success", 'status': 0, 'data': ""}

if __name__ == "__main__":
    readInter()
