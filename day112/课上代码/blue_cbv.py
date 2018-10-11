from flask import Blueprint, views

bp = Blueprint("bluename", __name__)


class bpclass(views.MethodView):

    def get(self):
        return "blue_get"


bp.add_url_rule("/blue",endpoint="blue",view_func=bpclass.as_view(name="bpclass"))
