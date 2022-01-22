# -*- coding:utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from itemadapter import ItemAdapter
import pymysql


class Tongcheng58Pipeline:

    f = None

    # 重写父类方法
    def open_spider(self, spider):
        """该方法只在开始爬虫时调用一次"""
        print("开始爬取")
        self.f = open('./58cheng.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print("结束爬虫")
        self.f.close()

    # 专门用来处理item对象
    def process_item(self, item, spider):
        # 取出数据
        text = item['text']
        # 持久化
        self.f.write(text + '\n')

        return item     # 传递给下一个即将被执行的管道类

# 管道文件中的一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPileLine(object):

    conn = None
    cur = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='mytestdb', charset='utf8')

    def process_item(self, item, spider):
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('insert into')
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

























