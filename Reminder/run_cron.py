import getpass
from crontab import CronTab
from datetime import datetime

#Get existing cronjobs for user using subprocess to capture the output of 'crontab -l'
class CronProcessor(object):
	''' To added a new cronjob , to edit and delete a cronjob'''

	def validity(self,date_time):
		curr = datetime.now()

		if date_time<curr:
			return 0
		return 1	

	def __init__(self , possessions , date_time):
		self.numReminders = sum(1 for line in open('myReminders.txt' ,'r'))
		self.possessions = possessions
		self.cron = CronTab(user=username)
		self.username = getpass.getuser()

		if validity(date_time):
			self.isValid = True
			self.date_time = date_time
		else
			self.isValid = False
			print "Your reminder date is invalid"

	def add_cron(self):
		if self.isValid:
			c = self.cron
			job = c.new(command='python -id '+self.newnum+' alarm.py' , comment=str(self.newnum))
			job.setall(self.date_time)
			job.enable()
			c.remove_all(time='* * * * *')
			c.write()
		else:
			print "Your date is invalid"