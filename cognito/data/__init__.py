import pandas as pd
import numpy as np


class Table(object):

	def __init__(self, filename):
		self.data = pd.read_csv(filename)



	def columns(self):
		return self.data.columns