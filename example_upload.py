#!/usr/bin/env python3
import requests, os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
#with open('/usr/share/apache2/icons/icon.sheet.jpeg', 'rb') as opened:
with open(os.path.expanduser('~/tmp/tiff-image.jpeg'), 'rb') as opened:
    r = requests.post(url, files={'file': opened})
