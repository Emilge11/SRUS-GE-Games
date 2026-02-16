import unittest 
from app.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_name(self):

        test_player = Player(1, 'Music')
        result = test_player.name()
        self.assertEqual(result, 'Music')
    
    def test_player_id(self):

        test_player = Player(1, 'Audio')
        result = test_player.uid()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()