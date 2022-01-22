# -*- coding: utf-8 -*-

from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    page_text = requests.get(url=url, headers=headers, proxies={'https': '223.104.122.169'}, timeout=5).text

    with open('./ip.html', 'w', encoding='utf-8') as f:
        f.write(page_text.encode('gbk', 'ignore').decode('gbk'))