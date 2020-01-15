from orderedset import OrderedSet


class Playfair:

    def __init__(self, passphrase='', skip_char='J', skip_char_replacement='I', pad_char='X'):
        self.char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.passphrase = passphrase.upper()
        self.skip_char = skip_char
        self.skip_char_replacement = skip_char_replacement
        self.pad_char = pad_char
        self.grid_map = {}
        self.grid_map_rev = {}
        self.build_grid()

    def build_grid(self):
        """ Builds the encoding/decoding grid based on passphrase and skip_letter """
        passphrase_list = list(OrderedSet(self.passphrase))
        ordered_char_set = passphrase_list + list(OrderedSet(self.char_set) - OrderedSet(self.passphrase + self.skip_char))

        grid_width = 5
        grid_col = 0
        grid_row = 0
        self.grid_map = {}
        for c in ordered_char_set:
            self.grid_map[c] = (grid_col, grid_row)
            grid_col = grid_col + 1
            if grid_col == grid_width:
                grid_col = 0
                grid_row = grid_row + 1
        self.grid_map_rev = dict([(value, key) for key, value in self.grid_map.items()])

        return self.grid_map, self.grid_map_rev

    # helpers
    def get_char_pos(self, c):
        return self.grid_map[c]

    def get_char(self, c, r):
        return self.grid_map_rev[(c % 5, r % 5)]

    #
    def process(self, message, decrypt=False):
        """ Encrypt/Decrypt using the Playfair cipher """
        message = message.upper().replace(' ', '').replace(self.skip_char, self.skip_char_replacement)
        if len(message) % 2 != 0:
            message = message + self.pad_char
        message = list(message)

        output = []
        while len(message) > 0:
            a = message.pop(0)
            b = message.pop(0)

            movement = 1
            if decrypt:
                movement = -1
            elif a == b:  # if the digram is repeating letters then convert the latter to replacement
                    b = self.pad_char

            c1, r1 = self.get_char_pos(str(a))
            c2, r2 = self.get_char_pos(str(b))
            if r1 == r2:
                output.append(self.get_char(c1 + movement, r1))
                output.append(self.get_char(c2 + movement, r1))
            elif c1 == c2:
                output.append(self.get_char(c1, r1 + movement))
                output.append(self.get_char(c1, r2 + movement))
            else:  # box case
                output.append(self.get_char(c2, r1))
                output.append(self.get_char(c1, r2))

        return ''.join(output)
