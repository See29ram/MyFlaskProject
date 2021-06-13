from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI  # import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app,start_server="flask")  # add app and parameters


@app.route("/")
def hello():
    return "Hey Hello"


if __name__ == "__main__":
    ui.run()


