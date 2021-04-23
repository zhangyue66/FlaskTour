from flask import Flask, make_response, request
import settings

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/index")
def hello_word():
    #make_response()
    print(request.headers) #对象 实例 可以访问属性 方法
    print(request.path)
    print(request.base_url)
    print(request.url)
    """
    Host: 127.0.0.1:5000
    Connection: keep-alive
    Cache-Control: max-age=0
    Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
    Sec-Ch-Ua-Mobile: ?0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run()