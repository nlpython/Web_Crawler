# 采集从1月23号以来的世界各国疫情数据
import json
from bs4 import BeautifulSoup
import re
import requests
from tqdm import tqdm
import pandas as pd

class CoronaVirusSpider(object):

    def __init__(self):
        self.homo_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_context_from_url(self, url):
        """
        根据url获取响应内容的字符串数据
        :param url: 请求的URL
        :return: 响应内容的字符串
        """
        # 1.发送请求, 获取疫情首页内容
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self, home_page):
        """
        解析首页内容, 返回解析后的python数据
        :param home_page:
        :return:
        """
        # 2.使用BeautifulSoup提取疫情数据
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id='getListByCountryTypeService2true')
        text = script.text
        # print(text)

        # 3.使用正则表达式, 提取json字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)

        # 5.把json字符串转换为python数据
        return json.loads(json_str)

    def save(self, data, path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)


    def crawl_last_day_corona_virus(self):
        """
        采集最近一天各国疫情信息
        :return:
        """
        home_page = self.get_context_from_url(self.homo_url)
        data = self.parse_home_page(home_page)
        self.save(data, 'data.json')

    def crawl_corona_virus(self):
        """采集从1月23号以来各国疫情数据"""
        # 1.加载各国疫情数据
        with open('data.json', encoding='utf-8') as f:
            last_day_corona_virus = json.load(f)
        # print(last_day_corona_virus)

        data_list = []
        # 2.遍历各国疫情数据, 获取统计的URL
        for country in tqdm(last_day_corona_virus, '采集1月23日以来的各国疫情信息'):
            # 3.发送请求, 获取各国从1月23号至今的数据
            statisticsData_data_url = country['statisticsData']
            statisticsData_data_json_str = self.get_context_from_url(statisticsData_data_url)

            # 4.把json数据转换为python数据, 添加到列表中
            statistics_data = json.loads(statisticsData_data_json_str)



            for one_day in statistics_data['data']:
                one_day['provinceName'] = country['provinceName']
                # print(one_day)
                data_list.append(one_day)
            # print(statistics_data)
        # print(data_list)
        # 5.把列表以json格式保存为文件
        self.save(data_list, 'corona_virus.json')

        # self.save_to_excel(data_list)

    def save_to_excel(self, data_list):
        pandas_data = pd.DataFrame(data_list)
        # print(pandas_data)
        writer = pd.ExcelWriter('./corona_virus.xlsx')  # 写入Excel文件
        pandas_data.to_excel(writer, 'page_1')  # ‘page_1’是写入excel的sheet名
        writer.save()
        writer.close()



    def run(self):
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()



if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()