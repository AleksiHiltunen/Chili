import os
import datetime
import time

STAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

class Logger:
	def __init__(self, file="log.log"):
		location = os.path.dirname(os.path.realpath(__file__))
		self.file = os.path.join(location, file)
		with open(self.file, 'w') as file:
			file.truncate()
		
	def log(self, msg):
		with open(self.file, 'a') as file:
			file.write(get_time_stamp() + " " + msg + "\n")
		
	def error_log(self, msg):
		with open(self.file, 'a') as file:
			file.write(get_time_stamp() + " **ERROR** " + msg + "\n")
			
	def warning_log(self, msg):
		with open(self.file, 'a') as file:
			file.write(get_time_stamp() + " *WARNING* " + msg + "\n")
			
def get_time_stamp():
	ts = time.time()
	return str(datetime.datetime.fromtimestamp(ts).strftime(STAMP_FORMAT))