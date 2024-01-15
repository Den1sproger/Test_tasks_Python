import socket
import selectors



SELECTOR = selectors.DefaultSelector()  # for i/o multiplexing



def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 1500))
    server_socket.listen()

    SELECTOR.register(fileobj=server_socket,
                      events=selectors.EVENT_READ,
                      data=accept_connection)



def accept_connection(server_socket: socket.socket) -> None:
    client_socket, _ = server_socket.accept()
    SELECTOR.register(fileobj=client_socket,
                      events=selectors.EVENT_READ,
                      data=send_message)



def send_message(client_socket: socket.socket) -> None:
    request = client_socket.recv(4096)

    if request:
        response = request.decode().upper().encode()
        client_socket.send(response)
    else:
        SELECTOR.unregister(client_socket)
        client_socket.close()



def event_loop():
    while True:        
        events = SELECTOR.select()

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)



if __name__ == '__main__':
    create_server()
    event_loop()