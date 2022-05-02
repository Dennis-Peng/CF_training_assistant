# -*- coding: utf-8 -*-
"""
本模块定义对数据库中users表所进行的各种操作方法

本模块中函数需要调用connect模块得到与数据库的连接

    函数：
    find_user_by_username(psycopg2.connection, string name) -> tuple(result list)
        通过本系统用户名查询用户，返回用户名相同的元组列表
    add_user(psycopg2.connection, string name, string password, string cf_name) -> None
        向数据库增加新用户(用户名，密码[md5]，codeforces用户名)
    find_user_by_username(psycopg2.connection, string name) -> tuple(result list)
        通过本系统用户名查询用户密码，返回包含密码的元组列表
        [由于系统中原则上来说只有一个用户，所以查询一个存在的用户，结果元组长度应该等于1]
"""

import psycopg2


def find_user_by_username(connection, name):
    cur = connection.cursor()
    cur.execute("SELECT * FROM users WHERE name=="+name)
    result = cur.fetchall()
    cur.close()
    return result


def add_user(connection, name, password, cf_name):
    cur = connection.cursor()
    cur.execute("INSERT INTO users(name, passwd, cf_name)\
                 VALUES("+name+", "+password+", "+cf_name+")"\
                 )
    cur.close()

def get_password_by_username(connection, name):
    cur = connection.cursor()
    cur.execute("SELECT passwd FROM users WHERE name=="+name)
    result = cur.fetchall()
    cur.close()
    return result
