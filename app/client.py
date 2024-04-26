import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)

client_socket.connect(server_address)

print("Connected to the server")

try:
    while True:
        question = input("[Magic 8 ball] Ask me a question\n=> ")
        client_socket.sendall(question.encode("utf-8"))

        answer = client_socket.recv(1024)
        print(answer.decode())

finally:
    client_socket.close()