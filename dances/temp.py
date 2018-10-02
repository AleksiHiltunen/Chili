# Choregraphe bezier export in Python.
from naoqi import ALProxy
import json

names = list()
times = list()
keys = list()

data ={}
for item in names:
	id = names.index(item)
	_p = {"times":times[id], "keys":keys[id]}
	d = {str(item):_p}
	data.update(d)
	
print json.dumps(data)
