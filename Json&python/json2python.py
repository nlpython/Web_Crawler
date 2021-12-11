import json

# 把json字符串, 转换为python数据
json_str = '''[{"provinceName": "美国", "currenConfirmedCount": 1179041, "confirmedCount": 259559}]'''
rs = json.loads(json_str)
print(rs)

# 把json格式文件, 转换为python类型的数据
# 1.构建指向该文件的文件对象
with open('data.json') as f:
    # 2.加载该文件对象, 转换为python数据
    python_list = json.load(f)
    print(python_list)