import random
import string
import itertools
import time
from tqdm import tqdm

s = string.ascii_lowercase

mapping = random.sample(s, len(s))
trantab_enc = str.maketrans(s, ''.join(mapping))
trantab_dec = str.maketrans(''.join(mapping), s)

original_text = "kitty"
encrypted_text = original_text.translate(trantab_enc)

print(f"Original text: {original_text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Encryption key: {''.join(mapping)}")

def brute_force(encrypted, alphabet, length, original_mapping):
    for comb in tqdm(itertools.product(alphabet, repeat=length), total=len(alphabet) ** length):
        candidate = ''.join(comb)
        if candidate.translate(trantab_enc) == encrypted:
            return candidate, ''.join(original_mapping)
    return None, None

start_time = time.time()
found_text, found_key = brute_force(encrypted_text, s, len(original_text), mapping)
end_time = time.time()

if found_text:
    print(f"Decrypted text: {found_text}")
    print(f"Found key: {found_key}")
else:
    print("Decryption failed.")

print(f"Brute force time: {end_time - start_time:.2f} seconds")
