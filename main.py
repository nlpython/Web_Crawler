import requests
from lxml import etree
import random
import os
from multiprocessing.dummy import Pool
if not os.path.exists('./video'):
    os.mkdir('./video')

urls = []
url = 'https://www.pearvideo.com/category_5'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
#取得页面的li列表
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
#循环遍历出页面视频的video的url和名称
for li in li_list:
#a_url作为https://www.pearvideo.com/videoStatus.jsp?contId='+str(code)+'&mrd='+str(mrd)中Referer的防盗链
    Referer_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]#video_1725312
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'#一边碧绿一边混黄，广西梧州这条江为何泾渭分明？
    #print(a_url)https://www.pearvideo.com/video_1725239
#创造随机数，处于0-1之间的浮点数
    mrd = random.random()
#取得video_后面的数字编号，写法为[0][-7:]
    code = li.xpath('./div/a/@href')[0][-7:]
    print(code)
    #print(code)1725239
#在主页面中发起请求，携带Referer参数
    main_url='https://www.pearvideo.com/videoStatus.jsp?contId='+str(code)+'&mrd='+str(mrd)
    print(main_url)
    main_headers={
        'Referer': Referer_url,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    page_text = requests.get(url=main_url,headers=main_headers)
    print(page_text.text)
    exit()
#获得页面response内容即
# {
# 	"resultCode":"1",
# 	"resultMsg":"success", "reqId":"ce4cd7ad-e2c8-483f-bd9b-d2cbe6f65ab9",
# 	"systemTime": "1617283350768",
# 	"videoInfo":{"playSta":"1","video_image":"https://image2.pearvideo.com/cont/20210331/11580529-205348-1.png","videos":{"hdUrl":"","hdflvUrl":"","sdUrl":"","sdflvUrl":"","srcUrl":"https://video.pearvideo.com/mp4/third/20210331/1617283350768-11580529-204116-hd.mp4"}}
# }
#将反馈内容中的['videoInfo']的['videos']的['srcUrl']使用eval函数装进video_url
    video_url = eval(page_text.text)['videoInfo']['videos']['srcUrl']
#print(video_url)获得的内容为https://video.pearvideo.com/mp4/third/20210401/1617287097549-15192550-102553-hd.mp4
#但是此时的url地址并不是视频地址只是一个伪装的url，需要进行split切割,replace替换
    oldStr = video_url.split('/')[-1].split('-')[0]
    #print(old_Str)
    #old_Str = video_url.split('/')[-1]的值为  1617287312085-15192550-102553-hd.mp4
    #oldStr = video_url.split('/')[-1].split('-')[0]的值为 1617287353462
    newStr = 'cont-' + str(code)
    true_video_url = video_url.replace(oldStr,newStr)
    #print(true_video_url)的值为https://video.pearvideo.com/mp4/third/20210401/cont-1725239-15192550-102553-hd.mp4
    #也就是取到了视频的真实地址
    #将上面得到的name和true_video_url属性装入字典，为下面的线程池处理做铺垫，添加进urls
    dic = {
        'name':name,
        'my_url':true_video_url
    }
    urls.append(dic)
#使用线程池请求视频数据
def video_data(dic):
    print(dic['name']+'正在下载'+'\n')
    data_url = dic['my_url']
    data = requests.get(url=data_url,headers=headers).content
    with open('./video/'+dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name']+'下载成功')
pool=Pool(4)
pool.map(video_data,urls)
pool.close()
pool.join()

