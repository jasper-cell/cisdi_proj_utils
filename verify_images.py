#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

import glob
import os


def verify(imgs_path, xmls_path, bad_images_path):

    xmls_list = [v.replace('.xml', '') for k,v in enumerate(os.listdir(xmls_path))]
    print(len(xmls_list))

    images_list = [v.replace('.jpg', '') for k,v in enumerate(os.listdir(images_path))]
    print(len(images_list))

    mv_list = []

    n = 0
    for k,v in enumerate(images_list):
        if v not in xmls_list:
            print(v)
            n += 1
            mv_list.append(v)

    for k,v in enumerate(mv_list):
        img_filename = v + '.jpg'
        cmd = "mv {}{} {}".format(images_path, img_filename, bad_images_path)
        os.system(cmd)


if __name__ == '__main__':

    xmls_path = '../data/n17_cooling_bed_loading_ic/xmls/'
    images_path = '../data/n17_cooling_bed_loading_ic/images/'
    bad_images_path = '../data/n17_cooling_bed_loading_ic/bad_images/'
    os.makedirs(bad_images_path) if not os.path.exists(bad_images_path) else None

    verify(images_path, xmls_path, bad_images_path)


