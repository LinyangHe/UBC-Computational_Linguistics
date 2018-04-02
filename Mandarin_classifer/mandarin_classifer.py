from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt

classifers = ['zuo', 'zhang', 'tiao', 'qun', 'ke']
features = ['foundation', 'tall', 'float', 'long', 'narrow', 'living', 'groups', 'plant']


def load_data(path, separator):
    file = open(path, encoding='utf-8')
    file.readline()  # strip header
    lines = [line.strip() for line in file]
    file.close()
    words = list()
    inputs = list()
    outputs = list()
    for line in lines:
        if not line:
            continue
        line = line.split(separator)
        words.append(line[0])
        # print(line)
        inputs.append([float(n) for n in line[1:9]])
        outputs.append([float(n) for n in line[9:]])
    return words, inputs, outputs


training_path = 'train.txt'
words, inputs, outputs = load_data(training_path, '\t')

# Create a dataset from pybrain
dataset = SupervisedDataSet(8, 5)
for index in range(len(inputs)):
    dataset.addSample(tuple(inputs[index]), tuple(outputs[index]))

# Build a network that uses backpropogration
network = buildNetwork(8, 7, 5)
trainer = BackpropTrainer(network, dataset)

# Train the network with 20 examples of each training item
err_train, err_valid = trainer.trainUntilConvergence(maxEpochs=500)
plt.plot(err_train, 'b', err_valid, 'r')
plt.show()
# close the plot to continue the program

# Test the network

test_path = 'test.csv'
test_words, test_inputs, test_outpust = load_data(test_path, ',')

for index, input_ in enumerate(test_inputs):
    results = network.activate(input_)
    highest = max(results)
    if highest == results[0]:
        category = classifers[0]
    elif highest == results[1]:
        category = classifers[1]
    elif highest == results[2]:
        category = classifers[2]
    elif highest == results[3]:
        category = classifers[3]
    else:
        category = classifers[4]

    print(test_words[index], category)
