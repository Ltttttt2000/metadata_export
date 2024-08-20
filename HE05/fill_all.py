import pandas as pd
# 打开Excel文件
path = 'D:/DATA/NC_2023_HE_05.xlsx'
part = 'HE05.csv'
# 读取时指定每列的数据类型
dtype = {
    'duration': float
}
df = pd.read_csv(part, dtype=dtype) # skiprows=2，不需要跳过任何行，第一行就是表头
to_sql = []



for index, row in df.iterrows():

    print(row['开始时间'])

# df.to_excel(path, index=False)

import pandas as pd

# 读取 Excel 文件
df_A = pd.read_excel(path)
df_B = pd.read_csv(part)
# 合并两个 DataFrame，基于 'session' 字段
merged_df = pd.merge(df_A, df_B, on='session', how='left')
merged_df.to_excel('merge.xlsx', index=False)