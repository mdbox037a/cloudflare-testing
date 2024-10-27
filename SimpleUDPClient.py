from socket import *
serverName = input('To whom would you like to connect?:')
serverPort = input('On which port are they listening?:')
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress ` clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()


# in progress - Oct  26 2024 20:27
