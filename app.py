from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"

def index():
    return "This is index!"
app.add_url_rule("/index",view_func=index)

if __name__ == "__main__":
    app.run()