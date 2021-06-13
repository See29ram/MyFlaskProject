from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>")
def info(name):
    return render_template("faq.html", content=name, location="chennai")


@app.route("/values")
def value():
    name = ['Java', 'Python', 'Golang']
    return render_template("values.html", content=name)


if __name__ == "__main__":
    app.run()
