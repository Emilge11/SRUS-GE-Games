import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_is_empty(self):
        test_list = PlayerList()
        result = test_list.is_empty()
        self.assertEqual(result, True)

    def test_insert_first(self):
        test_list = PlayerList()
        test_node = PlayerNode(Player(1, 'Ibiza'))
        test_list.insert_first(test_node)
        result = test_list.is_empty()
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()