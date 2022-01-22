# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains # 动作链
from lxml import etree
import time

def test():
    # 载入驱动程序并实例化
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    # 让浏览器发起一个 指定url请求
    bro.get(url='http://scxk.nmpa.gov.cn:81/xk/')
    # 获取浏览器当前的页面源码数据
    page_text = bro.page_source
    # print(page_text.encode('gbk', 'ignore').decode('gbk'))
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="gzlist"]/li')
    for li in li_list:
        name = li.xpath('./dl/@title')
        print(name)

    time.sleep(3)
    bro.quit()

def command():
    # 载入驱动程序并实例化
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://www.taobao.com/')
    # 标签定位搜索框
    search_input = bro.find_element_by_id('q')
    # 标签交互
    search_input.send_keys('元气森林')
    # 定位按钮
    button = bro.find_element_by_css_selector('.btn-search')
    # button = bro.find_element_by_class_name('btn-search')
    # 按下按钮
    button.click()

    # 执行一组js代码
    bro.execute_script('window.scroll(0, 1500)')

    bro.get('https://www.baidu.com/')
    time.sleep(2)
    bro.back()
    time.sleep(1)
    bro.forward()

    time.sleep(3)
    bro.quit()

def iframe():
    # 载入驱动程序并实例化
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get('https://www.runoob.com/try/try/php?filename=jqueryui-api-droppable')
    # 如果定位的标签是存在于iframe标签之中的，则必须通过如下操作再定位
    bro.switch_to.frame('iframeResult')  # 切换浏览器标签的定位的作用域
    div = bro.find_element_by_id('draggle')

    # 动作链
    action = ActionChains(bro)
    # 点击长按指定标签
    action.click_and_hold(div)
    # 光标偏移
    for i in range(5):
        # perform()表示立即执行动作链操作
        action.move_by_offset(xoffset=17, yoffset=0).perform()
        time.sleep(0.3)
    # 释放动作链
    action.release()

    bro.quit()

if __name__ == '__main__':
    command()
    pass
















