from nltk import bigrams, ConditionalFreqDist
from nltk.corpus import gutenberg
import random
from string import punctuation


def generate_text(cfdist, word, num=15):
    text = list()
    for i in range(num):
        most_common = cfdist[word].most_common(len(cfdist))
        total = sum(item[1] for item in most_common)
        dist = {word: freq / total for (word, freq) in most_common}
        n = random.random()
        sum_ = 0
        for word, frequency in dist.items():
            sum_ += frequency
            if n <= sum_:
                text.append(' '.join(word))
                break
    print('\n'.join(text))


def generate_sentence(cfdist, word, num=15):
    sentence = list()
    for i in range(num):
        most_common = cfdist[word].most_common(len(cfdist))
        total = sum(item[1] for item in most_common)
        dist = {word: freq / total for (word, freq) in most_common}
        n = random.random()
        sum_ = 0
        for word, frequency in dist.items():
            sum_ += frequency
            if n <= sum_:
                sentence.append(word)
                break
    print(' '.join(sentence))


text = gutenberg.words('austen-emma.txt')
text = [item for item in text if not item in punctuation]
bigrams = bigrams(text)
cfd = ConditionalFreqDist(bigrams)
start = random.choice(text)
generate_sentence(cfd, start)
