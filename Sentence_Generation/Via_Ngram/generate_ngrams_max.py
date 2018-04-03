from nltk import bigrams, ConditionalFreqDist
from nltk.corpus import gutenberg
from string import punctuation
import random


def generate_sentence(cfdist, word, num=15):
    sentence = list()
    for i in range(num):
        word = cfdist[word].max()
        sentence.append(word)
    print(' '.join(sentence))


text = gutenberg.words('bible-kjv.txt')
text = [item for item in text if item not in punctuation]
bigrams = bigrams(text)
cfd = ConditionalFreqDist(bigrams)
start = random.choice(text)
generate_sentence(cfd, start)
