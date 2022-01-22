# -*- coding: utf-8 -*-

from lxml import etree
import requests

def saveHtml():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    url = 'https://bj.58.com/xinfang/'
    res = requests.get(url, headers=headers)
    with open('./58tong.html', 'w', encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    # saveHtml()
    # 解析本地html数据
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('./58tong.html', parser=parser)

    div_list = tree.xpath('//div[@class="key-list imglazyload"]/div')
    print(div_list)
    title = div_list[0].xpath('//div[@class="infos"]/a[1]/span/text()')
    print(title)
    # div_list = tree.xpath('//div[@class="key-list imglazyload"]/div/div/a[1]/span/text()')
    # print(div_list)
    for div in div_list:
        print(div.xpath('./div/a[1]/span/text()'))

