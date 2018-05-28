import numpy, random

def randomText():
	text_file = open('randomtext.txt', 'w')	
	target_length = 456565
	random_string = ""
	while len(random_string) < target_length:
		random_string += random.choice('abcdefg ')
		text_file.write(random_string)
	random_text = random_string.split()
	text_file.close()
