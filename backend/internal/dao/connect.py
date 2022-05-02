# -*- coding: utf-8 -*-
"""
本模块包括返回 数据库的连接对象 的函数

使用configs中的参数选择数据库并进行连接

    函数：
    create_db_connection() -> psycopg2.connect
        建立与数据库的连接
    close_db_connection(psycopg2.connect) -> None
        提交自建立此次连接以来所有的数据库更改，关闭与数据库的连接
"""

import psycopg2
import _configs


def create_db_connection():
    """
    与数据库建立联系

    返回值:
        [type]: psycopg2中的连接类型对象
    """
    connection = None
    try:
        connection = psycopg2.connect(
            _configs.DATABASE_LOGIN_INFO
        )
        print("[Log]   Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print("[Error] The error '{e}' occured!")
    return connection

def close_db_connection(connection):
    connection.commit()
    connection.close()