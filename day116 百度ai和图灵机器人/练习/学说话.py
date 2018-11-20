"""
学说话：是把识别语音中的文字，然后将文字合成为语音
"""
from aip import AipSpeech
import os

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 语音识别
def get_file_content(filePath):
    cmd_str = f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
    os.system(cmd_str)
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

def xueshuohua(file_name):
    res = client.asr(speech=get_file_content(file_name),options={
        "dev_pid": 1536,
    })
    text = res.get("result")[0]  # 语音识别得到的文本文件
# 语音合成
    res_audio =  client.synthesis(text, options={  # 将得到的文本文件合成为语音
        "vol":8,
        "pit":8,
        "spd":5,
        "per":4
    })
    # 将合成的语音文件写到文件中
    with open("audio.mp3","wb") as f:
        f.write(res_audio)
    # 打开合成的语音文件
    os.system("audio.mp3")

xueshuohua("录音.m4a")
