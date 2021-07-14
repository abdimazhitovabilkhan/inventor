from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    f = open("goods.xlsx", "a", encoding="utf-8")
    xlsx = f.readlines()
    return render_template("index.html", goods=xlsx)