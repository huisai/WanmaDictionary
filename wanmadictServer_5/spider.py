#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 18-7-16 下午9:20
# @Author : Wulei# @Site : 
# @File : youdao_zh_en.py
# @Software: PyCharm
# 神兽保佑,永无BUG！


'''
youdao_zh_en = Youdao_zh_en(content)
youdao_zh_en.start()
返回数据如下：
{
		'translation':[string,...], --- 翻译字符串
		'example':[[英文例句,中文例句],[...],...], --- 例句字符串
		'phonetic':[英式音标,美式音标] --- 音标字符串
		'voice':[英式音频,美式音频] --- 音频文件流
		 }
没有获取到数据时，该键值为[]
'''

import requests # HTTP库
import re
import time
import random
import hashlib # hash算法类的库
import json # 处理json数据格式的模块
import langid # 可以识别语种


class Youdao_zh_en(object):
	'''
	传入待翻译内容，调用start函数返回翻译结果
	对象属性：
		self.content
		self.data
		self.headers
		self.url
		self.languages
	'''
	def __init__(self,content):
		'''
		初始化属性
		语种检测
		'''
		# 待翻译内容
		self.content = content
		client = 'fanyideskweb'
		salt = str(int(time.time() * 1000) + random.randint(1, 10))  # 时间戳+1~10  字符串
		sign = hashlib.md5((client + self.content + salt + 'ebSeFb%=XZ%T[KZ)c(sy!').encode('utf-8')).hexdigest()
		# 请求数据
		self.data = {
			'i': self.content,
		    'from': 'AUTO',
		    'to': 'AUTO',
		    'smartresult': 'dict',
		    'client': client,
		    'salt': salt,
			'sign': sign,
			'doctype': 'json',
			'version': '2.1',
			'keyfrom': 'fanyi.web',
			'action': 'FY_BY_CLICKBUTTION',
			'typoResult': 'false'
		}
		# 目标url
		self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
		# 请求头
		self.headers = {
			'Cookie': 'OUTFOX_SEARCH_USER_ID=1630693779@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=345009932.1042496;                                      _ntes_nnid=5bee0390fa62ba2a7fc9ee3e299ba8eb,1531400099358;                                                                        UM_distinctid=1648e8f90df4d9-051e283902caf-3f3c5b02-1fa400-1648e8f90e1ff9; fanyi-ad-id=46607;                                     fanyi-ad-closed=1; JSESSIONID=aaa8CAm_ZhuNe96lhYCsw; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|;                                  JSESSIONID=abciU_pCe76HT7ebrYCsw; ___rl__test__cookies=1531644308384',
			'Referer': 'http://fanyi.youdao.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162                Safari/537.36'
		}
		# 语种
		try:
			self.languages = langid.classify(self.content)[0]
			if self.languages == 'zh':
				print('源语种：中文')
			elif self.languages == 'en':
				print('源语种：英文')
		except:
			print('无法识别语种')

	# 启动爬虫
	def start(self):
		result_dict = {'voice': [], 'phonetic': [], 'translation': [], 'example': []} # 存放翻译后的内容
		# 获取json
		print('爬虫已启动，正在发送post请求...')
		try:
			html_json = requests.post(self.url, headers=self.headers, data = self.data, timeout=1)
		except:
			print('网络出现异常')
			return result_dict

		# 转换内容为字典
		'''
		格式类似如下，文档没有"smartResult"键
		{
			"translateResult": [[{"tgt": "得到", "src": "get"}]],
			"errorCode": 0,
			"type": "en2zh-CHS",
			"smartResult": {"entries": ["", "n. 生殖；幼兽\r\n", "vi. 成为；变得；到达\r\n",
							"vt. 使得；获得；受到；变成\r\n"],"type": 1}
		}
		'''
		self.content_dict = json.loads(html_json.text)
		print('post请求成功！')
		# 判断是否为文档
		if "smartResult" in self.content_dict:
			print("您要翻译的内容是单词类型")
			result_dict = self.__get_word() # 返回单词翻译内容
		else:
			print("您要翻译的内容是文档类型")
			result_dict = self.__get_text() # 返回文档翻译内容
		return result_dict

	# 获取文档翻译内容
	def __get_text(self):
		result_dict = {'voice': [], 'phonetic': [], 'translation': [], 'example': []}
		'''格式如下：
		{
		'translation':[string] --- 翻译字符串
		 }
		'''
		content = ''
		try:
			for i in self.content_dict["translateResult"][0]:
				content += i['tgt']
			result_dict['translation'] = [content]
		except:
			print("无法识别文档")
		return result_dict

	# 获取单词翻译内容
	def __get_word(self):
		print("已进入单词翻译内容获取功能")
		result_dict = {'voice':[],'phonetic':[],'translation':[],'example':[]} # 存放爬取的(音标)＋翻译＋例句＋(音频)
		'''格式如下：
		{
		'translation':[string,...], --- 翻译字符串
		 'example':[[英文例句,中文例句],[...],...], --- 例句字符串
		 'phonetic':[英式音标,美式音标] --- 音标字符串
		 'voice':[英式音频,美式音频] --- 音频文件流
		 }
		 '''
		# 请求头
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
							(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
		# url拼接
		content = self.content.replace(' ','_')
		url = 'http://dict.youdao.com/search?q=' + content + '&keyfrom=fanyi.smartResult'

		# 获取html源码
		print("正在发送get请求...")
		try:
			html = requests.get(url,headers=headers,timeout=1)
		except:
			print("网络出现异常")
		print("get请求成功！")
		# 获取例句
		example_content = self.__get_example(html)
		result_dict['example'] = example_content # 将翻译存入字典

		# 获取发音，音标，翻译
		print("正在获取发音，音标，翻译...")
		voice_phonetic_translation_content = self.__get_voice_phonetic_translation(html,headers)
		result_dict.update(voice_phonetic_translation_content)  # 将发音，音标，翻译存入字典
		print("已成功获取发音，音标，翻译！")

		return result_dict

	# 获取读音，音标，翻译
	def __get_voice_phonetic_translation(self,html,headers):
		content_dict = {'voice':[],'phonetic':[],'translation':[]}
		# 匹配发音，音标翻译所在区域
		pattern = r'<div id="phrsListTab" class="trans-wrapper clearfix">.*?' \
		          r'<div id="webTrans" class="trans-wrapper trans-tab">'
		content = re.findall(pattern,html.text,re.S)
		if not content:
			content_dict['translation'] = self.__get_text()['translation']
			return content_dict

		# 匹配音标
		def phonetic():
			pattern = r'<span class="phonetic">(.*?)</span>'
			phonetic＿content = re.findall(pattern,content[0])
			return phonetic＿content

		# 匹配读音
		def voice():
			pattern = r'<span class="pronounce">(.*?)</span>'
			voice_content = re.findall(pattern, content[0], re.S)  # [英式，美式]
			# 判断是否有发音
			if voice_content:
				try:
					# 英式读音
					uk_voice_url = 'http://dict.youdao.com/dictvoice?audio=%s&type=1' % self.content
					uk_content_voice = requests.get(uk_voice_url, headers=headers, timeout=1)
					# 美式读音
					us_voice_url = 'http://dict.youdao.com/dictvoice?audio=%s&type=2' % self.content
					us_content_voice = requests.get(us_voice_url, headers=headers, timeout=1)
				except:
					print("网络出现异常")
				return [uk_content_voice.content, us_content_voice.content]
			return voice_content

		# 匹配翻译
		def translation():
			pattern = r'<div class="trans-container">.*?<ul>(.*?)</ul>.*?</div>'
			translation_content = re.findall(pattern, content[0], re.S)
			if not translation_content:
				return self.__get_text()['translation']
			# 翻译：中->英
			def zh_en():
				# 再次匹配(每行的词性)
				pattern = r'<p class="wordGroup">(.*?)</p>'
				content = re.findall(pattern, translation_content[0], re.S)
				# 按标签分割
				L = []  # 总的词性翻译内容
				for i in content:
					content = re.split(r'<.*?>', i)
					# 去除多余元素
					str = ''  # 存放每行的词性
					for j in content:
						if re.search(r'\n+|\r+|\t+', j) == None and j != '':
							str += j # 每行的词性
					L.append(str)
				return L

			# 翻译：英->中
			def en_zh():
				# 按标签分割
				L = []  # 总的词性翻译内容
				content = re.split(r'<.*?>', translation_content[0])
				# 去除多余元素
				for i in content:
					if re.search(r'\n+|\r+|\t+', i) == None and i != '':
						L.append(i) # 每行的词性)
				return L

			if self.languages == 'zh':  # 中->英
				L = zh_en()
			else:  # 英->中
				L = en_zh()
			return L

		# 匹配音标
		print("开始匹配音标...")
		content_dict['phonetic'] = phonetic()
		print("音标匹配成功！")
		# 匹配读音
		print("开始匹配发音...")
		content_dict['voice'] = voice()
		print("发音匹配成功！")
		# 匹配翻译
		print("开始匹配翻译内容...")
		content_dict['translation'] = translation()
		print('翻译匹配成功！')

		return content_dict

	# 获取例句
	def __get_example(self,html):
		'''
		1.获取例句区域
		2.获取所有例句
		3.获取例句下的所有子句
		4.拼接子句
		'''
		example_list = []  # 存放处理后的所有例句
		# 获取例句区域
		pattern = r'<div id="bilingual" class="trans-container  tab-content">.*?</p>.*?</li>.*?</ul>.*?</div>'
		content = re.findall(pattern,html.text,re.S)
		if not content:
			return example_list
		content = re.findall(r'<li>(.*?)</li>', content[0], re.S)
		for i in content: # 遍历区域内例句
			# 获取该例句下的所有子句
			content = re.findall(r'<p>(.*?)</p>',i,re.S)
			if content:
				sentence_list = [] # 存放处理后的例句中所有子句
				for j in content: # 遍历例句中所有子句
					# 所有子句内的单词都可能有多余的字符，需要处理
					content = re.split(r'<.*?>',j) # 按标签分割，得到子句所有单词
					# 去除单词中多余元素(\n,\t,'')
					for k in content:
						if (('\n' or '\t') in k) or k == '':
							content.remove(k)
					# 将处理完后的子句内单词拼接成所需要的子句
					sentence = ''.join(content)
					# 将所需子句放进子句列表
					sentence_list.append(sentence)
				# 将子句列表放入例句列表
				example_list.append(sentence_list)
		return example_list
		# 例句读音
		# 考虑传输效率，此功能暂时不开放
		# 问句拼接
		# http://dict.youdao.com/dictvoice?audio=%s&le=eng % 以+拼接单词的句子+%3F
		# Why do you begrudge her success?
		# .句拼接
		# http://dict.youdao.com/dictvoice?audio=%s&le=eng % 以+拼接单词的句子+.
		# We all benefited from his success.


# 以下是模块测试代码
def main():
	while True:
		content = input("请输入要翻译的内容(输入q结束)>>>")
		if content == "q":
			break
		youdao_zh_en = Youdao_zh_en(content)
		d = youdao_zh_en.start()
		print("本次翻译结束！以下是翻译内容：")
		# for i in d.items():
		# 	print(i)
		print(d)


if __name__ == '__main__':
	main()
