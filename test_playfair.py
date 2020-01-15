import unittest
from playfair import Playfair


class TestPlayfair(unittest.TestCase):

    def setUp(self) -> None:
        self.passphrase = ''
        #self.skip_letter = 'J'
        self.playfair = Playfair(self.passphrase)#, self.skip_letter)
        pass

    @unittest.skip("WIP")
    def test_grid(self):
        self.playfair.build_grid('')
        c, r = self.playfair.get_char_pos('T')
        print("c {}, r {}".format(c, r))
        print(self.playfair.get_char(c,r))

    # @unittest.skip("WIP")
    def test_encrypt(self):
        self.playfair.process('The quick brown fox jumps over the lazy dog')
        # self.playfair.process('balloon')
        # self.playfair.process('no tomorrow at one')

    # @unittest.skip("WIP")
    def test_decrypt(self):
        self.playfair.process('SIAUTKEHGWMYLHNYKTNLTNZASUKCQFVZITHW', True)
        # self.playfair.process('CBNVNYSC', True)
        # self.playfair.process('OPYTNPSWMYDQPOCZ', True)

