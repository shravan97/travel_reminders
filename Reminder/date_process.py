import time

class dateProcessor:
	"""class dateProcessor"""
	def __init__(self , date):
		self.date = date

	def extract_elements(self):
		d = self.date
		elements = d.split('-')
		return elements

	def set_cron_date(self):
		inp = self.extract_elements(self.date)
		curr_yr = time.strftime("%y")
		curr_month = time.strftime("%m")
		curr_day = time.strftime("%d")