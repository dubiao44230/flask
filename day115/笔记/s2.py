from flask import Flask, request,render_template
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import json

app = Flask(__name__)

user_socket_dict = {} # {jinwangba:<geventwebsocket.websocket.WebSocket object at 0x000000000B35CE18>}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ws/<nickname>")  # WS://127.0.0.1:9527/ws
def ws(nickname):
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_dict[nickname]=user_socket
        print(len(user_socket_dict))
    else:
        return render_template("index.html",message="请使用Websocket链接")
    while 1:
        msg = user_socket.receive()
        for user_nick_name,socket in user_socket_dict.items(): # type:WebSocket
            if user_socket != socket:
                try:
                    socket.send(json.dumps({"sender":nickname,"msg":msg}))
                except:
                    continue


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9527),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
    # app.run("0.0.0.0", 9527, debug=True)
