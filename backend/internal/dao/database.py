# -*- coding: utf-8 -*-
"""
本模块定义创建本项目所需数据库的代码

本模块中函数需要调用connect模块得到与数据库的连接

    函数：
    initialize_database(psycopg2.connection) -> None
        通过连接,在DBS中初始化后端所需的数据库和表格
"""

import psycopg2


def initialize_database(connect):
    if not connect:
        return
    cur = connect.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS cf_assistant")
    cur.execute("CREATE TABLE IF NOT EXISTS database.users(\
                        uid     SERIAL      NOT NULL,\
                        name    TEXT        NOT NULL,\
                        passwd  char(16)    NOT NULL,\
                        cf_name TEXT        NOT NULL,\
                        PRIMARY KEY (uid)\
                    );"
                )
    cur.execute("CREATE TABLE IF NOT EXISTS database.preferences(\
                        uid     INT         NOT NULL,\
                        rating  INT,\
                        lb_rt   INT,\
                        ub_rt   INT,\
                        tags    BIT(40),\
                        PRIMARY KEY (uid),\
                        CONSTRAINT fk_users\
                            FOREIGN KEY (uid)\
                                REFERENCES users(uid)\
                    );"
                )
    cur.execute("CREATE TABLE IF NOT EXISTS database.tags(\
                        tagid   SERIAL      NOT NULL,\
                        tag     TEXT        NOT NULL,\
                        PRIMARY KEY (tagid)\
                    );"
                )
    
