from flask import Blueprint,render_template,session,views
import pymysql

list = Blueprint("list", __name__)
conn = pymysql.connect(host="localhost")

class List(views.MethodView):

    def get(self):

