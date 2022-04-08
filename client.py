from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread, Lock

# import time

class Client:
    # """
    # communicates with the server
    # """

    # GLOBAL CONSTANTS
    BUFSIZ = 1024
    HOST = 'localhost'
    MAX_CONNECTIONS = 10
    PORT = 5500
    ADDR = (HOST, PORT)

    def __init__(self, name):
        '''
        Initializes object and send name to server
        :param name: str
        '''
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()


    def receive_messages(self):
        '''
        receive messages from server 
        :return: None
        '''
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode('utf8')
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
                if msg == "{OK}":
                    self.client_socket.close()
                    print('You have successfully left the chat')
                    break
                elif msg and msg != '{OK}':
                    print(msg)
                else:
                    break
            except Exception as e:
                # print("[EXCEPTION TEST 1] ", e)
                break
    
    def send_message(self, msg):
        '''
        receive messages from server 
        :param msg: str
        :return: None
        '''
        self.client_socket.send(bytes(msg, 'utf8'))

    def get_messages(self):
        '''
        returns a list of string messages
        :return: list[str]
        '''
        # self.lock.acquire()
        # self.lock.release()
        return self.messages

    def disconnect(self):
        self.send_message('{quit}')