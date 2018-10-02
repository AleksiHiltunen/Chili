#import naoqi

class Say:
	def __init__(self, session, logger):
		self.tts = session.service("ALTextToSpeech")
		self.logger = logger
		
	def say(self, text):
		try:
			self.tts.say(text)
		except Exception as e:
			self.logger.error_log(str(e))
			
	def get_language(self):
		try:
			return self.tts.getLanguage()
		except Exception as e:
			self.logger.error_log(str(e))
			
	def change_language(self, lang):
		try:
			lang = lang.strip("\"")
			lang = lang.capitalize()
			self.tts.setLanguage(lang)
		except Exception as e:
			raise e
			
	def set_volume(self, vol):
		try:
			if vol > 1 and vol < 101:
				vol /= 100
			self.tts.setVolume(float(vol))
		except Exception as e:
			self.logger.error_log(str(e))
			
	def get_volume(self):
		try:
			return self.tts.getVolume()
		except Exception as e:
			self.logger.error_log(str(e))