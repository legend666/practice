#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 10:16
# @Author  : legend
import os
import shutil
import time

# 获取文件的时间
def file_time(file_name, time_att):
    # https: // www.cnblogs.com / xingchuxin / p / 10426303.html
    # getctime，文件创建时间(不是create)
    if time_att == 'change':
        file_change_time = time.localtime(os.path.getctime(file_name))
        return str(file_change_time.tm_year) + '-' + str(file_change_time.tm_mon)
    # getatime，文件访问时间
    if time_att == 'access':
        file_access_time = time.localtime(os.path.getatime(file_name))
        return str(file_access_time.tm_year) + '-' + str(file_access_time.tm_mon)    # getmtime，文件修改时间
    if time_att == 'modify':
        file_modify_time = time.localtime(os.path.getmtime(file_name))
        return str(file_modify_time.tm_year) + '-' + str(file_modify_time.tm_mon)


if __name__ == "__main__":
    path = r'G:\a7m2\20171120-20190724\100ANV01'
    dir = os.listdir(path)
    # os.getcwd()返回当前进程的工作目录
    # 切换到path目录
    # os.chdir(path)
    for file_name in dir:
        file_path = path + '\\' + file_name
        # 之前命名用了time报了这个错
        # AttributeError: 'str' object has no attribute 'localtime'
        # 命名冲突了,不要用time
        # 获取文件创建时间
        file_modify = file_time(file_path, 'modify')
        goal_path = str(path + '\\' + file_modify).strip()
        # 判断目标文件夹是否存在
        isExists = os.path.exists(goal_path)
        if not isExists:
            os.makedirs(goal_path)
            print(goal_path+'创建成功')
        # 移动文件
        # https://blog.csdn.net/woshisangsang/article/details/74360612
        shutil.move(file_path, goal_path + '\\' + file_name)
    print('分组成功')