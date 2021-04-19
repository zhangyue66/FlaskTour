from flask import Flask
app = Flask(__name__)
print(app.config)
@app.route("/")
def yuezhang():
    return "this is yue zhang first flask!"

@app.route("/yz")
def yz():
    return "this is 2nd website"

app.run(host=None,port=8080)

