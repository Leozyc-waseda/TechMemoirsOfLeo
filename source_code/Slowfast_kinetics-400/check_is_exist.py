import os
import csv

# 定义原始CSV文件和筛选后的CSV文件的路径
test_csv_path = "~/SlowFast/test.csv"
output_csv_path = "~/SlowFast/filtered_test.csv"
# 定义视频文件的存储目录
directory_path = "~/kinetics-dataset/k400/test/"

# 打开原始CSV文件进行读取
with open(test_csv_path, 'r') as csvinput:
    # 打开新的CSV文件进行写入
    with open(output_csv_path, 'w') as csvoutput:
        writer = csv.writer(csvoutput, delimiter=' ')
        reader = csv.reader(csvinput, delimiter=' ')

        # 遍历原始CSV文件中的每一行
        for row in reader:
            # 获取当前行记录的视频文件路径
            mp4_file_path = row[0]
            # 获取视频文件相对于指定目录的相对路径
            relative_path = os.path.relpath(mp4_file_path, directory_path)
            # 检查视频文件是否存在于指定目录中
            if os.path.exists(os.path.join(directory_path, relative_path)):
                # 如果存在，则将当前记录写入新的CSV文件中
                writer.writerow(row)

# 打印消息，表示已将筛选后的记录保存到新的CSV文件中
print(f"Filtered CSV saved to {output_csv_path}")
