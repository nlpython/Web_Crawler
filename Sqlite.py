import sqlite3

# 已经不需要导入, 可以直接使用
conn = sqlite3.connect("testdb")    # 打开或创建数据库文件
print("Opened database successfully.")

cursor = conn.cursor()   # 获取游标
sql = '''       
    create table movieTop250(
        id integer primary key autoincrement,
        super_link text not null,
        img_link text not null,
        name varchar not null,
        socore numeric,
        num numeric,
        instroduction text,
        info text
    )     
'''



cursor.execute(sql)      # 提交数据库操作
conn.commit()       # 关闭数据库连接

