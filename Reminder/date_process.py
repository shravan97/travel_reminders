import time
import datetime

class dateProcessor:
	"""class dateProcessor"""
	def __init__(self , date , Time):
		self.date = date
		self.Time = Time

	@staticmethod
	def get_curr_date():
		curr = [time.strftime("%y") , time.strftime("%m") ,time.strftime("%d")]
		return curr

	def set_cron_elements(self):
		curr = self.get_curr_date()

		t=self.Time
		d=self.date

		inp_Time = [t.hour , t.minute]
		inp_date = [d.year , d.month , d.day]

		cron_elements = {'time':[] , 'date':[]}
		cron_elements['time'] = inp_Time

		if int(inp_date[0])-int(curr[0])-2000 >1:
			return -1
		elif int(inp_date[0])-int(curr[0])-2000 ==1 :
			if int(inp_date[1])-int(curr[1]) > 0:
				return -1
			elif int(inp_date[1])-int(curr[1]) == 0:
				if int(inp_date[2])-int(curr[2]) >=0:
					return -1
				else:
					cron_elements['date'] = inp_date
			else:
				cron_elements['date'] = inp_date
		else:
			cron_elements['date'] = inp_date

		return 	cron_elements