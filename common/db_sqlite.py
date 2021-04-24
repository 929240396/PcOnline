#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "cxf"
# Email: 929240396@qq.com
# Date: 2021/4/23


import sqlite3

import os.path as path


class SQLITE:
    def __init__(self, dirpath, db_name):
        self.db_dir = dirpath
        self.db_name = db_name

    def connect(self):
        """
        连接数据库
        :param db_name: 数据库名称
        :return:        conn
        """
        try:
            conn = sqlite3.connect(self.db_dir + '/' + self.db_name + '.db')
            return conn
        except Exception as e:
            print(e)
    def getsqldata(self, sql, *args):
        """
        查询
        :param db_name: 数据库名
        :param sql:     sql语句
        :param args:    入参
        :return:        返回查询结果，无结果返回0
        """
        try:
            conn = self.connect()
            cur = conn.cursor()
            sql = sql.format(*args)
            # print(sql)
            cur.execute(sql)
            if cur:
                data = cur.fetchall()

                description = cur.description  # 获得游标所在表的信息 包含列名。
                column_name_list = []
                for i in description:
                    column_name_list.append(i[0])

                result = []
                for d in data:
                    data_dict = {}
                    for index in range(0, len(column_name_list)):
                        data_dict[column_name_list[index]] = d[index]
                    result.append(data_dict)
                # print(result)
                return result
            else:
                return 0
        except Exception:
            raise Exception("获取数据库数据失败！")
        finally:
            conn.close()

    def setsqldata(self, sql, *args):
        """
        更新数据
        :param db_name: 数据库名
        :param sql:     sql语句
        :param args:    入参
        :return:        null
        """
        try:
            conn = self.connect()
            cur = conn.cursor()
            sql = sql.format(*args)
            print(sql)
            sqllist = sql.split(";")
            for s in sqllist:
                cur.execute(s)
                conn.commit()
        except Exception:
            raise Exception("修改数据库数据失败！")
        finally:
            conn.close()


if __name__ == '__main__':

    sqlcur = SQLITE("asp")
    sqlcur.connect()
    sqlcur.getsqldata('select * from error_info')
