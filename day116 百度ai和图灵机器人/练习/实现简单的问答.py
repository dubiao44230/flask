from aip import AipSpeech
import os

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    # 将音频文件转化成pcm格式  ，因为百度的语音识别只有pcm格式识别最准确
    cmd_str = f"ffmpeg -y -i {file_path} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {file_path}.pcm"
    os.system(cmd_str)  # python中执行系统命令,将音频文件转化成pcm格式
    with open(f"{file_path}.pcm", "rb") as fb:
        return fb.read()


def xueshuohua(file_name):
    res = client.asr(speech=get_file_content(file_name),options={
        "dev_pid":1536,  # 普通话(支持简单的英文识别),别的语音看技术文档
    })
    # 获得语音转化成的文本文件
    text_def = res.get("result")[0]
    # 通过my_nlp_lowb函数的到问题答案
    text = my_nlp_lowb(text_def)
    # 将问题答案语音合成
    res_audio = client.synthesis(text, options={
        "vol": 8,
        "pit": 8,
        "spd": 5,
        "per": 4
    })
    with open("audio.mp3", "wb") as f:
        f.write(res_audio)
    os.system("audio.mp3")


def my_nlp_lowb(text_def):
    if text_def == "你叫什么名字":
        return "我的名字叫金王八"
    if text_def == "你今年几岁了":
        return "我今年999岁了"

xueshuohua("nj.m4a")