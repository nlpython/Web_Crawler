# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains # 动作链
from lxml import etree
import time

# 实现规避检测
from selenium.webdriver import Chrome, ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 实现无可视化
from selenium.webdriver.chrome.options import Options

chrom_options = Options()
chrom_options.add_argument('--headless')
chrom_options.add_argument('--disable-gpu')


if __name__ == '__main__':
    # 是无可视化界面
    url = 'https://baidu.com/'
    bro = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrom_options, options=option)

    bro.get(url)
    print(bro.page_source.encode('gbk', 'ignore').decode('gbk'))
    bro.quit()
