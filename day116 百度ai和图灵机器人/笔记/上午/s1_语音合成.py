"""
给他一个字符串
输出音频(二进制流)
"""

from aip import AipSpeech

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

res = client.synthesis("日照香炉生紫烟，遥看瀑布挂前川，清明上河图，完全搞不懂，平方差公式",options={
    "vol":8,
    "pit":8,
    "spd":5,
    "per":4
})

with open("audio.mp3","wb") as f:
    f.write(res)

