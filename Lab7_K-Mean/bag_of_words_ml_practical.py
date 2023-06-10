import nltk
nltk.download('punkt')
import re

text = """ You are beautiful, but you are empty,” he went on. “One could not die for you. To be sure, an ordinary passerby would think that my rose looked just like you — the rose that belongs to me. But in herself alone she is more important than all the hundreds of you other roses: because it is she that I have watered; because it is she that I have put under the glass globe; because it is she that I have sheltered behind the screen; because it is for her that I have killed the caterpillars (except the two or three that we saved to become butterflies); because it is she that I have listened to, when she grumbled, or boasted, or even sometimes when she said nothing. Because she is my rose.
"""
dataset = nltk.sent_tokenize(text)
for i in range(len(dataset)):
	dataset[i] = dataset[i].lower()
	dataset[i] = re.sub(r'\W', ' ', dataset[i])
	dataset[i] = re.sub(r'\s+', ' ', dataset[i])
print(dataset)

# Creating the Bag of Words model
word2count = {}
for data in dataset:
	words = nltk.word_tokenize(data)
	for word in words:
		if word not in word2count.keys():
			word2count[word] = 1
		else:
			word2count[word] += 1
print(word2count)