#!/usr/bin/env python3

import requests, os
import glob

# upload single image 
def upload_image(files,url="http://localhost/upload/"):
  try:
    r = requests.post(url, files=files)
    
    if r.status_code == 201:
        print(f"files:{files} uploaded successfully to url:{url}")
  except Exception as e:
    print(f"Exception: {e}\n")
    print(f"{files} failed to upload to URL: {url}\n")
    print("Is the remote web server running or accepting requests?\n")
  except ConnectionError as e:
    print(f"Connection Error: {e}")

# upload all images in specified directory
def upload_images(path, ext='jpeg', url="http://localhost/upload/"):
  for filepath in glob.glob(os.path.join(path,"*." + ext)):
    file, ext = os.path.splitext(filepath)
    image = open(filepath,'rb')

    filename=(os.path.basename(filepath))
    upload_image(files={'image': image},url=url)

    image.close()

if __name__ == "__main__":
  upload_images("supplier-data/images")
