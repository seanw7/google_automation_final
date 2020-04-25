#!/usr/bin/env python3

import os
import requests
from reports import generate_report

upload_files_from = "/home/{}/supplier-data/descriptions/".format(os.environ['USER'])
txt_file_loc = "/home/{}/supplier-data/descriptions/".format(os.environ['USER'])
post_url = 'http://34.71.14.76/fruits/'
# Now, you'll have to process the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/ directory and save them in a 
# data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:

def collect_txtfiles(folder_loc):
    all_files = os.listdir(folder_loc)
    txt_files = [file for file in all_files if file.endswith(".txt")]
    return txt_files

def process_txtfile(txt_file):
    # print(txt_file)
    dict_obj = {}
    with open(os.path.join(txt_file_loc,txt_file), 'r') as file_data:
        file = file_data.readlines()
        dict_obj['name'] = file[0].strip()
        # This is where i am attempting to strip all non digits from string in weight data
        numeric_filter = filter(str.isdigit, file[1].strip())
        numeric_string = "".join(numeric_filter)

        dict_obj['weight'] = int(numeric_string)
        # dict_obj['weight'] = file[1].strip()
        dict_obj['description'] = file[2].strip()
    # for k,v in dict_obj.items():
    #     print(k,v)
    return dict_obj

def post_product_json(dict_obj):
    print("Posted: {}, to {}".format(dict_obj, post_url))

    response = requests.post(post_url, json=dict_obj)
    if not response.ok:
        print(response.content)
        raise Exception("POST failed with status code {}".format(response.status_code))



upload_dict = dict()
txt_file_list = collect_txtfiles(txt_file_loc)
print(txt_file_list)
for file in txt_file_list:
    file_dict = process_txtfile(file)
    img_dict = {
            'Avocado': '002.jpeg',
            'Apple': '001.jpeg',
            'Blackberry': '003.jpeg',
            'Grape': '004.jpeg',
            'Kiwifruit': '005.jpeg',
            'Lemon': '006.jpeg',
            'Mango': '007.jpeg',
            'Plum': '008.jpeg',
            'Strawberry': '009.jpeg',
            'Watermelon': '010.jpeg'}
    file_dict['image_name'] = img_dict[file_dict['name']]
    print(file_dict)
    
    post_product_json(file_dict)
    #TODO: Line below is outdate and will need to reflect new report_email script
    # generate_report('processed.pdf', 'title_goes_here', file_dict['description'])

# name
# weight (in lbs)
# description

# The data model in the Django application fruit has the following fields: 
#     name, 
#     weight, 
#     description,
#     image_name. 
    
# The weight field is defined as an integer field. 
# So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. 
# For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

# The image_name field will allow the system to find the image associated with the fruit. 
# Don't forget to add all fields, including the image_name!




# The final JSON object should be similar to:
# {
#     "name": "Watermelon", 
#     "weight": 500, 
#     "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
#     "image_name": "010.jpeg"
# }

# Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL http://[linux-instance-external-IP]/fruits
