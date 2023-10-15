import csv
import os
import json

# 函数：将test.csv的格式转换为新格式
def generate_test_new_csv(test_csv_path, test_videos_dir, output_csv_path):
    video_label_mapping = {}
    with open(test_csv_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过表头行
        for row in csv_reader:
            label_name, video_id, start_time, end_time, split, is_cc = row
            # 将start_time和end_time格式化为6位数字的字符串
            start_time_str = f"{int(start_time):06d}"
            end_time_str = f"{int(end_time):06d}"
            video_filename = f"{video_id}_{start_time_str}_{end_time_str}.mp4"
            video_label_mapping[video_filename] = label_name

    # 从test_videos_dir中删除最后的斜线
    test_videos_dir = test_videos_dir.rstrip('/')
    
    with open(output_csv_path, mode='w') as output_csv_file:
        csv_writer = csv.writer(output_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for video_filename, label in video_label_mapping.items():
            video_path = os.path.join(test_videos_dir, video_filename)
            csv_writer.writerow([video_path, label])

# 函数：根据classids.json将名称替换为数字
def replace_name_with_number(csv_path, classids_path):
    # 读取classids.json
    with open(classids_path, "r") as f:
        classids = json.load(f)
    
    # 读取csv
    with open(csv_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        csv_data = list(reader)
    
    # 将名称替换为数字
    for row in csv_data:
        for class_name, class_id in classids.items():
            if row[1] == class_name.strip('\"'):
                row[1] = class_id
                break
    
    # 将替换后的数据写回csv
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    
    print("已经将test.csv的名字替换为classids.json的数字，并保存到test_new.csv。")

# 函数：检查文件夹内的视频文件是否真的存在
def filter_existing_videos(test_csv_path, output_csv_path, directory_path):
    with open(test_csv_path, 'r') as csvinput:
        with open(output_csv_path, 'w') as csvoutput:
            writer = csv.writer(csvoutput, delimiter=' ')
            reader = csv.reader(csvinput, delimiter=' ')
            
            for row in reader:
                mp4_file_path = row[0]
                relative_path = os.path.relpath(mp4_file_path, directory_path)
                if os.path.exists(os.path.join(directory_path, relative_path)):
                    writer.writerow(row)
    
    print(f"已保存过滤后的CSV到{output_csv_path}。")

# 主要的处理部分
if __name__ == '__main__':
    test_csv_path = '~/kinetics-dataset/k400/test.csv'
    test_videos_dir = '~/kinetics-dataset/k400/test'
    output_csv_path = '~/kinetics-dataset/k400/test_new.csv'
    classids_path = 'classids.json'
    
    # 将test.csv的格式转换为新格式
    generate_test_new_csv(test_csv_path, test_videos_dir, output_csv_path)
    # 根据classids.json将名称替换为数字
    replace_name_with_number(output_csv_path, classids_path)
    # 检查文件夹内的视频文件是否真的存在
    filter_existing_videos(output_csv_path, output_csv_path, test_videos_dir)
