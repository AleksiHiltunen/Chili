#import naoqi

class Posture:
	def __init__(self, session, logger):
		self.posture = session.service("ALRobotPosture")
		self.logger = logger
		
	def take_posture(self, posture, speed=0.4):
		try:
			posture = posture.capitalize()
			self.posture.goToPosture(posture, speed)
			self.logger.log("Taking posture: " + posture)
		except:
			raise e