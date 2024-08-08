import os

# 指定要操作的目录路径
directory_path = 'D:/DATA/Rats/'
print(directory_path)
# 列出目录中的所有文件和子文件夹
for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isdir(item_path):
        for d in os.listdir(item_path):
            pld_name = item_path + '/' + d
            new_name = item_path + '/' + item + '_' + d
            new_path = os.path.join(directory_path, new_name)
            # print(pld_name)
            os.rename(pld_name, new_path)
print("Finished renaming folders.")
