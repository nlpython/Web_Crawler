# https://movie.douban.com/top250
# 爬取豆瓣电影Top250的基本信息, 包括电源的名称, 豆瓣评分, 评价数, 电影概况, 电影链接等.

# coding=utf-8
from bs4 import BeautifulSoup     # 网页解析, 获取数据
import re       # 正则表达式, 进行文字匹配
import urllib.request, urllib.error # 指定URL, 获取网页数据
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

def main():
    baseurl = 'https://www.iqiyi.com/ranks/all'
    # 1.爬取网页
    data_list = getData(baseurl)
    print(data_list)
    print(len(data_list))
    save_path = './moviesTop250.xls'
    # 3.保存数据
    # saveData2Excel(save_path, data_list)
    saveData2DB(data_list)
    return None


# 正则表达式
super_link = re.compile(r'<a href="(.*?)">')        # 爬取超链接
img_link = re.compile(r'<img.*src="(.*?)" width="100"/>', re.S)   # 爬取图片链接 re.S让换行符包含在连接中
title = re.compile(r'<span class="title">(.*?)</span>')     # 电影名
rate = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')    # 电影评分
judge = re.compile(r'<span>(.*?)人评价</span>')    # 评价人数
inq = re.compile(r'<span class="inq">(.*?)</span>')     # 电影概况
Bd = re.compile(r'<p class="">(.*?)</p>', re.S)     # 相关内容



def getData(baseurl):
    data_list = []
    file = open('./douban.html', 'rb')
    html = file.read()
    # 逐一解析网页
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('div', class_='item'):
        data = [] # 保存一部电影的所有信息
        item = str(item)

        link = re.findall(super_link, item)[0]   # 通过正侧表达式查找指定的字符串
        data.append(link)
        data.append(re.findall(img_link, item)[0])
        data.append(re.findall(title, item)[0])
        data.append(re.findall(rate, item)[0])
        data.append(re.findall(judge, item)[0])
        data.append("" if re.findall(inq, item) == [] else re.findall(inq, item)[0])    # 有可能为空
        data.append(re.findall(Bd, item)[0].replace(" ", ""))

        data_list.append(data)

    return data_list

def saveData2Excel(save_path, data_list):
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表
    col = ["电影详情链接", "图片链接", "中文名", "评分", "评价人数", "概况", "其他信息"]
    for i in range(7):
        worksheet.write(0, i, col[i])
    for i in range(len(data_list)):
        for j in range(len(data_list[0])):
            worksheet.write(i+1, j, data_list[i][j])
    workbook.save(save_path)

def saveData2DB(data_list):
    import pymysql
    # 连接数据库
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mytestdb', charset='utf8')
    # 创建游标
    cursor = db.cursor()

    # 定义sql语句
    sql = '''
        create table movieTop250(
            sno int(6) primary key auto_increment,  
            info_link varchar(150),
            img_link varchar(150),
            title varchar(15),
            score double(2, 1),
            judge int(8),
            inq varchar(100),
            other varchar(150)
        );    
    '''
    # cursor.execute(sql)
    index = 1
    for data in data_list:
        cursor.execute(f"insert into movieTop250 values({index}, '{data[0]}', '{data[1]}', '{data[2]}', {data[3]}, {data[4]}, '{data[5]}', '{data[6]}');")
        index += 1

    # 提交数据库操作
    db.commit()
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    # askURL('https://baidu.com')
    main()