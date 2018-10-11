from flask import Flask,render_template,redirect,session,request

app = Flask(__name__)
app.secret_key = "asdasfsa3"
STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}
def wrapper(f):
    def inner(*args, **kwargs):
        if not session.get("user"):
            return redirect("/login")
        else:
            ret = f(*args, **kwargs)
            return ret
    return inner



@app.route("/index")
@wrapper
def index():
    # if not session.get("user"):
    #     return redirect("/login")
    return render_template("index.html", stu=STUDENT_DICT)


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
app.run()