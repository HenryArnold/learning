"""
factory = PoetryClientFactory(len(addresses))
from twisted.internet import reactor
for address in addresses:
    host, port = address
    reactor.connectTCP(host, port, factory)

def buildProtocol(self, address):
    proto = ClientFactory.buildProtocol(self, address)
    proto.task_num = self.task_num
    self.task_num += 1
    return proto

class PoetryClientFactory(ClientFactory):
    task_num = 1
    protocol = PoetryProtocol
"""
def hello():
    print("hello from the reactor loop")
    print("lately i feel like i'm stuck in a rut")
from twisted.internet import reactor
reactor.callWhenRunning(hello)
print('staring the reactor')
reactor.run() 
