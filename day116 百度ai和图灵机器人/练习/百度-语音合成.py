"""
给他一个字符串
输出音频(二进制流)
"""

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14454015'
API_KEY = '3E737wvObjiGjw3banDRg4rX'
SECRET_KEY = 'ycl07lIFckyOZcyXnQ45wVvDiZEzfhY1'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

res = client.synthesis("关关雎鸠", options={
    "per": 3,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
    "vol": 6,  # 音量，取值0-15，默认为5中音量
    "pit": 6,  # 音调，取值0-9，默认为5中语调
    "spd": 5,  # 语速，取值0-9，默认为5中语速
})
with open("gj.mp3", "wb") as f:
    f.write(res)