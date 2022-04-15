# First test on the Client class and the server together. Seeing if the threadlocking in client class works here

import time
from threading import Thread

from website.client import Client


def update_messages():
    '''
    updates local list of messages
    :return: None
    '''
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 0.1 seconds
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages

        for msg in msgs:  # display new messages
            if msg == "{quit}":
                run = False
                break
            else:
                # print(msg)
                # do work here
                break


Thread(target=update_messages).start()
c1 = Client('Kevin')
c2 = Client('Joey')

c1.send_message("Yo")
time.sleep(1)
c2.send_message("Whats up")
time.sleep(1)
c1.send_message("Not much, hbu")
time.sleep(1)
c2.send_message("I'm aiight")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()
