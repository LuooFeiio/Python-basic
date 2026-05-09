"""
演示Socket客户端开发
"""

# 1 创建socket对象
import socket
socket_client = socket.socket()
# 2 连接到服务端
socket_client.connect(("localhost", 8888))

while True: # 无限循环持续发送与接收消息
    # 3 发送消息
    msg = input("请输入要给服务端发送的消息：")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8")) # 发送的消息通过UTF-8编码，将字符串转换为字节数组
    # 4 接收返回消息
    recv_data = socket_client.recv(1024) # 1024是缓冲区的大小，一般1024即可
    # 同样recv方法是阻塞的
    print(f"服务端回复的消息是：{recv_data.decode('UTF-8')}")
# 5 关闭链接
socket_client.close()