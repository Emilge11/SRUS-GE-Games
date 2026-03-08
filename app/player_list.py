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

        if self._head is None:
            self._tail = None
        else:
            self._head.previous = None
    
    def delete_tail(self):
        if self.is_empty():
            return "The list is empty."
        
        deleted = self._tail
        self._tail = deleted.previous

        if self._tail is None:
            self._head = None
        else:
            self._tail.next = None
    
    def delete_by_key(self,key):
        if self.is_empty():
            return "The list is empty."
        
        current = self._head

        while current is not None:
            if current._current.key == key:
                prev = current.previous
                next = current.next

                if prev is None:
                    self._head = next
                else:
                    prev.next = next
                
                if next is None:
                    self._tail = prev
                else:
                    next.previous = prev
                break
            
            current = current.next
            
        return "Key not found"
            

    def is_empty(self):
        return self._head is None and self._tail is None

        