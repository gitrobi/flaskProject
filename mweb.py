from flask import Flask, render_template, request
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


@app.route("/play/")
def play():
    url = request.args.get("url")
    return render_template("play.html", url=url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9899, debug=True)
