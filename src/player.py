# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items

    def get(self, item):
        self.items.append(item)
        self.get(item)

    def drop(self, item):
        self.items.remove(item)
        self.drop(item)

    def __str__(self):
        return f'Hello, {self.name} you are in {self.room}'

    
    