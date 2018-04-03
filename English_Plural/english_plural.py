from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt

embedding_vowel = {'ʌ': 2.0, 'ɔ': 2.1, 'ɑ': 2.2, 'ɒ': 2.3,
                   'ɝ': 2.4, 'ɪ': 2.6, 'o': 2.7, 'ʊ': 2.8,
                   'u': 2.9, 'ə': 3.0, 'i': 3.1, 'e': 3.2,
                   'ɛ': 3.3, 'æ': 3.4, 'a': 3.5}

embedding_consonant = {'b': 0.1, 'n': 0.2, 'm': 0.3,
                       'l': 0.4, 's': 0.5, 'z': 0.6,
                       't': 0.7, 'd': 0.8, 'g': 0.9,
                       'k': 1.0, 'ʃ': 1.1, 'ʒ': 1.2,
                       'p': 1.3, 'v': 1.4}


def load_data(path, separator):
    file = open(path, encoding='utf-8')
    file.readline()
    lines = [line.strip() for line in file]
    file.close()
    words_singular = list()
    words_plural = list()
    ipa_singular = list()
    ipa_plural = list()
    for line in lines:
        if not line:
            continue
        line = line.split(separator)
        words_singular.append(line[0])
        ipa_singular.append(embedding_data(line[1]))
        words_plural.append(line[2])
        ipa_plural.append(embedding_data(line[3]))

    return words_singular, ipa_singular, words_plural, ipa_plural


def embedding_data(ipa_word):
    ipa_data = list()
    for letter in ipa_word:
        if letter in embedding_vowel:
            ipa_data.append(embedding_vowel[letter])
        elif letter in embedding_consonant:
            ipa_data.append(embedding_consonant[letter])
    return ipa_data


training_path = 'training_data.txt'

words_singular_tr, ipa_singular_tr, words_plural_tr, ipa_plural_tr = \
    load_data(training_path, '\t')
