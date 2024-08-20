# 读取出来的时间格式为2023-07-26 10:03:47.000033+00:00
import pandas as pd

path = 'D:/DATA/merge.xlsx'
# 读取时指定每列的数据类型
dtype = {
    '开始时间': str
}
df = pd.read_excel(path, dtype=dtype) # skiprows=2，不需要跳过任何行，第一行就是表头
to_sql = []


for index, row in df.iterrows():

    print(row['开始时间'].split('.')[0])
    df['开始时间'] = df['开始时间'].replace(row['开始时间'], row['开始时间'].split('.')[0])
    # df['column_a'] = df['column_a'].replace('old_value', 'new_value')
    # 修改duration为小数点后两位数
    df['持续时间'] = df['持续时间'].replace(row['持续时间'], round(row['持续时间'],2))




    # 保存修改后的 Excel 文件
df.to_excel('all.xlsx', index=False)