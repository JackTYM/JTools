import os
import sys

final = ''
lines = []

def err():
	print('It seems an error has occured.')
	print('(1) Restart program')
	print('(2) Close window')
	err = input()

	if err == ('1'):
		os.system('cls')
		list_creator()
	elif err == ('2'):
		sys.exit()
	else:
		err()

def list_creator():
	try:
		print('Input your placeholder (1 digit only):')
		placeholder = input()

		if len(placeholder) == 1:
			print('Input your list format using', placeholder, 'as your symbol to be replaced:')
			format = input()

			if placeholder in format:
				print('Select your output mode:')
				print('(1) Console (prints to console)')
				print('(2) File (saves to current dir)')
				output = input()

				if output == '1':
					print('Select your mode:')
					print('(1) List mode (each letter of the list is used instead of', placeholder)
					print('(2) Text mode (each line of text is used instead of', placeholder)
					mode = input()

					if mode:
						if mode == '1':
							print('Input your list:')
							list = input()

							if list:
								for letter in list:
									print(format.replace(placeholder, letter))
						elif mode == '2':
							while(True):
								print("Input your text file's name and extention or the filepath")
								file = input()

								if file:
									try: 
										x = open(file, 'r')
									except:
										print('The seems to be missing or cannot be opened. Try again or use the filepath')
										continue
									while(True):
										line = x.readline()

										if not line:
											break
										print(format.replace(placeholder, line.strip()))
									break
				elif output == '2':
						print('Select your mode:')
						print('(1) List mode (each letter of the list is used instead of', placeholder, ')')
						print('(2) Text mode (each line of text is used instead of', placeholder, ')')
						mode = input()

						if mode:
							if mode == '1':
								print('Input your list:')
								list = input()

								if list:
									try:
										os.remove('ListCreator.txt')
									except: pass
								
									finally:
										with open('ListCreator.txt', 'w') as fl:
											pass
											for letter in list:
												fl.write(format.replace(placeholder, letter))
												fl.write('\n')
							elif mode == '2':
								while(True):
									print("Input your text file's name and extention or the filepath")
									file = input()

									if file:
										try: 
											x = open(file, 'r')
										except:
											print('The seems to be missing or cannot be opened. Try again or use the filepath')
											continue
										finally:
											with open('ListCreator.txt', 'w') as fl:
												pass
												while(True):
													line = x.readline()
												
													if not line:
														break
													fl.write(format.replace(placeholder, line.strip()))
													fl.write('\n')
									break
	except:
		err()

list_creator()
