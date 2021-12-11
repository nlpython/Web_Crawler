# 采集最近一日世界各国的数据
import json
from bs4 import BeautifulSoup
import re
import requests

def getData(baseurl):
    # 1.发送请求, 获取疫情首页内容
    response = requests.get(baseurl)
    home_page = response.content.decode()
    # 2.使用BeautifulSoup提取疫情数据
    soup = BeautifulSoup(home_page, 'lxml')
    script = soup.find(id='getListByCountryTypeService2true')
    text = script.text
    # print(text)

    # 3.使用正则表达式, 提取json字符串
    json_str = re.findall(r'\[.+\]', text)[0]
    # print(json_str)

    # 5.把json字符串转换为python数据
    pythonType_data = json.loads(json_str)
    print(pythonType_data[1]['provinceName'])


if __name__ == '__main__':
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    getData(url)