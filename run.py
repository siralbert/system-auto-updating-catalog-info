#! /usr/bin/env python3

import os
import requests
import re
import json

from supplier_image_upload import *

UPLOAD_URL="http://localhost/upload"

def load_descriptions(path):
    if not path.endswith('/'):
      path = os.path.join(path + '/')
    list = []
    folder = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path + file))]
    for file in folder:
           fullpath=os.path.join(path + file) 
           imagefile,ext = os.path.splitext(file)
           imagefile = imagefile + '.jpeg' 
           with open(fullpath, 'r') as f:
               list.append({"name":f.readline().rstrip("\n"),
                   "weight":f.readline().rstrip("\n"),
                   "description":f.readline().rstrip("\n"),
                   "image_name":imagefile})
    return list

# convert descriptions to JSON format before uploading
def convert_descriptions(list):
    for item in list:
        item["weight"] = int(re.sub(r" lbs","",item["weight"]))
        item=json.dumps(item)
        print(item)
    return list
  
# upload JSON'ized' descriptions to web server
def upload_descriptions(list,url="http://localhost/upload"):
  for item in list:
      try:

        print(json.dumps(item))

        resp = requests.post(url, json=json.dumps(item))
        print(f"response: {resp}")
        if resp.status_code != 201:
            raise Exception('POST error status={}'.format(resp.status_code))
        print('Created feedback ID: {}'.format(resp.json()["id"]))
      except Exception as e:
        print(f"Exception: {e}\n")
        print("Is the remote web server running or accepting requests?\n")
        print(f"web server url: {url}  json object: {item}")
        return {'url' : url,'json_object' : json.dumps(item)}
      except ConnectionError as e:
        print(f"Connection Error: {e}")


if __name__ == "__main__":
#  upload_images("supplier-data/images",url=UPLOAD_URL)  #add parameter url="<new_url>" to change target url
  list=load_descriptions("supplier-data/descriptions")
  list=convert_descriptions(list)
  upload_descriptions(list, url="http://35.227.95.57/fruits")              #add parameter url="<new_url>" to change target url
  pass
