#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

connection = pymysql.connect("localhost", "root", "csss331331", "ecommerce", charset='utf8' )


cursor = connection.cursor(pymysql.cursors.DictCursor)


class CustomerManager():
    def create(self,id,first_name,last_name,phone,email,password):
        sql_insert = 'insert into customer' \
              '(id,first_name,last_name,phone,email,password)' \
              'values' \
              '(%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (id,first_name,last_name,phone,email,password)

        cursor.execute(sql_insert)
        connection.commit()
        #insert successfully will print this
        print "insert: %d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\'' % (id,first_name,last_name,phone,email,password)"

    def delete(self):
        select_id = int(raw_input('Choose an ID to delete: '))
        sql_del = 'delete from customer where id = %d' % select_id
        cursor.execute(sql_del)
        connection.commit()

        print "ID: %d was deleted!" % select_id

    def update(self,id,dict,value):

        sql_update = "update customer set %s = \'%s\' where id = %s" % (dict,value,id)
        cursor.execute(sql_update)
        connection.commit()

        print "ID: %d was updated!" % id

    def readAll(self):
        sql_read = 'select * from customer'
        cursor.execute(sql_read)
        data = cursor.fetchall()
        for user in data:
            name = user['last_name'] +" "+ user['first_name']
            email = user['email']
            phone = user['phone']
            password = user['password']
            id = user['id']

            #print user info
            print "User id: %s, Name: %s, Email: %s, Phone: %s, Password: %s" % \
                (id,name,email,phone,password)


