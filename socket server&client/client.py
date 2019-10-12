import socket

client = socket.socket()
client.connect(("localhost", 12345))
try:
    while True:
        message = input(">>>")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        print("data received...")
        print(data)
except:
    client.close()
    print("data transprant ended!")
