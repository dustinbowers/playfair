import unittest
from playfair import Playfair


class TestPlayfair(unittest.TestCase):

    def setUp(self) -> None:
        self.passphrase = 'LIZARD'
        self.skip_letter = 'J'
        self.skip_char_replacement = 'I'
        self.pad_char = 'X'
        self.playfair = Playfair(self.passphrase, self.skip_letter, self.skip_char_replacement, self.pad_char)

    def test_grid(self):
        grid_map, grid_map_rev = self.playfair.build_grid()
        expected_grid_map = {'L': (0, 0), 'I': (1, 0), 'Z': (2, 0), 'A': (3, 0), 'R': (4, 0), 'D': (0, 1),
                                  'B': (1, 1), 'C': (2, 1), 'E': (3, 1), 'F': (4, 1), 'G': (0, 2), 'H': (1, 2),
                                  'K': (2, 2), 'M': (3, 2), 'N': (4, 2), 'O': (0, 3), 'P': (1, 3), 'Q': (2, 3),
                                  'S': (3, 3), 'T': (4, 3), 'U': (0, 4), 'V': (1, 4), 'W': (2, 4), 'X': (3, 4),
                                  'Y': (4, 4)}
        expected_grid_map_rev = {(0, 0): 'L', (1, 0): 'I', (2, 0): 'Z', (3, 0): 'A', (4, 0): 'R', (0, 1): 'D',
                                      (1, 1): 'B', (2, 1): 'C', (3, 1): 'E', (4, 1): 'F', (0, 2): 'G', (1, 2): 'H',
                                      (2, 2): 'K', (3, 2): 'M', (4, 2): 'N', (0, 3): 'O', (1, 3): 'P', (2, 3): 'Q',
                                      (3, 3): 'S', (4, 3): 'T', (0, 4): 'U', (1, 4): 'V', (2, 4): 'W', (3, 4): 'X',
                                      (4, 4): 'Y'}
        self.assertEqual(grid_map, expected_grid_map)
        self.assertEqual(grid_map_rev, expected_grid_map_rev)

    def test_encrypt(self):
        encrypted = self.playfair.process('The quick brown fox jumps over the lazy dog')
        expected = 'PNCSVLKQFIQUTNSULVHSTPXBFYMBIRRWGUMU'
        self.assertEqual(encrypted, expected)

    def test_decrypt(self):
        decrypted = self.playfair.process('PNCSVLKQFIQUTNSULVHSTPXBFYMBIRRWGUMU', True)
        expected = 'THEQUICKBROWNFOXIUMPSOVERTHELAZYDOGX'
        self.assertEqual(decrypted, expected)
