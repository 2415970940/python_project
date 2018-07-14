#!/usr/bin/env python
# encoding: utf-8
import socket
import time
# 服务器ip
HOST='127.0.0.1'
PORT=8080
# url对应函数
def f1(request):
    f = open('index.html','rb')
    data =f.read()
    f.close()
    return data

def f2(request):
    f = open('list_user.html','r')
    data = f.read()
    ctime = time.time()
    # 动态
    data = data.replace('##dd##',str(ctime))
    f.close()
    return bytes(data,encoding='utf-8')
# url列表
routes=[
    ('/xxx',f1),
    ('/ooo',f2),
]

def func():
    # 创建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口
    sock.bind((HOST,PORT))
    # 监听
    sock.listen(3)

    while 1:
        # 接受数据
        conn,add = sock.accept()
        data = conn.recv(1024)
        data = str(data,encoding='utf-8')

        # 取出url
        head,favicon = data.split('\r\n\r\n')
        head_list = head.split('\r\n')
        method,url,protocal = head_list[0].split(' ')
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
        # 找到索要的url,调用函数,返回结果
        func_name=None
        for item in routes:
            if item[0]==url:
                func_name = item[1]
                break
        if func_name:
            respond = func_name(data)
        else:
            respond=b'404'
        # 发送结果
        conn.send(respond)
        conn.close()


if __name__ == '__main__':
    func()