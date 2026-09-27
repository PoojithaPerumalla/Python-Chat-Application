import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("===================================")
print("      Python Chat Client")
print("===================================")

client_socket.connect((HOST, PORT))

print("Connected to the server!")
print("You can now start chatting!")
print("Type 'exit' to close the chat.\n")

while True:
    message = input("You: ")

    client_socket.send(message.encode())

    if message.lower() == "exit":
        print("Chat ended.")
        break

    reply = client_socket.recv(1024).decode()

    print(f"Server: {reply}")

    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

client_socket.close()