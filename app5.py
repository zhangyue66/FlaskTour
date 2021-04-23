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

@app.route("/register2",methods=["post","get"])
def register2():#获取页面获取的值
    print(request.args)#只能拿到get方法的值
    print(request.args.get("username"))
    print(request.args.get("address"))#只能拿到get方法的值
    print(request.form)#只能拿到post方法的值
    print(request.form.get("username"))
    return "submit is done"

if __name__ == "__main__":
    print(app.url_map) #URL路由表
    """
    Map([<Rule '/register1' (GET, HEAD, OPTIONS) -> register1>,
    <Rule '/register' (GET, HEAD, OPTIONS) -> register>,
    <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>])
    """
    app.run()