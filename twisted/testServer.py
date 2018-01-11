from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class gameSocket(Protocol):
    def connectionMade(self):
        print("new client")

    def connectionLost(self, reason):
        print("lost client")

    def dataReceived(self, data):
        print("gat data:" + str(data))
        self.transport.write("bingo! I got your msg:" + str(data))

if __name__ == '__main__':
    f = Factory()
    f.protocol = gameSocket
    reactor.listenTCP(5200, f)
    print ("server started...")
    reactor.run()
