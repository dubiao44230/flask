from flask import Flask,session,render_template,request,flash,get_flashed_messages
from serv import add_stu
from serv import del_stu
import flask_config


app = Flask(__name__,template_folder="template",static_folder="static123123",static_url_path="/static") #self.static_url_path

app.config.from_object(flask_config.Config)

app.register_blueprint(add_stu.addstu)
app.register_blueprint(del_stu.delstu)


@app.route("/index")
def index():
    res = get_flashed_messages()
    if not res:
        res = [""]
    flash("你刚才访问了index")
    return render_template("index.html",msg=res[0])

@app.route("/home")
def index1():
    res = get_flashed_messages()
    if not res:
        res = [""]
    flash("你刚才访问了home")
    return render_template("index.html",msg=res[0])

if __name__ == '__main__':
    app.run()
