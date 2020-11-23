from flask import Flask, render_template
from movie import iqiyi

app = Flask(__name__)


def get_movie_list():
    return iqiyi.get_latest_list()


@app.route('/favicon.ico')
def favicon():
    return ''


@app.route("/")
def index():
    return render_template("html5.html")


@app.route("/movie")
def movie():
    return render_template("movie.html", result=get_movie_list())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9899, debug=True)
