import random

grammar = {'B': ['S', 'V', 'O'],
           'S': ['gerbils', 'wolves', 'rabbits', 'cats'],
           'V': ['chase', 'eat', 'like'],
           'O': ['cheese', 'apples', 'homework']}

sentence = []
for symbol in grammar['B']:
    word = random.choice(grammar[symbol])
    sentence.append(word)

sentence = ' '.join(sentence)
print(sentence)
