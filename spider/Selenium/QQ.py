# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains # 动作链
from lxml import etree
import time

if __name__ == '__main__':
    url = 'https://i.qq.com/'
    # 载入驱动程序并实例化
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 让浏览器发起一个 指定url请求
    bro.get(url=url)
    # 有iframe标签，切换作用域
    bro.switch_to.frame('login_frame')
    button = bro.find_element_by_id('switcher_plogin')
    button.click()

    # 输入账号密码
    input_u = bro.find_element_by_id('u')
    input_p = bro.find_element_by_id('p')

    input_u.send_keys('2994056734')
    input_p.send_keys('*****')
    # 点击登录按钮
    login_button = bro.find_element_by_id('login_button')
    login_button.click()

