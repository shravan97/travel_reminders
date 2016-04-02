import getpass
from crontab import CronTab

# For now , set a cronjob in the name of user and later add root
username = getpass.getuser()
#Get existing cronjobs for user using subprocess to capture the output of 'crontab -l'
class CronProcessor(object):
	''' To added a new cronjob , to edit and delete a cronjob'''
	
	def __init__(self , possessions):
		self.numReminders = sum(1 for line in open('myReminders.txt' ,'r'))
		self.possessions = possessions
		self.cron = CronTab(user=username)

	def add_cron(self , date_time):
		c = self.cron
		job = c.new(command='python -id '+self.newnum+' alarm.py' , comment=str(self.newnum))
		job.setall(date_time)