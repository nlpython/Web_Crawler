# -*- coding: utf-8 -*-
# 爬取网站的章节和内容

from bs4 import BeautifulSoup
import lxml
import requests

def getHtml():
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    response = requests.get(url, headers=headers)
    # print(response.text.encode('iso-8859-1').decode('utf-8'))
    with open('./sanguo.html', 'w+', encoding='utf-8') as f:
        f.write(response.text.encode('iso-8859-1').decode('utf-8'))

if __name__ == '__main__':

    with open('./sanguo.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

    li_list = soup.select('.book-mulu > ul > li')
    link_list = []
    title_list = []
    for li in li_list:
        link_list.append('https://www.shicimingju.com/' + li.a['href'])
        title_list.append(li.a.text)
    # print(link_list)
    # print(title_list)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    for title, link in zip(title_list, link_list):
        url = link
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')
        with open('./三国演义/'+title+'.txt', 'w', encoding='utf-8') as f:
            f.write(soup.select('.chapter_content')[0].text)











