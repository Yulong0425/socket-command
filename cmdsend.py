import socket

socket_client = socket.socket()

socket_client.connect(("192.168.43.96", 6324))


while True:
    send_msg = input("请输入要发送给服务端的消息：")
    if send_msg == "exit":
        break
    
    socket_client.send(send_msg.encode("UTF-8"))
    

socket_client.close()
