grammar = {'S': ['A', 'B'],
           'A': ['C', 'a'],
           'B': ['A', 'b'],
           'C': ['c']}


def generate(symbol, output):
    if symbol.isupper():
        for s in grammar[symbol]:
            generate(s, output)
    else:
        output.append(symbol)
    return output  # what should return is a tree! not a leter


output = []
for symbol in grammar['S']:
    generate(symbol, output)
print(output)
