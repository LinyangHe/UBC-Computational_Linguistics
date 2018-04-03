import os
import random


def load_grammar():
    grammar = {}
    with open(os.path.join(os.getcwd(), 'grammar.txt')) as f:
        for line in f:
            line = line.strip().split('->')
            grammar[line[0]] = line[1].split(' ')
    return grammar


def generate(symbol, output):
    if symbol:
        for s in grammar[symbol]:
            if '(' in s:
                n = random.random()
                if n > 0.9:
                    s = s[1:-1]
                else:
                    s = ''

            if s.isupper():
                print(s)
                generate(s, output)
            else:
                if symbol:
                    #print(symbol)
                    output.append(random.choice(grammar[symbol]))
                    return output


grammar = load_grammar()
for i in range(10):
    sentence = []
    for symbol in grammar['S']:
        generate(symbol, sentence)
    print(' '.join(sentence) + '\n')
