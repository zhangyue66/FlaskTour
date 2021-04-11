from flask import Flask
app = Flask(__name__)

@app.route("/")
def yuezhang():
    return "this is yue zhang first flask!"

app.run()