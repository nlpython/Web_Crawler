import scrapy


class TiebaidSpider(scrapy.Spider):
    name = 'tiebaID'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://tieba.baidu.com/p/7700694543?pn=1']

    base_url = 'https://tieba.baidu.com/p/7700694543?pn='
    page_num = 2

    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div/div[2]/div/div[4]/div[1]')
        print(len(div_list))
        # with open(r'D:\Codefield\PycharmProjects\Web_Crawler\Scrapy\tieba\tieba\spiders\tieba.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        for div in div_list:
            print(div.xpath('./a/text()'))

        if self.page_num <= 11:
            true_url = self.base_url + str(self.page_num)
            self.page_num += 1
            # 手动请求发送，callback回调函数时专门用作于数据解析
            yield scrapy.Request(url=true_url, callback=self.parse)
