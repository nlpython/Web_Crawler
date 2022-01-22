# -*- coding: utf-8 -*-

import time
import requests
from lxml import etree
import asyncio

async def request(url):
    print('正在请求', url)
    print('请求成功', url)
    return url

# async修饰的函数调用之后返回一个协程对象
c = request('www.baidu.com')

# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

def use_task():
    """task的使用"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(c)
    print(task)
    loop.run_until_complete(task)
    print(task)


def use_future():
    """future的使用"""
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(c)
    print(future)
    loop.run_until_complete(future)
    print(future)

def call_back_func(task):
    print(task.result())

def call_back_binding():
    """回调绑定"""
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(c)
    # 将回调函数绑定到任务对象中
    task.add_done_callback(call_back_func)
    loop.run_until_complete(task)



if __name__ == '__main__':
    # use_future()
    # use_task()
    call_back_binding()