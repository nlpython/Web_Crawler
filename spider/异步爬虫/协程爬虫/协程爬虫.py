# -*- coding: utf-8 -*-
import asyncio
import time
import aiohttp

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]
start_time = time.time()

async def get_page(url):
    print('正在下载', url)
    # requests发起的请求是基于同步的，必须使用基于异步的网络请求
    # response = requests.get(url=url)   # 同步代码
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            # text()方法返回字符串形式的响应数据
            # read()方法返回二进制形式的响应数据
            # json()方法返回json形式的响应数据
            # 注意：获取响应数据之前一定要使用await进行手动挂起
            page_text = await response.text()
            print('下载成功', page_text)

tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时：', time.time() - start_time)     # 2s
