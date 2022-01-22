# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains # 动作链

if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    bro = webdriver.Chrome(executable_path='./chromedriver.exe')
    bro.get(url)

    # 输入账号密码
    input_u = bro.find_element_by_id('J-userName')
    input_p = bro.find_element_by_id('J-password')

    input_u.send_keys('18571139145')
    input_p.send_keys('y20020130__')

    # 点击登录
    button = bro.find_element_by_id('J-login')
    button.click()

    time.sleep(3)   # 必须延迟几秒，否则获取不到更新的页面
    # print(bro.page_source.encode('gbk', 'ignore').decode('gbk'))

    # 滑动验证
    action = ActionChains(bro)

    # 锁定滑块
    div = bro.find_element_by_id('nc_1__bg')
    # 点击长按滑块
    action.click_and_hold(div)
    # 向右拖动
    for _ in range(1):
        # 如果分多次拖动，每次都必须重新定位，因为页面会强制刷新
        action.move_by_offset(400, 0).perform()
        time.sleep(0.5)
    # 松开点击
    action.release()

    time.sleep(5)
    bro.quit()