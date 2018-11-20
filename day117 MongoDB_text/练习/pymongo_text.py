
import pymongo
mongo_client = pymongo.MongoClient(host="127.0.0.1",port=27017)

mongo_db = mongo_client["Oldboy"]
#
#
# res = mongo_db.user.find()
# print(res)
# for i in res:
#     print(i)

# res = mongo_db.user.insert_one({"name": "ssssssssss"})
# print(res.inserted_id)


res = mongo_db.user.update_one({"name": "ssssssssss"}, {"$set":{"name": "ddd"}})


print(res, dir(res), res.modified_count)