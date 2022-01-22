# -*- coding: utf-8 -*-
import json
import requests

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    # post请求参数处理
    data = {
        'kw': 'dog'
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    # 返回json数据对象
    dict_obj = response.json()

    # 持久化存储
    with open('dog.json', 'w+', encoding='utf-8') as f:
        json.dump(dict_obj, fp=f, ensure_ascii=False)


