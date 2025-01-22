import re
import string
from collections import Counter

characters = " " + string.ascii_lowercase
characters = list(characters)
key = "abcdefghijklmnopqrstyvwxyz" + " "
print(f"chars: {characters}")
print(f"key: {key}")


cipher_text = ""
with open("../data/given_text.txt", encoding="utf-8") as plain_text:
    file_content = plain_text.read()

for letter in file_content:
    if letter in characters:
        if letter == " ":
            cipher_text += letter
        else:
            i = characters.index(letter)
            cipher_text += key[i]
    else:
        cipher_text += letter

print("**********")
print("encrypted text:")
print(cipher_text)

decrypted_txt = cipher_text
plain_text = ""
for letter in decrypted_txt:
    if letter in key:
        i = key.index(letter)
        plain_text+= characters[i]
    else:
        plain_text += letter

print("**********")
print("Decrypted text:")
print(plain_text)



print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



TOP_K = 20
N_GRAM = 3

def ngrams(n, text):
    for i in range(len(text) - n + 1):
        if not re.search(r'\s', text[i:i + n]):
            yield text[i:i + n]

for N in range(N_GRAM):
    print("{}-gram top {}):".format(N + 1, TOP_K))
    counts = Counter(ngrams(N + 1, cipher_text))
    sorted_counts = counts.most_common(TOP_K)
    for ngram, count in sorted_counts:
        print("{}: {}".format(ngram, count))



attemp = cipher_text
replacements = {
    "e": "\033[31me\033[0m",
    "a": "\033[31mt\033[0m",
    "t": "\033[31ms\033[0m",
    "j": "\033[31mi\033[0m",
    "p": "\033[31mo\033[0m",
    "x": "\033[31mw\033[0m",
    "y": "\033[31mt\033[0m",
    "i": "\033[31mh\033[0m",
    "c": "\033[31mb\033[0m",
    "f": "\033[31me\033[0m",
    "b": "\033[31ma\033[0m",
    "v": "\033[31mu\033[0m",
    "g": "\033[31mf\033[0m",
    "l": "\033[31mk\033[0m",
    "o": "\033[31mn\033[0m",
    "h": "\033[31mg\033[0m",
    "m": "\033[31ml\033[0m",
    "s": "\033[31mr\033[0m",
    "q": "\033[31mp\033[0m",
    "n": "\033[31mm\033[0m",
    "z": "\033[31my\033[0m",
    "w": "\033[31mv\033[0m",
    "d": "\033[31mc\033[0m",
}

symbol_map = {}
for letter, replacement in replacements.items():
    symbol = chr(ord(letter) + 128)
    attemp = attemp.replace(letter, symbol)
    symbol_map[symbol] = replacement

for symbol, replacement in symbol_map.items():
    attemp = attemp.replace(symbol, replacement)

print("**********")
print("Replaced text:")
print(attemp)


