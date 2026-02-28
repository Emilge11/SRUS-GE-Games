from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def head(self):
        if self.is_empty():
            return None
        
        return self._head

    def insert_first(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = self._head
        else:
            new_node = PlayerNode(player)
            prev_head = self._head
            self._head = new_node
            prev_head._previous = self._head
            self._head.next = prev_head
      
    def is_empty(self):
        return self._head is None and self._tail is None

        