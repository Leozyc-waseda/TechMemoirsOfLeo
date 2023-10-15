import csv
import json

# 读取classids.json文件
with open("classids.json", "r") as f:
    classids = json.load(f)  # 该JSON文件包含类别名称到数字ID的映射

# 读取test.csv文件
with open("~/kinetics-dataset/k400/test.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    csv_data = list(reader)  # 将CSV文件的所有行存储为列表

# 用数字ID替换类别名称
for row in csv_data:
    for class_name, class_id in classids.items():  # 遍历JSON中的每个映射
        # 如果当前CSV行中的类别名称与JSON映射中的类别名称匹配
        if row[1] == class_name.strip('\"'):
            row[1] = class_id  # 用相应的数字ID替换
            break  # 找到匹配后，退出内部循环

# 将处理后的数据写入test_new.csv文件
with open("~/kinetics-dataset/k400/test_new.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)  # 写入所有处理后的行

