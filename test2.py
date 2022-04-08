# First test on the Client class and the server together. Seeing if the threadlocking in client class works here

from client import Client
import time

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






