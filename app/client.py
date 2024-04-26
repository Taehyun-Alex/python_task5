import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)

client_socket.connect(server_address)

print("connected to the server")

try:
    message = input("[Magic 8 ball] Ask me a question\n=> ")
    random.seed(123)
    client_socket.sendall(message.encode("utf-8"))

    data = client_socket.recv(1024)
    print(data.decode())

finally:
    client_socket.close()