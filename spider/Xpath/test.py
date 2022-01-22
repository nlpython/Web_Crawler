# -*- coding: utf-8 -*-

from lxml import etree

if __name__ == '__main__':
    # 解析本地html数据
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('../sogou.html', parser=parser)

    # print(tree.xpath('/html/head/title')[0].text)
    print(tree.xpath('//div')[3].text)
    print(tree.xpath('//div[@class="top-nav"]')[0].text)
    print(tree.xpath('//div[@class="top-nav"]/ul/li/a')[0].text)
    print(tree.xpath('//div[@class="top-nav"]/ul/li[3]/a/text()')[0])
    print(tree.xpath('//div[@class="top-nav"]/ul[1]/li//text()'))
    # 属性
    print(tree.xpath('//div[@class="top-nav"]/ul/li[6]/a/@href'))
