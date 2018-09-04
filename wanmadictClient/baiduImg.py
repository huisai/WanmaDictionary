
import urllib3,base64
from urllib.parse import urlencode
import requests
import json

#获取token
def get_token():
    server = 'https://openapi.baidu.com/oauth/2.0/token?'
    grant_type = "client_credentials"
    client_id  = 'gKGtGoZf0GrDk4HwqhMxUDII'
    client_secret = '2GQYpksgFXzxq1bbDHGCitmmNVPdWKpk'
    #将表单数据拼接成url
    url = "%sgrant_type=%s&client_id=%s&client_secret=%s" % (server, grant_type, client_id, client_secret)
    #主机发出请求
    res = requests.post(url)
    token = json.loads(res.text)['access_token']
    return token

def get_word_img(img,token=''):
    http = urllib3.PoolManager()
    if not token:
        token = get_token()
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='+token
    # f = open(r'D:\pyproject\wanmadict7.18-7.23\wanmadict7.18\01.png','rb')
    # img = base64.b64encode(f.read())
    print(type(img))
    params = {'image':img}
    params = urlencode(params)
    reques = http.request('POST',
                          url,
                          body=params,
                          headers={'Content-Type':'application/x-www-form-urlencoded'})
    result = str(reques.data,'utf-8')
    a=json.loads(result)
    print(a)
    s = ''
    try:
        for x in a.get('words_result'):
            s += x.get('words')
        print(s)
        return s
    except:
        return

    # f.close()



if __name__ == '__main__':
    token = get_token()
    get_word(token)
