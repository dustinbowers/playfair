# Playfair Cipher

A very basic implementation of Playfair ciphering/deciphering

> The Playfair cipher or Playfair square or Wheatstone-Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair for promoting its use.

**Note:** Playfair ciphering is lossy; the deciphered plaintext will often not be a perfect match to the input

### Usage

`python playfair_cmd.py <passphrase> <plaintext>`

### Example
```
python playfair_cmd.py lemon "attack at dawn"
key: lemon
input: attack at dawn
ciphertext: DQQDDIDQFBZE
decoded : ATTACKATDAWN
```

### Useful Links

[https://en.wikipedia.org/wiki/Playfair_cipher](https://en.wikipedia.org/wiki/Playfair_cipher)

