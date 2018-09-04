import socket
import json
import os


# 导出单词本
# １．导出到默认文件夹　２．导出到用户指定文件夹
def export_favorite(L):
    def export(path='wanmadictionary/user'):
        path = os.path.join(os.path.expanduser('~'), path)
        if not os.path.exists(path):
            os.makedirs(path)
        filename = os.path.join(path, 'favoritewords.txt')
        with open(filename, 'w') as f:
            for x in L:
                # 读取历史记录的收藏标志位，若为已收藏则导出
                if x[3] == 1:
                    f.write(x[0] + '   ' + x[1] + ';')
                    f.write('\n')

    n = input('１．导出到默认文件夹　２．导出到用户指定文件夹:')
    if n == '1':
        export()
    elif n == '2':
        path = input('请输入你要保存在哪个目录：~/')
        export(path)


def communite(ip='172.28.34.4'):
    '''
    通信
    '''
    try:
        sockfd = socket.socket()
        # address = ('176.122.15.59',9999)
        address = (ip, 8888)
        # address = ('192.168.1.7', 9999)
        # sockfd.settimeout(5)
        sockfd.connect(address)
        # sockfd.settimeout(100)
        print('成功创建套接字')
        return sockfd
    except Exception as e:
        print('communicate出错', e, '创建套接字失败')
        return 0


def is_cn(text):
    '''判断传入字符是中文还是英文
    返回ｔｒｕｅ为中文，ｆａｌｓｅ为英文'''
    for x in text:
        if u'\u4e00' <= x <= u'\u9fa5':
            return True
    return False


# 点击注册,注册成功返回ture,失败返回false
def click_zhuce(sockfd):
    while True:
        user = input("输入用户名：")
        # if len(user) < 6:
        #     print('用户名不能小于６位')
        #     continue
        for c in user:
            if 'a' <= c <= 'z' or 'a' <= c <= 'z' or '0' <= c <= '9':
                continue
            else:
                print('用户名由数字或字母组成')
                break
        else:
            break

def get_path(pth,flnm,creat=True):
    path0 = os.path.split(os.path.realpath(__file__))[0]
    path1 = os.path.join(path0, 'temp', pth)
    filepth = os.path.join(path1,flnm)
    print(filepth)
    if not os.path.exists(path1) and creat:
        os.mkdir(path1)
    return filepth




def write_pw(user, psw='', list_u=0, filename='list_f', p='wanmabengteng'):
    filepath = get_path('sys',filename)
    print('write_pw()中list_u=', list_u, 'psw=', psw)
    if list_u != 0:
        for x in list_u:
            if user == x['u']:
                list_u.remove(x)
                break
    else:
        list_u = []
    d = {}
    d['u'] = user
    d['p'] = psw
    list_u.append(d)
    try:
        with open(filepath, 'w') as f:
            print(list_u, '密码列表')
            json.dump(list_u, f)  # list_u=[{'user':..,'p':...},...]
    except Exception as e:
        print(e, 'write_pw出错')


def read_pw(filename='list_f', p='wanmabengteng'):
    filepath = get_path('sys', filename)
    try:
        with open(filepath, 'r') as f:
            list_r = json.load(f)
            u, p = list_r[0]['u'], list_r[0]['p']
    except Exception as e:
        print(e, 'read_pw出错')
        if filename == "al":
            return None, None
        return []
    if filename == "al":
        return u, p
    return list_r


if __name__ == '__main__':
    main()
