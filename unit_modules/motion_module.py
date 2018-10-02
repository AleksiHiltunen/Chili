#import naoqi
import sys
import os
import json

PI=3.14159265359

class Motion:
	def __init__(self, session, logger):
		self.motion = session.service("ALMotion")
		self.logger = logger
		self.motion.moveInit()
		
	def move(self, x, y, z):
		#z coordinate need to be radians
		z = z * (PI/180)
		try:
			self.logger.log("Starting to move")
			reach = self.motion.moveTo(x, y, z)
			if reach:
				self.logger.log("Arrived at destination")
				return True
			else:
				self.logger.warning_log("Couldn't arrive at destination")
				return False

		except Exception as e:
			self.logger.error_log(str(e))
			
	def dance(self, dance):
		try:
			dance_dir = os.path.dirname(sys.argv[0]) + "\dances\\"
			dance_json = dance_dir + dance + ".json"
			names = list()
			keys = list()
			times = list()
			with open(dance_json, 'r') as file:
				dance_moves = json.load(file)
				
			for move in dance_moves:
				names.append(move)
				keys.append(dance_moves[move]["keys"])
				times.append(dance_moves[move]["times"])
				
			self.motion.angleInterpolation(names, keys, times, True)	
			self.logger.log("Danced " + dance)

		except Exception as e:
			self.logger.warning_log("Robot may not be familiar with \"" + dance + "\" dance")
			raise e
			
	def move_joint(self, joint, position, speed=0.4):
		try:
			dir_path = os.path.dirname(os.path.realpath(__file__))
			with open(os.path.join(dir_path, "default_joint_positions.json"), 'r') as f:
				data = json.load(f)
			end_position = data["joint"][joint][position]
			res = self.motion.setAngles(joint, end_position, speed)
			self.logger.log("Attempted to move " + joint + " to position " + position)
			if res:
				self.logger.log("Success")
			else:
				self.logger.warning_log("Could not reach gives position")
				
		except Exception as e:
			self.logger.error_log(str(e))
			
	def get_current_joint_position(self, joint, sensor=True):
		try:
			return self.motion.getAngles(joint, sensor)
		except Exception as e:
			raise e
			
	def open_hand(self, joint):
		try:
			return self.motion.openHand(joint)
		except Exception as e:
			raise e
			
	def close_hand(self, joint):
		try:
			return self.motion.closeHand(joint)
		except Exception as e:
			raise e
			