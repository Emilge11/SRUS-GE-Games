import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_is_empty(self):
        test_list = PlayerList()
        result = test_list.is_empty()
        self.assertEqual(result, True)
    
    def test_insert_first_into_empty_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node)

        test_head = test_list.head()
        result = test_head._current.key
        self.assertEqual(result, 1)
    
    def test_insert_first_into_single_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node)
        test_node = PlayerNode(Player(2, 'Alice'))
        test_list.insert_first(test_node)

        test_head = test_list.head()
        result = test_head._current.key
        self.assertEqual(result, 2)
    
    def test_insert_first_into_multi_list(self):
        test_list = PlayerList()

        test_node = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node)
        test_node = PlayerNode(Player(2, 'Alice'))
        test_list.insert_first(test_node)
        test_node = PlayerNode(Player(3, 'Charlie'))
        test_list.insert_first(test_node)

        test_head = test_list.head()
        result = test_head._current.key
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()