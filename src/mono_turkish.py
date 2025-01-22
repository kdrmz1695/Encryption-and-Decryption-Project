import re
from collections import Counter

tchars = "abcçdefgğhıijklmnoöprsştuüvyz" + " "
tkey = "zyvüutşsrpöonmlkjiıhğgfedçcba" + " "

print(f"turkish chars: {tchars}")
print(f"turkish key:{tkey}")

t_cipher_text = ""
with open("../data/given_text_turkish.txt", encoding="utf-8") as t_plain_text:
    file_content = t_plain_text.read()

for letter in file_content:
    if letter in tchars:
        if letter == " ":
            t_cipher_text += letter
        else:
            i = tchars.index(letter)
            t_cipher_text += tkey[i]
    else:
        t_cipher_text += letter

print("**********")
print("Encrypted Turkish Text:")
print(t_cipher_text)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

decrypted_text = t_cipher_text
t_plain_text = ""
for letter in decrypted_text:
    if letter in tkey:
        i = tkey.index(letter)
        t_plain_text += tchars[i]
    else:
        t_plain_text += letter

print("Decrypted Turkish Text:")
print(t_plain_text)

TOP_K = 20
N_GRAM = 3

def ngrams(n, text):
    for i in range(len(text) - n + 1):
        if not re.search(r'\s', text[i:i + n]):
            yield text[i:i + n]

for N in range(N_GRAM):
    print("{}-gram top {}):".format(N + 1, TOP_K))
    counts = Counter(ngrams(N + 1, t_cipher_text))
    sorted_counts = counts.most_common(TOP_K)
    for ngram, count in sorted_counts:
        print("{}: {}".format(ngram, count))

t_attemp = t_cipher_text
replacements = {
    "d": "\033[31mu\033[0m",
    "m": "\033[31mk\033[0m",
    "h": "\033[31mp\033[0m",
    "e": "\033[31mt\033[0m",
    "z": "\033[31ma\033[0m",
    "o": "\033[31mi\033[0m",
    "t": "\033[31me\033[0m",
    "g": "\033[31ms\033[0m",
    "k": "\033[31mm\033[0m",
    "u": "\033[31md\033[0m",
    "j": "\033[31mn\033[0m",
    "c": "\033[31mv\033[0m",
    "s": "\033[31mg\033[0m",
    "ğ": "\033[31mr\033[0m",
    "ü": "\033[31mç\033[0m",
    "b": "\033[31my\033[0m",
    "i": "\033[31mo\033[0m",
    "y": "\033[31mb\033[0m",
    "ö": "\033[31mı\033[0m",
    "a": "\033[31mz\033[0m",
    "v": "\033[31mc\033[0m",
    "f": "\033[31mş\033[0m",
    "ş": "\033[31mf\033[0m",
}

t_symbol_map = {}

for letter, replacement in replacements.items():
    symbol = chr(ord(letter) + 128)
    t_attemp = t_attemp.replace(letter, symbol)
    t_symbol_map[symbol] = replacement

for symbol, replacement in t_symbol_map.items():
    t_attemp = t_attemp.replace(symbol, replacement)

print("**********")
print("Broke text:")
print(t_attemp)
