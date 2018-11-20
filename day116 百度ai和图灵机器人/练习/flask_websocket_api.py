from flask import Flask, request, render_template
from uuid import uuid4
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import web_request_an

app = Flask(__name__) #type:Flask

@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    while True:
        msg = user_socket.receive()

        q_file_name = f"{uuid4()}.wav"
        with open(q_file_name, "wb") as f:
            f.write(msg)

        ret_file_name = web_request_an.xueshuohua(q_file_name)
        user_socket.send(ret_file_name)

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9528), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()