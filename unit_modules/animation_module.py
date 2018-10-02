class Animation:
	def __init__(self, session, logger):
		self.animation = session.service("ALAnimationPlayer")
		self.logger = logger
		
	def play(self, key):
		try:
			self.animation.runTag(key)
		except Exception as e:
			print "(This) Pepper may not know animation: \"" + key + "\", check the name and spelling of animation"
			raise e