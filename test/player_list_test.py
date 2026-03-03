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

if __name__ == '__main__':
    unittest.main()