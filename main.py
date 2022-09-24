from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/shows/most-rated')
def most_rated():
    shows = queries.get_most_rated_shows()
    return render_template('most-rated.html', shows=shows)

@app.route('/tv-show/<int:show_id>', methods=["GET", "POST"])
def show(show_id):
    shows = queries.showTitles(show_id)
    videoTag =((shows[0]['trailer'].split('=')[1]))
    return render_template("show.html", shows=shows, show_id=show_id, videoTag=videoTag)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
