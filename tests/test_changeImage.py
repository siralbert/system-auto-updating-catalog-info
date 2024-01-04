#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")

from changeImage import *

class TestChangeImage(unittest.TestCase):
  def test_basic(self):
    testcase = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    expected = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    self.assertEqual(testcase,expected)

  def test_convert_images(self):
    testcase = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images',
                'size' : (600,400),
                'rotation' : 0}
    expected =  {
                 "size" : (600,400),
                 "mode" : 'RGB',
                 "format" : 'JPEG',
                } 
    convert_images(testcase['src_dir'],size=testcase['size'],rotation=testcase['rotation'])
    for infile in glob.glob(os.path.join(testcase['dest_dir'],'*.jpeg')):
        image_attr = view_image_attr(infile)
        self.assertEqual(image_attr['size'],expected['size'])
        self.assertEqual(image_attr['mode'],expected['mode'])
        self.assertEqual(image_attr['format'],expected['format'])

  def test_convert_image(self):
    testcase = {'src_path'  : 'supplier-data/images/sample.tif',
                  'dest_path' : 'supplier-data/images/sample.jpeg'}
    expected =  {
                 "size" : (600,400),
                 "mode" : 'RGB',
                 "format" : 'JPEG',
                } 
    convert_image(testcase['src_path'],testcase['dest_path'],size=(600,400))
    image_attr = view_image_attr(testcase['dest_path'])
    self.assertEqual(image_attr['size'],expected['size'])
    self.assertEqual(image_attr['mode'],expected['mode'])
    self.assertEqual(image_attr['format'],expected['format'])

  def test_view_image_attr(self):
    testcase = 'supplier-data/images/sample.tif'
    view_image_attr(testcase)

unittest.main()
