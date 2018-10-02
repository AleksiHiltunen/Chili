codes = {
	#"head":"BrainLeds",
	"face":"FaceLeds",
	"all":"AllLeds",
	"ears":"EarLeds",
	"chest":"ChestLeds",
	"eyes":"FaceLeds"
	#"feet":"FeetLeds"
}

class Leds:
	def __init__(self, session, logger):
		self.leds = session.service("ALLeds")
		self.logger = logger
		
	def leds_on(self, led):
		try:
			self.leds.on(codes[led])
		except KeyError as e:
			self.logger.warning_log(str(e))
		except Exception as e:
			raise e
			
	def leds_off(self, led):
		try:
			self.leds.off(codes[led])
		except KeyError as e:
			self.logger.warning_log(str(e))
		except Exception as e:
			raise e

	def rotate_eyes(self, duration=5):
		try:
			self.leds.rotateEyes( 0x0000ff, 0.4, duration)
		except Exception as e:
			raise e