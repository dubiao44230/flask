from aip import AipSpeech
from aip import AipNlp
from uuid import uuid4
import os
import to_tuling

APP_ID = '14446007'
API_KEY = 'QrQWLLg5a8qld7Qty7avqCGC'
SECRET_KEY = 'O5mE31LSl17hm8NRYyf9PwlE5Byqm0nr'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    cmd_str = f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
    os.system(cmd_str)
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()


def xsh(file_name):
    ret_file_name = f"{uuid4()}.mp3"
    res = client.asr(speech=get_file_content(file_name), options={
        "dev_pid": 1536,
    })

    text_def = res.get("result")[0]
    print(text_def)
    text = my_nlp_lowb(text_def)
    print(text)
    res_audio = client.synthesis(text, options={
        "vol": 8,
        "pit": 8,
        "spd": 5,
        "per": 4
    })

    with open(ret_file_name, "wb") as f:
        f.write(res_audio)

    return ret_file_name


def my_nlp_lowb(text_def):

    if nlp_client.simnet("你叫什么名字", text_def).get("score") >= 0.72:
        return "我的名字叫金王八"

    if nlp_client.simnet("你今年几岁了", text_def).get("score") >= 0.72:
        return "我今年999岁了"

    return to_tuling.goto_tuling(text_def,"xiaowangba")


