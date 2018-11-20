# a ={
#     11600:{"request","session"},#request
#     11040:{"request","session"}#request
# }
#
# {
#     11600:{"stack":[1,2,3,4]}
# }

class MyStack(object):
    def __init__(self):
        self.data = []

    def push(self,args):
        self.data.append(args)

    def top(self):
        return self.data[-1]

mystack = MyStack()
mystack.push("1")
mystack.push("2")
mystack.push("3")

print(mystack.top())