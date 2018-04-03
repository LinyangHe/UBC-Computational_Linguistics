from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt

voiceless_con = ['p', 't', 's', 'k']
voiced_con = ['b', 'd', 'z', 'g']


def load_data(path, separator):
    file = open(path, encoding='utf-8')
    file.readline()  # strip header
    lines = [line.strip() for line in file]
    file.close()
    japanese_wordlist = list()
    inputs = list()
    outputs = list()
    for line in lines:
        if not line:
            continue
        line = line.split(separator)
        japanese_wordlist.append(line[0])
        inputs.append(input_embedding(line[0]))
        outputs.append([float(n) for n in line[1:]])

    return japanese_wordlist, inputs, outputs


def load_test(path, separator):
    file = open(path, encoding='utf-8')
    lines = [line.strip() for line in file]
    file.close()
    japanese_wordlist = list()
    english_wordlist = list()
    test_input = list()
    for line in lines:
        if not line:
            continue
        line = line.split(separator)
        japanese_wordlist.append(line[0])
        test_input.append(input_embedding(line[0]))
        english_wordlist.append(line[1])
    return japanese_wordlist, test_input, english_wordlist


def input_embedding(word):
    embedding_data = [0.0, 0.0, 0.0, 0.0, 0.0]
    if 'ch' in word:
        embedding_data[0] = 1.0
    if 'i' in word:
        embedding_data[1] = 1.0
    if 'o' in word:
        embedding_data[2] = 1.0
    for letter in word:
        if letter in voiceless_con:
            embedding_data[3] = 1.0
        if letter in voiced_con:
            embedding_data[4] = 1.0
    return embedding_data


train_path = 'training.txt'
train_wordlist, inputs, outputs = load_data(train_path, '\t')
# print(inputs)
# print(outputs)


dataset = SupervisedDataSet(5, 6)
for index in range(len(inputs)):
    dataset.addSample(tuple(inputs[index]), tuple(outputs[index]))

network = buildNetwork(5, 6, 6)
trainer = BackpropTrainer(network, dataset)

#
# for j in range(200):
#     trainer.train()

err_train, err_valid = trainer.trainUntilConvergence(maxEpochs=500)
plt.plot(err_train, 'b', err_valid, 'r')
plt.show()
# close the plot to continue the program.

test_path = 'test.txt'
test_wordlist, test_input, english_wordlist = load_test(test_path, '\t')

print('word\tsmallness\tquickness\tshallowness\trarity\tlightness\thigh-pitched')

for index, input_ in enumerate(test_input):
    results = network.activate(input_)
    print(test_wordlist[index], results, english_wordlist[index])
