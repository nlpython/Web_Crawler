# https://movie.douban.com/top250
# 爬取豆瓣电影Top250的基本信息, 包括电源的名称, 豆瓣评分, 评价数, 电影概况, 电影链接等.

# coding=utf-8
from bs4 import BeautifulSoup     # 网页解析, 获取数据
import re       # 正则表达式, 进行文字匹配
import urllib.request, urllib.error # 指定URL, 获取网页数据
import xlwt     # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    data_list = getData(baseurl)
    print(data_list)
    print(len(data_list))
    # print(len(data_list))
    save_path = './moviesTop250.xls'
    # 3.保存数据
    # saveData(save_path, data_list)
    saveDataToSQlite(data_list, 'movieTop250')


def askURL(url):
    # 伪装成浏览器
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        "Referer": url
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        print(e)
    return html

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
    for i in range(10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析网页
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = [] # 保存一部电影的所有信息
            item = str(item)
            # print(item)
            link = re.findall(super_link, item)[0]   # 通过正侧表达式查找指定的字符串
            # print(link)
            data.append(link)
            data.append(re.findall(img_link, item)[0])
            data.append(re.findall(title, item)[0])
            data.append(re.findall(rate, item)[0])
            data.append(re.findall(judge, item)[0])
            data.append("" if re.findall(inq, item) == [] else re.findall(inq, item)[0])    # 有可能为空
            data.append(re.findall(Bd, item)[0].replace(" ", ""))

            data_list.append(data)

    return data_list

def saveData(save_path, data_list):
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
    worksheet = workbook.add_sheet('sheet1')  # 创建工作表
    col = ["电影详情链接", "图片链接", "中文名", "评分", "评价人数", "概况", "其他信息"]
    for i in range(7):
        worksheet.write(0, i, col[i])
    for i in range(len(data_list)):
        for j in range(len(data_list[0])):
            worksheet.write(i+1, j, data_list[i][j])
    workbook.save(save_path)

def init_SQLite(dbpath):
    import sqlite3

    conn = sqlite3.connect(dbpath)  # 打开或创建数据库文件
    print("Opened database successfully.")

    cursor = conn.cursor()  # 获取游标
    sql = '''       
        create table moviesTop250(
            id integer primary key autoincrement,
            super_link text not null,
            img_link text not null,
            name varchar not null,
            score numeric,
            num numeric,
            instroduction text,
            info text
        )     
    '''

    cursor.execute(sql)
    conn.commit()  # 提交数据库操作

def saveDataToSQlite(data_list, dbpath):
    init_SQLite(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    id = 1
    for data in data_list:
        # 拼写数据
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into moviesTop250 (
                id, super_link, img_link, name, score, num, instroduction, info)
                values (%s)
        '''%(f'"{id}",' + ",".join(data))
        # print(sql)
        cursor.execute(sql)
        conn.commit()
        id += 1

    conn.close()


if __name__ == '__main__':
    # askURL('https://baidu.com')
    main()