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
        msg_dic = json.loads(msg)
        to_user = msg_dic.get("to_user")  # 获取要发送消息的人
        to_user_socket = user_socket_dict.get(to_user)  # 获取要发送消息的人的链接
        send_str = json.dumps({"sender":nickname,"msg":msg_dic.get("msg")})
        to_user_socket.send(send_str)

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0", 8008), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()