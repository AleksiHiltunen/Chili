##################################################################
##########   HOW TO USE MIDDLEWARE ON PEPPER   ###################
##################################################################

git clone this repo or direct download

#Used in PC without Choregraphe
	Requirements:
		*Python 2.7
		*NAOqi Python SDK
	
	Setting up:
		- copy the "chili"-folder to <path_to_python_2.7>/Lib/
		- make sure there is: 	<path_to_python_2.7>/Lib/site-packages/qi 
								<path_to_python_2.7>/Lib/site-packages/naoqi.py
	
	Using:
		- help:
			command prompt: python <path_to_python_2.7>/Lib/chili/middleware.py --help
		- run middleware interpreter:
			command prompt: python <path_to_python_2.7>/Lib/chili/middleware.py
		- run middleware interpreter with certain ip and port:
			command prompt: python <path_to_python_2.7>/Lib/chili/middleware.py --ip <ip_address> --port <port>
		- run middleware with scirpt:
			command prompt: python <path_to_python_2.7>/Lib/chili/middleware.py --script <path_to_the_script>
		
		- using virtual robot with middleware:
			Start choregraphe
			Connect to virtual robot
			Remember the port of the virtual robot (seen in choregraphe)
			command prompt: python <path_to_python_2.7>/Lib/dippatyo/middleware.py --ip localhost --port <check_the_port_from_choregraphe>
			

#Used in Choregraphe created application (I don't know if this works with virtual robot)
	You need:
		*Pepper
		*Choregraphe
		*install the middleware into Pepper
		
	Installing middleware in Pepper:
		Download or git clone the middlware from gitlab to your PC
		copy the dippatyo folder into pepper
			command prompt (Windows): pscp -r "<path_to_middleware>" <pepper_username>@<pepper_ip>:/<path_to_install_to>
			(I've installed the middleware into path /home/nao/ in Pepper. It can be used from there if it's not deleted)
			
	Using in Choregraphe:
		- Create a middleware understandable script in Pepper
		- In Choregraphe add these lines of code to the place where you want to execute a middleware script:
			import os
			os.system("python <path_to_middleware> --ip <Peppers_ip> --port <Peppers_port> --script <path_to_script">)
	