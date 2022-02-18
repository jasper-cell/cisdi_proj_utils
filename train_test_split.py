import glob
import random
import numpy
import shutil

txt_labels_paths = glob.glob("./txt_sum/*.txt")
print(f"original: {txt_labels_paths[0]}")
random.shuffle(txt_labels_paths)
# print(txt_labels_paths[0])
txt_length = len(txt_labels_paths)
train_num = int(0.7 * txt_length)
val_num = int(0.1 * txt_length)
test_num = txt_length - train_num - val_num
txt_dir_train = "./n17_cooling_bed/labels/train/"
txt_dir_val = "./n17_cooling_bed/labels/val/"
txt_dir_test = "./n17_cooling_bed/labels/test/"

for index, txt_label_path in enumerate(txt_labels_paths):
    filname = txt_label_path.split("\\")[-1].split(".")[0]
    print(filname, index)
    if index < train_num:
        shutil.copyfile(txt_label_path, txt_dir_train + filname + ".txt")
        shutil.copyfile("../datasets/n17_cooling_bed_loading_ic/images_fin/train/" + filname + ".jpg", "./n17_cooling_bed/images/train/" + filname + ".jpg")
    elif train_num < index < (train_num + val_num):
        shutil.copyfile(txt_label_path, txt_dir_val + filname + ".txt")
        shutil.copyfile("../datasets/n17_cooling_bed_loading_ic/images_fin/train/" + filname + ".jpg",
                        "./n17_cooling_bed/images/val/" + filname + ".jpg")
    else:
        shutil.copyfile(txt_label_path, txt_dir_test + filname + ".txt")
        shutil.copyfile("../datasets/n17_cooling_bed_loading_ic/images_fin/train/" + filname + ".jpg",
                        "./n17_cooling_bed/images/test/" + filname + ".jpg")
    # shutil.copyfile(txt_label_path, txt_dir + )

    # break
