import socket
import random
from magic_8_ball_answers import answers


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)

server_socket.bind(server_address)

server_socket.listen(5)

while True:
    connection, client_address = server_socket.accept()
    print(f"Connection from: {client_address}")

    try:
        data = connection.recv(1024)
        question = data.decode()

        random.seed(hash(question))

        answer = random.choice(answers)
        connection.sendall(answer.encode())

    finally:
        connection.close()
