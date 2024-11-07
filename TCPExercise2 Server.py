from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

def handleClient(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper().strip()
        connectionSocket.send(capitalizedSentence.encode())

        print(capitalizedSentence)
        if (capitalizedSentence == 'STOP'):
            print(1)
            connected = False
            connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handleClient, args=(connectionSocket, addr))
    client_thread.start()
