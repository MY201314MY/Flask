import socket

server = socket.socket()
host = socket.gethostname()
print("The computer's name:", host)
port = 12345
server.bind(("localhost", port))

server.listen()
while True:
    conn, address = server.accept()
    print('Address:', address)
    while True:
        data = conn.recv(1024)
        if not data:
            print("连接已断开")
            break
        print("Data received:%s" % data)
        conn.send(data.upper())
    server.close()