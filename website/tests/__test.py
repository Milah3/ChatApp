# Set up demo client to test initial server as well as the structure that will be used for the Client class
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import time

# GLOBAL CONSTANTS
BUFSIZ = 512
HOST = 'localhost'
MAX_CONNECTIONS = 10
PORT = 5500
ADDR = (HOST, PORT)

# GLOBAL VARIABLES
test_socket = socket(AF_INET, SOCK_STREAM)
test_socket.connect(ADDR)
messages = []


def receive_messages():
    '''
    receive messages from server 
    :return: None
    '''
    while True:
        try:
            msg = test_socket.recv(BUFSIZ).decode('utf8')
            messages.append(msg)
            if not msg:
                break
            elif msg == "{OK}":
                test_socket.close()
                print('You have successfully left the chat')
            else:
                print(msg)
        except Exception as e:
            print("[EXCEPTION TEST 1] ", e)
            break


def send_message(msg):
    '''
    receive messages from server 
    :param msg: str
    :return: None
    '''
    try:
        test_socket.send(bytes(msg, 'utf8'))

    except Exception as e:
        print("[EXCEPTION Test 2] ", e)


receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("James")
time.sleep(2)
send_message('Hey goes it?')
time.sleep(2)
send_message("{quit}")
