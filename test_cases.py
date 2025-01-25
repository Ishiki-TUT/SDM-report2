#!/usr/bin/python3
#test_case.py

import unittest
from calc_mul import calc
import sys

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        #正常系テスト
        def test_valid_multiplication(self):
                self.assertEqual(21, calc(3,7))
                self.assertEqual(1,calc(1,7))
                self.assertEqual(20000,calc(100,200))

        #異常系テスト
        def test_boundary_values(self):
                self.assertEqual(-1,calc(0,7))          # ゼロ
                self.assertEqual(-1,calc(-1,7))         # 負数
                self.assertEqual(-1,calc(0.1,999))      # 小数
                self.assertEqual(-1,calc('a',7))        # 文字列
                self.assertEqual(-1,calc(None,7))       # None

        #境界値テスト
        def test_boundary_values(self):
                self.assertEqual(sys.maxsize,calc(sys.maxsize,1))       # 最大値
                self.assertEqual(-1,calc(-sys.maxsize - 1,1))           # 負の最大値
                self.assertEqual(-1,calc(0,1))                          # ゼロ
                

