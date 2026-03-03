from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        if self.is_empty():
            return "The list is empty."
        
        return self._head
    
    @property
    def tail(self):
        if self.is_empty():
            return "The list is empty."
        
        return self._tail

    def insert_first(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = self._head
        else:
            prev_head = self._head
            self._head = new_node
            prev_head.previous = self._head
            self._head.next = prev_head
    
    def insert_tail(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self._tail = new_node
            self._head = self._tail
        else:
            new_tail = new_node
            self._tail.next = new_tail
            new_tail.previous = self._tail
            self._tail = new_tail
    
    def delete_head(self):
        if self.is_empty():
            return "The list is empty."
        
        deleted = self._head
        self._head = deleted.next
        self._head.previous = None
            
    def is_empty(self):
        return self._head is None and self._tail is None

        