from flask import Flask,Response
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route("/")
def show():
    return "<font color='red'> Hellow Yuezhang </font>"
#返回的字符串其实也是封装了一个Response的class
@app.route("/index4")
def return_Response():
    return Response("<h1>大家想吃什么？</h1>")

if __name__ == "__main__":
    app.run(port=8080)

