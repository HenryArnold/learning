import traceback
def stack():
    print("the python stack")
    traceback.print_stack()

from twisted.internet import reactor
reactor.callWhenRunning(stack)
reactor.run()
