#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")

from run import *

class TestRun(unittest.TestCase):
  
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

  # test load_descriptions from files into a list
  def test_load_descriptions(self):
    testcase = {'path' : 'supplier-data/descriptions'}
    expected = ['001.txt','002.txt','003.txt','004.txt','005.txt','006.txt','007.txt','008.txt','009.txt','010.txt']

    dict = load_descriptions(testcase['path'])
    list = []
    for elem in dict:
        list.append(elem['image_name'])
    self.assertEqual(sorted(list),expected)

  # test converting descriptions to proper json format for upload
  def test_convert_descriptions(self):
    testcase = [{'name': 'Kiwifruit', 'weight': '250 lbs', 'description': 'Kiwifruit contains rich vitamin C, which can strengthen the immune system and supplement the nutrients consumed by the brain. Its perfect ratio of low sodium and high potassium can replenish the energy lost by working long hours.', 'image_name': '005.txt'}]
    expected = [{'name': 'Kiwifruit', 'weight': 250, 'description': 'Kiwifruit contains rich vitamin C, which can strengthen the immune system and supplement the nutrients consumed by the brain. Its perfect ratio of low sodium and high potassium can replenish the energy lost by working long hours.', 'image_name': '005.txt'}]
    self.assertEqual(convert_descriptions(testcase),expected)

  # test upload_descriptions of json objects from list to web server
  def test_upload_descriptions(self):
    testcase = [{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"},{"name": "Plum", "weight": 150, "description": "Plums are rich in sugar, vitamins, fruit acids, amino acids and other nutrients. With high nutritional value, Plums have outstanding health-care functions, which includes refreshing and nourishing liver, relieving depression and poisoning, and clearing dampness and heat of the human body.", "image_name": "008.txt"}]

    expected = [{"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"},{"name": "Plum", "weight": 150, "description": "Plums are rich in sugar, vitamins, fruit acids, amino acids and other nutrients. With high nutritional value, Plums have outstanding health-care functions, which includes refreshing and nourishing liver, relieving depression and poisoning, and clearing dampness and heat of the human body.", "image_name": "008.txt"}]

    dict = upload_descriptions(testcase)
#    self.assertEqual(dict[],expected)

  # test that upload_descriptions function does not raise an error or exception when no descriptions are in directory
  def test_load_descriptions_nofiles(self):
    testcase = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    expected = {'path'  : 'supplier-data/',
                'url' : 'http://localhost/upload'}
    list=load_descriptions("supplier-data/")

  def tearDown(self):
    pass

unittest.main()
