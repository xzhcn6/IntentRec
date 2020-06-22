#!/usr/bin/python
# -*-coding:utf-8 -*-
#  ------------------------------------------------------
# @File    : data_prs.py
# @Date    : 2020-05-15 13:13
# @Author  : Jupiter
# @Function Description: 
#  ------------------------------------------------------


import re
import random


def ReadFileDatas():
    FileNamelist = []
    file = open('data/train.txt', 'r+',encoding="utf-8")
    for line in file.readlines():
        line = line.strip('\n')  # 删除每一行的\n
        FileNamelist.append(line)
    print('len ( FileNamelist ) = ', len(FileNamelist))
    file.close()
    return FileNamelist


def WriteDatasToFile(listInfo):
    file_handle = open('data/sh_train.txt', 'w',encoding="utf-8")
    for idx in range(len(listInfo)):
        str = listInfo[idx]
        # 查找最后一个 “_”的位置
        ndex = str.rfind('_')
        # print('ndex = ',ndex)
        # 截取字符串
        str_houZhui = str[(ndex + 1):]
        # print('str_houZhui = ',str_houZhui)
        str_Result = str + '\n'  # + str_houZhui+'\n'
        print(str_Result)
        file_handle.write(str_Result)
    file_handle.close()


if __name__ == "__main__":
    listFileInfo = ReadFileDatas()
    # 打乱列表中的顺序
    random.shuffle(listFileInfo)
    WriteDatasToFile(listFileInfo)


# with open("data/trans_result_60684.txt", "r", encoding="utf-8")as fr:
#     with open("data/train.txt", "w+", encoding="utf-8")as fw:
#         class_intent = []
#         list = []
#         count = 0
#         for line in fr.readlines():
#             count += 1
#             pattern = "([^\t]+)\t([^\t]+)"
#             res = re.search(pattern, line)
#             if res is None:
#                 print("not find\n")
#             else:
#                 text = res.group(2)
#             if count % 2 == 1:
#                 label = text.lstrip(" ")
#                 if re.search(r"SearchC", label):
#                     label = "搜索-创建工作"
#                 if re.search(r"SearchS", label):
#                     label = "搜索-事件查询"
#                 if re.search(r"播放音乐", label):
#                     label = "查询-音乐|播放-音乐"
#                 if re.search(r"添加到播放列表", label):
#                     label = "查询-音乐|播放-添加到列表"
#                 if re.search(r"天气", label):
#                     label = "查询-天气查询"
#                 if re.search(r"飞机|飞行", label):
#                     label = "航班-航行"
#                 if re.search(r"地面|航空公司|机票|数量|容量|距离", label):
#                     label = "航班-地面服务"
#                 if re.search(r"航空公司", label):
#                     label = "航班-航空公司"
#                 if re.search(r"机票", label):
#                     label = "航班-机票"
#                 if re.search(r"最便宜的", label):
#                     label = "航班-价格"
#                 if re.search(r"数量", label):
#                     label = "航班-航线数量"
#                 if re.search(r"容量", label):
#                     label = "航班-座位容量"
#                 if re.search(r"距离", label):
#                     label = "航班-飞行距离"
#                 if re.search(r"缩写", label):
#                     label = "搜索-缩写查询"
#                 if re.search(r"[ ]*搜索", label):
#                     label = "搜索-查询"
#                 if re.search(r"书餐厅|餐厅", label):
#                     label = "餐厅-预定"
#                 if re.search(r"市", label):
#                     label = "航班-城市"
#                 if re.search(r"天气", label):
#                     label = "查询-天气"
#                 if re.search(r"航班日期", label):
#                     label = "航班-日期"
#                 if re.search(r"限制", label):
#                     label = "航班-限制"
#                 if re.search(r"电影", label):
#                     label = "播放-电影|查询-电影"
#                 if re.search(r"音乐", label):
#                     label = "查询-音乐|播放-音乐"
#                 if re.search(r"价目表", label):
#                     label = "查询-价格"
#                 if re.search(r"膳食", label):
#                     label = "航班-膳食"
#                 print(str(count)+":"+label)
#                 if label.rstrip("\n") not in class_intent:
#                     if label.rstrip("\n")=="天":
#                         list.append(count)
#                     class_intent.append(label.rstrip("\n"))
#             else:
#                 sent = text
#                 if label is not None and sent is not None:
#                     fw.write(label.rstrip('\n')+' '+sent.rstrip("\n")+"\n")
#                     label = None
#                     sent = None
#         print(class_intent)
#         print(list)

# line = "search 	 搜索"
# pattern = "([^\t]+)\t([^\t]+)"
# res = re.search(pattern, line)
# print(res.group(2))