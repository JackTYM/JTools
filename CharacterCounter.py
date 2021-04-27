import time

def text():
	characters = 0
	spaces = 0
	lines = 0
	print("Input your text file's name and extention or the filepath")
	file = input()

	if file:
		#try: 
		x = open(file, 'r')
		while(True):
			line = x.readline()

			lines =+ 1
			if not line:
				break
			for letter in line.strip():
				if letter != (' '):
					characters +=  1
				else:
					spaces += 1
					characters += 1
		print('There are ' + str(characters), 'characters')
		print('There are ' + str(spaces), 'spaces')
		print('There are ' + str(lines), 'lines')
		#except:
			#print('The seems to be missing or cannot be opened. Try again or use the filepath')
			#text()

def Counter():

	characters = 0
	spaces = 0
	lines = 0

	print('Select your input mode:')
	print('(1) 1 Line/Paste')
	print('(2) Text file')
	mode = input()

	if mode == ('1'):
		print('Input your text now')
		string = input()


		if string:
			print('You said "' + string + '"')

			time.sleep(.5)

			print('Counting')

			time.sleep(.5)

			for letter in string:
				if letter != (' '):
					characters +=  1
					print(characters)

					time.sleep(0.25)
				else:
					spaces += 1
					characters += 1

			print('There are ' + str(characters), 'characters')
			print('There are ' + str(spaces), 'spaces')
		else:
			print('That string was invalid.')
			time.sleep(1)
			Counter()
	elif mode == ('2'):
		text()

print("""
 _    _      _                            _____     
| |  | |    | |                          |_   _|    
| |  | | ___| | ___ ___  _ __ ___   ___    | | ___  
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/ 
                                                    
                                                    """)

print("""
 _____ _                          _              _____                   _            _ 
/  __ \ |                        | |            /  __ \                 | |          | |
| /  \/ |__   __ _ _ __ __ _  ___| |_ ___ _ __  | /  \/ ___  _   _ _ __ | |_ ___ _ __| |
| |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__| | |    / _ \| | | | '_ \| __/ _ \ '__| |
| \__/\ | | | (_| | | | (_| | (__| ||  __/ |    | \__/\ (_) | |_| | | | | ||  __/ |  |_|
 \____/_| |_|\__,_|_|  \__,_|\___|\__\___|_|     \____/\___/ \__,_|_| |_|\__\___|_|  (_)
                                                                                        
                                                                                        """)

Counter()