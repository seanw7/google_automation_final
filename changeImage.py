#!/usr/bin/env python3

# import PIL
from PIL import Image
import os
import glob


img_search_path = "/home/{}/supplier-data/images/".format(os.environ['USER'])
resize_to = (600,400)
img_type_to_convert = 'tiff'
save_files_loc = '/home/{}/supplier-data/images/'.format(os.environ['USER'])


def list_of_imgfiles(folder_loc):
    all_files = os.listdir(folder_loc)
    print(all_files)
    img_files = [file for file in all_files if file.endswith(img_type_to_convert)]
    print(img_files)
    return img_files


def modify_image(img, img_dimensions):
    im = Image.open(img)
    file_name = os.path.basename(img)
    new_filename = file_name.strip(".{}".format(img_type_to_convert))
    print("Saving file: {}, at {}.jpeg".format(img, new_filename))
    im.resize(img_dimensions).convert("RGB").save("{}/{}.jpeg".format(save_files_loc,new_filename))

def main():
    ### Grabs all files with img_type_to_convert extension ###
    img_files = list_of_imgfiles(img_search_path)
    ### Loops over images in array and modifys them ###
    for img in img_files:
        full_img_path = os.path.join(img_search_path,img)
        modify_image(full_img_path, resize_to)

main()
