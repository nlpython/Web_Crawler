# -*- coding: utf-8 -*-
# 梨视频案例
import time
import requests
from lxml import etree
import random
from multiprocessing.dummy import Pool  # 导入线程池相关类

def get_video_data(dic):
    url = dic['true_url']
    title = dic['name']
    print(f'{title} 开始下载')
    data = requests.get(url=url).content
    with open('./mp4s/' + title, 'wb') as f:
        f.write(data)
    print(f'{title} 下载成功')


if __name__ == '__main__':
    url = 'https://www.pearvideo.com/category_8'
    page_text = requests.get(url).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')

    urls = []
    for li in li_list:
        # a_url作为https://www.pearvideo.com/videoStatus.jsp?contId='+str(code)+'&mrd='+str(mrd)中Referer的防盗链
        Referer_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]  # video_1725312
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        # print(a_url)https://www.pearvideo.com/video_1725239
        # 创造随机数，处于0-1之间的浮点数
        mrd = random.random()
        # 取得video_后面的数字编号，写法为[0][-7:]
        code = li.xpath('./div/a/@href')[0][-7:]
        # print(code)1725239
        # 在主页面中发起请求，携带Referer参数
        main_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=' + str(code) + '&mrd=' + str(mrd)
        main_headers = {
            'Referer': Referer_url,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        page_text = requests.get(url=main_url, headers=main_headers)
        video_url = eval(page_text.text)['videoInfo']['videos']['srcUrl']
        # print(video_url)获得的内容为https://video.pearvideo.com/mp4/third/20210401/1617287097549-15192550-102553-hd.mp4
        # 但是此时的url地址并不是视频地址只是一个伪装的url，需要进行split切割,replace替换
        oldStr = video_url.split('/')[-1].split('-')[0]
        # print(old_Str)
        # old_Str = video_url.split('/')[-1]的值为  1617287312085-15192550-102553-hd.mp4
        # oldStr = video_url.split('/')[-1].split('-')[0]的值为 1617287353462
        newStr = 'cont-' + str(code)
        true_video_url = video_url.replace(oldStr, newStr)

        dic = {
            'name': name,
            'true_url': true_video_url
        }
        urls.append(dic)

    pool = Pool(4)
    pool.map(get_video_data, urls)

    pool.close()
    pool.join()



    # link_list = tree.xpath('//*[@id="listvideoListUl"]/li/div/a/@href')
    # title_list = tree.xpath('//*[@id="listvideoListUl"]/li/div/a/div[2]/text()')
    #
    # for link in link_list:
    #
    #     detail_url = 'https://www.pearvideo.com/videoStatus.jsp?' + link
    #
    #     # 次级页面是ajax加载的
    #     param = {
    #         'contId': link[-7:0],
    #         'mrd': '0.4654208577583523'
    #     }
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
    #         'Referer': 'https://www.pearvideo.com/' + link
    #     }
    #     detail_page_json = requests.get(detail_url, params=param, headers=headers).json()
    #     print(detail_page_json)



