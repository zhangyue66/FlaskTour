host默认为localssh，如果修改host参数可以外网访问

app.run(host="0.0.0.0",port=8080,debug=True)
开始debug模式 如果代码改变 服务器会reloading然后显示新的内容
debug=False是默认 代码改变也不会显示
production vs development


设置配置文件
print(app.config)
<Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(seconds=43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
因为是字典 可以通过字典改变 比如下面：
app.config["ENV"] = "development"
app.config["DEBUG"] = True

解耦配置文件 settings.py
app.config.from_pyfile("settings.py")

import settings
app.config.from_objects(settings)

#flask 配置文件
ENV = "development"
DEBUG = True

路由的请求与相应：

http://127.0.0.1/test

http request:
GET POST PUT
request URL
request header
request body


http response:
response status : status code 200 404 403 500...
response header:
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 42
Server: Werkzeug/1.0.1 Python/3.8.1
Date: Mon, 12 Apr 2021 08:40:37 GMT
response body


=========================================

Day2

1.路由

192.168.1.10:8080
@app.ruote("/")
def index():
    return "index!"

怎么实现的？
def route(self,rule,**options):
    def decorator(f):
        self.add_url_rule(rule,endpoint,f,**options)
        return f
    return decorator

利用add_url_rule函数 将字符串和视图函数绑定一起

变量规则 variable rules -》https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
string

(default) accepts any text without a slash

int

accepts positive integers

float

accepts positive floating point values

path

like string but also accepts slashes

uuid

accepts UUID strings