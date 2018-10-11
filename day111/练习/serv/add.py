from flask import Blueprint, render_template

addstu = Blueprint("add", __name__,
                   template_folder="blueprint_temp",
                   static_folder="blueprint_static",
                   static_url_path=None
                   )

@addstu.route("/add_stu")
def add():
    return render_template("add_stu.html")