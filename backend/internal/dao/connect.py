# -*- coding: utf-8 -*-
"""
本模块包括返回 数据库的连接对象 的函数

使用configs中的参数选择数据库并进行连接
"""

import psycopg2
import _configs


def create_connection():
    """
    与数据库建立联系

    返回值:
        [type]: psycopg2中的连接类型对象
    """
    connection = None
    try:
        connection = psycopg2.connect(
            _configs.database_login_info
        )
        print("[Log]   Connection to PostgreSQL DB successful")
    except psycopg2.OperationalError as e:
        print("[Error] The error '{e}' occured!")
    return connection