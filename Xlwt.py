import xlwt     # 进行excel操作

workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
# worksheet.write(0, 0, 'hello')  # 写入数据, 表示0行0列, 内容
for i in range(1, 10):
    for j in range(1, 10):
        worksheet.write(i - 1, j - 1, str(i)+"*"+str(j)+"="+str(i*j))

workbook.save('./mul.xls')
