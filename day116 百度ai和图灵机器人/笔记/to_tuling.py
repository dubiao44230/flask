import requests,json

tuling_url = "http://openapi.tuling123.com/openapi/api/v2"

def goto_tuling(q_text,uid):
    to_tuling_str = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": q_text
            },
        },
        "userInfo": {
            "apiKey": "d4e62f62153641bc81403f51b26d042c",
            "userId": uid
        }
    }
    # xiaobeijiqiren：【今天，北京】
    a = requests.post(tuling_url,json=to_tuling_str)
    tuling_res = json.loads(a.content)
    return tuling_res.get("results")[0]["values"]["text"]