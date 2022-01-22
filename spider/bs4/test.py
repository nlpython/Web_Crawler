# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    # 将本地的html文档中的数据加载到该对象中
    with open('../sogou.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')
    # print(soup.encode('gbk', 'ignore').decode('gbk'))
    print(soup.select('.wrapper > .header > .top-nav > ul > li > a')[0]['href'])