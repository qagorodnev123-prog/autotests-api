import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)


    server_socket.listen(10)

    all_messages = []
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        all_messages.append(data)
        response = '\n'.join(all_messages)
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == '__main__':
    server()