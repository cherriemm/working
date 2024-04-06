# -*- coding: UTF-8 -*-

import base64

#题目十五：Base64编解码
def b64en(path_in, path_out):
    with open(path_in, 'rb')  as file_object:
        binary = file_object.read()



def b64de(path_in, path_out):
    pass


if __name__ == '__main__':
    b64en("./pic.jpg", "./pic_en.txt")
    b64de("./pic_en.txt", "./pic_de.jpg")
