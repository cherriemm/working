# -*- coding: UTF-8 -*-
import os
import re
# 题目十三：C程序文件处理
def filter_c_file(dir_path):
    folder = dir_path
    file_list = os.listdir(folder)
    for file_name in file_list :
        if file_name.endswith('.c') or file_name.endswith('.cpp') :
            with open(dir_path+"/"+file_name,'r',encoding="utf-8") as file_object:
                file = re.sub(r'\..*', '', file_name)
                content = file_object.read()
                content = re.sub(r'#include.*\n', '', content)
                content = re.sub(r'/\*.*\*/', '', content)
                content = re.sub(r'//.*\n', '', content)
                content = re.sub(r'\s+', '', content)


                with open(dir_path+'/'+file+'.txt', 'w',encoding="utf-8") as file_object1:
                    file_object1.write(content)




if __name__ == '__main__':
    dir_path = "./testData"
    filter_c_file(dir_path)
