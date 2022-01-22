import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python']

    # 回调函数
    def parse_detail(self, response):
        job_desc = response.xpath('//*[@id="main"]/div[1]/text()')
        print(job_desc)

        item = response.meta['item']
        item['job_desc'] = job_desc

        # 提交给管道
        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(response.text)
        print(li_list)
        print('hello')
        for li in li_list:
            job_name = li.xpath('./span[@class="job-area"]/text()').extract_firt()

            item = BossproItem()
            item['job_name'] = job_name

            print(job_name)
            detail_url = li.xpath('./a/@href').extract_first()

            # 手动发送请求                                                                请求传参
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        pass
