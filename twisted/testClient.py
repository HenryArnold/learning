import socket, stackless
sockIndex = 1

def connToServer():
    global sockIndex
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 5200))
    conn.send("hi, I'm NO." + str(sockIndex))

    print (sockIndex)
    sockIndex += 1

    while True:
        
