import sys
from orderedset import OrderedSet


class Playfair:

    def __init__(self, passphrase='', skip_char='J', skip_char_replacement='I', pad_char='X'):
        self.char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.passphrase = passphrase
        self.skip_char = skip_char
        self.skip_char_replacement = skip_char_replacement
        self.pad_char = pad_char
        self.grid_map = {}
        self.grid_map_rev = {}
        self.build_grid(self.passphrase)

    def build_grid(self, passphrase):
        passphrase_list = list(OrderedSet(passphrase))
        ordered_char_set = passphrase_list + list(OrderedSet(self.char_set) - OrderedSet(passphrase + self.skip_char))
        #print(ordered_char_set)
        #print(len(ordered_char_set))

        grid_width = 5
        grid_col = 0
        grid_row = 0
        i = 0
        self.grid_map = {}
        for c in ordered_char_set:
            self.grid_map[c] = (grid_col, grid_row)
            grid_col = grid_col + 1
            if grid_col == grid_width:
                grid_col = 0
                grid_row = grid_row + 1
        self.grid_map_rev = dict([(value, key) for key, value in self.grid_map.items()])
        #print(self.grid_map)
        #print(self.grid_map_rev)

    def get_char_pos(self, c):
        return self.grid_map[c]

    def get_char(self, c, r):
        return self.grid_map_rev[(c % 5, r % 5)]

    def encrypt(self, plaintext, decrypt=False):
        if len(plaintext) % 2 != 0:
            plaintext = plaintext + self.pad_char
        plaintext = plaintext.upper()
        plaintext = list(plaintext)

        output = []
        while len(plaintext) > 0:
            a = plaintext.pop(0)
            b = plaintext.pop(0)
            #print("A: {0}, B: {1}".format(a, b))

            if a == self.skip_char:
                a = self.skip_char_replacement

            if b == self.skip_char:
                b = self.skip_char_replacement





            #print((c1, r1, c2, r2))

            movement = 1
            if decrypt:
                movement = -1
            else:
                if a == b:
                    b = self.pad_char

            c1, r1 = self.get_char_pos(str(a))
            c2, r2 = self.get_char_pos(str(b))
            if r1 == r2:
                output.append(self.get_char(c1 + movement, r1))
                output.append(self.get_char(c2 + movement, r1))
                continue
            elif c1 == c2:
                output.append(self.get_char(c1, r1 + movement))
                output.append(self.get_char(c2, r1 + movement))
                continue
            else:
                # box case
                output.append(self.get_char(c2, r1))
                output.append(self.get_char(c1, r2))

        print("MOVEMENT {0}".format(movement))
        print(''.join(output))

    def decrypt(self, ciphertext):
        pass
