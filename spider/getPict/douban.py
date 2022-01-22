# -*- coding: utf-8 -*-

import requests
import re

def getHtml():
    url = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    response = requests.get(url, headers=headers)

    page_text = response.text.encode('GBK', 'ignore').decode('GBK')
    print(page_text)
    with open('./douban.html', 'w', encoding='utf-8') as f:
        f.write(page_text)

if __name__ == '__main__':

    with open('./douban.html', 'r', encoding='utf-8') as f:
        html = f.read().encode('gbk', 'ignore').decode('gbk')

    # <img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
    src = '<img width="100" alt=.*? src="(.*?)" class="">'
    src_list = re.findall(src, html, re.S)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }

    # save images
    for idx, link in enumerate(src_list):
        bin_image = requests.get(url=link, headers=headers).content

        with open('./images/'+str(idx)+'.jpg', 'wb+') as f:
            f.write(bin_image)




