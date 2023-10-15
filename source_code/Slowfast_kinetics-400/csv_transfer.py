import csv
import os

# 定义一个函数，其目的是生成一个新的测试CSV文件
def generate_test_new_csv(test_csv_path, test_videos_dir, output_csv_path):
    # 用于存储视频文件名与其对应的标签
    video_label_mapping = {}
    
    # 打开原始CSV文件并读取内容
    with open(test_csv_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # 跳过CSV文件的表头
        
        # 逐行读取CSV内容
        for row in csv_reader:
            label_name, video_id, start_time, end_time, split, is_cc = row
            
            # 将开始和结束时间格式化为6位数的字符串
            start_time_str = f"{int(start_time):06d}"
            end_time_str = f"{int(end_time):06d}"
            
            # 根据video_id、start_time和end_time生成视频文件名
            video_filename = f"{video_id}_{start_time_str}_{end_time_str}.mp4"
            video_label_mapping[video_filename] = label_name

    # 移除test_videos_dir路径末尾的斜杠，确保路径格式的统一性
    test_videos_dir = test_videos_dir.rstrip('/')
    
    # 创建新的CSV文件并写入数据
    with open(output_csv_path, mode='w') as output_csv_file:
        csv_writer = csv.writer(output_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # 遍历video_label_mapping字典，并写入视频的完整路径和标签
        for video_filename, label in video_label_mapping.items():
            video_path = os.path.join(test_videos_dir, video_filename)
            csv_writer.writerow([video_path, label])

# 判断当前脚本是否作为主程序运行
if __name__ == '__main__':
    # 定义原始CSV文件、视频文件夹和新CSV文件的路径
    test_csv_path = '~/kinetics-dataset/k400/test.csv'
    test_videos_dir = '~kinetics-dataset/k400/test'
    output_csv_path = '~kinetics-dataset/k400/test_new.csv'
    
    # 调用函数生成新的CSV文件
    generate_test_new_csv(test_csv_path, test_videos_dir, output_csv_path)
