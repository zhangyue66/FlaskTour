# app.py 与模板 templates的结合使用

from flask import Flask, request, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/register1")
def register1():
    return "abc"

@app.route("/register")
def register():
    r = render_template("register.html")
    return r


if __name__ == "__main__":
    app.run()