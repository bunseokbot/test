import socket

HOST = ''
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while True:
    try:
        conn, addr = s.accept()
        print("Connected from {}:{}".format(addr[0], addr[1]))
        conn.close()
    except:
        pass

s.close()