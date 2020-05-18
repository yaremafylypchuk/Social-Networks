import csv
from flask import Flask, render_template, request, redirect
from response_handler import check_values
import sqlite3 as s

# Configure the app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('New_style.html')


@app.route('/explore_more')
def explore_more():
    return render_template('Explore_more.html')


@app.route('/news', methods=["POST", "GET"])
def news():
    return render_template('Find_the_news.html')


@app.route('/register', methods=["POST"])
def register():
    start_date = request.form.get('start')
    end_date = request.form.get('end')
    source = request.form.get('source')
    with open("search.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow((start_date, end_date, source))
    conn = s.connect('news.db')
    cur = conn.cursor()
    start, stop, source_news = check_values()
    if source_news == 'all':
        rows = cur.execute("SELECT * FROM news WHERE time_as_number >= ? AND time_as_number <= ? "
                           "ORDER BY time_as_number DESC LIMIT 20", (start, stop))
    else:
        rows = cur.execute("SELECT * FROM news WHERE time_as_number >= ? AND time_as_number <= ? "
                           "AND source = ? ORDER BY time_as_number DESC LIMIT 20", (start, stop, source_news))
    return render_template("success.html", rows=rows)


@app.route('/results')
def research_results():
    return render_template('research_results.html')


if __name__ == '__main__':
    app.run(debug=True)
