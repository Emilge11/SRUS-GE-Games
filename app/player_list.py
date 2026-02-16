from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def insert_first(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
    
    def is_empty(self):
        return self._head is None

        