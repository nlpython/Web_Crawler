# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:

    f = None

    # ��д���෽��
    def open_spider(self, spider):
        """�÷���ֻ�ڿ�ʼ����ʱ����һ��"""
        print("��ʼ��ȡ")
        self.f = open('./58cheng.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        print("��������")
        self.f.close()

    # ר����������item����
    def process_item(self, item, spider):
        # ȡ������
        text = item['text']
        # �־û�
        self.f.write(text + '\n')

        return item
