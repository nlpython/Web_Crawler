# -Tag
# -NavigableString
# -Beatuiful
# -Comment
import re

import requests.auth
from bs4 import BeautifulSoup
file = open('./baidu.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, 'html.parser')

# 1.Tag 标签及其内容: 拿到它所找到的第一个内容
print(bs.title)     # <title>百度一下，你就知道</title>
print(bs.a)         # <a class="toindex" href="/">百度首页</a>
# print(bs.head)

# 2.NavigableString 标签里的内容(字符串)
print(bs.title.string)  # 百度一下，你就知道

# 3.Beatuiful 返回标签中的所有属性值(字典格式)
print(bs.a.attrs)   # {'class': ['toindex'], 'href': '/'}

# 4.Comment 是第一个特殊的NavigableString, 输入的内容不包括注释符号
print('-' * 45)


# 文档的遍历
def traverse():
    # tag.content 属性可以将tag的子节点以列表的方式输出
    # print(bs.head.contents)
    print(bs.head.contents[1])
    pass

# 文档的搜索
def search():
    # 1.会查找出所有的a标签
    t_list = bs.find_all('a')
    print(t_list)
    # 2.正则表达式搜索  返回所有包含a标签的内容
    t_list = bs.find_all(re.compile('a'))
    # print(t_list)
    # 3.方法来搜索 (自定义搜索)
    t_list = bs.find_all(name_is_exists('name'))
    pass

# css选择器
def css():
    # 通过标签来查找
    t_list = bs.select('title')
    # 通过类名来查找
    t_list = bs.select('.mnav')
    # 通过id来查找
    t_list = bs.select('#u1')
    # 通过属性来查找
    t_list = bs.select('a[class="bri"]')
    # 通过子标签来查找
    t_list = bs.select('head > title')
    # 通过兄弟标签查找
    t_list = bs.select('.mnav ~ .bri')
    pass


def name_is_exists(tag):
    return tag.has_attr('name')

if __name__ == '__main__':
    # traverse()
    search()