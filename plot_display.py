import pylab

def display():
	word_freqs =
	nltk.FreqDist(brown.words(categories='news')).most_common()
	words_by_freq = [w for (w, _) in word_freqs]
	cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
	sizes = 2 ** pylab.arange(15)
	perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Unigram, Default tagger performance with Varying Model
	Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()
