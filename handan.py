#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import numpy


def get_raw_tuple(file_name):
    dict = {}
    with open(file_name) as f:
        lines = f.readlines()
    i = 0
    text_list = []
    category_list = []
    for line in lines:
        if i == 0:
            i = 1
            # text_list.append(line)
            seg_list = jieba.cut(line)
            seg_id_list = []
            for seg in seg_list:
                if seg in dict:
                    dict[seg]["freq"] += 1
                else:
                    dict[seg] = {}
                    dict[seg]["id"] = len(dict)
                    dict[seg]["freq"] = 1
                seg_id_list.append(dict[seg]["id"])
            text_list.append(seg_id_list)
            # print("|".join(seg_list))
        else:
            i = 0
            category_list.append(int(line.strip()))

    return text_list, category_list


def load_data():
    jieba.load_userdict('dict.txt')
    (train_x_raw, train_y_raw) = get_raw_tuple('handan-train.txt')
    (test_x_raw, test_y_raw) = get_raw_tuple('handan-test.txt')
    x_train = numpy.array(train_x_raw)
    y_train = numpy.array(train_y_raw)
    x_test = numpy.array(test_x_raw)
    y_test = numpy.array(test_y_raw)
    return (x_train, y_train), (x_test, y_test)
