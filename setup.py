
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ServerFactory as ServFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(Protocol) : 
    def connectionMade(self) : 
        print("New connection") 
        self.transport.write("Server running on port :2000".encode('utf-8'))
        self.transport.loseConnection()

class ServerFactory(ServFactory) : 
    def buildProtocol(self, addr) : 
        return Server()

if __name__ == '__main__' : 
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()

