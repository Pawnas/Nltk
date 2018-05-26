def zipFreq():
	ranks = []
	freqs = []
	from nltk import FreqDist
	fd = FreqDist()
	textfile = input("please enter the name of the text ending in
	.txt: ")
	open_file = open(textfile, 'r')
	file_to_string = open_file.read()
	import re
	words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)
	import matplotlib.pyplot as plt
	for word in words:
		fd[word] += 1
	for rank, (word, _) in enumerate(fd.most_common()):
		ranks.append(rank+1)
		freqs.append(fd[word])
	plt.loglog(ranks, freqs)
	plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
	plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
	plt.grid(True)
	plt.show()
