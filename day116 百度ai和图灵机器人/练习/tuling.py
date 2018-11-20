import requests
import json

# 图灵机器人的接口地址
tuling_url = "http://openapi.tuling123.com/openapi/api/v2"

def to_tuling(request_text, user_id):
    msg = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": request_text  # 问题
            },
        },
        "userInfo": {
            "apiKey": "81843ccccbb643319af5c7821fcf3332",
            "userId": user_id  # 用户id
        }
    }
    ret = requests.post(tuling_url, json=msg)
    ret_msg = json.loads(ret.content)  # 这里注意 ret.content才能拿到返回的信息
    # ss = ret.json()   这种方法也可以反序列化
    return ret_msg.get("results")[0]["values"]["text"]


