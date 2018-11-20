from aip import AipNlp

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

res = client.simnet("你今年多大了","How old are you")

print(res)