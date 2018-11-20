import pymongo

mongo_client = pymongo.MongoClient(host="127.0.0.1",port=27017)

mongo_db = mongo_client["S12DAY117"]

#查询
res = mongo_db.user.find()
print(res)
for i in res:
    print(i)
res = mongo_db.user.find_one({"name":"yinwangba"})
print(res)


# 插入
res = mongo_db.chat.insert_one({})
res = mongo_db.chat.insert_many([{},{},{}])
print(res,res.inserted_ids)


# 改：
res = mongo_db.user.update_one({"name":"jinwangba"},{"$set":{"age":888}})
res = mongo_db.user.update_many({"age":{"$gte":0}},{"$set":{"age":888}})
print(res,dir(res),res.modified_count)


# 删除：
res = mongo_db.user.delete_one({"name":"xiaozhuer"})
res = mongo_db.user.delete_many({})
print(res,dir(res),res.deleted_count)


res = mongo_db.user.find_one({"name":"mjj"})
print(res)

for index,item in enumerate(res.get("course")):
    if res.get("course")[index]["course_name"] == "Python":
        res.get("course")[index]["course_name"] = "Django Web框架"

    if res.get("course")[index]["course_name"] == "Vue.js":
        res.get("course")[index]["course_name"] = "Flask Web框架"

    if res.get("course")[index]["course_name"] == "MySQL":
        res.get("course")[index]["course_name"] = "MongoDB"


res = mongo_db.user.update_one({"name":"mjj"},{"$set":res})
