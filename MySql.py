# import sqlite3
#
# # 已经不需要导入, 可以直接使用
# conn = sqlite3.connect("testdb")    # 打开或创建数据库文件
# print("Opened database successfully.")
#
# c = conn.cursor()   # 获取游标
# sql = ""            # 定义sql语句
# c.execute(sql)      # 提交数据库操作
# conn.commit()       # 关闭数据库连接

import pymysql
# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mytestdb', charset='utf8')
# 创建游标
cursor = db.cursor()
# 查询数据库版本
# cursor.execute("select version()")
# data = cursor.fetchone()
# print(" Database Version:%s" % data)

# 定义sql语句
sql = '''
    create table movieTop250(
        sno int(6) primary key auto_increment,  
        info_link varchar(150),
        img_link varchar(150),
        title varchar(15),
        score double(2, 1),
        judge int(8),
        inq varchar(30),
        other varchar(150)
    );    
'''
cursor.execute(sql)


# 提交数据库操作
db.commit()
# 关闭数据库连接
db.close()


