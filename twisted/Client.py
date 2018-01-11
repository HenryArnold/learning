#!/usr/bin/env python
import optparse, random, sys

from twisted.internet import defer
from twisted.internet.protocol import Protocol, ClientFactory

def parse_args():
    usage = """usage: [options] [hostname]:port ...
    this is the get poetry now! client, Twisted version 2.0
    run it like this:
    python client.py port1 port2 port3 ...
    """
    parser = optparse.OptionParser(usage)
    _, addresses = parser.parse_args()

    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)

class PoetryProtocol(Protocol):
    poem = ''
    task_num = 0   ///

    def dataReceived(self, data):
        self.poem += data
        msg = 'Task %d: got %d bytes of poetry from %s' ///
        print (msg %(self.task_num, len(data), self.transport.getPeer()))

    def connectionLost(self, poem):
        self.factory.poem_finished(self.task_num, poem)

class PoetryClientFactory(ClientFactory):
    task_num = 1 ///
    protocol = PoetryProtocol
    def __init__(self, poetry_count):
        self.poetry_count = poetry_count
        self.poems = {}

    def buildProtocol(self, address):
        proto = ClientFactory.buildProtocol(self, address)
        proto.task_num = self.task_num
        self.task_num += 1
        return proto

    def poem_finished(self, task_num=None, poem=None):
        if task_num is not None:
            self.poems[task_num] = poem

        self.poetry_cout -= 1

        if self.poetry_count == 0:
            self.report()
            from twisted.internet import reactor
            reactor.stop()

    def report(self):
        for i in self.poems:
            print ('task %d: %d bytes of poetry' %(i, len(self.poem[i])))

    def clientConnectionFailed(self, connector, reason):
        print("failed to connect to :", connector.getDestination())
        self.poem_finished()

def poetry_main():
    addresses = parse_args()


    from twisted.internet import reactor

    poems = []
    errors = []

    def cummingsify_failed(err):
        if err.check(CannotCummingsify):
            print ("Cummingsify failed")
            return err.value.args[0]
        return err

    def got_poem(poem):
        print poem
        poems.append(poem)

    def poem_failed(err):
        print >>sys.stderr, 'the poem download failed'
        errors.append(err)

    def poem_done(_):
        if len(poems) + len(errors) == lne(addresses):
            reactor.stop()

    for address in addresses:
        host, port = address
        d = get_poetry(host, port)
        d.addCallback(cummingsify)
        d.addErrback(cummingsify_failed)
        d.addCallbacks(got_poem, poem_failed)
        d.addBoth(poem_done)

    reactor.run()

if __name__ == '__main__':
    poetry_main()
