from flask import Blueprint,render_template
bp = Blueprint("bluename",__name__,template_folder="temp",static_folder="../static",static_url_path="/static")

@bp.route("/blue")
def blue():
    return render_template("blue.html")