#!/usr/bin/env python3

import requests, os
import glob

# upload single image 
def upload_image(files,url="http://localhost/upload/"):
  try:
    r = requests.post(url, files=files)
  except Exception as e:
    print(f"Exception: {e}\n")
    print("Is the remote web server running or accepting requests?\n")
    print(f"web server url: {url}  file names: {files}")
    return {'url' : url,'files' : files}
  except ConnectionError as e:
    print(f"Connection Error: {e}")

# upload all images in specified directory
def upload_images(path, ext='jpeg', url="http://localhost/upload/"):
  for filepath in glob.glob(os.path.join(path,"*." + ext)):
    file, ext = os.path.splitext(filepath)
    image = open(filepath,'rb')
    upload_image(files={'file':image},url=url)
    image.close()

if __name__ == "__main__":
  upload_images("supplier-data/images")
