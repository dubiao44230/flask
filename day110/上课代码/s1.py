from flask import Flask, render_template, redirect, request,Markup,session

app = Flask(__name__)
app.secret_key = "you_happy_is_good_Markup_session_redirect"

STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'}

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '女'}
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}


@app.route("/")  # ret_inner = route(index)
def index():
    return "Hello World!"

@app.template_global()
def add_sum(*args):
    return sum(args)

@app.template_filter()
def oushu(sum):
    if not sum % 2:
        return "偶数"
    else:
        return "奇数"

@app.route("/login", methods=("POST", "GET", "PUT"))  # ret_inner = route(index)
def login():
    met = request.method
    if met == "GET":
        text_tag = "<p>你大爷看见了吗xiaowangba:<input type='text' name='xiaowangba'></p>"
        text_tag = Markup(text_tag)
        return render_template("login.html",msg=text_tag)

    if met == "POST":
        print(request.form.to_dict())
        print(request.values.to_dict())
        print(request.form.to_dict())
        # request.json
        # request.data
        # print(request.json)  # application/json
        # print(request.data)  # jinwangbayinwangba
        username = request.form.get("username")
        pwd = request.form.get("password")
        if username == "alex" and pwd == "jinwangba":
            session["user"] = username + "you_happy_is_good_Markup_session_redirect"
            return redirect("/detail_dict")

        return render_template("login.html", msg="你丫写错了")


@app.route("/detail")
def detail():
    return render_template("detail.html", **STUDENT)


@app.route("/detail_list")
def detail_list():
    return render_template("detail_list.html", stu_list=STUDENT_LIST)


@app.route("/detail_dict")
def detail_dict():
    if not session.get("user"):
        return redirect("/login")
    return render_template("detail_dict.html", stu_dict=STUDENT_DICT)

@app.route("/bo")
def bo():
    return render_template("bo.html")


app.run(host="0.0.0.0", port=9527, debug=True)

# wsgi 应用程序网关接口 把你请求处理后发送给对应的app中
# werkzeug Flask使用的
