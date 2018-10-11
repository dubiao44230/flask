from flask import Blueprint

delstu = Blueprint("delstu", __name__)


@delstu.route("/del_stu")
def deletestu():
    return "del_stu_blueprint"
