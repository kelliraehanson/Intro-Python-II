class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def get(self):
        return f"\nYou just took a {self.name}.\n"