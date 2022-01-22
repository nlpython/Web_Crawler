# -*- coding: utf-8 -*-
# 爬取搜狗首页数据

import requests

if __name__ == '__main__':
    # 1.指定URL
    url = 'https://www.sogou.com/'
    # 2.发起请求
    response = requests.get(url=url)
    # 3.获取响应数据
    page_text = response.text
    print(page_text)
    # 4.持久化存储
    with open('./sogou.html', 'w+', encoding='utf-8') as f:
        f.write(page_text)

