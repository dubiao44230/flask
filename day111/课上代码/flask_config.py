class Config(object):
    DEBUG = True
    SECRET_KEY = "1233211234567"
    REDIS = "127.0.0.1:6379"
    MYSQL = "127.0.0.1:3306"

# class App(object):
#     pass
#
#
#
# c = Config()
# app = App()
# print(dir(app))
#
# for key in dir(c):
#     if key.isupper():
#         setattr(app,key,getattr(c, key))
#
# print(dir(app))
