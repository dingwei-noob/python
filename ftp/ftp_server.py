"""
ftp文件服务器，服务端
env ：python3
多进程/线程并发 socket
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)


# 创建类实现服务器文件处理功能
class FTPServer:
    """
    查看列表，下载，上传，退出处理
    """


# 搭建网络服务端模型
def main():
    s= socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('127.0.0.1',8888))
    s.listen(5)

    while True:
        # 循环处理客户端链接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception as e:
            print(e)
            continue
        data = c.recv(1024)
        print(data)






if __name__ == "__main__":
    main()