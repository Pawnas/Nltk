def top10():
	book = input("enter the name of the file ending in .txt: ")
	import nltk #using imports in a function to make it quicker
	from nltk import FreqDist
	fd = FreqDist()
	open_file = open(book, 'r')
	file_to_string = open_file.read()
	import re
	words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
	for word in words:
		fd[word] += 1
	for word, count in fd.most_common(10):
		print(word, count)
