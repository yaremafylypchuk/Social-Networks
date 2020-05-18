import json
import os
import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt


#Exapmle of using json.

def return_value(item):
    if type(item) == dict:
        value = '<dict>'
    elif type(item) == list:
        value = '<list>'
    else:
        value = item
    return value


def recursive_manager(node):
    message = ''
    while True:
        print('\n' * 100)
        if type(node) == dict:
            for index, key in enumerate(node):
                value = return_value(node[key])
                print(f'{index + 1}. {key}: {value}')
        elif type(node) == list:
            for index, item in enumerate(node):
                value = return_value(item)
                print(f'{index + 1}. {value}')
        print('0. return')
        if message:
            print(message)
            message = ''
        command = input('Enter command: ')

        if command.isdigit():
            command = int(command)
            if command <= len(node) or command == 0:
                if command == 0:
                    return
                elif type(node) == dict:
                    key = list(node.keys())[command - 1]
                    if type(node[key]) == dict or type(node[key]) == list:
                        recursive_manager(node[key])
                    else:
                        message = 'You can not enter this, as it is not a node'
                elif type(node) == list:
                    if type(node[command - 1]) == dict or type(node[command - 1]) == list:
                        recursive_manager(node[command - 1])
                    else:
                        message = 'You can not enter this, as it is not a node'

            else:
                message = 'A command with such an index does not exit'

        else:
            message = 'This is a invalid command, please enter a valid command (number)'


with open('response.json', encoding='utf-8') as f:
    data = json.load(f)

# recursive_manager(data)


#Exapmle of using nltk.

#nltk.download()

my_text = "Hello Andriy, how are you? I hope everything is going well. Today is a good day, I hope quarantine will end soon."
my_text2 = "Hallo! Ich heiße Yarema und bin 17 Jahre alt. Ich finde programmierung sehr cool und interessant."
# print(sent_tokenize(my_text))
# print(word_tokenize(my_text))
# print(sent_tokenize(my_text2, 'german'))

word = wordnet.synsets("example")
# print(word[0].definition())
# print(word[0].examples())

synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
# print(synonyms)

stemmer = PorterStemmer()
# print(stemmer.stem('increases'))

lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('increases'))


#Exapmle of using matplotlib.

labels = ['1990', '1995', '2000', '2005', '2010', '2015']
men_means = [33.7, 34.5, 35.7, 36.8, 37.4, 37.9]
women_means = [39.0, 39.6, 40.7, 41.8, 42.6, 43.1]
width = 0.35

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, label='Men')
ax.bar(labels, women_means, width, bottom=men_means,label='Women')

ax.set_ylabel('Age')
ax.set_title('Average age of ukrainians by gender')
ax.legend()

# plt.show()

data = {'1990': 33.7, '1995': 34.5, '2000': 35.7, '2005': 36.8, '2010': 37.4, '2015': 37.9}
years = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()
ax.plot(years, values)

ax.set_ylabel('Age')
ax.set_title('Average age of men in Ukraine')

# plt.show()
