#!/usr/bin/env python3

import requests, os
import glob

# upload all images specified in a dictionary
def upload_image(files={"~/tmp/tiff-image.jpeg":open(os.path.expanduser("~/tmp/tiff-image.jpeg"),'rb')},url="http://localhost/upload/"):
  try:
    r = requests.post(url, files=files)

  except Exception as e:
    print(f"Exception: {e}\n")
    print("Is the remote web server running or accepting requests?\n")
#    file = [key for key in files]
    print(f"web server url: {url}  file names: {files}")
    return {'url' : url,'files' : files}
  except ConnectionError as e:
    print(f"Connection Error: {e}")
  finally:
    #TODO: New Connection Error generating exception of reading of closed file
    for key in files:
      files[key].close()

# upload all images in specified directory
def upload_images(path, ext='jpeg', url="http://localhost/upload/"):
  files={}
  for filepath in glob.glob(os.path.join(path,"*." + ext)):
    file, ext = os.path.splitext(filepath)
#    print(f"filepath: {filepath} file: {file} ext: {ext}")
    image = open(filepath,'rb')
    files[filepath]=image
  listofimages=upload_image(files=files,url=url)
  if files:
    for key in files:
      files[key].close()
  print(listofimages)
  return(listofimages)

if __name__ == "__main__":
  upload_image()
  upload_images()
