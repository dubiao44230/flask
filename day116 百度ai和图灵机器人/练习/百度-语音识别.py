import os
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14454015'
API_KEY = '3E737wvObjiGjw3banDRg4rX'
SECRET_KEY = 'ycl07lIFckyOZcyXnQ45wVvDiZEzfhY1'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    # 将音频文件转化成pcm格式  ，因为百度的语音识别只有pcm格式识别最准确
    cmd_str = f"ffmpeg -y -i {file_path} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {file_path}.pcm"
    os.system(cmd_str)  # python中执行系统命令
    with open(f"{file_path}.pcm", "rb") as fb:
        return fb.read()

res = client.asr(speech=get_file_content("录音.m4a"),options={
    "dev_pid":1536,  # 普通话(支持简单的英文识别),别的语音看技术文档
})

print(res)
