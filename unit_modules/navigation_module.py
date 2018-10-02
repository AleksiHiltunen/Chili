class Navigation:
	def __init__(self, session, logger):
		self.navigation = session.service("ALNavigation")
		self.logger = logger
	
	def explore(self, radius=1.0):
		try:
			self.navigation.explore(radius)
		except Exception as e:
			raise e