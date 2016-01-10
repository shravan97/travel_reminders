import os,time

def getInput(err):
	if err:
		travel = raw_input("Please enter a correct date : ")
	else :
		travel = raw_input("Please enter in your travel date : ")	
	return travel


def validate(travel):
	#Check if the user entered a valid date using regular expressions
	#And then return a boolean
	return 1 #for now	


def InputChk(err=0):
	inp = getInput(err)
	if validate(inp)==0:
		return InputChk(1)
	else:
		return inp

inp = InputChk()
print "Thank you!!!"