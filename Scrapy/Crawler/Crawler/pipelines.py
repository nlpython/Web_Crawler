# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:

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

        return item
