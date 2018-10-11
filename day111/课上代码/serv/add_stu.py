from flask import Blueprint,render_template

addstu = Blueprint("addstu", __name__,
                   template_folder="blueprint_temp",
                   static_folder="blueprint_static",
                   static_url_path="/static2")


@addstu.route("/add_stu")
def add():
    return render_template("add_stu.html")
