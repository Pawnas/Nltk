import nltk
from nltk.corpus import brown
from random import shuffle

def performance(cfd, wordlist):
	brown_tagged_sents = brown.tagged_sents(categories='news')
	brown_sents = brown.sents(categories='news')
	size = int(len(brown_tagged_sents) * 0.9)
	train_sents = brown_tagged_sents[:size]
	test_sents = brown_tagged_sents[size:]
	lt = dict((word, cfd[word].max()) for word in wordlist)
	u_tagger=nltk.UnigramTagger(model=lt,
	backoff=nltk.DefaultTagger('NN'))
	return u_tagger.evaluate(test_sents)
