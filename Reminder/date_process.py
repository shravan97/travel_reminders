import time

class dateProcessor:
	"""class dateProcessor"""
	def __init__(self , date , Time):
		self.date = date
		self.Time = Time

	def extract_elements(self , k):
		if k:
			d = self.date
			elements = d.split('-')
			return elements
		t = self.Time
		return t.split(':')		

	def set_cron_elements(self):
		inp_date = self.extract_elements(1)
		inp_Time = self.extract_elements(0)
		curr_yr = time.strftime("%y")
		curr_month = time.strftime("%m")
		curr_day = time.strftime("%d")
		
		cron_elements = {'time':[] , 'date':[]}
		cron_elements['time'] = inp_Time

		if int(inp_date[0])-int(curr_yr)-2000 >1:
			return -1
		elif int(inp_date[0])-int(curr_yr)-2000 ==1 :
			if int(inp_date[1])-int(curr_month) > 0:
				return -1
			elif int(inp_date[1])-int(curr_month) == 0:
				if int(inp_date[2])-int(curr_day) >=0:
					return -1
				else:
					cron_elements['date'] = inp_date
			else:
				cron_elements['date'] = inp_date
		else:
			cron_elements['date'] = inp_date			