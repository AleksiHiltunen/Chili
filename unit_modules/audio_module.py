class Audio:
	def __init__(self, session, logger):
		self.audio = session.service("ALAudioPlayer")
		self.logger = logger
		
	def play_file(self, path):
		try:
			self.audio.playFile(path)
			self.logger.log("Successfully played file " + path)
		except Exception as e:
			raise e
	