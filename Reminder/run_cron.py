import getpass
from crontab import CronTab

# For now , set a cronjob in the name of user and later add root
username = getpass.getuser()
#Get existing cronjobs for user using subprocess to capture the output of 'crontab -l'