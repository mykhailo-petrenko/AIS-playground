import socket
from pyais.stream import UDPStream

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# sock = socket.socket(socket.AF_INET, # Internet
#                      socket.SOCK_DGRAM) # UDP
# sock.bind((UDP_IP, UDP_PORT))


for msg in UDPStream(UDP_IP, UDP_PORT):
    message =  msg.decode()
    
    print(message.content)

# while True:
#     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
#     print("received message: %s" % data.decode('utf-8'))

#     message = decode_msg(data.decode('utf-8'))
#     print(message)
    