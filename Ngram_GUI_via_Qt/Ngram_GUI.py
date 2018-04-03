import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QDialog, QApplication,
                             QComboBox, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTextEdit, QLabel, QLineEdit,
                             QMessageBox)
from nltk.corpus import gutenberg
from nltk import bigrams as nltkBigrams
from nltk import trigrams as nltkTrigrams


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ngram Visualizer')
        self.corpustList = QComboBox()

        for filename in gutenberg.fileids():
            self.corpustList.addItem(filename)

        selectCorpusButton = QPushButton()
        selectCorpusButton.setText('Select')
        selectCorpusButton.clicked.connect(self.showCorpus)

        self.gramsOptions = QComboBox()
        self.gramsOptions.addItem('Find bigrams for...')
        self.gramsOptions.addItem('Find trigrams for...')

        bigramLabel = QLabel()
        bigramLabel.setText('Find bigrams for...')

        self.textEntry = QLineEdit()

        bigramButton = QPushButton()
        bigramButton.setText('Search')
        bigramButton.clicked.connect(self.showBigram)

        self.fullText = QTextEdit()
        self.fullText.setReadOnly(True)

        self.bigramResult = QTextEdit()
        self.bigramResult.setReadOnly(True)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.corpustList)
        topLayout.addWidget(selectCorpusButton)
        topLayout.addWidget(bigramLabel)
        topLayout.addWidget(self.textEntry)
        topLayout.addWidget(bigramButton)

        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.fullText)
        bottomLayout.addWidget(self.bigramResult)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)

    def showCorpus(self):
        fileName = self.corpustList.currentText()
        text = gutenberg.raw(fileName)
        self.fullText.setText(text)

    def showBigram(self):
        chosenGrams = self.gramsOptions.currentText()
        if 'bigrams' in chosenGrams:
            gramsFunction = nltkBigrams
        else:
            gramsFunction = nltkTrigrams

        text = gutenberg.words(self.corpustList.currentText())
        searchItem = self.textEntry.text()
        show_text = [bigram for bigram in gramsFunction(text) if searchItem == bigram[0]]
        show_text = [' '.join(line) for line in show_text]

        if not show_text:
            alert = QMessageBox()
            alert.setWindowTitle('No results')
            warning = 'Sorry no results for {} in {} corpus!'.format(searchItem, self.corpustList.currentText())
            alert.setText(warning)
            alert.exec_()
        else:
            self.bigramResult.setText('\n'.join(show_text))

        # find the currently selected corpus
        # find the text that the user entered
        # find the bigrams
        # put them inro self.bigramResults


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
