# -*- coding: utf-8 -*-

import time
import requests
import json
from lxml import etree


def getJDComment():
    url = 'https://item.jd.com/10026602545284.html#comment'
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026602545284&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'
    # url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026602545284&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
    # url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026602545284&score=0&sortType=5&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1'
    base_url_head = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=10026602545284&score=0&sortType=5&page='
    base_url_tail = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
    headers = {
        'referer': 'https://passport.jd.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'cookie': '__jdu=16039414288401537194531; shshshfpa=dfc43489-6285-dbfd-961a-d5fdb50cceba-1603941430; shshshfpb=rc6TXsalYcw2BK%2FnkwJ6l5A%3D%3D; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1614774481; areaId=17; ipLoc-djd=17-1381-50712-50817; __jdc=122270672; ip_cityCode=1381; unpl=JF8EAKluNSttCxxTVk9XSRMZTl4HW1ldSR5QamICVFxfHgYCE1ITEhB7XlVdXhRKFx9sZBRUWFNIUA4eBSsSEXtdVV9cDEkRBGpmNWRtW0tkBCsCHBMSQ1hUW14BQhICb2MHUl1QTlAHGzIrEhhPbWRuXQ1NEwFqbgFRXWhKZAUeBBMTFUlcVFttSSUQCmdvBFwQWExVBxMHGxcTQlRRX10MSREDZ2IBVl1oSmQG; CCC_SE=ADC_jnpVxGPoI547LpsWTbuLjh1uE%2bkXDdMqvAKDEBMmHRq08e%2fP7LkjI9X9bQEFiCI88HOywoTj8NgghgZFCuDZxTtnKCEMMZ%2fpml6p6f2YciXBiocKxoeWUOl1BN6p2wu3a4r52GZ0w1cQay%2fu486poMCcRYYMhYoeHX1VmbuYEg%2fZdzmhXlNeZl0VycNLgr3eNe0yGghjU%2fu%2b8MVKaEK2antYOyupoyr%2fAJvF9J7LFDfAmmn3jX1I8iN0Gh7H04VG8Y7IO26uqJua4kcqZBRwQ6ZN59luotwODeolvTk8QOvY7G0TmT%2f%2falX%2bzxvoQ4FqrWWnHV0rAoo0Hr91rhfHYRwGV7hrUZ4KTZHW5Fe8JDIaZfrM0eSZlSn3TFUZZnKLIbkZdrMoJVMpr2%2baQnzRl8Cre7UCCs0vMNyWZych4IldLpPCmB7MOXtVU4uqvOBEO8ddBnWIc72fbIzJV99niYvb8PnXN%2ft2HGe4tDJ1xvTybUZ7VVIJ03rspcNY7hUWGDvcGXQi3z4Dhfe2V6zCSgohOrGtMAEy2LUpnOFmo3g%3d; __jda=122270672.16039414288401537194531.1603941428.1642832254.1642832751.12; __jdv=122270672|union-click.jd.com|t_1000537640_|tuiguang|bf6bedc0842b45d38b446106dc69a911|1642832750909; shshshfp=e5708a05e8ca703bd8285295d71aabe2; wlfstk_smdl=m9xb9fpv8fygygtse2agzo7dg5m5x3vk; TrackID=1SDRonH9fJysxDTykV3-iGxjEyaI-QMh71RFIFxNT36vX48zY9T4ZyjmBvxwakW8RxFAMLt6SG9CFGtQA65NgO_SrJOrvDLxu2RmA6jkkDoLqlcA_HwfaXGg-Vj1-f0sHPicldnOYMSJXLdzU78_Wpg; thor=82263F66283DEFC31033ECC7244AD0E110AC862F883F877D20AD4846253DC88924324FA107C9D770650DCD312D5160E345EE295317B54C82792672C9E6AD0F2119411D8235132D807C92CEE2AD537C172E84175604CA486E6DE568A20D0DA46B2DE0B1F1BD32056BD4F5A87CA3A63D42E8134BFDCB28FC07ADE04B3C93166E5758FF0DD84626F4060BBB79CD8E91F6C5610A3B6F28B3F5452D4E839738DC2D6F; pinId=LpbkuBiMJtj84Brly-d1oLV9-x-f3wj7; pin=jd_4330a035e4d1f; unick=jd_4330a035e4d1f; ceshi3.com=103; _tp=A8OOLg5ReYPGgmA5%2FNaLFQnMStYEc%2Bj%2BBYen3H3Eyyc%3D; _pst=jd_4330a035e4d1f; token=48fa61085f1c124af46c76bb6a4ef3f6,3,912685; __tk=ff7a4c5397bc59cd995bc590906db0c3,3,912685; __jdb=122270672.12.16039414288401537194531|12.1642832751; shshshsID=714c8e4995eaa25fb6fdd0cc72b87179_13_1642833371785; 3AB9D23F7A4B3C9B=TREMT57SLVUSV265AKBGAB7PDP74KP2DFZFC3IIGDKUGX3LSVR745HV3YYVWSSRWGSVE3ZAITYCJAF3LZUK5MYBNQM'
    }
    with open('comments1.txt', 'w+', encoding='utf-8') as f:
        for page in range(150):
            print(page)
            url = base_url_head + str(page) + base_url_tail
            response = requests.get(url, headers=headers)
            page_text = response.text
            with open('./com.html', 'w', encoding='utf-8') as fp:
                fp.write(page_text.encode('gbk', 'ignore').decode('gbk'))
            page_text = page_text[20:-2]
            print(page_text)
            # print(page_text)
            rs = json.loads(page_text)
            # print(rs['comments'])
            comments = rs['comments']
            for comment in comments:
                print(comment['content'])
                f.write(comment['content'] + '\n')

def getTBComment():
    base_url_head = 'https://rate.tmall.com/list_detail_rate.htm?itemId=638553335141&spuId=1972837672&sellerId=3311179966&order=3&currentPage='
    base_url_tail = '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvt9vUvbpvUvCkvvvvvjiWR2q96j18nLMwQjthPmPyQj3nRFSZsjYVPFdWAjnbi9hvCvvvpZogvpvIvvCvpvvvvvvvvhxuvvvmkpvvoHIvvvEHvvCU79vvvk6vvh34vvvmb49Cvv9vvhhMCeel1U9CvvOCvhE2tnQUvpCWvdKh3CzpHFKzrmphQRA1%2BbeAOHcIAfUTKFyK2uc6%2Bu6fd5QXfamKHs4Aby5BIX%2FOeC1lLJFOV3QfHFXXiXhpVE01Ux8x9C%2BaRfU6ppvCvvOv9hCvvvvRvpvhvv2MMs9CvvpvvhCv&needFold=0&_ksTS=1642847695440_460&callback=jsonp461'
    page = 1
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'referer': 'https://detail.tmall.com/item.htm?id=638553335141',
        'cookie': 'cna=C6pTGNbBpSICARsTyBLDCz9x; xlly_s=1; t=939b3e737ff985112aa5f7e70ef650df; _tb_token_=5ee381b180a5e; cookie2=12f1d8260ae633c95ca1d058be1b3b17; dnk=t_1512311050745_0359; uc1=cookie14=UoewAjYbh6WBqA%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&pas=0&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=WqG3DMC9VAQiUQ%3D%3D; uc3=vt3=F8dCvU15Ws4yrc%2FvtMM%3D&id2=UNX%2FRJZm5QzWWw%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&nk2=F6k3HS2k%2FbNwD951FARr2Cc8iSQ%3D; tracknick=t_1512311050745_0359; lid=t_1512311050745_0359; uc4=id4=0%40UgJ6x62tw5ECp7oGjpljBFIHlnO5&nk4=0%40FbMocxjZZjGdq9RW7yewn%2Bcpgk7sROxhvPgoG7q8Mw%3D%3D; _l_g_=Ug%3D%3D; unb=3541983868; lgc=t_1512311050745_0359; cookie1=BYiLTq3at2I7Y91kPdEDjMgbu8tXXr7FCmPzm0bANsU%3D; login=true; cookie17=UNX%2FRJZm5QzWWw%3D%3D; _nk_=t_1512311050745_0359; sgcookie=E10064ZusiQYEd%2Fyp%2BOKxuvc0tiWcw8BGCtZA1JG4rBL8qKEiN0%2BxELYb1Kvox2JMHhMXvBVv%2BMZrDTTINSLG%2Fjey6dSvjTDQg2i919gwhnpu7ouOR%2Fq%2F9%2Fbj%2Fa2HhZk0R0e; cancelledSubSites=empty; sg=981; csg=97145a8e; enc=77FYYmkmPqLHNi4GOTp9tEHMNHs1ruXuRiWze%2Fu0iZgCLksZmxYcdT5TgnC0bWxNP227OVszJjJkbsGmnJuCXw%3D%3D; x5sec=7b22617365727665723b32223a2237393162343161373439363234383862646364636437613934646666386462324350724272343847454c5030774965437234764751686f4d4d7a55304d546b344d7a67324f4473784b414977727148786a51493d227d; l=eB_o2_Drg7Zpq8VMBO5Cnurza77t6QAb8lVzaNbMiInca1rhsCdiuNCpjfSW-dtjgtfXaetrTan6ERUy8u4_WK_ceTwhKXIpBxJ9-; tfstk=ccc1B2_oBGj6ib9V_VTFudSbDmPPZ45ukC4-5xcb4yk9aW31inCzVMgSViV4ky1..; isg=BN7ebVNLM-KF-2cGNwo6E16EL3Qgn6IZR9lQOYhlPSFCq3-F8C57KwVNo7enqJox'
    }
    with open('TBComments.txt', 'w+', encoding='utf-8') as f:
        for page in range(1, 150):
            url = base_url_head + str(page) + base_url_tail
            # url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=638553335141&spuId=1972837672&sellerId=3311179966&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvmpvxvOQvUvCkvvvvvjiWR2q96jnVR2SZQj1VPmP9zjDvnLzpzjibPLFUljr29vhvHnsGglqkzYswz2gY7%2FN3MnSwAliidvhvmpvU8UV4e9ChgTQCvvyvm2emmv9vjVk%2BvpvBUv9CvF%2Bqvv9y84GuUZWE3we%2BvpvBUvLKv9GPvvom84GuUZWE3we%2BvpvEvvLPvyrbvvpC39hvCvvhvvvvvpvVvvpvvhCvKvhv8vvvvvCvpvvvvvvmMhCvhhQvvvpEphvp89vvCvDvpCCivvvhmZCvhVeIvpvUvvmvPGVeAa8UvpvVmvvC9jDRmvhvLvpE49vjOezyaNoAdcvrfXxr08TKfvVgQacnnCB1BnsysnA4e7DHrfFClfy64Hey%2Bb7gRbIs7T2hibmAdcOdYbLh%2B2yZwlMU%2BExrVTgRvpvhvv2MMs9Cvvpvvvvvi9hvCvvv9U8%2BvpvEvv97vrPLvC2LdvhvHmQUrpbDtpvZ8oeSULELKXhH6LItdvhvHmQUsv8m99vZgkeSULELKXhH6LItdvhvhovUPIEHBpvOWmeSI2BvAxZ1dvhvmpvh4UVuu9CUq29Cvvpvvvvv&needFold=0&_ksTS=1642848552826_484&callback=jsonp485'
            response = requests.get(url, headers=headers, proxies={'http': '49.89.222.124:7082'})
            page_text = response.text
            with open('./TBcom.html', 'w', encoding='utf-8') as fp:
                fp.write(page_text.encode('gbk', 'ignore').decode('gbk'))
            page_text = page_text[11:-1]
            print(page_text.encode('gbk', 'ignore').decode('gbk'))
            rs = json.loads(page_text)

            con_list = rs['rateDetail']['rateList']
            for content in con_list:
                # print(content['rateContent'])
                f.write(content['rateContent'] + '\n')

def getWBComment():
    url = 'https://s.weibo.com/weibo?q=%E5%85%83%E6%B0%94%E6%A3%AE%E6%9E%97&page=1'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'cookie': 'SINAGLOBAL=7577770610167.609.1610187849466; UOR=,,www.baidu.com; SUB=_2A25M75uVDeRhGeBN7FcU9y7PyDmIHXVvnIpdrDV8PUNbmtAKLWj9kW9NRDqaR3P0F-ODOHj6wmU0xhh7-cdb-qjh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWrjyTSmcBmJVp5yjR-j1Oa5JpX5KzhUgL.Foq0S0-fS050e0-2dJLoIpeLxK-LB.BLBo2LxK.L1-zLB-2_; ALF=1674387269; SSOLoginState=1642851269; _s_tentry=weibo.com; Apache=1035406477837.7369.1642851288805; ULV=1642851288902:4:1:1:1035406477837.7369.1642851288805:1633852490939',
        'referer': 'https://s.weibo.com/weibo?q=%E5%85%83%E6%B0%94%E6%A3%AE%E6%9E%97'
    }

    response = requests.get(url, headers=headers)
    page_text = response.text
    # with open('./WBCom.html', 'w+', encoding='utf-8') as f:
    #     f.write(page_text.encode('gbk', 'ignore').decode('gbk'))
    # print(page_text.encode('gbk', 'ignore').decode('gbk'))
    tree = etree.HTML(response.text)
    div_list = tree.xpath('//*[@id="pl_feedlist_index"]/div[2]/div')
    print(tree.xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/p[2]//text()'))

    # for div in div_list:
    #     text = div.xpath('./div[@class="info"]/p[2]//text()')
    #     print(text)



if __name__ == '__main__':
    # getJDComment()
    getTBComment()
    # getWBComment()