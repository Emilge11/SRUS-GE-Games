import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_list_is_empty(self):
        test_list = PlayerList()
        result = test_list.is_empty()

        self.assertEqual(result, True)
    
    def test_insert_first_into_empty_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node)

        test_head = test_list.head
        result1 = test_head._current.key
        result2 = test_head._previous
        result3 = test_head._next

        self.assertEqual(result1, 1)
        self.assertIsNone(result2, None)
        self.assertIsNone(result3, None)
    
    def test_insert_first_into_single_list(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, 'Alice'))
        test_list.insert_first(test_node2)

        test_head = test_list.head
        result1 = test_head._current.key
        result2 = test_head._next._current.key
        result3 = test_head._previous

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)
        self.assertIsNone(result3, None)
    
    def test_insert_first_into_multi_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node)

        test_node = PlayerNode(Player(2, 'Alice'))
        test_list.insert_first(test_node)

        test_node = PlayerNode(Player(3, 'Charlie'))
        test_list.insert_first(test_node)

        test_head = test_list.head
        result1 = test_head._current.key
        result2 = test_head._next._current.key
        result3 = test_head._previous

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 2)
        self.assertIsNone(result3, None)
    
    def test_insert_tail_into_empty_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_tail(test_node)

        test_tail = test_list.tail
        test_head = test_list.head
        result1 = test_tail._current.key
        result2 = test_head._current.key

        self.assertEqual(result1, 1)
        self.assertEqual(result2, 1)
    
    def test_insert_tail_into_single_list(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, 'Alice'))
        test_list.insert_tail(test_node2)

        test_tail = test_list.tail
        tail_prev = test_tail._previous
        result1 = test_tail._current.key
        result2 = tail_prev._current.key
        result3 = test_tail.next

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)
        self.assertIsNone(result3, None)
    
    def test_insert_tail_into_multi_list(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, 'Alice'))
        test_list.insert_tail(test_node2)

        test_node3 = PlayerNode(Player(3, 'Charlie'))
        test_list.insert_tail(test_node3)

        test_tail = test_list.tail
        tail_prev = test_tail.previous
        result1 = test_tail._current.key
        result2 = tail_prev._current.key
        result3 = test_tail.next

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 2)
        self.assertIsNone(result3, None)
    
    def test_deleted_head(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_node2 = PlayerNode(Player(2, "Alice"))

        test_list.insert_first(test_node1)
        test_list.insert_first(test_node2)

        test_list.delete_head()

        test_head = test_list.head
        result1 = test_head._current.key
        result2 = test_head._previous
        self.assertEqual(result1, 1)
        self.assertIsNone(result2, None)
    
    def test_deleted_head_multi(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_node2 = PlayerNode(Player(2, "Alice"))
        test_node3 = PlayerNode(Player(3, "John"))
        test_node4 = PlayerNode(Player(4, "Mark"))

        test_list.insert_first(test_node1)
        test_list.insert_first(test_node2)
        test_list.insert_first(test_node3)
        test_list.insert_first(test_node4)

        test_list.delete_head()
        test_list.delete_head()

        test_head = test_list.head
        result1 = test_head._current.key
        result2 = test_head._previous
        result3 = test_head._next._current.key
        
        self.assertEqual(result1, 2)
        self.assertIsNone(result2, None)
        self.assertEqual(result3, 1)

if __name__ == '__main__':
    unittest.main()