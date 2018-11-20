import threading, time
from threading import local

# s_local = local()
# s_local.g = 1
#
# def func(num):
#     g = num
#     time.sleep(1)
#     print(g,threading.current_thread().name,threading.current_thread().ident)
#     return g
#
# if __name__ == '__main__':
#
#     for num in range(20):
#         th = threading.Thread(target=func,args=(num,))
#         th.start()


env = "GET /index HTTP1.1\r\n"


class BaseReq():
    def __init__(self, env):
        self.env = env

    @property
    def method(self):
        return self.env.split(" ")[0]

    @property
    def path(self):
        return self.env.split(" ")[1]


request = BaseReq(env)

print(request.method)
print(request.path)
