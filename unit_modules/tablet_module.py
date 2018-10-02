import time

INDEX_PATH = "http://198.18.0.1/apps/images-979a7b/index.html"
SUFFIX = ".jpg"

class Tablet:
	def __init__(self, session, logger):
		self.tablet = session.service("ALTabletService")
		self.logger = logger
		
	def show_image(self, filename):
		try:
			if not filename.endswith(".jpg"):
				filename = filename + SUFFIX
			if not self.tablet.showWebview(INDEX_PATH + "?url=" + filename):
				self.logger.log("Did not find given file " + str(filename))
		except Exception as e:
			raise e
			
	def turn_on(self):
		try:
			self.tablet.wakeUp()
		except Exception as e:
			raise e
			
	def turn_off(self):
		try:
			self.tablet.goToSleep()
		except Exception as e:
			raise e
			
	def load_page(self, url):
		try:
			if not url.startswith("http"):
				url = fix_url(url)
			self.tablet.loadUrl(url)
		except Exception as e:
			raise e
			
def fix_url(url):
	if not url.startswith("www"):
		url = "www." + url
	return "http://" + url