#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba
import numpy

handan_dict = {}


def get_raw_tuple(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    i = 0
    text_list = []
    category_list = []
    lines_raw = []
    for line in lines:
        if i == 0:
            i = 1
            seg_list = jieba.cut(line)
            seg_id_list = []
            lines_raw.append(line)
            for seg in seg_list:
                if seg in handan_dict:
                    handan_dict[seg]["freq"] += 1
                else:
                    handan_dict[seg] = {}
                    handan_dict[seg]["id"] = len(handan_dict)
                    handan_dict[seg]["freq"] = 1
                seg_id_list.append(handan_dict[seg]["id"])
            text_list.append(seg_id_list)
        else:
            i = 0
            category_list.append(int(line.strip()))

    return text_list, category_list, lines_raw


def load_data(include_dict=True):
    if include_dict:
        jieba.load_userdict('dict.txt')
    (train_x_raw, train_y_raw, train_x_lines) = get_raw_tuple('handan-train.txt')
    (test_x_raw, test_y_raw, test_x_lines) = get_raw_tuple('handan-test.txt')
    x_train = numpy.array(train_x_raw)
    y_train = numpy.array(train_y_raw)
    x_test = numpy.array(test_x_raw)
    y_test = numpy.array(test_y_raw)
    return (x_train, y_train), (x_test, y_test), (train_x_lines, test_x_lines)
