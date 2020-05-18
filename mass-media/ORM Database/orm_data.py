import json
import json_handler as j
import peewee as p
import sqlite3 as s
import os


db = p.SqliteDatabase('news.db')


class News(p.Model):
    id = p.AutoField()
    time_as_number = p.IntegerField()
    time = p.TextField()
    source = p.TextField()
    title = p.TextField(unique=True)
    url = p.TextField()
    content = p.TextField()

    class Meta:
        database = db


def database_fill(filename):
    str_data = open(filename).read()
    json_data = json.loads(str_data)
    if j.check_response(json_data):
        for entry in json_data['articles']:
            number_date, time, source, title, url, content = j.article_categorizer(entry)
            article = News(time=time, time_as_number=number_date,  source=source, title=title, url=url, content=content)
            try:
                article.save()
            except:
                continue


if __name__ == '__main__':
    db.connect()
    db.create_tables([News])
    directory = 'Responses_sorted_by_countries'
    for filename in os.listdir(directory):
        file_to_open = os.path.join('Responses_sorted_by_countries', filename)
        database_fill(file_to_open)

