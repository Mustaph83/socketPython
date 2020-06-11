import socket
import threading

HEAD = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr}')
    connected = True
    while connected:
        msg_length = conn.recv(HEAD).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')
            conn.send('Message received!'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f'[LISTENING...] server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE PROCESSING] {threading.activeCount() - 1}')

    print('[STARTING] the server is started')

start()