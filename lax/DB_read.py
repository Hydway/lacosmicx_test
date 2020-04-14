#! /usr/bin/env python
# encoding:utf-8

import re
import linecache
import pandas as pd

def CPF_read(file):
    lineNumber = 1
    keys = 'name', 'mag', 'RA', 'Dec', 'cen_x', 'cen_y', 'pos_x', 'pos_y', 'cen-pos_x', 'cen-pos_y'
    data = pd.DataFrame(columns=(keys))
    with open(file, 'r') as f:
        number = []
        for line in f.readlines():
            m = re.findall(r"GAIA \w+", line)
            if m:
                number.append(lineNumber)
            lineNumber += 1

        j = len(number)
        start = number[0] - 1
        end = number[j - 1]
        destlines = linecache.getlines(file)[start:end]
        for i in range(len(destlines)):
            dict_temp = {}
            destlines[i].replace('\n', '')
            des = destlines[i].split()
            des = des[1:]
            dict_temp = dict(zip(keys, des))
            data = data.append(dict_temp, ignore_index=True)
        f.close()
        return data

def QMPF_read(file):
    lineNumber = 1
    keys = 'name', 'RA', 'Dec', 'cen_x_1', 'cen_y_1', 'cen_x', 'cen_y', 'unknown1', 'unknown2', 'unknown3',
    data = pd.DataFrame(columns=(keys))
    with open(file, 'r') as f:
        number = []
        for line in f.readlines():
            m = re.findall(r"STAR = GAIA \w+", line)
            if m:
                number.append(lineNumber)
            lineNumber += 1

        j = len(number)
        start = number[0] - 1
        end = number[j - 1]
        destlines = linecache.getlines(file)[start:end]
        for i in range(len(destlines)):
            dict_temp = {}
            destlines[i].replace('\n', '')
            des = destlines[i].split()
            des = des[1:]
            dict_temp = dict(zip(keys, des))
            data = data.append(dict_temp, ignore_index=True)
        f.close()
        return data