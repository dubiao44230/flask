from flask import Flask,views,session,render_template,request
from flask_session import Session
from redis import Redis
import blueprint_cbv


app = Flask(__name__)
app.register_blueprint(blueprint_cbv.cbv)
app.config["DEBUG"] = True
app.config['SESSION_TYPE'] = "redis"
app.config["SESSION_REDIS"] = Redis(host="localhost", port=6379, db=5)
Session(app)

def wrapper():
    pass


from wtforms.fields import simple,core
from wtforms import Form
from wtforms import validators

class LoginForm(Form):

    username = simple.StringField(
        label="用户名",
        validators = [
           validators.DataRequired(message="数据不能为空") ,
            validators.Length(min=5, max=16, message="大于5小于16")
        ],
        render_kw={"class":"dddd"}  # 自定义标签属性
    )
    password = simple.PasswordField(
        label="密码",
        validators = [
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=5, max=16, message="大于5小于16"),
            validators.Regexp(regex="\d+", message="密码必须为数字")
        ],
    )


class login(views.MethodView):
    methods = ["POST", "GET"]
    # decorators = [wrapper]

    def get(self):
        loginfm = LoginForm()
        return render_template("login.html", fm=loginfm)

    def post(self):
        loginfm = LoginForm(request.form)
        if not loginfm.validate():
            return render_template("login.html", fm=loginfm)
        session["user"] = "I am"
        return "i am post"

app.add_url_rule("/login", endpoint=None, view_func=login.as_view(name="login"))


class RegForm(Form):


    # def __init__(self, hobby_list):
    #     self.hobby_list = hobby_list
    #     self.init_hobby()
    #     super(RegForm, self).__init__()
    #
    # def init_hobby(self):
    #     for index, item in enumerate(self.hobby_list):
    #         self.hobby_init.append([index, item])

    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=5, max=16, message="大于5小于16")
        ],
        render_kw={"class": "jinyinwangba"}
    )

    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.Length(min=5, max=16, message="大于5小于16"),
            validators.Regexp(regex="\d+", message="密码必须为数字")
        ],
    )

    repassword = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="数据不能为空"),
            validators.EqualTo("password", message="两次密码不一致")
        ],
    )

    gender = core.RadioField(
        label="性别",
        choices=(
            (1, "女"),
            (2, "男"),
            (3, "wangba")
        ),
        coerce=int,
        default=3
    )

    hobby = core.SelectMultipleField(
        label="嗜好",
        choices=[[1,"cy"]],
        coerce=int,
        default=1
    )


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        # hobby_list = ["cy","hj","bd","ysd","啤酒泡枸杞","熬夜敷面膜"]
        regfm = RegForm()
        return render_template("reg.html", fm=regfm)
    else:
        regfm = RegForm(request.form)
        if not regfm.validate():
            return render_template("reg.html", fm=regfm)

        print(regfm.data.get("hobby"),regfm.data.get("gender"))

        return "注册成功"



if __name__ == '__main__':
    app.run()