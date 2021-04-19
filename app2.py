from flask import Flask
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route('/projects/')
def projects():
    return 'The project page'
# http://127.0.0.1:5000/projects/ 和 http://127.0.0.1:5000/projects都不会报错
@app.route('/about')
def about():
    return 'The about page'
#http://127.0.0.1:5000/about/ 会报错
app.run()