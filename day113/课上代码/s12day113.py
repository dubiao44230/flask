2018年10月12日：
上节回顾：
	1.Flask-Session
		from flask import session
		from flask_session import Session
		
		app.config["SESSTION_TPYE"] = "redis"
		app.config["SESSTION_REDIS"] = Redis("ip",port,db=1)
		# select 1  ----- [1]
		
		Session(app)
		
		session["key"] = "value"
		session["key"]
		
	2.Flask CBV
		class Index(views.MethodView):
			methods = ["GET"]
			decorators = [a,b,c]
			def get():
				return "file"
				
		
		app.add_url_rule("/",endpoint="index",view_func=Index.as_view(name="index"))
		
		if 1 : endpoint = None = name = "index"
		elif 2: endpoint="index" != name="index123"
	
	3.Flask WTForms
		from wtforms import Form,validators,widgets
		from wtforms.fields import simple
		class LgoinForm(Form)：
			username = simple.StringField(
				label = "用户名",
				validators=[
					validators.DataRequired(message="用户名不能为空"),
				],
				widget = widgets.TextInput(),
				render_kw = {"class":"jinwangba"}
			)
		
		def a():
			"GET":
			return render_template("a.html",fm = LgoinForm())
			"POST":
			request.form
			lfm = LgoinForm(request.form)
			lfm.validate() true false
		
		{{ fm.username.label }} {{ fm.username }} {{ fm.username.errors.0 }}
		
			
Flask回顾：
	# 1.路由@app.route('/',methods=["GET","POST"],endpoint="helloWorld",strict_slashes=True)
	# 动态路由参数 /<arg> def viewfunc(arg)
	# url_for
	# 2.三贱客：
	# HTTPResponse return 'Hello World!'
	# render retrun render_template("index.html")
	# redirect retrun redirect("/login")

	# 3.request
	# 存放数据：
	# request.form # 从表单 FormData 获取到的数据
	# request.args # URL传参时 获取到的数据
	# request.json # Content-Type:application/json 获取数据
	# request.data # b"" Content-Type:xiaowangba 获取数据
	# 请求属性的
	# request.method = "GET"/"POST"
	# request.path = "/index"
	# request.url = "http://127.0.0.1:5000/index"
	# 坑
	# request.values.to_dict() 同名被GET(args)覆盖

	# 4.session : Flask-Session
	# app.secret_key = "加密字符串"
	# 存放在浏览器Cookies中的被序列化后的session
	# session["key"] = "value"
	# session["key"]
	# session 默认31天的生命周期

	# 5.Blueprint
	# 蓝图对象 可以理解为 一个不可以被启动的Flask对象
	# bp = Blueprint("bluename",__name__,template_folder="temp_blue")
	# @bp.route("/blue")
	# app.register_blueprint(blueprint.bp)

	# 6.Flask配置
	# 1.Flask对象实例配置
	# class Obj(object):
	#     DEBUG = True
	#     SESSION_TYPE = "redis"
	#     SESSION_REDIS = Redis(db=5)
	# app.config.from_object(Obj)

	# 2.Flask初始化的配置
	# template_folder = 模板文件存放路径
	# static_folder = "静态文件存放路径"
	# static_url_path = "/静态文件URL访问地址"默认是static_folder


	# 7.Flask Jinja2
	# {{  }} 当引用变量 和 执行函数的时候 ， 非逻辑引用
	# {% %} if for 逻辑代码引用
	# obj.name obj.get("name") obj["name"]  obj_list.1  obj_list[1]
	# Markup  | safe
	# @app.template_global()
	# @app.template_filter()

	# 8.before_request after_request errorhandler(404,500)
	# @app.before_request 多个before_request依次执行
	# def be1():
	#     return None

	# @app.after_request 多个after_request，反序执行
	# def af1(response)
	#     return response

	# 正常情况： be1-be2-af2-af1
	# 异常情况： be1-af2-af1
	# @app.errorhandler(404) 重定义错误信息

	# 9.flash
	# flash("be_fr1")
	# get_flashed_messages()


	# 10.send_file jsonify
	# send_file("文件路径") 打开并返回文件内容
	# jsonify({k:v}) 将字典序列化json，打包一个Content-Type：application/json 返回给客户端

	# 11.Flask CBV
	# class Index(views.MethodView):
	# 	methods = ["GET"]
	# 	decorators = [a,b,c]
	# 	def get():
	# 		return "file"
	#
	#
	# app.add_url_rule("/",endpoint="index",view_func=Index.as_view(name="index"))
	#
	# if 1 : endpoint = None = name = "index"
	# elif 2: endpoint="index" != name="index123"
	
	
今日内容	
	1.DBUtils 数据库连接池
		
	2.Flask请求上下文，应用上下文
		基于Flask源代码
		app.run = werkzeug.run_simple("ip",port,app) = app() = app.__call__ = wsgi_app()


思考：		
look and say
1
11
21
1211
111221
312211
13112221
1113213211




开发者日志：
	2018年10月12日：上午
		app.append()
		基于ListObject实现stack
		
		
		
