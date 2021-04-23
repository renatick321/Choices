from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def label():
    return "<strong>Миссия Колонизация планет</strong>"

@app.route("/choice/<planet_name>")
def promotion_image(planet_name):
    return render_template("index.html", name=planet_name.upper())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')