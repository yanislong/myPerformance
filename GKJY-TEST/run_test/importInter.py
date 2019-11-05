#!/usr/bin/env python3

import xlrd

from lhlmysql.lhlsql import lhlSql

def readInter():
    wb = xlrd.open_workbook(filename='./excel/interfacedata.xlsx')
    print(wb.sheet_names())
    s1 = wb.sheet_by_index(0)
    mydata = lhlSql()
    for i in range(1,s1.nrows):
        row = s1.row_values(i)
        if row[7]:
            mydata.insertInterface(row[0],row[3],row[2],row[5],row[4],row[6],row[1],str(int(row[7])))
        else:
            mydata.insertInterface(row[0],row[3],row[2],row[5],row[4],row[6],row[1],'None')
        print(row)

if __name__ == "__main__":
    readInter()
