#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:jasper

import os
import glob
# import pandas as pd
import xml.etree.ElementTree as ET
import cv2
import time

def convert(size, box, ratio=0.75):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        # print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # print(root.find('filename').text)
        save_txt = []
        for member in root.findall('object'):
            filename = root.find('filename').text  # filenamend('size').find('height').text)
            width = int(root.find('size').find('width').text)  # width
            height = int(root.find('size').find('height').text)  # height
            class_id = int(member.find('name').text)  # class
            # xmin = int(member.find('bndbox').find('xmin').text)  # xmin
            # ymin = int(member.find('bndbox').find('ymin').text)  # ymin
            # xmax = int(member.find('bndbox').find('xmax').text)  # xmax
            # ymax = int(member.find('bndbox').find('ymax').text)  # ymax
            b = (float(member.find('bndbox').find('xmin').text), float(member.find('bndbox').find('xmax').text), float(member.find('bndbox').find('ymin').text),
                 float(member.find('bndbox').find('ymax').text))

            # print(f'filename {filename}, class_id: {class_id}')
            res = convert((width, height), b)
            # print(res)
            mid = []
            # ratio = 360.0 / 480
            mid.append(class_id)
            mid.append(res[0])
            mid.append(res[1])
            mid.append(res[2])
            mid.append(res[3])
            print(mid)
            print("----------------------------")
            save_txt.append(mid)
            # print(filename)
            image = cv2.imread(f"../datasets/n17_cooling_bed_loading_ic/images_/{filename}")
            # cv2.imshow("img", image)
            # image = cv2.resize(image, (640, 480))
            cv2.imwrite(f"../datasets/n17_cooling_bed_loading_ic/images_fin/train/{filename}", image)
            # cv2.waitKey(0)

            # exit()
            filename = filename.split(".")[0]
            print(save_txt)
        with open(f"./txt_sum/{filename}.txt", 'w') as f:
            for item in save_txt:
                print("==================================")
                info = str(item)
                info = info.strip("[]")
                # print(info.strip("[]"))
                # print(info.replace(",", ''))
                info = info.replace(",", '')
                info = info + "\n"
                # print(info)
                # time.sleep(2)
                # cv2.waitKey(0)
                # exit()
                f.write(info)
                # cv2.putText()
            # exit()
            # xml_list.append(value)


    # column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    # xml_df = pd.DataFrame(xml_list, columns=column_name)
    # return xml_df


def main():
    data_dir = '../datasets/n17_cooling_bed_loading_ic/xmls'
    # for directory in ['train', 'test', 'validation']:
    #     xml_path = os.path.join(os.getcwd(), data_dir + 'annotations/{}'.format(directory))
    #     os.makedirs(xml_path) if not os.path.exists(xml_path) else None
    #
    #     xml_df = xml_to_csv(xml_path)
    #     # xml_df.to_csv('whsyxt.csv', index=None)
    #     xml_df.to_csv(os.path.join(os.getcwd(), data_dir + 'data/{}_labels.csv'.format(directory)), index=None)
    #     print('Successfully converted xml to csv.')
    xml_to_csv(data_dir)


if __name__ == '__main__':
    main()
