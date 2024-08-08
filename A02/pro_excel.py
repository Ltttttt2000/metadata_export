import pandas as pd
# 打开Excel文件
path = 'D:/DATA/Rats/read.xlsx'

# 读取时指定每列的数据类型
dtype = {
    'duration': float
}
df = pd.read_excel(path, dtype=dtype) # skiprows=2，不需要跳过任何行，第一行就是表头
to_sql = []



for index, row in df.iterrows():
    # print(row['动物ID'], row['记录日期'])
    # filename = row['动物ID'] + '_' + str(row['记录日期'])
    # df.at[index, '文件夹名'] = filename

    if row['duration'] != 0:
        df.at[index, 'nex5'] = 1
    else:
        df.at[index, 'nex5'] = 0

df.to_excel(path, index=False)
