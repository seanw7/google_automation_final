#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# the Python Requests module



lab_ip = "TODO: INSERT THIS"
url = "http://{}/upload".format(lab_ip)
type_to_convert = ('.jpg','.jpeg')
upload_files_from = "/home/sean/Documents/courses/google_python_automation/course 6/"

def list_of_imgfiles(folder_loc):
    all_files = os.listdir(folder_loc)

    img_files = [file for file in all_files if os.path.splitext(file)[1] in type_to_convert]    
    # print(img_files)
    return img_files

def post_files(list_of_files):
    for file in list_of_files:
        with open(os.path.join(upload_files_from, file), 'rb') as opened:
            # print(opened)
            requests.post(url, files={'file': opened})


files_to_upload = list_of_imgfiles(upload_files_from)
post_files(files_to_upload)







