import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 10000))

sock.listen(1)

connections = []

def handler(c, a):
    global connections
    while True:
        data = crecv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connnections.remove(c)
            c.close()
            break

while True:
    c, a = sock.accept()
    cThread = threading.thread(target = handler, args = (c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)