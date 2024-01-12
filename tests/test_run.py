#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")

from run import *
import json

import subprocess
import shutil

class TestRun(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
#    cls._connection = createExpensiveConnectionObject()

    #test cases require list of files in 'supplier-data/images' and in supplier-data/descriptions directories to pass
    #extract sample archive which creates a supplier-data folder and puts the required directories and files in it.
    if os.path.isdir("supplier-data"):
        shutil.rmtree('supplier-data')
   
    result=subprocess.run(['tar', 'xvf', '../bak/supplier-data.tar.gz']) 
    if result.returncode == 0:
        print()
        print("Successfully extracted directories and files from supplier-data.tar.gz archive to supplier-data/ directory . . .\n")
    else:
        print()
        print("An error occured: {} {}\n".format(result.stdout,result.stderr))

    #may not need these variables to be initialized
    cls.list_descripnames, cls.list_imagenames = load_descripfilenames_imagefilenames()
  
  @classmethod
  def tearDownClass(cls):
#    cls._connection.destroy() 
    pass

  # setup Mock web server for uploading images to 
  # (patch requests.post method with a mock )
  # NOTE: setUp runs once per test instance
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

# test converting images to correct format
  def test_convert_images(self):
      convert_images('supplier-data/images')
      expected=['007.jpeg', '010.jpeg', '006.jpeg', '004.jpeg', '005.jpeg', '002.jpeg', '008.jpeg', '003.jpeg', '009.jpeg', '001.jpeg']
      files = [file for file in os.listdir('supplier-data/images') if '.jpeg' in file]
      self.assertEqual(sorted(expected),sorted(files))

# test uploading images, will raise an exception if no webserver found at localhost
  def test_upload_images(self):
      result = upload_images("supplier-data/images",url="http://localhost/upload")
      self.assertRaises(Exception,result)

# test loading image and description filenames into a list using default parameter values supplied by function load_descripfilenames_imagefilenames( path_images= 'supplier-data/images', path_descriptions='supplier-data/descriptions')
  def test_load_descripfilenames_imagefilenames(self):
      testcase = {} # use default paths as described in comment above
      expected = (['005.txt', '008.txt', '003.txt', '006.txt', '002.txt', '009.txt', '001.txt', '004.txt', '007.txt', '010.txt'],['007.jpeg', '010.jpeg', '006.jpeg', '004.jpeg', '005.jpeg', '002.jpeg', '008.jpeg', '003.jpeg', '009.jpeg', '001.jpeg']) 
      self.assertEqual(load_descripfilenames_imagefilenames(),expected)

# this test also uses default parameter values supplied by the load_descripfilenames_imagefilenames function tested above
  def test_create_supplier_data_object_list(self):
    descripfilenames, imagenames =  load_descripfilenames_imagefilenames()
    objectlist = create_supplier_data_object_list(descripfilenames,imagenames)
#The following two lines of code creates a file for use as the expected JSON objects.  These objects can be loaded (deserialized) into a python list for comparison with the object list returned from calling create_supplier_data_object_list 
#    with open('test_create_supplier_data_object_list_testcase.json','w') as jsonfile:
#        json.dump(list,jsonfile,indent=2)
    with open('test_create_supplier_data_object_list_testcase.json','r') as jsonfile:
        expected=json.load(jsonfile)
    self.assertEqual(objectlist,expected)

  # test that upload_descriptions function does not raise an error or exception when no descriptions are in directory
  def test_create_supplier_data_object_list_nofiles(self):
    testcase = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    expected = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    list=create_supplier_data_object_list([],[])

  def tearDown(self):
    pass

unittest.main(verbosity=2)
