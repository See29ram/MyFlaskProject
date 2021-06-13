from flask import Flask, redirect , url_for

app = Flask(__name__)
print(dir(app))


@app.route("/")
def index():
    return "Hello Home Page"


@app.route("/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()



