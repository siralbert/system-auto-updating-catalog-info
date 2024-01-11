#!/usr/bin/env python3

import unittest
from unittest import mock
#from unittest.mock import MagicMock
import sys
sys.path.append("..")

from supplier_image_upload import *

def mocked_requests_post(*args,**kwargs):
    print("post request sent: . . .")

# remove these unit tests?

class TestSupplierImageUpload(unittest.TestCase):
  
  # setup Mock web server for uploading images to 
  # (patch requests.post method with a mock )
  def setUp(self):
    url = "http://localhost/upload/"
    def web_server_post_received(request):
        return(201,f"request: {request} sent to web server")


  def test_basic(self):
    testcase = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    expected = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    self.assertEqual(testcase,expected)

  # return input web server url and file to be uploaded to server
  def test_upload_image_singlefile(self):
    testcase = {'url':'http://localhost/upload/',
                'files' : {'file' : open('supplier-data/images/009.jpeg','rb')}}
    expected = {'url':'http://localhost/upload/',
                'files' : {'file' : open('supplier-data/images/009.jpeg','rb')}}
    # expect an Exception to be raised since web server is not running
#    self.assertRaises(Exception,upload_image(testcase['file']),testcase['url'])
    self.assertRaises(Exception,upload_image(testcase['files']),testcase['url'])
    # TODO: How can test if url and file name parameters input to function are the expected values
#    self.assertEqual(upload_image(testcase['file'],testcase['url']),expected)
    self.assertEqual(upload_image(testcase['files'],testcase['url']),expected)
  
  # return input web server url and files to be uploaded to server
  def test_upload_image_multiplefiles(self):
    testcase = {'url':'http://localhost/upload/',
                'files' : {'supplier-data/images/009.jpeg':open('supplier-data/images/009.jpeg','rb'),'supplier-data/images/008.jpeg':open('supplier-data/images/008.jpeg','rb'),'supplier-data/images/007.jpeg':open('supplier-data/images/007.jpeg','rb')}
                }
    expected = {'url':'http://localhost/upload/',
                'files' : {'supplier-data/images/009.jpeg':open('supplier-data/images/009.jpeg','rb'),'supplier-data/images/008.jpeg':open('supplier-data/images/008.jpeg','rb'),'supplier-data/images/007.jpeg':open('supplier-data/images/007.jpeg','rb')}
                }
    # expect an Exception to be raised since web server is not running
    self.assertRaises(Exception,upload_image(testcase['files']),testcase['url'])
    # TODO: How can I test if url and file name parameters input to function are the expected values
    self.assertEqual(upload_image(testcase['files'],testcase['url']),expected)

  # TODO: test that dictionary of all images and image file descriptors were generated successfully
  def test_upload_images(self):
    test = {'path'  : 'supplier-data/images',
                'url' : 'http://localhost/upload'}
    expc = {'path'  : 'supplier-data/images',
                'images' : [image for image in glob.glob(os.path.join(test['path'],"*." + 'jpeg'))]} 
    diction=upload_images(test['path'],url=test['url'])

    print(expc['images'])
    print(f"files: {diction}")

  # test that upload_images function does not raise an error or exception when no images are in directory
  def test_upload_images_nofiles(self):
    test = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    expc = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    upload_images(test['path'],url=test['url'])
  
  def tearDown(self):
    pass

unittest.main()
