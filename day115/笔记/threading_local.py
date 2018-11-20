from threading import local
import threading
import time

# class local(object):
#     pass


foo = local()


def func(num):
    foo.num = num
    time.sleep(1)
    print(foo.num,threading.current_thread().ident)


for i in range(20):
    th = threading.Thread(target=func,args=(i,))
    th.start()