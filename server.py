import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("===================================")
print("      Python Chat Server")
print("===================================")
print(f"Server is running on {HOST}:{PORT}")
print("Waiting for client connection...")

conn, address = server_socket.accept()

print(f"Client connected: {address}")
print("You can now start chatting!")
print("Type 'exit' to close the chat.\n")

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    print(f"Client: {message}")

    if message.lower() == "exit":
        print("Client ended the chat.")
        break

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "exit":
        print("Chat ended.")
        break

conn.close()
server_socket.close()

print("Server closed.")