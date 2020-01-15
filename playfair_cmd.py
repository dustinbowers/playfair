import sys
from playfair import Playfair

if len(sys.argv) != 3:
    print("Usage: python playfair_cmd.py <passphrase> <plaintext>")
    exit(0)

argv = sys.argv
key = argv[1]
phrase = argv[2]

playfair = Playfair(key)
encrypted = playfair.process(phrase)
decrypted = playfair.process(encrypted, decrypt=True)

print("key: {0}\ninput: {1}\nciphertext: {2}\ndecoded : {3}"
      .format(key, phrase, encrypted, decrypted))

