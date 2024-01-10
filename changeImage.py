#!/usr/bin/env python3

from PIL import Image
import re
import glob, os

#import subprocess
#from multiprocessing import Pool

# modifies image attributes (format, size, and rotation)
# (dest_path includes filename and extension type of source file)
def convert_image(path, dest_path, ext='.jpeg', size=(128,128), rotation=270):
  im = Image.open(path)
  new_dest_path = re.sub(r"\.\w{1,4}$",'.jpeg',dest_path)
  im.rotate(rotation).resize(size).convert("RGB").save(new_dest_path)
  im.close()


# retrieves Image attributes from file
def view_image_attr(path):
  im = Image.open(path)
  size = im.size
  mode = im.mode
  fmt = im.format
  im.close()
  return {'size':size,'mode':mode,'format':fmt}

# process all images in current directory
def convert_images(path,size=(128,128),rotation=0):
  size = 600, 400
  for infile in glob.glob(os.path.join(path,"*.tiff")):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
      destfile = file + '.jpeg'
      convert_image(file + ext,destfile, size=size,rotation=rotation)

if __name__ == "__main__":
#    spawn_thread()
  convert_images('supplier-data/images')

