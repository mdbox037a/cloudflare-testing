from socket import *
serverName = input('To whom would you like to connect?:')
serverPort = input('On which port are they listening?:')
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input loercase sentence:')


# in progress - Oct  26 2024 11:52
