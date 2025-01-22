import random, string, itertools, time
from tqdm import tqdm

N = 1000
s = "abcdefghijklmnopqrstuvwxyz"

trantab_enc = [None] * N
trantab_dec = [None] * N

for i in range(0, N):
    mapping = random.sample(s, len(s))
    trantab_enc[i] = str.maketrans(s, ''.join(mapping))
    trantab_dec[i] = str.maketrans(''.join(mapping), s)

with open("../data/given_text.txt", encoding="utf-8") as t_plain_text:
    txt = t_plain_text.read()

print(f"key: {mapping}")
print(txt)

ciphertext = [None] * len(txt)
for i in range(0, len(txt)):
    ciphertext[i] = txt[i].translate(trantab_enc[i % N])
enctext = "".join([str(i) for i in ciphertext])
print(f"encrypted text:")
print(enctext)

# Decryption
newtext = [None] * len(enctext)
for i in range(0, len(enctext)):
    newtext[i] = enctext[i].translate(trantab_dec[i % N])
dectext = "".join([str(i) for i in newtext])
print(f"decrypted text:")
print(dectext)

alphabet_en = s
char_length = 6

def brute_force(target, alphabet, length):
    target_tuple = tuple(target)
    char_list = [alphabet] * length
    for comb in tqdm(itertools.product(*char_list), total=len(alphabet) ** length):
        if comb == target_tuple:
            return ''.join(comb)
    return None

target_password = "cherry"
start_time = time.time()
found_password = brute_force(target_password, alphabet_en, char_length)
end_time = time.time()

if found_password:
    print(f"Found password: {found_password}")
else:
    print("Password not found.")

print(f"Brute force time: {end_time - start_time:.2f} seconds")
