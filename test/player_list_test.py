import unittest
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player import Player

class TestPlayerList(unittest.TestCase):
    def test_list_is_empty(self):
        test_list = PlayerList()
        result = test_list.is_empty()

        self.assertEqual(result, True)
    
    def test_insert_first(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, 'Alice'))
        test_list.insert_first(test_node2)
        
        # Assert after 2nd insert
        self.assertEqual(test_list.head._current.key, 2)
        self.assertIsNone(test_list.head._previous)
        self.assertEqual(test_list.head._next._current.key, 1)

        test_node3 = PlayerNode(Player(3, 'John'))
        test_list.insert_first(test_node3)

        # Assert after 3rd insert
        self.assertEqual(test_list.head._current.key, 3)
        self.assertEqual(test_list.head._next._current.key, 2)
        self.assertIsNone(test_list.head._previous)
    
    def test_insert_tail(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_tail(test_node1)

        test_node2 = PlayerNode(Player(2, 'John'))
        test_list.insert_tail(test_node2)

        #Assert after 2nd insert
        self.assertEqual(test_list.tail._current.key, 2)
        self.assertEqual(test_list.head._current.key, 1)

        test_node3 = PlayerNode(Player(3, 'Alice'))
        test_list.insert_tail(test_node3)

        #Assert after 3rd insert
        self.assertEqual(test_list.tail._current.key, 3)
        self.assertEqual(test_list.tail._previous._current.key, 2)
        self.assertIsNone(test_list.tail._next)
       
    def test_delete_head(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, "Alice"))
        test_list.insert_first(test_node2)

        test_node3 = PlayerNode(Player(3, "John"))
        test_list.insert_first(test_node3)

        test_list.delete_head()

        # Assert after 1st delete
        self.assertEqual(test_list.head._current.key, 2)
        self.assertEqual(test_list.head._next._current.key, 1)
        self.assertIsNone(test_list.head._previous)

        test_list.delete_head()

        # Assert after 2nd delete
        self.assertEqual(test_list.head._current.key, 1)
        self.assertIsNone(test_list.head._next)
        self.assertIsNone(test_list.head._previous)

        test_list.delete_head()

        # Assert after 4rd delete - list is empty
        self.assertEqual(test_list.delete_tail(), "The list is empty.")
    
    def test_delete_tail(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_list.insert_tail(test_node1)

        test_node2 = PlayerNode(Player(2, "Alice"))
        test_list.insert_tail(test_node2)

        test_node3 = PlayerNode(Player(3, "John"))
        test_list.insert_tail(test_node3)

        test_list.delete_tail()

        # Assert after 1st delete
        self.assertEqual(test_list.tail._current.key, 2)
        self.assertIsNone(test_list.tail._next)
        self.assertEqual(test_list.tail._previous._current.key, 1)

        test_list.delete_tail()

        # Assert after 2nd delete
        self.assertEqual(test_list.tail._current.key, 1)
        self.assertIsNone(test_list.tail._next)
        self.assertIsNone(test_list.tail._previous)

        test_list.delete_tail()

        # Assert after 4rd delete - list is empty
        self.assertEqual(test_list.delete_tail(), "The list is empty.")

if __name__ == '__main__':
    unittest.main()