from flask import Flask
import settings

app=Flask(__name__)
app.config.from_object(settings)

@app.route("/")
def show():
    return "<font color='red'> Hellow Yuezhang </font>"

if __name__ == "__main__":
    app.run(port=8080)

