import json
from bson import ObjectId


data =  {"username":"jinwangba","user_id":ObjectId("5bc6b21ef7ac9a09b4ff6c0e")}
data["user_id"] = str(data["user_id"])

print(json.dumps(data))

objid = "5bc6b21ef7ac9a09b4ff6c0e"

print(objid,type(objid))   # 字符串类型

print(ObjectId(objid),type(ObjectId(objid)))  # ObjectId(objid)转换成ObjectId类型