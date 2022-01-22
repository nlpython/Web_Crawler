# -*- coding: utf-8 -*-
# 模拟线程池
import time
from multiprocessing.dummy import Pool  # 导入线程池相关类

def get_page(str):
    print(f'正在下载: {str}')
    time.sleep(3)
    print(f'下载成功: {str}')

def single():
    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    start_time = time.time()

    for name in name_list:
        get_page(name)

    end_time = time.time()
    print(f'{end_time - start_time} seconds.')  # 12s

def mutils():
    name_list = ['xiaozi', 'aa', 'bb', 'cc']
    start_time = time.time()
    # 实例化一个线程池对象
    pool = Pool(4) # 4个线程
    # 将列表中的每个元素传递给get_page进行处理
    # 如果有返回值，那么map的返回值是一个列表
    pool.map(get_page, name_list)
    end_time = time.time()
    print(f'{end_time - start_time} seconds.')  # 3s

if __name__ == '__main__':
    mutils()















