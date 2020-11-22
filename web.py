from flask import Flask, render_template

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return ''


@app.route("/")
def index():
    return render_template("html5.html")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
