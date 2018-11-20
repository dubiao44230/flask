from aip import AipNlp

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

res = client.simnet("你今年多大了","你今年几岁了")

print(res)  # {'log_id': 7892701626517169080, 'texts': {'text_2': '你今年几岁了', 'text_1': '你今年多大了'}, 'score': 0.908771}