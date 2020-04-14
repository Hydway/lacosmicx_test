# -*- coding: utf-8 -*-
import numpy as np

def bgclean(n, im, star_x, star_y):

    # 检查越界（如果星星在最右边上，右边的像素就不用保存到new矩阵中了）
    def isValid(im, x, y):
        return x >= 0 and x < im.shape[0] and y >= 0 and y < im.shape[1]

    # 建立和原矩阵一样大的new矩阵；star_xy记录星星及邻域的坐标
    n = (n-1)/2
    new = np.zeros((len(im), len(im[0])))
    star_xy = []

    # 把星星及邻域的坐标复制到新矩阵里，用star_xy记录其坐标
    for index in range(len(star_x)):
        for x in range(int(round(star_x[index])) - n, int(round(star_x[index]) + n)):
            for y in range(int(round(star_y[index])) - n, int(round(star_y[index]) + n)):
                if isValid(im, x, y) is True:
                    star_xy.append([x, y])
                    new[x, y] = im[x, y]

    # Sum：把除去星星和射线的背景值像素加起来，方便下面计算背景平均值
    # n：疑似宇宙射线的像素点个数（非星星且像素值大于100）
    # s：星星邻域像素点个数；m：原矩阵总像素点个数
    Sum = 0
    n = 0
    s = 0
    m = len(im) * len(im[0])

    # 求Sum
    for i in range(len(im)):
        for j in range(len(im[0])):
            if im[i, j] in star_xy:
                s = s + 1
                continue;
            if im[i, j] > 100:
                im[i, j] = 0
                n = n + 1
            else:
                Sum = Sum + im[i, j]

    # 求背景平均值
    average = Sum / (m - n - s)

    # 除星星邻域外其他所有地方全部赋值为背景平均值
    for i in range(len(im)):
        for j in range(len(im[0])):
            if [i, j] not in star_xy:
                new[i, j] = average

    return new