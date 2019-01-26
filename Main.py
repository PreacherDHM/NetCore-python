import NetCore

def main():
    NetCore.Sockets.Connechion(('localhost', 9090))
    NetCore.Sockets.SendToServer('this is a test')
    NetCore.Sockets.CloseSocket()

main();
