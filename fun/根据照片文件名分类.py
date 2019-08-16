# @Time : 2019/8/15 19:48 
# @Author : legend
import os
import shutil

path = r'G:\日常照片\老婆手机照片\2016-0909_20160915'
dir = os.listdir(path)
for file_name in dir:
    file_path = path + '\\' + file_name
    if file_name.find('_') >= 0:
        file_time = file_name.split('_')[0][:4] + '-' + file_name.split('_')[0][4:6]
        isExists = os.path.exists(path+'\\'+file_time)
        if not isExists:
            os.makedirs(path+'\\'+file_time)
            print(file_time+'创建成功')
        goal_path = path + '\\' + file_time
        shutil.move(file_path, goal_path + '\\' + file_name)
