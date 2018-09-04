import wave

from pyaudio import PyAudio,paInt16
import json
import base64
import os
import requests
import time
from .tool import *

RATE = "16000"
FORMAT = "wav"
CUID="wate_play"
DEV_PID="1536"  #中英文
# DEV_PID="1737"    #英文

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=100

def get_token():
    server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    #API Key
    # client_id = "FfUpzroDhsDpi2WRODOuIuhz"
    client_id = 'x00zG5adXuYFcSxG86xRTSFl'

    #Secret Key
    # client_secret = "NrGYmTgYuXgq5gWqizZ9rGGeDKhv7O2y"
    client_secret = 'AsUfr74tFlAe4MxUGnC6g095OaP6BeQZ'

    #拼url
    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(server,grant_type,client_id,client_secret)
    #获取token
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token

def get_word(token):
    try:
        filpath = get_path('wav', '01.wav')
        with open(filpath, "rb") as f:
            speech = base64.b64encode(f.read()).decode('utf8')
        size = os.path.getsize(filpath)
        headers = { 'Content-Type' : 'application/json'}
        url = "https://vop.baidu.com/server_api"
        data={
                "format":FORMAT,
                "rate":RATE,
                "dev_pid":DEV_PID,
                "speech":speech,
                "cuid":CUID,
                "len":size,
                "channel":1,
                "token":token,
            }

        req = requests.post(url,json.dumps(data),headers)
        result = json.loads(req.text)
        print(result)
        ret=result["result"][0]
    except Exception as e:
        print(e)
        return "!@#"
    return ret[:-1]

def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record(e):
    pa=PyAudio()
    print('开始录音')
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    print('.')
    # t0 = time.time()
    while count < TIME:#控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        if not e.is_set():
            break
    print('录音结束')
    filpath = get_path('wav','01.wav')
    save_wave_file(filpath,my_buf)
    stream.close()
    e.set()


chunk=2014
def play():
    wf=wave.open(r"mp3.wav",'rb')
    print(wf.readframes(1000))
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    while True:
        data=wf.readframes(chunk)
        if data=="":break
        stream.write(data)
    stream.close()
    p.terminate()

def play_mp3(filename,second):
    from pygame import mixer
    mixer.init()
    track1 = mixer.music.load(filename)
    mixer.music.play()
    time.sleep(second)  # 播放n秒
    mixer.music.stop()  # 停止播放

def get_word_img(img,token):
    http = urllib3.PoolManager()
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+token
    f = open(r'D:\pyproject\wanmadict7.18-7.23\wanmadict7.18\01.png','rb')
    # img = base64.b64encode(f.read())
    # print(img)
    params = {'image': img}
    params = urlencode(params)
    reques = http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/x-www-form-urlencoded'})
    result = str(reques.data,'utf-8')
    a=json.loads(result)
    for x in a.get('words_result'):
        print(x.get('words'))
    # f.close()

if __name__ == '__main__':
    pass
    # play()
