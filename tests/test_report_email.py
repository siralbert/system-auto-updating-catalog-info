#!/usr/bin/env python3

import unittest
import sys
sys.path.append("..")
import shutil
import subprocess

from report_email import *

class TestReportEmail(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
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

  @classmethod
  def tearDownClass(cls):
    shutil.rmtree('supplier-data')
    pass

  # NOTE: setUp runs once per test instance
  def setUp(self):
    pass

  def test_basic(self):
    testcase = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    expected = {'src_dir'  : 'supplier-data/images',
                'dest_dir' : 'supplier-data/images'}
    self.assertEqual(testcase,expected)

  def test_process_data(self):
    print(process_data())
  def test_process_data_diff_path(self):
    print(process_data('supplier-data/descriptions'))
  def test_process_data_nofiles(self):
    print(process_data('supplier-data/'))
  def test_process_data_nofiles_2ndtest(self):
    print(process_data('supplier-data'))

  def tearDown(self):
    pass

unittest.main(verbosity=2)
