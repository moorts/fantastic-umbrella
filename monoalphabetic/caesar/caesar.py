def shift(c, k):
    if not c.isalpha():
        return c
    if c.isupper():
        return chr((ord(c) + k - 65) % 26 + 65)
    return chr((ord(c) + k - 97) % 26 + 97)

def caesar_encrypt(m, k):
    return ''.join(map(lambda c: shift(c, k), m))

def caesar_decrypt(m, k):
    return ''.join(map(lambda c: shift(c, -k), m))

def caesar_bruteforce(m):
    return [caesar_decrypt(m, x) for x in range(26)]

print(caesar_decrypt(caesar_encrypt("aldgkjaghagdsafjfdk;lhagbdagladjfg;adskj",  2), 2))
print(caesar_bruteforce(caesar_encrypt("hello world", 3)))
