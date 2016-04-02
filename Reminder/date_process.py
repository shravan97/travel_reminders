from datetime import datetime

class date_time_Processor:
	"""class for processing the input date and time and set the cron variables"""
	def __init__(self , DateTime):
		self.DateTime = DateTime

	def set_cron_elements(self):
		curr = datetime.now()
		inp = self.DateTime

		if inp<curr:
			return -1
		else:
			return self.DateTime