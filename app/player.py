class Player:
    def __init__(self, id, name):
        self.__private_id = id
        self.__private_name = name

    def uid(self):
        return self.__private_id
    
    def name(self):
        return self.__private_name
    
    def __str__(self):
        return f'Name: {self.__private_name}, ID: {self.__private_id}'