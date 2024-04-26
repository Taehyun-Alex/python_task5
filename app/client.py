import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)

client_socket.connect(server_address)

print("connected to the server")

try:
    message = "Will I pass my assessment?"
    client_socket.sendall(message.encode("utf-8"))

    data = client_socket.recv(1024)
    print(data.decode())

finally:
    client_socket.close()