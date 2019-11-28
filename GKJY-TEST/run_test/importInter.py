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
        if row[7]:
            mydata.insertInterface(row[0],row[3],row[2],json.dumps(json.loads(row[5])),row[4],row[6],row[1],str(int(row[7])))
        else:
            mydata.insertInterface(row[0],row[3],row[2],json.dumps(json.loads(row[5])),row[4],row[6],row[1],'None')
        print(row)

if __name__ == "__main__":
    readInter()
