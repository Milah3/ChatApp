class Person:
    def __init__(self, addr, client):
        self.addr = addr
        # self.name = name
        self.client = client
    
    def __repr__(self):
        print(f'Person({self.addr, self.name})')

    def set_name(self, name):
        self.name = name