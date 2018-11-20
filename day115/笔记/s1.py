from flask import Flask, request
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)


@app.route("/ws")  # WS://127.0.0.1:9527/ws
def ws():
    # request.environ["wsgi.websocket"] = <链接>
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    while 1:
        msg = user_socket.receive()
        print(msg)
        user_socket.send(msg)


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0", 9527), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
    app.run("0.0.0.0", 9527, debug=True)
