import os
import sys
import argparse
import string
import thread
import json
import time

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, "robot_broker"))

import Robot

help_text = {
	"say":"say <>",
	"speak":"speak <>",
	"listen":"listen <array_of_words_to_expoect> <visual_expression_when_word_recognized>",
	"detect":"detect <array_of_words_to_expoect> <visual_expression_when_word_recognized>",
	"move":"move <foward/backward/left/rigth/clockwise/counterclockwise]=value>",
	"walk":"walk <foward/backward/left/rigth/clockwise/counterclockwise]=value>",
	"unknown":"Not known command",
	"play":"play <path_to_file>"
}
	
def _print_help(issue):
	for _i, cmds in commands.items():
		if issue in cmds[0]:
			print cmds[2]
			return
	print "Not known command"
		
def _say(r, words):
	sentance = ""
	for word in words:
		sentance = sentance + " " + word
	r.say(sentance)
			
def _listen(r, word_list):
	r.listen(word_list)

def _move(r, to):
	return r.move(to)
	
def _show_image(r, path):
	r.show_image(path)
	
def _play_file(r, path):
	r.play_file(path)
		
def _dance(r, dance):
	r.dance(str(dance[0]))

def _wait(r, _time):
	time.sleep(float(_time[0]))
	
def _animation(r, key):
	r.animation(key)
	
def _change_language(r, lang):
	r.change_language(str(lang[0]))
	
def _set_volume(r, vol):
	r.set_vol(vol)
	
def _exec_script(r, args):
	try:
		for item in args:
			parse_script(r, str(item))
			
	except Exception as e:
		raise e
		
def _take_picture(r, args):
	r.take_picture(args)
	
def _move_joint(r, args):
	r.move_joint(args)
	
def _posture(r, args):
	r.go_to_posture(args)
	
def _autonomous_life(r, args):
	r.set_autolife_state(str(args[0]))
	
def _stop(r, args):
	r.stop_move()
	
def _goto_charge(r, args):
	r.goto_charge_station(args)
	
def _turn_on_leds(r, args):
	r.turn_on_leds(args)
	
def _turn_off_leds(r, args):
	r.turn_off_leds(args)
	
def _roll_eyes(r, args):
	r.roll_eyes(args)

def _explore(r, args):
	r.explore(args)

def _tablet(r, args):
	r.show_tablet(args)
	
def _webpage(r, args):
	r.show_webpage(args)
	
def _quit():
	sys.exit(0)
	
commands = {
	"quit_command":[["quit", "exit", "end"], _quit, "Exits Chili \n\nquit, exit, end \nExample: ()o_o) exit"],
	"say_command":[["say", "speak"],_say,"speaks out a word or a sentence \n\nsay <> \nExample: ()o_o) say Hello, world!"],
	"move_command":[["move", "walk"],_move,"Moves to gives direction specified amount of meters \nExample: ()o_o) move forward=1 clockwise=180 left=0.5"],
	"show_image_command":[["show", "image", "show_image", "picture"],_show_image,"Shows a image on the tablet  \n\nshow, image, show_image, picure\nExample: ()o_o) image picture1.jpg"],
	"play_command":[["play", "play_sound", "play_file"],_play_file,"Plays a sound file from Peppers filesystem \n\nplay, play_sound, play_file \nExample: ()o_o) play /home/nao/wav/whistle.wav"],
	"dance_command":[["dance"],_dance,"Dances the given dance. Does nothing if not known dance \n\n dance \nExample: ()o_o) dance disco"],
	"wait_command":[["wait"],_wait,"Waits for given amount of seconds \n\n wait \nExample: wait 4"],
	"animation_command":[["animation"],_animation,"Play a random animation from given animation tag \n\n animation \nExample: ()o_o) animation hello"],
	"language_command":[["language"],_change_language,"Changes a current spoken language \n\nlanguage \nExample: ()o_o) language Finnish"],
	"volume_command":[["volume"],_set_volume,"Changes volume \n\nvolume \n Example: ()o_o) volume 50"],
	"script_command":[["script"],_exec_script,"Run a script file (.txt) \n\nscript\nExample: ()o_o) script test.txt"],
	"take_picture_command":[["take_picture", "shoot", "photo", "picture"],_take_picture,"Takes a picture using the forehead camera. Saves the picture as given filename. If filename already exists, overwrites the older one. \n\ntake_picture, shoot, photo, picture \nExample: ()o_o) picture pic1.jpg"],
	"motion_command":[["motion", "rotate", "joint"],_move_joint,"Joint manipulation \n\njoin, rotate\nExample: ()o_o) joint larm=up"],
	"posture_command":[["posture", "take_posture", "go_to_posture"],_posture,"Attempts to take a given posture \n\nposture, take_posture, go_to_posture\nExample: ()o_o) posture Crouch"],
	"autonomous_life_command":[["autonomous_life", "autolife", "auto_life"],_autonomous_life,"Set state of autonomous moving/life \n\nautolife, auto_life, autonomous_life \nExample: ()o_o) autolife disabled"],
	"stop_command":[["seize", "stop", "freeze", "halt"],_stop,"Stops all current movements\n\nstop, seize, freeze, halt\nExample: ()o_o) halt"],
	"goto_charge_station_command":[["charge", "go_to_charge_station"],_goto_charge,"PLACEHOLDER"],
	"leds_on_command":[["leds_on", "turn_on", "turn_on_leds", "illuminate", "lights_on"],_turn_on_leds,"Turn on the given group of LEDs\n\nleds_on, turn_on, turn_on_leds, illuminate, lights_on\nExample: ()o_o) turn_on ears"],
	"leds_off_command":[["leds_off", "turn_off", "turn_off_leds", "lights_off"],_turn_off_leds,"Turn off the given group of LEDs\n\nleds_off, turn_off, turn_off_leds, lights_off\nExample: ()o_o) turn_off ears"],
	"rotate_eyes_command":[["rotate_eyes", "random_eyes", "eyes_roll"],_roll_eyes,"Rotates eyes LEDs for given amount of seconds \n\n rotate_eyes, random_eyes, eyes_roll \nExample: ()o_o) random_eyes 4"],
	"exploration_command":[["wander", "move_around", "explore"],_explore,"Moves Pepper around in given radius in meters \n\nwander, move_around, explore\nExample: ()o_o) move_around 5"],
	"show_tablet_command":[["tablet", "display", "monitor"],_tablet,"Command to turn the tablet on/off \n\ntablet, display, monitor\nExample: ()o_o) tablet off"],
	"load_web_page_command":[["website", "webpage"],_webpage,"Displays a given website on tablet\n\nwebsite, webpage\nExample: ()o_o) webpage www.google.com"]
}	
		
	
def command_handler(r, cmd):
		if len(cmd[0]) == 0 or cmd[0].startswith("#"):
			return
		prime = [cmd[0].lower()]
		found = 0
		temp = []
		for index in cmd:
			index = index.lower()
			temp.append(index)
		cmd = temp
		for _k, value in commands.items():
			if prime[0] not in value[0]:
				continue
			elif prime[0] in value[0]:
				found = 1
				break
				
		if not found:
			print "unknown_command: " + prime[0]
			return
		
		cmd = [x for x in cmd if x != '']
		if len(cmd) > 1 and (cmd[1] == "--help" or cmd[1] == "-h"):
			_print_help(prime[0])
			return
		
		if prime[0] in commands["quit_command"][0]:
			_quit()
		
		for command in commands.values():
			if prime[0] in command[0]:
				if len(cmd) == 1 and prime[0] != "stop" and prime[0] != "seize" and prime[0] != "freeze":
					print("Invalid number of parameters: At least one parameter required")
					_print_help(prime[0])
				elif cmd[-1] == "&":
					thread.start_new_thread(command[1],(r, cmd[1:]))
				else:
					return command[1](r, cmd[1:])
	
def parse_script(r, file):
	data = ""
	try:
		with open(file, 'r') as f:
			data = f.read()
	except Exception as e:
		print "Failed to read the script file", file, e
	
	data = data.splitlines()
	for line in data:
		line = line.split(" ")
		command_handler(r, line)
			
def real_time_command(r):
	cmd = ""
	while True:
		cmd = raw_input("()o_o) ")
		cmd = cmd.split(" ")
		command_handler(r, cmd)
		
def main(args):
	parser = argparse.ArgumentParser(description='Robot Broker')
	parser.add_argument("-A", "--ip", help="IP address of the robot. Defaults to 192.168.1.101", default="192.168.1.101")
	parser.add_argument("-P", "--port", help="Port of the Robot. Defaults to 9559", default="9559")
	parser.add_argument("-s", "--script", help="Script file, see example script or something...", default=None)
	parsed_args = parser.parse_args()
	
	try:
		r = Robot.Robot(parsed_args.ip, parsed_args.port)
	except Exception as e:
		print "Failed to initiate robot", e
		return 1
		
	if parsed_args.script != None:
		parse_script(r, parsed_args.script)
	else:
		real_time_command(r)
	
if __name__ == "__main__":
	main(sys.argv)
	