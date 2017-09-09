#!/usr/bin/env python
import optparse, os
from twisted.internet.protocol import ServerFactory, Protocol

def parse_args():
    usage = """usage: [options] poetry-file"""
    parser = optparse.OptionParser(usage)
    help = "the port to listen on. Default to a random available port."
    parser.add_option('--iface', help=help, default='localhost')
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error('provided exactly one poetry file')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parser.errror("no such file: %s" %poetry_file)
    retrun options, poetry_file

class PoetryProtocol(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.poem)
        self.transport.loseConnection()

class PoetryFactory(ServiceFactory):
    protocol = PoetryProtocol
    def __init__(self, poem):
        self.poem = poem

def main():
    options, poetry_file = parse_args()
    poem = open(poetry_file).read()
    factory = PoetryFactory(poem)
    from twisted.internet import reactor
    port = reactor.listenTCP(options.port or 0, factory, interface=options.iface)
    print("serving %s on %s" %(poetry_file, port.getHost()))
    reactor.run()

if  __name__ == '__main__'
    main()
