class PlayerNode:
    def __init__(self, player):
        self._current = player
        self._next = None
        self._previous = None
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, val):
        self._next = val
    
    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, val):
        self._previous = val

    @property
    def key(self):
        return self._current.uid()
    
    def __str__(self):
        return f"Current: {self._current}, Next: {self._next}, Previous: {self._previous}"