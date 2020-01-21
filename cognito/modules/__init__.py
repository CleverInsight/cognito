"""
{ item_description }
"""
import os
import sys
import pandas as pd
import numpy as np


class Check(object):

	def __ini__(self):
		pass


	@staticmethod
	def is_categorical(col):
		"""
		Determines whether the specified col is categorical.
		
		:param      col:  column name
		:type       col:  { pandas.series }
		:return 	boolean

		Usage:
		======
			>> Check.is_categorical(data['Age'])
			>> True
		"""
		pass
		

	@staticmethod
	def is_continuous(col):
		"""
		Determines whether the specified col is continuous.
		
		:param      col:  column name
		:type       col:  { pandas.series }
		:return 	boolean

		Usage:
		======
			>> Check.is_continuous(data['Age'])
			>> True
		"""
		pass
