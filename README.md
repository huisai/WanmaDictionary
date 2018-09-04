# 万码词典
## 需求分析
###  客户端
1. 实现基本英单词查询，返回详细解释，例句以及单词发音。
2. 实现中文词汇查询，返回对应英文翻译。
3. 实现简单中英句子查询，返回对应文翻译。
4. 实现用户注册
5. 实现用户名登陆或邮箱登陆，密码修改
6. 用户登陆后，可收藏单词，浏览 单词本，后台记录查询历史单词查询次数
7. 实现记住密码自动登陆
8. 实现语音输入查询翻译
9. 实现截图识别输入查询翻译
10. 实现文档翻译
###  服务端
1. 创建用户账号数据库，记录用户的收藏，查询历史。
2. 创建英文单词词典数据库。
## 具体实现
### 服务端
1. 服务端主程序监听网络接收信息，一接收到客户端查询请求，创建子进程，进行数据库查询
2. 字典数据库包含一下字段
-   | word | 单词名称 |
- | phonetic | 音标，以英语英标为主 |
-  | translation | 单词释义（中文），每行一个释义 |
- | oxford | 是否是牛津三千核心词汇 | 
- | tag | 字符串标签：zk/中考，gk/高考，cet4/四级 等等标签，空格分割 |
- | bnc | 英国国家语料库词频顺序 |
- | frq | 当代语料库词频顺序 |
3. 服务端与客户端按照自定义报文格式进行交互
### 客户端
1. 先判断查询的单词中是否包含中文字，只要包含中文字，即按中文查询
2. 客户端可以在不登录进行查询,以一个全局变量log_state作为登陆状态标志位。
3. 收藏单词、查看收藏单词本、删除收藏，先判断登录状态，若为已登录可继续执行操作，若为未登录弹出提示窗口
4. 单词的详细解释，例句，发音分开接收，发音以MP3格式保存在本地，用户点击播放发音按钮则播放
5. 软件关闭前先判断用户的登陆状态和是否是否设置了自动登陆，满足这两个条件将账户密码保存在本地，下次打开软件时读取该文件，自动发送登陆请求，实现自动登陆
6. 与服务端断开连接后马上重连并判断登陆状态，若已登陆则自动发送登陆请求。
7. 打开客户端后先创建套接字，并发送通信测试报文，若通信失败则弹出窗口提示未连接客户端。在主界面可手动修改主机地址。发送任何报文都先判断套接字创建是否成功，成功继续存操作，不成功则再次创建并提示创建结果。客户端就可以在未连接服务端的状态下打开页面，并在发送请求前再次连接。
### 自定义客户端/服务端交互协议

### 各窗口界面的UI设置模块
各窗口用户界面的设计主要使用PyQt的 QtDesigner完成基础样式的设计，根据需求完成窗口拖拽，按钮的连接，动态显示等功能的添加。

### 语音&图像识别模块(yuyin.py)
语音识别和图像识别主要调用了百度云的接口，客户端完成录音，屏幕截图后，将数据传至百度并返回识别结果。最后在客户端完成查询操作。
#### 一、环境搭建（准备工作）
 
##### 百度提供的API调用前需要做的准备工作：
-  注册百度云账户
-  创建应用
-  选择相应功能（语音识别/文字识别）
-  安装百度包baidu-aip
       
#####  调用接口需要使用的库（语音识别/文字识别）：urllib3 、  base64、 json、 requests、

语音识别：录音 + 百度API（语音识别）
录音需要使用的库： pyaudio中的   pyaudio（录音），palnt16（初始化麦克风的参数）

####  二、语音识别（录音技术文档）

##### 录音模块
##### pyaudio调用（麦克风）硬件初始化参数：

- 帧速率  = 16000            #百度识别要求
- 声音采样率 = 2000        #采用频率越高声音越清晰，8000为电话录入采样率。
- 声道数 = 1                     #左右声道合成单声道
- 取样声道 = 2                 #双声道取声
- 录音时间 = 60               #百度最高识别时长

##### 录音流程：
  1.封装（录音写操作），录音以二进制方式写入文件，以便录音函数调用（参数：文件名，数据）
  
  2.创建录音函数，使用pyaudio（）创建麦克风对象
  
  3.初始化麦克风参数（此处采用提前写好的硬件初始化参数）
                                                        
                                                        pa.open(format = paInt16,channels=1,
              rate=framerate,input=True,
            frames_per_buffer=NUM_SAMPLES）

  4.创建一个空的列表作为声音的数据缓存
 
  5.用while循环，循环60秒，以声音采用2000的频率循环读取
        将录制的声音以队列存储的方式持续追加进用作数据缓存的列表中去

  6.此处调用流程1所封装的函数（录音写操作）

  7.并定义文件格式为wav，并保存为本地文件(百度识别支持的 pcm / wav/ arm）

  8.关闭麦克风（录音硬件）

##### 调用百度API模块（语音识别接口）
##### 请求方式为：
将音频数据放入body中以JSON或raw两种方式提交（本次采用的是JSON）
-     百度需要的表单数据：
- 帧数率 = 16000
- 录音文件格式 = wav
- 用户唯一识别码 = 此处任意填写
语言端口编码  =  1536 （支持普通话识别，简单的英文识别）

##### 可选语言端口（1536 普通话 + 简单英文识别）
【  1537  普通话（纯中文） 、1737 英语、 1637粤语、 1837 四川话 、 1936 普通话远场】


##### 调用语音识别流程：
首先需要封装获取token的函数（通过创建应用提供的appKey secretKey换取接口密钥）
    
##### 一、换取token的表单数据：
1、准备访问的url及API需要的表单数据：
    访问地址 = "https://openapi.baidu.com/oauth/2.0/token?"   
    API_Key = '应用提供的接口密钥'              #百度云应用随机生成供用户调用
    Secret_Key = '应用提供的客户端密钥'      #百度云应用随机生成供用户调用
    将以上数据拼接出url（将表单数据带入url）

2、使用requests向url以post格式发送请求         #百度要求

3、将返回的数据用json从字符串对象转换成字典对象，观察其字典格式并索引出token
             如：  json.loads(自定义文本变量.text)["access_token"]

4、返回token出去（预留给获取文本函数调用）


##### 二、获取返回的文本内容
##### API需要的表单数据：
- 录音文件格式：wav,
- 帧数率:16000,
- 用户唯一识别码:任意填写
- 声音文件编码: 用base64编码，并decode成utf8格式
- 用户唯一识别码:CUID        
- 字节长度:size（os.path.getsize获取录音文件的字节数）
- 声道数:1
- 密钥:token（调用函数获取token）

##### 编写流程：
5.用with以二进制格式读取
用base64编码，并decode成utf8格式
用os.path.getsize获取文件的字节数(API需要的表单数据）

    因为使用的是JSON格式，需要告知API使用的是JSON格式
           需要此参数headers = { 'Content-Type' : 'application/json'} （表单数据）

6.使用requests以post方式发送请求到url，用json编码发送表单数据携带headers

7.将百度返回的数据用json解析，从字符串对象转换成字典对象

8.打印出数据，观察数据结构并索引result["result"][0]

9.将索引出的识别结果返回给调用对象并输出给前端显示

#### 文字识别调用流程：
1.调用换取token函数（任何百度API调用前需要换取token）

2.创建http 使用urllib3.PoolManager( )创建连接池

3.二进制方式打开图片文件
4.将图片文件流进行base64编码，并读取

5.将图片格式用urlencode编码

6.通过http链接池发送请求以post格式，向url发送，请求体为urlencode编码
    并携带表单数据headers={'Content-Type':'application/x-www-form-urlencoded'}

7.将返回的数据解码为utf-8格式

8.用json解析数据，从字符串对象解析为字典对象

9.使用for循环，用get获取识别结果并循环输入给前端显示

10.关闭文件流.


### 验证码自动生成(yanzhengma.py)
  
#####    环境配置： 
   PIL（Image，ImageDraw，ImageFont）、random、string、os
   
##### 代码思维

1.使用Image.new( )设定背景图片颜色，宽高及验证码字体大小

2.ImageDraw.Draw( 图片对象)创建画刷使用上一步的参数，画出背景图

3.获取系统字体路径    

4.ImageFont.ruetype( )获取指定路径的字体

5.获取随机生成的验证码的值

6.draw.text( )将验证码画在图片上

7.for循环随机画干扰线，返回图片和文本内容

8.将图片输出给前端交互，文本输入在服务端以便测试.