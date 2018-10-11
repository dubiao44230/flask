2018年10月11日：
昨日回顾：
	1.解决视图函数名重复的问题，装饰器返回内部函数的名称是一样， endpoint = viewfunc.__name__ ,endpoint
	
	2.flask中的路由：
		@app.route("/login")
		1.methods=("GET","POST") 允许请求方式
		2.endpoint = "反向url"  # 
		3.url_for("反向url - endpoint") == "/"
		4.redirct_to = "/login" 在请求进入视图函数之前返回，跳转
		5./<arg>  动态路由参数 def index(arg)
	
	3.Flask中的配置：
		1.Flask实例配置app
			app.config.from_object(obj)
			class obj():
				DEBUG=True,
				REDIS=redis.Redis("127.0.0.1",6379,db=1),
				SECRET_KEY = "123123"
				JSONIFY_MIMETYPE="application/json"
			
		2.Flask初始化配置：
			template_folder="模板存放目录"
			static_folder = "静态文件存放目录"
			static_url_path = 默认 f"/{static_folder}" "在URL路径上所使用的地址"
	
	4.蓝图 (Buleprint)
		from flask import Buleprint
		bp = Buleprint("bluename",__name__,template_folder,static_folder,static_url_path)
		@bp.route("/blue",methods=(),endpoint)
		def bl()
			return 
	
	5.before_request after_request errorhandler
		1.before_request 在请求进入视图函数之前，做出处理 @app.before_request
		2.after_request 在请求结束视图函数之后，返回客户端之前，做出处理
		def affunc(response)
		
			return response
		
		正常场景
			be1-be2-af2-af1
		异常场景
			be1-af2-af1
		
		3.errorhandler(404) 定义错误信息的返回
		def error(arg)
			return render_template
			
	6.闪现 flash
		from flask import flash , get_flashed_messages
		
		flash("123")
		flash("123")
		msg = get_flashed_messages()[0]
		
		使用一次即可消失
	
	7.send_file() jsonify
		from flask import send_file ,jsonify
		
		send_file("文件路径") 打开文件并返回客户端
		
		jsonify({k:v})	将dict序列化成json 返回给客户端之前加入一个Content-Type:application/json
		
		
		
		
今日内容：
	1.Flask 中的 CBV
		class Index(views.MethodView):
			# methods = ["POST"]
			# decorators = [war,nei]

			def get(self):
				return "I am Gay"

			def post(self):
				return "I am Les"

		app.add_url_rule("/index", endpoint="calss_index", view_func=Index.as_view(name="index"))
		as_view中的name 是在endpoint存在时作为 endpoint
	
	2.Flask中的插件 之 终于可以不用session  Flask-Session
		导入：
			from flask import Flask, session
			from flask_session import Session
			from redis import Redis
		配置：
			app.config["SESSION_TYPE"] = "redis"
			app.config["SESSION_REDIS"] = Redis(host="127.0.0.1",port=6379,db=5)
		替换：
			Session(app)
		使用：
			session["user"] = "aasdf"
			session.get("user")
	
	3.Flask中的插件 之 如果你不使用前后端分离的话，这东西很好用 WTForms
		from wtforms.fields import simple
		from wtforms import Form
		from wtforms import validators

		class LoginForm(Form):
			username = simple.StringField(
				label="用户名",
				validators=[
					validators.DataRequired(message="数据不能为空"),
					validators.Length(min=5, max=16, message="大于5小于16")
				],
				render_kw={"class": "jinyinwangba"}
			)
			
		class Index(views.MethodView):
			def get(self):
				loginfm = LoginForm()
				return render_template("index.html", fm=loginfm)
			def post(self):
				loginfm = LoginForm(request.form)
				if not loginfm.validate():
					return render_template("index.html", fm=loginfm)
				session["user"] = "I am jinyinwangba"
				return "I am Les"
		
	
今日总结：
	
	1.Flask CBV
		from flask import views
		class index(views.MethodView):
			methods = ["GET"]
			def get()
			def post()
		
		app.add_url_rule("/index",endpoint=None,view_func=index.as_view(name="index"))
		
	2.Flask-Session
		三方组件：
		from flask import session
		from flask_session import Session
		
		app.config["SESSION_TYPE"] = "redis"
		app.config["SESSION_REDIS"] = REDIS("127.0.0.1",6379,db=12)
		
		Session(app)
		
		session["key"] = "123"
		session["key"]
		
		前缀+sid(session:asdfas-fasdfasdf-asdfsafsadf)

	3.WTForms
		simple.StringField(
			label = "name"
			validators=[
				validators.校验方法(message="")
			]
		)
		PasswordField
		
		core.SelectMuitilField(
			label = "name"
			validators=[
				validators.校验方法(message="")
			],
			choices = [
				[1,"1"],[2,"2"],[3,"3"]
			],
			coerce = int
		)
		
		传递From
			fm = wtfFrom()
			return render_template("tem.html",fm = fm)
		
		校验:
			fm = wtfFrom(request.form)
			if fm.validate():
				return 成功
			return render_template("tem.html",fm = fm)
		
	

	
	
今日作业：
	学生管理 + 注册登录(Flask CBV,Flask-Session,WTForms) + pymsql
	
	4.DBUtils 数据库连接池 DBPool
		- 自制sqlHelper
	
	

	