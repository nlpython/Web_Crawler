# -*- coding: utf-8 -*-

from lxml import etree
import requests
from chaojiying_Python.chaojiying import getResult

if __name__ == '__main__':
    # 创建一个session对象
    session = requests.Session()

    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    src = tree.xpath('//div[@class="mainreg2"]//div[@class="mainreg2"][3]/img/@src')[0]
    link = 'https://so.gushiwen.cn' + src

    img_res = requests.get(link, headers=headers).content
    with open('./imgs/code.jpg', 'wb') as f:
        f.write(img_res)

    # 调用官方示例代码进行验证码识别
    code = getResult('./imgs/code.jpg')
    print(code)

    # post请求模拟登录
    login_url = 'http://so.gushiwen.cn/user/collect.aspx'
    param = {
        '__VIEWSTATE': 'KXkTA4zC3cQxZ9Qwngd7B+LIuZ+xvu0OTYsJFh2c819cZDdkkINrF9TcekZAiyKbAsrghcINnH4JcexZcoLHoKjAxFph7j7uB65wqF+COfHmrQ9vHmpuj9+6U3g=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '1857113914',
        'pwd': 'y20020130..',
        'code': code+'0',
        'denglu': '登录'
    }
    login_res = session.post(url=login_url, data=param, headers=headers)
    print(login_res.status_code)
    print(login_res.text.encode('gbk', 'ignore').decode('gbk'))
    with open('./gushiwen.html', 'w', encoding='utf-8') as f:
        f.write(login_res.text)

    detail_url = 'https://www.gushiwen.cn/'
    detail_res_text = session.get(url, headers=headers).text
    print(detail_res_text.encode('gbk', 'ignore').decode('gbk'))











