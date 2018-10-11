from flask import Flask,render_template,redirect,session,request,url_for,jsonify
from serv import add
app = Flask(__name__)
app.secret_key = "asdasfsa3"
app.config["DEBUG"] = True
STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}
app.register_blueprint(add.addstu)
def wrapper(f):
    def inner(*args, **kwargs):
        if not session.get("user"):
            return redirect("/login")
        else:
            ret = f(*args, **kwargs)
            return ret
    return inner


@app.route("/index", endpoint="index")
@wrapper
def index():
    print(url_for("index"))
    return render_template("index.html", stu=STUDENT_DICT)


@app.route("/detail", endpoint="detail")
@wrapper
def detail():
    return render_template("detail.html", stu=STUDENT_DICT)



@app.route("/login", methods=("GET", "POST"))
def login():
    met = request.method
    if met == "GET":
        return render_template("login.html")
    else:
        name = request.form.get("name")
        pwd = request.form.get("pwd")

        if name == "alex" and pwd == "1234":
            session["user"] = name
            return redirect("/index")
        return render_template("login.html", msg="你丫写错了")


@app.route("/do/<int:age>", defaults={"age":999}, strict_slashes=True )
def do(age):
    ret = {"age": age}
    return jsonify(ret)


app.run()