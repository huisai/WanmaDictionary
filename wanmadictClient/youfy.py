import urllib.request
import urllib.parse
import json
# print('＝＝＝有道在线翻译＝＝＝')

# while True:
def fanyi_youdao(shuru):
    print('调用有道')
    line = str(shuru)
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
    #创建字典存储
    #发送请求时需要传输的数据
    data={}
    data['i'] = line
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1517799189818'
    data['sign'] = '8682192c0707c52ecdffbc98f77a17ac'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'true'
    #将字典数据传输告知服务端为utf-8的格式
    data = urllib.parse.urlencode(data).encode('utf-8')
    #返回翻译结果给response绑定起来
    response = urllib.request.urlopen(url,data)
    #将翻译结果使用读取方法并转换中文格式
    html = response.read().decode('utf-8')
    #找到翻译结果，load函数能将str转换成dict类型
    translate_results = json.loads(html)
    #过滤掉一些信息,只索引出需要的信息
    translate_results = translate_results['translateResult'][0][0]['tgt']
    return translate_results
    # return 'sdjfsdfhksdhfkshdkfshhkfsdksfsfsdsfsdf'

print(fanyi_youdao('''
Wang Yi says Washington's actions won't eliminate its trade imbalance

The United States will not only fail to reach its goal but will also reap what it has sown, State Councilor and Foreign Minister Wang Yi said on Thursday in response to Washington's latest threat to ratchet up trade tensions with Beijing.

The US "still cannot eliminate what it claims as its trade imbalance" if it reduces imports from China and raises them from other countries, Wang said at a news conference on the sidelines of the annual the Association of Southeast Asian Nations Foreign Ministers' Meeting and related meetings in Singapore.'''))