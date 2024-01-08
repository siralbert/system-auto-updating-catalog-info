#!/usr/bin/env python3

import unittest
from unittest.mock import MagicMock
import sys
sys.path.append("..")

from reports import *

class TestReports(unittest.TestCase):
  
  def setUp(self):
    pass

  def test_basic(self):
    testcase = "" 
    expected = "" 
    self.assertEqual(testcase,expected)

  def test_generate(self):
    testcase = "" 
    expected = "" 
    self.assertEqual(testcase,expected)
  
  def tearDown(self):
    pass

unittest.main()

