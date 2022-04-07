# Set up demo client to test server

from email import message
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

# GLOBAL CONSTANTS
BUFSIZ = 1024
HOST = 'localhost'
MAX_CONNECTIONS = 10
PORT = 5500
ADDR = (HOST, PORT)

# GLOBAL VARIABLES
test_socket = socket(AF_INET, SOCK_STREAM)
test_socket.connect(ADDR)
messages = []

def receive_messages():
    print('Receiving messages...')
    '''
    receive messages from server 
    :return: None
    '''
    # while True:
    try:
        msg = test_socket.recv(BUFSIZ).decode('utf8')
        messages.append(msg)
        print('Receiving messages...:' + msg)
        # print('Message received: ' + msg)
    except OSError as e:
        print("[OSError] ", e)
        # break
    except Exception as e:
        ("[EXCEPTION] ", e)
        # break

def send_message(msg):
    '''
    receive messages from server 
    :param msg: str
    :return: None
    '''
    try:
        test_socket.send(bytes(msg, 'utf8'))
        # if (msg == '{quit}'):
            # test_socket.close()
    except Exception as e:
        print("[EXCEPTION] ", e)

receive_thread = Thread(target=receive_messages)
receive_thread.start()

# send_msg_thread = Thread(target=send_message, args=('This is my message',))

# send_message("Miler")
# send_message('Hey there!')
# send_message('What it do bro')
send_message('{quit}')

