import scrapy
from tongch eng58.items import Tongcheng58Item


class Tong58Spider(scrapy.Spider):
    name = 'tong58'
    allowed_domains = ['www.bj.58.com']
    start_urls = ['https://bj.58.com/xinfang/']

    def parse(self, response):
        # ��������ҳ�Ƽ����µı��������
        a_list = response.xpath('/html/body/div/div/div[3]/div/p/a')
        print(len(a_list))

        # ֻ��ʹ�þ���·��
        # with open(r'D:\Codefield\PycharmProjects\Web_Crawler\Scrapy\Crawler\Crawler\htmls\58tong.html', 'w+', encoding='utf-8') as f:
        #     f.write(response.text)

        # �б�Ҳ�ܵ���extract()����
        print(response.xpath('/html/body/div/div/div[3]/div/p//text()').extract())
        dic_list = []
        for div in a_list:
            # extract()����Selector�����е�data����
            text = div.xpath('./text()')[0].extract()
            text = div.xpath('./text()').extract_first()  # ���б���ֻ��һ��Ԫ��ʱ�����ߵȼ�
            print(text)

            # ʵ����
            item = Tongcheng58Item()
            item['text'] = text
            # �ύ���ܵ�
            yield item




