import json
import requests

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    param = {
        'on': 'true',
        'page': 1,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    response = requests.post(url=url, data=param, headers=headers)
    page = response.json()


    dict_list = page['list']
    id_list = []
    for item in dict_list:
        id_list.append(item['ID'])

    url_post = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    with open('makeupDetails.json', 'w+') as f:
        for id in id_list:
            param = {
                'id': id
            }
            response = requests.post(url=url_post, params=param, headers=headers)
            str_json = response.json()
            json.dump(str_json, fp=f, ensure_ascii=False)





