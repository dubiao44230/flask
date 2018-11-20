from flask import Flask, request, jsonify

app = Flask(__name__)  # type:Flask


@app.route("/login", methods=["POST"])
def login():
    RET = {
        "code": 0,
        "msg": "登录成功",
        "data": {}
    }
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "alex" and password == "jinwangba":
        RET["data"] = {"user_id": 9527, "username": "alex", "nickname": "金王吧"}
        return jsonify(RET)

    else:
        RET["msg"] = "登陆失败"
        return jsonify(RET)


if __name__ == '__main__':
    app.run("0.0.0.0", 9527, debug=True)
