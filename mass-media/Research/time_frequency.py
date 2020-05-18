import sqlite3 as s
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

conn = s.connect('news.db')
cur = conn.cursor()
rows = cur.execute("SELECT * FROM news")


def create_time_frequency_dict():
    date_dict = dict()
    for row in rows:
        date = row[2]
        if date in date_dict:
            date_dict[date] += 1
        else:
            date_dict[date] = 1

    sorted_dict = {s: q for s, q in sorted(date_dict.items(), key=lambda item: item[0])}
    return sorted_dict


def visualise_time():
    sorted_dict = create_time_frequency_dict()
    time = sorted_dict.keys()
    y_pos = np.arange(len(time))
    frequency_per_date = sorted_dict.values()

    plt.barh(y_pos, frequency_per_date, align='center', alpha=0.7)
    plt.yticks(y_pos, time, fontsize=8, fontname='monospace')
    plt.xlabel('Frequency')
    plt.title('Frequency per date')
    plt.savefig("date.png")


if __name__ == "__main__":
    visualise_time()