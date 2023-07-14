import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# If using a public server, specify the info here
# instead of localhost and a default PORT
client.connect(("localhost", 3306))

message = client.recv(1024).decode()
client.send(input(message).encode())

message = client.recv(1024).decode()
client.send(input(message).encode())

print(client.recv(1024).decode())