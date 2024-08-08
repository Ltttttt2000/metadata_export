import csv
import os

import pandas as pd

# path = '/GPFS/xzd_lab_permanent/liutong/A02data/Rats/read.xlsx'
path= 'D:/DATA/Rats/read - 副本.xlsx'
df = pd.read_excel(path)
to_sql = []

with open(path, "w") as csvfile:
    writer = csv.writer(csvfile)

for index, row in df.iterrows():

    ps = '/GPFS/xzd_lab_permanent/liutong/A02data/Rats/' + str(row['id']) + '/' + str(row['time'])
    print(ps)

    files = os.listdir(ps)
    count = 0
    for file in files:
        if file == 'Behavioral':
            df.at[index, 'behavior'] = 1
        if file.endswith('.pl2'):
            count += 1
    if count == 2:
        df.at[index, 'sorted'] = 1


df.to_excel(path, index=False)
