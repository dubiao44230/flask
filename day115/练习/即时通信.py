from flask import Flask, request
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket  # 使pycharm支持WebSocket语法：有提示
    while 1:
        msg = user_socket.receive()
        print(msg)
        user_socket.send(msg)


if __name__ == '__main__':
    http_serv =  WSGIServer(("0.0.0.0", 8008), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()