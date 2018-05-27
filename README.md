# Nltk
Exploring nltk, word frequencies and POS taggers

### Top10()
In this function I am reading a given text file with the Open() function then finding all the Strings with the pytho regular expression function Re() and looping through all the words in the text while incrementing the word count for the frequency distribution function and printing out the top 10 words with the highest frequency.

![image](https://user-images.githubusercontent.com/25343679/40591778-32d189b2-620f-11e8-801a-7c7ddb665287.png)


### zipFreq()
First I assign two empty lists which are the ranks and freqs, next using the
python3 input() function to get the name of the local text file that will be analyzed. Then using
the python file.read() function I get the number of characters from the file, further I use the re
function to get the Strings. Next step is to run the for loops and get the word count and
frequencies with NLTK FreqDist() function. Finally using the imported functions from matplotlib
we construct the grid and labels.
![image](https://user-images.githubusercontent.com/25343679/40591842-1449a712-6210-11e8-84e8-5355d4d73bb2.png)


### randomText()
In this function we open() an already existing empty text file, Then assigning the target_length an integer of
456565 which could be any but I chose this for no reason at all. Then we assign an empty brackets
for the random_string value. Then we run the while loop which states that while the target
_length is higher than random_string and adding “abcdef” string to random_string container
using the random module with each iteration it mixes up the letters and keeps adding them to
random_string. Then at the end it splits them randomly. And finally we close the file.

### dm_tagger()
Best way to deal with the trade-off between accuracy and coverage is to use the most accurate
algorithms whenever possible, which is why in my application I have decided to use the 4 taggers with
the flow of: Trigram tagger -> backoff to Bigram tagger -> backoff to Unigram Tagger -> backoff to
Regular expression tagger. Regular expression tagger by default tags everything it does not understand
as NN which is the same as default tagger.
![image](https://user-images.githubusercontent.com/25343679/40591941-01401aec-6211-11e8-87e7-2aea0a30aee1.png)
![image](https://user-images.githubusercontent.com/25343679/40591949-152e6d74-6211-11e8-969f-af1db55f27ea.png)
