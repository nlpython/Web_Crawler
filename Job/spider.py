import sqlite3
import urllib.request, urllib.error
from bs4 import BeautifulSoup

def main():
    url = 'https://search.51job.com/list/180200,000000,0000,00,9,99,python,2,1.html'
    data_list = getData(url)

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30",
        "Referer": url
    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('gbk')
        # print(html)
    except urllib.error.URLError as e:
        print(e)
    return html


def getData(url):
    html = askURL(url)
    # print(html)
    bs = BeautifulSoup(html, 'html.parser')

    eldiv = bs.select('.e > span > a')  # class就.x  不带class的标签直接用标签名span
    print(eldiv)
    for item in eldiv:
        print(item['href'])
        print(item.text)


    return None


if __name__ == '__main__':
    main()