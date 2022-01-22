# -*- coding: utf-8 -*-

import time
import asyncio

async def request(url):
    print('正在下载', url)
    # 在异步协程中出现同步模块的代码，那么就无法实现异步
    # time.sleep(2)
    # 在asyncio中遇到阻塞操作，必须手动进行挂起
    await asyncio.sleep(2)
    print('下载完毕', url)

start_time = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.bilibili.com'
]
# 任务列表
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time() - start_time)     # 2s


