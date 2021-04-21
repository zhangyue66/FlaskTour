from flask import Flask, Response, make_response
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route("/")
def show():
    return "<font color='red'> Hellow Yuezhang </font>"
#返回的字符串其实也是封装了一个Response的class
@app.route("/index3")
def return_Response():

    return Response("<h1>大家想吃什么？</h1>")

@app.route("/yz")
def return_res():
    response = Response("hello")
    print(response.headers)
    print(response.status_code)
    print(response.content_type)
    return response


@app.route("/index4")
def index4():
    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MainPage</title>
</head>
<body>
<h1>welcome to Yue Zhang Website</h1>
</body>
</html>
    """
    response = make_response(content)
    response.headers['YueZhangTest'] = "123abc"
    #不能带空格
    response.headers["test"] = "abc123"
    return response

if __name__ == "__main__":
    app.run(port=8080)

