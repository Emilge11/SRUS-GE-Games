from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None

    def insert_first(self):
        new_node = PlayerNode()
        if self.is_empty():
            self._head = new_node
    
    def is_empty(self):
        if self._head is None:
            return True
        