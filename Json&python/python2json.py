import json

# python类型转换为json字符串
json_str = '''[{"provinceName": "美国", "currenConfirmedCount": 1179041, "confirmedCount": 259559}]'''
rs = json.loads(json_str)

json_str = json.dumps(rs, ensure_ascii=False)  # ensure_ascii默认为True, 不显示中文
print(json_str)


# python数据写到json文件中
with open('data.json', 'w') as f:
    json.dump(rs, f, ensure_ascii=False)
