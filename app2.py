from flask import Flask
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route('/projects/')
def projects():
    return 'The project page'
# http://127.0.0.1:5000/projects/ 和 http://127.0.0.1:5000/projects都不会报错

# 127.0.0.1 - - [19/Apr/2021 00:02:41] "GET /projects HTTP/1.1" 308 -


@app.route('/about')
def about():
    return 'The about page'
#http://127.0.0.1:5000/about/ 会报错
# 127.0.0.1 - - [19/Apr/2021 00:02:57] "GET /about/ HTTP/1.1" 404 - Not Found
app.run()