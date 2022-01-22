import scrapy
from tongch eng58.items import Tongcheng58Item


class Tong58Spider(scrapy.Spider):
    name = 'tong58'
    allowed_domains = ['www.bj.58.com']
    start_urls = ['https://bj.58.com/xinfang/']

    def parse(self, response):
        # 解析：首页推荐文章的标题和链接
        a_list = response.xpath('/html/body/div/div/div[3]/div/p/a')
        print(len(a_list))

        # 只能使用绝对路径
        # with open(r'D:\Codefield\PycharmProjects\Web_Crawler\Scrapy\Crawler\Crawler\htmls\58tong.html', 'w+', encoding='utf-8') as f:
        #     f.write(response.text)

        # 列表也能调用extract()方法
        print(response.xpath('/html/body/div/div/div[3]/div/p//text()').extract())
        dic_list = []
        for div in a_list:
            # extract()返回Selector对象中的data数据
            text = div.xpath('./text()')[0].extract()
            text = div.xpath('./text()').extract_first()  # 当列表中只有一个元素时，二者等价
            print(text)

            # 实例化
            item = Tongcheng58Item()
            item['text'] = text
            # 提交给管道
            yield item




