#@author Yichen Fan
import unittest
import matplotlib as plt
import numpy as np
from PS7Q1 import *
from PS7Q2 import *
from PS7Q3 import *
from PS7Q4 import *

class TestQ1Answers(unittest.TestCase):
	"""Testing for Test Question 1 Answers"""
	def setup(self):
			pass
	def test_Q1_answer(self):
			testQ1 = Question1()
			self.assertTrue(np.array_equal(testQ1.Q1a(),np.array([2,7,12,4,9,14]).reshape(2,3)))
			self.assertTrue(np.array_equal(testQ1.Q1b(),np.array([6,7,8,9,10])))
			self.assertTrue(np.array_equal(testQ1.Q1c(),np.array([2,7,12,3,8,13,4,9,14]).reshape(3,3)))
if __name__ == '__main__':
	unittest.main()
