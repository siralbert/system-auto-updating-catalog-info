#! /usr/bin/env python3
 
import os
import requests
 
from changeImage import * 
from supplier_image_upload import *
UPLOAD_IMAGES_URL="http://localhost/upload"

#two lines below not needed
BASEPATH_SUPPLIER_TEXT_DES = 'supplier-data/descriptions/'
BASEPATH_SUPPLIER_IMAGE = 'supplier-data/images/'
 
# load list of description file names and image file names and returns a list of text files
def load_descripfilenames_imagefilenames(path_descriptions='supplier-data/descriptions', path_images='supplier-data/images'):
    list_text_files = os.listdir(path_descriptions)
    list_files = [file_name for file_name in list_text_files if '.txt' in file_name]

    list_image_files = os.listdir(path_images)
    list_images = [image_name for image_name in list_image_files if '.jpeg' in image_name]

    return((list_files,list_images))

# load descriptions from files into a list
def create_supplier_data_object_list(list_files, list_images):
    list = []
    for text_file in list_files:
      with open('supplier-data/descriptions/' + text_file, 'r') as f:
        data = {"name":f.readline().rstrip("\n"),
        "weight":int(f.readline().rstrip("\n").split(' ')[0]),
        "description":f.readline().rstrip("\n")}
     
      for image_file in list_images:
        if image_file.split('.')[0] in text_file.split('.')[0]:
          data['image_name'] = image_file

      list.append(data)
    return list
"""
for item in list:
  print(item)
  resp = requests.post('http://35.227.45.62:80/fruits/', json=item)
  if resp.status_code != 201:
    raise Exception('POST error status={}'.format(resp.status_code)) 
  print('Created feedback ID: {}'.format(resp.json()["id"]))
"""
if __name__ == "__main__":
# pre-processes images to correct format before uploading to web server
  convert_images('supplier-data/images')
# upload processed images to web server
  upload_images("supplier-data/images",url=UPLOAD_IMAGES_URL)  #add parameter url="<new_url>" to change target url
# create a list of file names with corresponding list of image names which contain data required by web server
  filelist, imagelist = load_descripfilenames_imagefilenames(path_descriptions='supplier-data/descriptions', path_images='supplier-data/images')
# create a list of JSON objects from file data and image names
  objectlist= create_supplier_data_object_list(filelist,imagelist)
# upload JSON object list containing descriptions and image names to web server
  

