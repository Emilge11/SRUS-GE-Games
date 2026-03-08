import unittest 
from app.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_name(self):

        test_player = Player(1, 'Alice')
        result = test_player.name()
        self.assertEqual(result, 'Alice')
    
    def test_player_id(self):

        test_player = Player(1, 'John')
        result = test_player.uid()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()