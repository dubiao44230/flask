from flask import Flask, render_template, request,Markup
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import json

app = Flask(__name__)
user_socket_dict = {}

@app.route("/")
def index():
    return render_template("ql.html")

@app.route("/ws/<nickname>")
def ws(nickname):
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    if user_socket:     # 如果有链接就把链接人的姓名和链接保存在字典中
        user_socket_dict[nickname] = user_socket
    else:
        return render_template("ql.html", message = "请使用Websocket链接")
    while 1:
        msg = user_socket.receive()   # 接受发送的消息
        msg = json.loads(msg)
        for us_nick_name, socket in user_socket_dict.items():   # type:WebSocket
            if user_socket != socket:   # 不能自己给自己发消息
                try:
                    socket.send(json.dumps({"sender": nickname, "msg": msg["msg"]}))  # 发送消息
                except:
                    continue


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0", 8008), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()