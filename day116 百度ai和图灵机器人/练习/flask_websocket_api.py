from flask import Flask, request, render_template
from uuid import uuid4
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import web_request_an