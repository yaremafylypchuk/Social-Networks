import sqlite3 as s
from nltk.corpus import stopwords
import matplotlib.pyplot as plt;plt.rcdefaults()
import numpy as np

conn = s.connect('news.db')
cur = conn.cursor()
rows = cur.execute("SELECT * FROM news")

all_stopwords = stopwords.words('english')
all_stopwords.extend(['says', 'the', 'near', 'new', 'amid', '|', '.'])


def create_word_frequency_lst():
    words_dict = dict()
    for row in rows:
        title = row[4]
        words = title.split()
        for word in words:
            if word not in all_stopwords:
                word = word.lower()
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1

    sorted_dict = {w: f for w, f in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)}
    sorted_dict['coronavirus'] += sorted_dict['coronavirus:']
    del sorted_dict['coronavirus:']
    del sorted_dict['the']
    return sorted_dict


def visualise_top_used_words():
    sorted_dict = create_word_frequency_lst()
    words_dict = dict()
    for key in sorted_dict:
        if len(words_dict) != 15:
            words_dict[key] = sorted_dict[key]

    sources = words_dict.keys()
    y_pos = np.arange(len(sources))
    frequency = words_dict.values()

    plt.barh(y_pos, frequency, align='center', alpha=0.7)
    plt.yticks(y_pos, sources, fontsize=5, fontname='monospace')
    plt.xlabel('Word Frequency')
    plt.title('Frequency per word')
    plt.savefig("words.png")


if __name__ == '__main__':
    visualise_top_used_words()