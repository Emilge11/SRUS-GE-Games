class Player:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def uid(self):
        return self._id
    
    def name(self):
        return self._name
    
    def __str__(self):
        return f'Name: {self._name}, ID: {self._id}'