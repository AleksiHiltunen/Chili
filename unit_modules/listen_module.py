#import naoqi

class Listen:
	def __init__(self, session, logger):
		try:
			self.listen = session.service("ALSpeechRecognition")
			self.logger = logger
			self.memory = session.service("ALMemory")
		except Exception as e:
			raise e
			
	def listen_for(self, word_list, visual=None):
		try:
			
			#if visual:
			#	self.listen.setVisualExpression(visual)
			#	self.listen.pushContexts()
			self.listen.pause(True)
			#self.memory.unsubscribeToEvent("WordRecognized", "self.listen_for")
			self.listen.removeAllContext()	
			self.listen.setVocabulary(word_list, True)
			self.memory.subscribeToEvent("WordRecognized", "self.listen_for", "onWordRecognized")
			self.listen.pause(False)
     
		except Exception as e:
			raise e
		
	def onWordRecognized(self):
		say = session.service("ALTextToSpeech")
		say.say("Hello there then")
		return