from flask import Flask, request, render_template, redirect, session

# request : LocalProxy()

from flask_session import Session
import flask_settings
from lantu import blue

app = Flask(__name__)
app.config.from_object(flask_settings.FlaskSet)

Session(app)
app.register_blueprint(blue.bp)

@app.route('/index', methods=["GET", "POST"], endpoint="helloWorld", strict_slashes=True)
def index():
    return redirect("/login")


@app.route('/login', methods=["GET", "POST"])
def login():
    session["user"] = 123123
    return render_template("index.html")



if __name__ == '__main__':
    app.__call__
    app.wsgi_app
    app.run()

