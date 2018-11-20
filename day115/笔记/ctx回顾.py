from flask import Flask,request,session

app = Flask(__name__)  # type:Flask

@app.route("/")
def index():
    # request.method
    # session["user"]
    return "123"

if __name__ == '__main__':
    app.run()
    app.__call__
    app.wsgi_app

