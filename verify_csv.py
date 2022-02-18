#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

import os
import csv
import numpy as np
import cv2


def verify(data_dir):

    for directory in ['train', 'test', 'validation']:

        csv_path = os.path.join(os.getcwd(), data_dir + 'data/{}_labels.csv'.format(directory))
        f = open(csv_path, 'r')
        csvreader = csv.reader(f)
        final_list = list(csvreader)[1:]

        number = len(final_list)
        for i in range(number):
            filename = final_list[i][0]
            label = final_list[i][3]
            xmin = int(final_list[i][4])
            ymin = int(final_list[i][5])
            xmax = int(final_list[i][6])
            ymax = int(final_list[i][7])

            # cv2.namedWindow('images', cv2.WINDOW_NORMAL)
            # img_path = os.path.join(os.getcwd(),'images/{}'.format(filename))
            img_path = data_dir + 'images/%s' % filename
            img = cv2.imread(img_path)
            img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 255), 4)

            # show
            # cv2.imshow('images', img)
            # print(label)

            if i >= 10:
                break

            cv2.imwrite(data_dir + 'data/verify_results/{}'.format(str(i) + '.jpg'), img)

            # if cv2.waitKey(1) & 0xff == ord("q"):
            #     break
        # cv2.destroyAllWindows()

if __name__ == '__main__':

    data_dir = '../data_/n1_double_steel_ic/'
    verify(data_dir)
