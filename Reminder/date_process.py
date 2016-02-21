import time

class dateProcessor:
	"""class dateProcessor"""
	def __init__(self , date):
		self.date = date

	def extract_elements(self):
		d = self.date
		elements = d.split('-')
		return elements