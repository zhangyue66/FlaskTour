from flask import Flask
app = Flask(__name__)
#print(app.config)
@app.route("/")
def yuezhang():
    return "this is yue zhang first flask!"

@app.route("/yz")
def yz():
    return "this is 2nd website"

dict = {"a":"beijing","b":"shanghai","c":"shenzhen"}
@app.route("/get_city/<key>")
def get_city(key):
    return dict[key]

@app.route("/add/<int:num>")
def add(num):
    return str(99+num)

@app.route("/add1/<float:money>")
def add1(money):
    return str(10+money)


@app.route("/index/<path:p>")
def get_path(p):
    print("path is %s" %(type(p)))
    return p

@app.route("/test/<uuid:id>")
def get_uuid(id):
    return str(id)

app.run(host=None,port=8080)

