class AutonomousLife:
	def __init__(self, session, logger):
		self.aa = session.service("ALAutonomousLife")
		self.logger = logger
		
	def set_state(self, state):
		try:
			self.aa.setState(state)
		except Exception as e:
			raise e
	