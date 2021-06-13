from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("parent.html")


@app.route("/child", methods= ["POST", "GET"])
def child_page():

    if request.method == "POST":
        user = request.form["nm"]
        #return render_template('child.html',name =user)
        return redirect(url_for('/child', name= user))
    return render_template('child.html')


if __name__ == "__main__":
    app.run(debug=True)