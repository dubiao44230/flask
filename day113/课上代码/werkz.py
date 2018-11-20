from werkzeug.serving import run_simple
from werkzeug.wrappers import Request,Response
from flask import Flask

@Request.application
def app(request):
    print(request.method)
    return Response("200 OK!")

run_simple("0.0.0.0",9527,app)

# app(request)

# class Oldboy(object):
#
#     def __call__(self, *args, **kwargs):
#         print("666")
#
#
# ob = Oldboy()
#
# ob()
