import os
import sys
import argparse
import string
import thread
import json
import time

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, "..", "unit_modules"))

import audio_module
import camera_module
import listen_module
import motion_module
import speak_module
import tablet_module
import animation_module
import posture_module
import autonomouslife_module
import recharge_module
import leds_module
import navigation_module

import Logger
import qi

class Robot:
	def __init__(self, logger, ip="192.168.1.101", port=9559 ):
		try:
			self.logger = logger
			self.logger.log("Initiating Robot")
			self.ip = ip
			self.port = port
			
			self.session = qi.Session()
			self.session.connect("tcp://" + self.ip + ":" + str(self.port))
			
			#initialize robot abilities
			try:
				self._audio = audio_module.Audio(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._say = speak_module.Say(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._motion = motion_module.Motion(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._posture = posture_module.Posture(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._autolife = autonomouslife_module.AutonomousLife(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._leds = leds_module.Leds(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._navigation = navigation_module.Navigation(self.session, self.logger)
			except Exception as e:
				print(e)
			try:
				self._animation = animation_module.Animation(self.session, self.logger)
			except Exception as e:
				print(e)
			#Following abilities do not work properly or at all with virtual robot so they are not initiated to avoid exceptions
			#"localhost" indicates directly to virtual robot
			if self.ip != "localhost":
				try:
					self._camera = camera_module.Camera(self.session, self.logger)
				except Exception as e:
					print(e)
				try:
					self._listen = listen_module.Listen(self.session, self.logger)
				except Exception as e:
					print(e)
				try:
					self._tablet = tablet_module.Tablet(self.session, self.logger)
				except Exception as e:
					print(e)
				try:
					self._recharge = recharge_module.Recharge(self.session, self.logger)
				except Exception as e:
					print(e)
				
			else:
				self.logger.log("Not initiating certain features since virtual robot is used")
				
			self.logger.log("Robot initiated")
			
		except Exception as e:
			self.logger.error_log("Robot initiation failed: " + str(e))
			raise e
			
	def say(self, text):
		try:	
			self._say.say(text)
			self.logger.log("Robot says " + text)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log(str(e))
			
	def listen(self, word_list, visual=None):
		try:
			if len(word_list) < 1:
				self.logger.log("Input error: please give parameter array [word1, word2, ..., wordN]")
				return
			self._listen.listen_for(word_list, visual)
			self.logger.log("Robot listen to words: " + str(word_list))
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log(str(e))
			
	def move(self, to=None):
		x = 0.0
		y = 0.0
		z = 0.0
		try:
			for item in to:
				if "forward=" in item:
					x = float(item.strip("forward="))
				elif "right=" in item:
					y = -float(item.strip("right="))
				elif "left=" in item:
					y = float(item.strip("left="))
				elif "back=" in item:
					x = -float(item.strip("back="))
				elif "counterclockwise=" in item:
					z = float(item.strip("counterclockwise="))
				elif "clockwise=" in item:
					z = -float(item.strip("clockwise="))
				
			self.logger.log("Robot moves " + str(x) + " forward, " + str(y) + " side and " + str(z) + " around its axis.")			
			if self._motion.move(x,y,z):
				return True
			else:
				return False
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log(str(e))
			
	def show_image(self, path):
		try:
			self._tablet.show_image(str(path[0]))
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log(str(e))
			
	def play_file(self, path):
		try:
			self._audio.play_file(str(path[0]))
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.log(str(e))
			
	def dance(self, dance):
		try:
			self._motion.dance(dance)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.log(str(e))
			
	def animation(self, key):
		try:
			anim = ""
			i = 0
			while i in range(0, len(key)):
				anim += str(key[i])
				if i == len(key) - 1:
					break
				anim += " "
				i += 1
			self._animation.play(anim)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.log(str(e))
			
	def change_language(self, lang):
		try:
			self._say.change_language(lang)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			print("Language not installed")
			self.logger.log(str(e))
			
	def set_vol(self, vol):
		vol = vol[0]
		if vol == "up":
			vol = self._say.get_volume() + 0.1
		elif vol == "down":
			vol = self._say.get_volume() - 0.1
		try:
			self._say.set_volume(float(vol))
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.log(str(e))
			
	def move_joint(self, args):
		try:
			for arg in args:
				if "larm=" in arg:
					joint = "LArm"
					position = arg.strip("larm=")
				elif "rarm=" in arg:
					joint = "RArm"
					position = arg.strip("rarm=")
				elif "head" in arg:
					joint = "Head"
					position = arg.strip("head=")
				elif "lhand" in arg:
					position = arg.strip("lhand=")
					if position == "open":
						self._motion.open_hand("LHand")
					elif position == "close":
						self._motion.close_hand("LHand")
					continue;
				elif "rhand" in arg:
					position = arg.strip("rhand=")
					if position == "open":
						self._motion.open_hand("RHand")
					elif position == "close":
						self._motion.close_hand("RHand")
					continue
				else:
					self.logger.error_log("Unknown joint")
					continue
				self._motion.move_joint(joint, position)
				
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			raise e
			
	def take_picture(self, args):
		try:
			path = str(args[0])
			self._camera.take_picture(path)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			raise e
			
	def go_to_posture(self, posture):
		try:
			self._posture.take_posture(str(posture[0]))
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log("Failed to reach posture: " + str(posture[0]) + " " + str(e))
			
	def set_autolife_state(self, state):
		try:
			self._autolife.set_state(state)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log("Unable to set autonomous life state to: " + state)
			
	def stop_move(self):
		try:
			self.move()
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log("Cannot stop: " + str(e))
			
	def turn_on_leds(self, param):
		try:
			for p in param:
				self._leds.leds_on(p)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log("Unable to modify leds: " + str(e))
			
	def turn_off_leds(self, param):
		try:
			for p in param:
				self._leds.leds_off(p)
		except AttributeError as e:
			self.logger.log("AttributeError. Are you using virtual robot? " + str(e))
		except Exception as e:
			self.logger.error_log("Unable to modify leds: " + str(e))
			
	def roll_eyes(self, param):
		try:
			self._leds.rotate_eyes(float(param[0]))
		except Exception as e:
			self.logger.error_log("Unable to modify leds: " + str(e))
			
	def explore(self, param):
		try:
			radius = float(param[0])
			self._navigation.explore(radius)
		except Exception as e:
			self.logger.error_log("Unable to start exploration: " + str(e))
			
	def show_tablet(self, param):
		try:
			if str(param[0]) == "on":
				self._tablet.turn_on()
			elif str(param[0]) == "off":
				self._tablet.turn_off()
			else:
				print("Can't do that.. Try \"tablet on\" or \"display off\"")
				return
				
		except Exception as e:
			self.logger.log("Unable to turn turn tablet " + str(param[0]) + " " + str(e))
			
	def show_webpage(self, param):
		try:
			url = str(param[0])
			self._tablet.load_page(url)
		except Exception as e:
			self.logger.log("Can't load page " + url)