#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Manager import CustomerManager;


import pymysql

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = connection.cursor(pymysql.cursors.DictCursor)

manager = CustomerManager()



# 执行Manager函数
#manager.create(4,"test","Number 1",'1111111','11111@gmail.com','woshi111')


#print全表
manager.readAll()


# 关闭数据库连接
connection.close()