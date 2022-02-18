#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):

    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(root.find('filename').text)

        for member in root.findall('object'):
            value = (root.find('filename').text,  # filenamend('size').find('height').text)
                     int(root.find('size').find('width').text),  # width
                     int(root.find('size').find('height').text),  # height
                     int(member.find('name').text),  # class
                     int(member.find('bndbox').find('xmin').text),  # xmin
                     int(member.find('bndbox').find('ymin').text),  # ymin
                     int(member.find('bndbox').find('xmax').text),  # xmax
                     int(member.find('bndbox').find('ymax').text),  # ymax
                     )
            # print(value)
            xml_list.append(value)

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():

    data_dir = '../data/n17_cooling_bed_loading_ic/'
    for directory in ['train', 'test', 'validation']:
        xml_path = os.path.join(os.getcwd(), data_dir + 'annotations/{}'.format(directory))
        os.makedirs(xml_path) if not os.path.exists(xml_path) else None

        xml_df = xml_to_csv(xml_path)
        # xml_df.to_csv('whsyxt.csv', index=None)  
        xml_df.to_csv(os.path.join(os.getcwd(), data_dir + 'data/{}_labels.csv'.format(directory)), index=None)
        print('Successfully converted xml to csv.')


if __name__ == '__main__':
    main()
