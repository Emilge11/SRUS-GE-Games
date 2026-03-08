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
        self.assertEqual(test_list.head.key, 2)
        self.assertIsNone(test_list.head._previous)
        self.assertEqual(test_list.head._next.key, 1)

        test_node3 = PlayerNode(Player(3, 'John'))
        test_list.insert_first(test_node3)

        # Assert after 3rd insert
        self.assertEqual(test_list.head.key, 3)
        self.assertEqual(test_list.head._next.key, 2)
        self.assertIsNone(test_list.head._previous)
    
    def test_insert_tail(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, 'Bob'))
        test_list.insert_tail(test_node1)

        test_node2 = PlayerNode(Player(2, 'John'))
        test_list.insert_tail(test_node2)

        #Assert after 2nd insert
        self.assertEqual(test_list.tail.key, 2)
        self.assertEqual(test_list.head.key, 1)

        test_node3 = PlayerNode(Player(3, 'Alice'))
        test_list.insert_tail(test_node3)

        #Assert after 3rd insert
        self.assertEqual(test_list.tail.key, 3)
        self.assertEqual(test_list.tail._previous.key, 2)
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
        self.assertEqual(test_list.head.key, 2)
        self.assertEqual(test_list.head._next.key, 1)
        self.assertIsNone(test_list.head._previous)

        test_list.delete_head()

        # Assert after 2nd delete
        self.assertEqual(test_list.head.key, 1)
        self.assertIsNone(test_list.head._next)
        self.assertIsNone(test_list.head._previous)

        test_list.delete_head()

        # Assert 4th delete - list is empty now
        self.assertEqual(test_list.delete_head(), "The list is empty.")
    
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
        self.assertEqual(test_list.tail.key, 2)
        self.assertIsNone(test_list.tail._next)
        self.assertEqual(test_list.tail._previous.key, 1)

        test_list.delete_tail()

        # Assert after 2nd delete
        self.assertEqual(test_list.tail.key, 1)
        self.assertIsNone(test_list.tail._next)
        self.assertIsNone(test_list.tail._previous)

        test_list.delete_tail()
        
        # Assert 4th delete - list is empty now
        self.assertEqual(test_list.delete_tail(), "The list is empty.")

    def test_delete_key_empty_list(self):
        test_list = PlayerList()

        # Assert  - empty list
        self.assertEqual(test_list.delete_by_key(1), "The list is empty.")

    def test_delete_key(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_list.insert_first(test_node1)

        test_node2 = PlayerNode(Player(2, "Alice"))
        test_list.insert_first(test_node2)

        test_node3 = PlayerNode(Player(3, "John"))
        test_list.insert_tail(test_node3)

        test_list.delete_by_key(3)

        # Assert after 1st delete by key
        self.assertEqual(test_list.tail.key, 1)
        self.assertIsNone(test_list.tail._next)
        self.assertEqual(test_list.tail._previous.key, 2)

        test_list.delete_by_key(1)

        # Assert after 2nd delete by key
        self.assertEqual(test_list.head.key, 2)
        self.assertIsNone(test_list.head._next)
        self.assertIsNone(test_list.head._previous)

        # Assert after 3rd delete by key - not found
        self.assertEqual(test_list.delete_by_key(3), "Key not found")
    
    def test_display_empty(self):
        test_list = PlayerList()

        # Assert when list is empty
        self.assertEqual(test_list.display(None), "The list is empty.")

    def test_display(self):
        test_list = PlayerList()

        test_node1 = PlayerNode(Player(1, "Bob"))
        test_list.insert_first(test_node1)

        # Assert after 1st insert
        self.assertEqual(test_list.display(True), [1])
        self.assertEqual(test_list.display(False), [1])
        
        test_node2 = PlayerNode(Player(2, "Alice"))
        test_list.insert_tail(test_node2)

        test_node3 = PlayerNode(Player(3, "John"))
        test_list.insert_tail(test_node3)

        # Assert after 3rd insert - display list
        self.assertEqual(test_list.display(True), [1, 2, 3])
        self.assertEqual(test_list.display(False), [3, 2, 1])
        self.assertEqual(test_list.display(None), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()