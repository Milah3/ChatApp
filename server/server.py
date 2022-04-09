from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# import time
from person import Person

# GLOBAL CONSTANTS
BUFSIZ = 512
HOST = 'localhost'
MAX_CONNECTIONS = 10
PORT = 5500
ADDR = (HOST, PORT)

# GLOBAL VARIABLES
persons = []
messages = []

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    '''
    send new messages to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return: 
    '''
    for person in persons:
        client = person.client
        client.send(bytes(name + ": ", 'utf8') + msg)


def handle_client(person):
    # Thread to handle all messages to and from person/client
    # :param person: Person
    # :return: None

    client = person.client
    persons.append(person)  # add person to persons list

    # Get person's name first and fill in name param in person object
    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    # msg = bytes(name + ' has joined the chat!', "utf8") # Was giving weird ":" at the beginning so commented it out
    broadcast(b'has joined the chat!', name)  # broadcast welcome message

    while True:  # wait for any messages from person
        try:
            msg = client.recv(BUFSIZ)

            if msg == bytes('{quit}', 'utf8'):  # if message is quit, disconnect client
                client.send(bytes('{OK}', 'utf8'))
                client.close()
                persons.remove(person)
                broadcast(b'has left the chat.', name)
                print("[DISCONNECTED] " + name + " has disconnected")
                break
            elif not msg or msg == " ":
                break
            else:  # otherwise, send message to all other clients
                print(f'{name}:', msg.decode('utf8'))
                broadcast(msg, name)
        except Exception as e:
            print('[EXCEPTION]', e)
            break


def wait_for_connection():
    # wait for connection from new clients, start new thread once connected
    # :param SERVER: SOCKET
    # :return: NONE

    while True:  # wait for any new connections
        try:
            client, client_address = SERVER.accept()  # accept any new connection requests
            person = Person(client_address, client)  # create new person per connection

            print(f'[CONNECTION] {client_address[0]} has connected to the server')
            Thread(target=handle_client, args=(person,)).start()
        except Exception as e:
            print('[EXCEPTION]', e)
            run = False
    print('SERVER EXITED')


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)  # Open server to listen for connections
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
