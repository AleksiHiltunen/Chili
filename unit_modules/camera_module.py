BASEPATH = "/home/nao/.local/share/PackageManager/apps/images-979a7b/html/"

class Camera:
	def __init__(self, session, logger):
		self.camera = session.service("ALPhotoCapture")
		self.logger = logger
	
	def take_picture(self, filename):
		try:
			self.camera.takePicture(BASEPATH, filename)
		except Exception as e:
			raise e
