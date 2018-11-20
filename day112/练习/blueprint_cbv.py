from flask import Blueprint, views

cbv = Blueprint("CBV", __name__)

class index(views.MethodView):

    def get(self):

        return "blue"

cbv.add_url_rule("/index",view_func=index.as_view(name="index"))