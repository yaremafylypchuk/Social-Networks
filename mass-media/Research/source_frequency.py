import sqlite3 as s
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

conn = s.connect('news.db')
cur = conn.cursor()
rows = cur.execute("SELECT * FROM news")


def create_source_frequency_dict():
    sources_dict = dict()
    for row in rows:
        source = row[3]
        if source in sources_dict:
            sources_dict[source] += 1
        else:
            sources_dict[source] = 1

    sorted_dict = {s: q for s, q in sorted(sources_dict.items(), key=lambda item: item[1])}
    return sorted_dict

def visualise_sources():
    sorted_dict = create_source_frequency_dict()
    sources = sorted_dict.keys()
    y_pos = np.arange(len(sources))
    frequency = sorted_dict.values()

    plt.barh(y_pos, frequency, align='center', alpha=0.7)
    plt.yticks(y_pos, sources, fontsize=5, fontname='monospace')
    plt.xlabel('Frequency')
    plt.title('Frequency per source')
    plt.savefig("frequency.png")


if __name__ == "__main__":
    visualise_sources()
