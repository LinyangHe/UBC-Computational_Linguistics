import random

grammar = {'S': ['A', 'B'],
           'A': ['C', 'a'],
           'B': ['A', 'b'],
           'C': ['A*', 'c']}


def generate(symbol, output):
    if '*' in symbol:
        n = random.random()
        if n > 0.5:
            symbol = symbol[0]
        else:
            symbol = ''  # nothing

    if symbol.isupper():
        for s in grammar[symbol]:
            generate(s, output)
    else:
        if symbol:
            output.append(symbol)
    return output  # what should return is a tree! not a leter


output = []
for symbol in grammar['S']:
    generate(symbol, output)
print(output)
