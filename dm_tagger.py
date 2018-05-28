import nltk
from nltk.corpus import brown
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk import ne_chunk

def dm_tagger():
	brown_tagged_sents = brown.tagged_sents(categories='news')
	brown_sents = brown.sents(categories='news')
	size = int(len(brown_tagged_sents) * 0.9)
	train_sents = brown_tagged_sents[:size]
	test_sents = brown_tagged_sents[size:]
	default_tagger = nltk.RegexpTagger(
		[(r'.*ing$', 'VBG'), # gerunds
		(r'.*ed$', 'VBD'), # simple past
		(r'.*es$', 'VBZ'), # 3rd singular present
		(r'.*ould$', 'MD'), # modals
		(r'.*\'s$', 'NN$'), # possessive nouns
		(r'.*s$', 'NNS'), # plural nouns
		(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
		(r'(The|the|A|a|An|an)$', 'AT'), # articles
		(r'.*able$', 'JJ'), # adjectives
		(r'.*ness$', 'NN'), # nouns formed from adjectives
		(r'.*ly$', 'RB'), # adverbs
		(r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
		(r'(His|his|Her|her|Its|its)$', 'PRP$'), # possesive
		(r'(my|Your|your|Yours|yours)$', 'PRP$'), # possesive
		(r'(on|On|in|In|at|At|since|Since)$', 'IN'),# time prepopsitions
		(r'(for|For|ago|Ago|before|Before)$', 'IN'),# time prepopsitions
		(r'(till|Till|until|Until)$', 'IN'), # time prepopsitions
		(r'(by|By|beside|Beside)$', 'IN'), # space prepopsitions
		(r'(under|Under|below|Below)$', 'IN'), # space prepopsitions
		(r'(over|Over|above|Above)$', 'IN'), # space prepopsitions
		(r'(across|Across|through|Through)$', 'IN'),# space prepopsitions
		(r'(into|Into|towards|Towards)$', 'IN'), # space prepopsitions
		(r'(onto|Onto|from|From)$', 'IN'), # space prepopsitions
		(r'\.$','.'), (r'\,$',','), (r'\?$','?'), # fullstop, comma, Qmark
		(r'\($','('), (r'\)$',')'), # round brackets
		(r'\[$','['), (r'\]$',']'), # square brackets
		(r'(Sam)$', 'NAM'),
		(r'.*', 'NN') # nouns (default)
		])
	u_tagger=nltk.UnigramTagger(train_sents, backoff=default_tagger)
	b_tagger=nltk.BigramTagger(train_sents, backoff=u_tagger)
	t_tagger=nltk.TrigramTagger(train_sents, backoff=b_tagger)
	textfile = input("please enter the name of the text ending in .txt: ")
	f_read=open(textfile,'r')
	given_text=f_read.read();
	segmented_lines=nltk.sent_tokenize(given_text)
	for text in segmented_lines:
		words=word_tokenize(text)
		sent = t_tagger.tag(words)
	print("\nprinting some words to see how the tagger performs: \n\n",
	ne_chunk(sent[1:10]))
	print("\nEvaluation of combined taggers on train sents \n\n ",
	t_tagger.evaluate(train_sents))
	print("\nEvaluation of combined taggers on test sents \n\n ",
	t_tagger.evaluate(test_sents))
